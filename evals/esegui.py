#!/usr/bin/env python3
"""Esegue i casi di prova di evals.json e valuta le risposte.

Uso:
    python evals/esegui.py                      # tutti i casi
    python evals/esegui.py --solo 3,7           # solo alcuni, per id o per nome
    python evals/esegui.py --rivaluta           # non riesegue: rivaluta le risposte già salvate
    python evals/esegui.py --solo 6 --ripeti 3  # lo stesso caso tre volte
    python evals/esegui.py --modello sonnet --paralleli 4 --uscita evals/risultati

Ogni caso parte in una sessione nuova di Claude Code (`claude -p`) con la skill
caricata da questa repo, in una cartella vuota. Della risposta si controllano:
se la skill si è attivata, quali riferimenti ha aperto, le segnalazioni di
controlla.py e i «controlli» dichiarati nel caso. La cartella di lavoro sta fuori
dalla repo, così la sessione non eredita memoria e istruzioni di questo progetto.

I controlli automatici dicono se una risposta è sbagliata, non se è buona: le
risposte restano in <uscita>/<nome>/risposta.md e vanno lette confrontandole
con «expected_output».

Lo stesso caso può passare in un'esecuzione e fallire in quella dopo. Prima di
concludere che una modifica alla skill ha funzionato conviene ripetere i casi
interessati con --ripeti, e guardare quante volte passano su quante.

Solo libreria standard, Python 3.8 o successivo. Serve `claude` nel PATH.
"""

import argparse
import concurrent.futures
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "skills" / "italian-master" / "scripts"))
import controlla  # noqa: E402


def esegui_caso(caso, cartella, modello):
    """Lancia una sessione nuova e restituisce (risposta, strumenti usati, costo)."""
    # Fuori dalla repo, perché la sessione non erediti memoria e istruzioni di questo progetto.
    lavoro = Path(tempfile.mkdtemp(prefix="italian-master-"))
    for percorso, contenuto in (caso.get("files") or {}).items():
        destinazione = lavoro / percorso
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        destinazione.write_text(contenuto, encoding="utf-8")
    comando = [shutil.which("claude") or "claude", "-p", "--plugin-dir", str(REPO), "--output-format", "stream-json",
               "--verbose", "--allowedTools", "Read,Glob,Grep,Skill,Write,Bash(python:*),Bash(python3:*)", "--model", modello]
    processo = subprocess.run(comando, input=caso["prompt"], capture_output=True, text=True, encoding="utf-8",
                              cwd=lavoro, timeout=900)
    (cartella / "sessione.jsonl").write_text(processo.stdout, encoding="utf-8")
    shutil.rmtree(lavoro, ignore_errors=True)
    risposta, strumenti, costo = "", [], None
    for riga in processo.stdout.splitlines():
        try:
            evento = json.loads(riga)
        except ValueError:
            continue
        if evento.get("type") == "assistant":
            for blocco in evento["message"].get("content", []):
                if blocco.get("type") == "tool_use":
                    dati = blocco.get("input", {})
                    cosa = dati.get("file_path") or dati.get("skill") or dati.get("pattern") or ""
                    strumenti.append(f"{blocco['name']}:{str(cosa).replace(chr(92), '/')}")
        elif evento.get("type") == "result":
            risposta = evento.get("result") or ""
            costo = evento.get("total_cost_usd")
    if not risposta:
        raise RuntimeError(f"nessuna risposta (codice {processo.returncode}): {processo.stderr[:300]}")
    (cartella / "risposta.md").write_text(risposta, encoding="utf-8")
    (cartella / "strumenti.json").write_text(json.dumps({"strumenti": strumenti, "costo": costo}, ensure_ascii=False),
                                             encoding="utf-8")
    return risposta, strumenti, costo


def valuta(caso, risposta, strumenti):
    """Restituisce (falliti, note, dati): i controlli non passati, le segnalazioni dello script e le misure."""
    controlli = caso.get("controlli") or {}
    falliti = []
    if not any(s.startswith("Skill:") and "italian-master" in s for s in strumenti):
        falliti.append("la skill non si è attivata")
    for atteso in controlli.get("deve_leggere", []):
        if not any(atteso in s for s in strumenti):
            falliti.append(f"non ha aperto {atteso}")
    for modello in controlli.get("deve", []):
        if not re.search(modello, risposta, re.IGNORECASE | re.MULTILINE):
            falliti.append(f"manca: {modello}")
    # Le note citano spesso l'originale: quello che sta tra virgolette o in una riga con «→» non conta.
    senza_citazioni = re.sub(r'«[^»]*»|“[^”]*”|"[^"\n]*"|`[^`\n]*`|^.*→.*$', " ", risposta, flags=re.MULTILINE)
    for modello in controlli.get("non_deve", []):
        trovato = re.search(modello, senza_citazioni, re.IGNORECASE | re.MULTILINE)
        if trovato:
            falliti.append(f"c'è «{trovato.group(0)}» ({modello})")
    esito, dati = controlla.analizza(risposta, bambini=bool(controlli.get("bambini")))
    for chiave, (minimo, massimo) in (controlli.get("misure") or {}).items():
        if chiave not in dati:
            falliti.append(f"{chiave}: testo troppo breve per misurarlo")
        elif not minimo <= dati[chiave] <= massimo:
            falliti.append(f"{chiave} = {dati[chiave]}, atteso tra {minimo} e {massimo}")
    note = [f"{categoria}: {t['testo']}" for categoria, trovati in esito.items() for t in trovati]
    return falliti, note, dati


def main():
    for flusso in (sys.stdout, sys.stderr):
        try:
            flusso.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(description="Esegue e valuta i casi di prova della skill.")
    parser.add_argument("--solo", help="id o nomi dei casi, separati da virgola")
    parser.add_argument("--modello", default="sonnet", help="modello per le sessioni di prova (predefinito: sonnet)")
    parser.add_argument("--paralleli", type=int, default=4, help="sessioni in parallelo (predefinito: 4)")
    parser.add_argument("--uscita", default=str(REPO / "evals" / "risultati"), help="cartella dei risultati")
    parser.add_argument("--rivaluta", action="store_true", help="rivaluta le risposte già salvate senza rieseguire")
    parser.add_argument("--ripeti", type=int, default=1, help="quante volte eseguire ogni caso (predefinito: 1)")
    args = parser.parse_args()

    casi = json.loads((REPO / "evals" / "evals.json").read_text(encoding="utf-8"))["evals"]
    if args.solo:
        scelti = {s.strip() for s in args.solo.split(",")}
        casi = [c for c in casi if str(c["id"]) in scelti or c["name"] in scelti]
    uscita = Path(args.uscita)

    def lavora(coppia):
        caso, giro = coppia
        cartella = uscita / caso["name"] if args.ripeti == 1 else uscita / caso["name"] / str(giro)
        cartella.mkdir(parents=True, exist_ok=True)
        try:
            if args.rivaluta:
                risposta = (cartella / "risposta.md").read_text(encoding="utf-8")
                salvati = json.loads((cartella / "strumenti.json").read_text(encoding="utf-8"))
                strumenti, costo = salvati["strumenti"], salvati["costo"]
            else:
                risposta, strumenti, costo = esegui_caso(caso, cartella, args.modello)
        except (OSError, RuntimeError, subprocess.TimeoutExpired) as errore:
            return caso, [f"non eseguito: {errore}"], [], {}, [], None
        falliti, note, dati = valuta(caso, risposta, strumenti)
        return (caso, falliti, note, dati, strumenti, costo)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.paralleli)) as gruppo:
        risultati = list(gruppo.map(lavora, [(c, g) for c in casi for g in range(1, args.ripeti + 1)]))

    riepilogo = []
    for caso, falliti, note, dati, strumenti, costo in risultati:
        aperti = sorted({s.split("references/")[-1] for s in strumenti if "references/" in s})
        print(f"\n== {caso['id']}. {caso['name']}: {'PASSA' if not falliti else 'NON PASSA'} ==")
        print(f"   riferimenti aperti: {', '.join(aperti) or 'nessuno'}")
        if "parole_per_frase" in dati:
            print(f"   {dati['parole']} parole, {dati['parole_per_frase']} per frase, Gulpease {dati['gulpease']}")
        for f in falliti:
            print(f"   ✗ {f}")
        for n in note:
            print(f"   · {n}")
        riepilogo.append({"id": caso["id"], "name": caso["name"], "passa": not falliti, "falliti": falliti,
                          "segnalazioni": note, "misure": dati, "riferimenti": aperti, "costo": costo})
    uscita.mkdir(parents=True, exist_ok=True)
    (uscita / "esito.json").write_text(json.dumps(riepilogo, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.ripeti > 1:
        print()
        for caso in casi:
            esiti = [r["passa"] for r in riepilogo if r["id"] == caso["id"]]
            print(f"{caso['id']:>3}. {caso['name']}: passa {sum(esiti)} volte su {len(esiti)}")
    passati = sum(r["passa"] for r in riepilogo)
    spesa = sum(r["costo"] or 0 for r in riepilogo)
    print(f"\n{passati} esecuzioni su {len(riepilogo)} passano i controlli automatici. "
          f"Segnalazioni dello script: {sum(len(r['segnalazioni']) for r in riepilogo)}. Costo: {spesa:.2f} $.")
    print(f"Le risposte sono in {uscita}: vanno lette.")
    return 0 if passati == len(riepilogo) else 1


if __name__ == "__main__":
    sys.exit(main())

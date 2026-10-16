#!/usr/bin/env python3
"""Benchmark: le versioni della skill contro Claude senza skill, sugli stessi casi.

Uso:
    python evals/benchmark.py v1.0.0 0af8ebe HEAD   # misura queste versioni (tag, commit o HEAD per la cartella di lavoro)
    python evals/benchmark.py --grafico             # ridisegna soltanto il grafico da evals/benchmark/esiti.json

Ogni caso di evals/benchmark/casi.json viene eseguito --ripeti volte con la skill e altrettante
senza. Ogni risposta con la skill va contro la risposta senza skill dello stesso caso e dello
stesso giro: una sessione separata, che non sa quale delle due abbia usato la skill, sceglie la
migliore o dice pari. Accanto al giudizio c'è una misura che non dipende da nessun modello:
quante formule segnala controlla.py ogni mille parole (sempre la versione attuale dello script,
per tutte le versioni).

Le risposte e i giudizi restano in evals/risultati/benchmark/ (fuori dalla repo) e si riusano:
rilanciare lo stesso comando riprende da dove si era fermato. Nella repo vanno solo i numeri
aggregati, in evals/benchmark/esiti.json, e il grafico .github/benchmark.svg.

Il giudice è un modello linguistico, e i casi sono stati scritti insieme alla skill: i numeri
dicono in quale direzione va il lavoro, non sono una misura indipendente della qualità.
"""

import argparse
import concurrent.futures
import datetime
import json
import random
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import esegui  # noqa: E402
from esegui import controlla  # noqa: E402

REPO = esegui.REPO
CASI = REPO / "evals" / "benchmark" / "casi.json"
ESITI = REPO / "evals" / "benchmark" / "esiti.json"
GRAFICO = REPO / ".github" / "benchmark.svg"
USCITA = REPO / "evals" / "risultati" / "benchmark"

# Le note all'utente citano spesso l'originale: quello che sta tra virgolette o in una riga con «→» non conta.
CITAZIONI = re.compile(r'«[^»]*»|“[^”]*”|"[^"\n]*"|`[^`\n]*`|^.*→.*$', re.MULTILINE)
NON_FORMULE = {"Forma e ritmo", "Da guardare"}

GIUDICE = """Sei un redattore editoriale italiano di grande esperienza. Ti mostro una richiesta e due risposte, A e B, scritte da due assistenti diversi. Devi dire quale delle due consegna il testo scritto meglio per lo scopo richiesto.

Criteri, in ordine di peso:
1. Rispetto della richiesta e dei fatti forniti: nessun dato inventato, nessuna informazione chiesta che manchi.
2. Italiano corretto e naturale, senza formule fatte, frasi a effetto, triadi di aggettivi, «non è solo… è», calchi dall'inglese e altri tic dei testi generati.
3. Registro adatto al destinatario e coerente dall'inizio alla fine.
4. Precisione del lessico e ritmo delle frasi.

Non premiare la lunghezza né la formattazione. Giudica il testo consegnato; le note rivolte a chi ha fatto la richiesta contano solo se contengono errori. Se la differenza è trascurabile o di puro gusto, rispondi «pari».

## Richiesta

{prompt}

## Che cosa ci si aspetta

{atteso}

## Risposta A

{a}

## Risposta B

{b}

Rispondi soltanto con un oggetto JSON, senza altro testo: {{"vince": "A" oppure "B" oppure "pari", "motivo": "una frase"}}"""


def git(*argomenti):
    return subprocess.run(["git", *argomenti], cwd=REPO, capture_output=True, text=True, check=True).stdout.strip()


def versione_di(cartella):
    return json.loads((cartella / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]


def esegui_lato(casi, cartella, plugin, ripeti, modello, paralleli):
    """Esegue i casi mancanti con un plugin (o senza, se plugin è None)."""
    lavori = [(c, g) for c in casi for g in range(1, ripeti + 1)
              if not (cartella / c["name"] / str(g) / "risposta.md").exists()]

    def lavora(coppia):
        caso, giro = coppia
        destinazione = cartella / caso["name"] / str(giro)
        destinazione.mkdir(parents=True, exist_ok=True)
        if esegui.limite_raggiunto.is_set():
            return
        try:
            esegui.esegui_caso(caso, destinazione, modello, plugin)
        except (OSError, RuntimeError, subprocess.TimeoutExpired) as errore:
            print(f"   {caso['name']} giro {giro}: non eseguito, {errore}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=paralleli) as gruppo:
        list(gruppo.map(lavora, lavori))


def giudica(caso, con, senza, seme, modello):
    """Confronto alla cieca; restituisce «con», «senza» o «pari»."""
    lati = ["con", "senza"]
    random.Random(seme).shuffle(lati)
    testi = {"con": con, "senza": senza}
    domanda = GIUDICE.format(prompt=caso["prompt"], atteso=caso["expected_output"],
                             a=testi[lati[0]].strip(), b=testi[lati[1]].strip())
    lavoro = Path(tempfile.mkdtemp(prefix="italian-master-giudice-"))
    try:
        processo = subprocess.run([shutil.which("claude") or "claude", "-p", "--output-format", "json", "--model", modello],
                                  input=domanda, capture_output=True, text=True, encoding="utf-8", cwd=lavoro, timeout=600)
    finally:
        shutil.rmtree(lavoro, ignore_errors=True)
    risultato = json.loads(processo.stdout or "{}").get("result") or ""
    if esegui.LIMITE.search(risultato[:300]):
        esegui.limite_raggiunto.set()
        raise RuntimeError("limite di utilizzo del piano raggiunto")
    trovato = re.search(r"\{.*\}", risultato, re.DOTALL)
    if not trovato:
        raise RuntimeError(f"giudizio illeggibile: {risultato[:200]}")
    voto = json.loads(trovato.group(0))
    vince = {"A": lati[0], "B": lati[1]}.get(str(voto.get("vince")).strip().upper(), "pari")
    return {"vince": vince, "motivo": voto.get("motivo", ""), "ordine": lati}


def formule(testo):
    """(formule segnalate, parole) del testo senza le citazioni."""
    # Una parola neutra al posto della citazione, perché non restino spazi doppi da segnalare.
    pulito = CITAZIONI.sub(lambda m: "" if "→" in m.group(0) else "citazione", testo)
    esito, _ = controlla.analizza(pulito)
    return sum(len(v) for k, v in esito.items() if k not in NON_FORMULE), controlla.conta_parole(pulito)


def misura_formule(cartella, casi, ripeti):
    trovate = parole = risposte = 0
    for caso in casi:
        for giro in range(1, ripeti + 1):
            file = cartella / caso["name"] / str(giro) / "risposta.md"
            if file.exists():
                f, p = formule(file.read_text(encoding="utf-8"))
                trovate, parole, risposte = trovate + f, parole + p, risposte + 1
    return round(trovate * 1000 / parole, 2) if parole else None, risposte


def attivazioni(cartella, casi, ripeti):
    conto = 0
    for caso in casi:
        for giro in range(1, ripeti + 1):
            file = cartella / caso["name"] / str(giro) / "strumenti.json"
            if file.exists():
                strumenti = json.loads(file.read_text(encoding="utf-8"))["strumenti"]
                conto += any(s.startswith("Skill:") and "italian-master" in s for s in strumenti)
    return conto


def caricata(cartella, casi, ripeti):
    """Vero se almeno una sessione elencava la skill tra quelle disponibili."""
    for caso in casi:
        for giro in range(1, ripeti + 1):
            file = cartella / caso["name"] / str(giro) / "sessione.jsonl"
            if file.exists() and re.search(r'"skills":\[[^\]]*italian-master', file.read_text(encoding="utf-8")):
                return True
    return False


def misura_versione(rif, casi, senza_dir, args):
    copia = None
    if rif == "HEAD":
        plugin, commit = REPO, git("rev-parse", "HEAD")
    else:
        commit = git("rev-parse", rif + "^{commit}")
        copia = Path(tempfile.mkdtemp(prefix="italian-master-bench-")) / "versione"
        git("worktree", "add", "--detach", str(copia), commit)
        plugin = copia
    try:
        versione = versione_di(plugin)
        cartella = USCITA / f"v{versione}"
        print(f"\n== {versione} ({commit[:7]})")
        esegui_lato(casi, cartella, plugin, args.ripeti, args.modello, args.paralleli)
    finally:
        if copia:
            git("worktree", "remove", "--force", str(copia))

    coppie = []
    for caso in casi:
        for giro in range(1, args.ripeti + 1):
            con_file = cartella / caso["name"] / str(giro) / "risposta.md"
            senza_file = senza_dir / caso["name"] / str(giro) / "risposta.md"
            giudizio_file = cartella / caso["name"] / str(giro) / "giudizio.json"
            if con_file.exists() and senza_file.exists():
                coppie.append((caso, giro, con_file, senza_file, giudizio_file))

    def lavora(coppia):
        caso, giro, con_file, senza_file, giudizio_file = coppia
        if giudizio_file.exists() or esegui.limite_raggiunto.is_set():
            return
        try:
            voto = giudica(caso, con_file.read_text(encoding="utf-8"), senza_file.read_text(encoding="utf-8"),
                           f"{versione}/{caso['name']}/{giro}", args.giudice)
            giudizio_file.write_text(json.dumps(voto, ensure_ascii=False, indent=2), encoding="utf-8")
        except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as errore:
            print(f"   giudizio {caso['name']} giro {giro}: non riuscito, {errore}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.paralleli) as gruppo:
        list(gruppo.map(lavora, coppie))

    voti = [json.loads(c[4].read_text(encoding="utf-8"))["vince"] for c in coppie if c[4].exists()]
    conto = {k: voti.count(k) for k in ("con", "senza", "pari")}
    ogni_mille, risposte = misura_formule(cartella, casi, args.ripeti)
    totale = len(casi) * args.ripeti
    if len(voti) < totale:
        print(f"   incompleta: {len(voti)} giudizi su {totale}; rilancia lo stesso comando per finire")
    return {"versione": versione, "commit": commit[:7], "data": git("log", "-1", "--format=%cs", commit),
            "vittorie": conto["con"], "pari": conto["pari"], "sconfitte": conto["senza"], "giudizi": len(voti),
            "quota": round((conto["con"] + conto["pari"] / 2) / len(voti), 3) if voti else None,
            "formule_ogni_mille": ogni_mille, "risposte": risposte,
            "attivazioni": attivazioni(cartella, casi, args.ripeti), "completa": len(voti) == totale,
            "caricata": caricata(cartella, casi, args.ripeti)}


def chiave_versione(voce):
    return tuple(int(n) for n in voce["versione"].split("."))


def main():
    for flusso in (sys.stdout, sys.stderr):
        try:
            flusso.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(description="Benchmark della skill contro Claude senza skill.")
    parser.add_argument("versioni", nargs="*", help="tag, commit o HEAD")
    parser.add_argument("--ripeti", type=int, default=2, help="esecuzioni per caso (predefinito: 2)")
    parser.add_argument("--modello", default="sonnet", help="modello che scrive (predefinito: sonnet)")
    parser.add_argument("--giudice", default="opus", help="modello che giudica (predefinito: opus)")
    parser.add_argument("--paralleli", type=int, default=4, help="sessioni in parallelo (predefinito: 4)")
    parser.add_argument("--grafico", action="store_true", help="ridisegna soltanto il grafico")
    args = parser.parse_args()

    casi = json.loads(CASI.read_text(encoding="utf-8"))["evals"]
    esiti = json.loads(ESITI.read_text(encoding="utf-8")) if ESITI.exists() else {"versioni": []}
    if not args.grafico:
        if not args.versioni:
            parser.error("indica almeno una versione, oppure --grafico")
        senza_dir = USCITA / f"senza-{args.modello}"
        print("== Claude senza skill")
        esegui_lato(casi, senza_dir, None, args.ripeti, args.modello, args.paralleli)
        ogni_mille, risposte = misura_formule(senza_dir, casi, args.ripeti)
        esiti.update({"modello": args.modello, "giudice": args.giudice, "casi": len(casi), "ripetizioni": args.ripeti,
                      "senza": {"formule_ogni_mille": ogni_mille, "risposte": risposte}})
        for rif in args.versioni:
            if esegui.limite_raggiunto.is_set():
                break
            voce = misura_versione(rif, casi, senza_dir, args)
            if not voce["caricata"]:
                print("   attenzione: Claude Code non ha caricato la skill di questa versione, il grafico la esclude")
            esiti["versioni"] = sorted([v for v in esiti["versioni"] if v["versione"] != voce["versione"]] + [voce],
                                       key=chiave_versione)
            print(f"   con la skill meglio {voce['vittorie']}, pari {voce['pari']}, peggio {voce['sconfitte']}; "
                  f"formule ogni mille parole {voce['formule_ogni_mille']} (senza skill {ogni_mille}); "
                  f"skill attivata {voce['attivazioni']} volte su {voce['risposte']}")
        esiti["aggiornato"] = datetime.date.today().isoformat()
        ESITI.write_text(json.dumps(esiti, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if esegui.limite_raggiunto.is_set():
            print("\nIl piano ha raggiunto il limite di utilizzo: rilancia lo stesso comando più tardi per finire.")
    import grafico_benchmark
    grafico_benchmark.disegna(esiti, GRAFICO)
    print(f"\nGrafico: {GRAFICO}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

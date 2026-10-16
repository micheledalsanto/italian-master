"""Disegna il grafico del benchmark (SVG, chiaro e scuro) da evals/benchmark/esiti.json.

Una linea per versione: quanto spesso il testo con la skill è giudicato migliore di quello di
Claude senza skill, con il 50% (alla pari) come riferimento. Le altre misure stanno nella tabella
del README. Solo libreria standard.
"""

from html import escape
from pathlib import Path

TESTI = {
    "it": {
        "titolo": "Testi giudicati migliori con la skill, versione dopo versione",
        "sotto": "Contro Claude senza skill, sulle stesse richieste, giudicati alla cieca. La fascia è il rumore del giudice.",
        "pari": "alla pari",
        "piede": "{casi} casi × {rip} esecuzioni per versione · scrive {mod}, giudica {giu} · aggiornato al {data}",
    },
    "en": {
        "titolo": "Texts judged better with the skill, version by version",
        "sotto": "Against Claude without the skill, on the same requests, judged blind. The band is the judge's noise.",
        "pari": "even",
        "piede": "{casi} cases × {rip} runs per version · written by {mod}, judged by {giu} · updated {data}",
    },
}

STILE = """
.sfondo{fill:#fcfcfb}.t1{fill:#0b0b0b}.t2{fill:#52514e}.t3{fill:#73726c}
.fascia{fill:#ecebe7}.griglia{stroke:#e4e3df}.rif{stroke:#a3a29b}.serie{stroke:#2a78d6}.punto{fill:#2a78d6;stroke:#fcfcfb}
@media (prefers-color-scheme: dark){
.sfondo{fill:#1a1a19}.t1{fill:#f0efec}.t2{fill:#c3c2b7}.t3{fill:#9c9b93}
.fascia{fill:#262624}.griglia{stroke:#33332f}.rif{stroke:#6f6e68}.serie{stroke:#3987e5}.punto{fill:#3987e5;stroke:#1a1a19}}
text{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
"""

LARGHEZZA, ALTEZZA = 760, 340
SINISTRA, DESTRA, SOPRA, SOTTO = 56, 90, 84, 70

MESI = {"it": "gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split(),
        "en": "January February March April May June July August September October November December".split()}


def data(iso, lingua):
    if not iso:
        return ""
    anno, mese, giorno = (int(n) for n in iso.split("-"))
    mese = MESI[lingua][mese - 1]
    return f"{giorno} {mese} {anno}" if lingua == "it" else f"{mese} {giorno}, {anno}"


def pct(valore):
    return f"{round(valore * 100)}%"


def svg(esiti, lingua):
    t = TESTI[lingua]
    # Una versione che Claude Code non ha caricato misura Claude contro Claude, non la skill.
    voci = [v for v in esiti["versioni"] if v.get("quota") is not None and v.get("caricata", True)]
    alto, basso = SOPRA, ALTEZZA - SOTTO
    sx, dx = SINISTRA, LARGHEZZA - DESTRA
    y = lambda v: basso - v * (basso - alto)  # noqa: E731
    n = len(voci)
    x = (lambda i: (sx + dx) / 2) if n == 1 else (lambda i: sx + i * (dx - sx) / (n - 1))
    parti = [f'<text class="t1" x="16" y="30" font-size="16" font-weight="600">{escape(t["titolo"])}</text>',
             f'<text class="t2" x="16" y="52" font-size="12.5">{escape(t["sotto"])}</text>']
    rumore = esiti.get("rumore", {}).get("quota")
    if rumore is not None:
        scarto = abs(0.5 - rumore)
        parti.append(f'<rect class="fascia" x="{sx}" y="{y(0.5 + scarto):.1f}" width="{dx - sx}" '
                     f'height="{y(0.5 - scarto) - y(0.5 + scarto):.1f}"/>')
    for v in (0, 0.25, 0.5, 0.75, 1):
        classe, spessore = ("rif", 1.5) if v == 0.5 else ("griglia", 1)
        parti.append(f'<line class="{classe}" x1="{sx}" x2="{dx}" y1="{y(v):.1f}" y2="{y(v):.1f}" stroke-width="{spessore}"/>')
        parti.append(f'<text class="t3" x="{sx - 10}" y="{y(v) + 4:.1f}" font-size="11" text-anchor="end">{pct(v)}</text>')
    parti.append(f'<text class="t2" x="{dx + 10}" y="{y(0.5) + 4:.1f}" font-size="11">{escape(t["pari"])}</text>')
    for i, voce in enumerate(voci):
        parti.append(f'<text class="t3" x="{x(i):.1f}" y="{basso + 22}" font-size="11.5" text-anchor="middle">'
                     f'{escape(voce["versione"])}</text>')
    if n > 1:
        traccia = " ".join(f"{x(i):.1f},{y(v['quota']):.1f}" for i, v in enumerate(voci))
        parti.append(f'<polyline class="serie" points="{traccia}" fill="none" stroke-width="2" '
                     'stroke-linejoin="round" stroke-linecap="round"/>')
    for i, voce in enumerate(voci):
        parti.append(f'<circle class="punto" cx="{x(i):.1f}" cy="{y(voce["quota"]):.1f}" r="4.5" stroke-width="2">'
                     f'<title>{escape(voce["versione"])}: {pct(voce["quota"])}</title></circle>')
    if voci:
        ultima = voci[-1]
        parti.append(f'<text class="t1" x="{x(n - 1) + 10:.1f}" y="{y(ultima["quota"]) - 8:.1f}" font-size="13" '
                     f'font-weight="600">{pct(ultima["quota"])}</text>')
    piede = t["piede"].format(casi=esiti["casi"], rip=esiti["ripetizioni"], mod=esiti["modello"].capitalize(),
                              giu=esiti["giudice"].capitalize(), data=data(esiti.get("aggiornato", ""), lingua))
    parti.append(f'<text class="t3" x="16" y="{ALTEZZA - 14}" font-size="11">{escape(piede)}</text>')
    descrizione = "; ".join(f"{v['versione']}: {pct(v['quota'])}" for v in voci)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LARGHEZZA} {ALTEZZA}" width="{LARGHEZZA}" '
            f'height="{ALTEZZA}" role="img" aria-label="{escape(t["titolo"])}. {escape(descrizione)}">'
            f"<style>{STILE}</style>"
            f'<rect class="sfondo" width="{LARGHEZZA}" height="{ALTEZZA}" rx="8"/>' + "".join(parti) + "</svg>\n")


def disegna(esiti, percorso):
    percorso = Path(percorso)
    percorso.write_text(svg(esiti, "it"), encoding="utf-8")
    percorso.with_suffix(".en.svg").write_text(svg(esiti, "en"), encoding="utf-8")

#!/usr/bin/env python3
"""Segnala i sospetti più comuni di "sbobba artificiale" in un testo italiano.

Uso:
    python controlla.py testo.md
    python controlla.py bozza.txt altro.md
    cat testo.txt | python controlla.py
    python controlla.py testo.md --json
    python controlla.py testo.md --strict   # esce con codice 1 se trova qualcosa

È un aiuto alla rilettura, non un giudice: un testo senza segnalazioni può
essere pessimo, e una segnalazione può essere un falso allarme. Le spiegazioni
e le alternative sono in references/sbobba.md e negli altri riferimenti.

Solo libreria standard, Python 3.8 o successivo.
"""

import argparse
import json
import re
import statistics
import sys

# ---------------------------------------------------------------------------
# Formule: (espressione regolare, suggerimento). Ricerca senza distinzione
# tra maiuscole e minuscole. Per aggiungerne una basta una riga.
# ---------------------------------------------------------------------------

FORMULE = {
    "Aperture a tappeto": [
        (r"\bin un mondo (sempre più|in cui|dove)", "parti dal fatto"),
        (r"\bnel (panorama|contesto|mondo|scenario) (odierno|attuale|contemporaneo|digitale|moderno)", "parti dal fatto"),
        (r"\bnell'era (digitale|moderna|dell'|del |della )", "parti dal fatto"),
        (r"\bin un'epoca (in cui|di|dove)", "parti dal fatto"),
        (r"\bche tu sia\b", "scegli a chi parli"),
        (r"\bti sei mai chiest[oa]\b", "se è un trampolino, entra in argomento"),
        (r"\bquando si (tratta|parla) di\b", "«per», «quanto a», oppure il soggetto"),
        (r"\b(è|sono) (molto )?più di un[a']? ?semplic[ei]\b", "di' che cos'è"),
        (r"\bnegli ultimi anni\b.{0,60}\bsempre più\b", "che cosa è successo, quando, con che numeri"),
    ],
    "Falso contrasto": [
        (r"\bnon (è|sono|si tratta) (solo|soltanto|semplicemente|solamente)\b", "scrivi la parte affermativa"),
        (r"\bnon si tratta di\b.{0,80}\b(ma|bensì)\b", "scrivi la parte affermativa"),
        (r"\bnon solo\b.{0,80}\bma anche\b", "spesso basta «e»"),
    ],
    "Domanda e risposta a frammenti": [
        (r"\b(il|la|i|le) (risultato|verità|soluzione|risposta|buona notizia|cattiva notizia|parte migliore|segreto|problema|differenza|chiave)\?", "di' la cosa in una frase"),
        (r"\be indovina( un po')?\b", "taglia"),
        (r"\becco la verità\b|\bla verità è che\b|\bil punto è (questo|che)\b|\buna cosa è certa\b", "di' la cosa"),
    ],
    "Lessico gonfiato": [
        (r"\b(svolg\w+|gioc\w+|ricopr\w+|riveste?\w*) un ruolo (chiave|cruciale|fondamentale|centrale|determinante|essenziale|di primo piano)", "di' che cosa fa"),
        (r"\b(rappresenta|costituisce|si configura come|si pone come|si presenta come)\b", "quasi sempre «è»"),
        (r"\b(una )?testimonianza (di|del|della|dell')", "«dimostra», oppure taglia"),
        (r"\b(immergiamoci|tuffiamoci|addentriamoci|esploriamo insieme|scopriamo insieme|approfondiamo insieme)\b", "comincia e basta"),
        (r"\b(immerg\w+|tuff\w+|addentr\w+) (nel|nella|nell'|nei|nelle|in) ", "verbo da brochure, se è figurato"),
        (r"\bsblocc\w+ (il|tutto il|il tuo|il vero|il pieno|nuove|nuovi)", "«permettere», «rendere possibile»"),
        (r"\bnavig\w+ (le|la|il|i|tra le|tra i|nelle|in questo) (complessità|sfid\w+|incertezz\w+|cambiament\w+|panorama|scenario)", "«affrontare», «orientarsi»"),
        (r"\babbracci\w+ (il|la|l'|le|i|nuov\w+) ?(cambiament\w+|innovazion\w+|futuro|sfid\w+|tecnologi\w+|digitale)", "«accettare», «adottare»"),
        (r"\b(fare|fa|fanno|farà) leva su\b", "«usare»"),
        (r"\b(portare|porta|portano|porterà|portalo|portala) .{0,25}al livello successivo\b", "«migliorare», e come"),
        (r"\b(cambia|cambiano|cambiare|cambierà) le regole del gioco\b|\bgame[- ]changer\b", "di' che cosa cambia"),
        (r"\bfa(re|nno)? la differenza\b", "di' quale differenza"),
        (r"\bun ver[oa] e propri[oa]\b|\bdei veri e propri\b|\bdelle vere e proprie\b", "togli"),
        (r"\b(una )?(vasta|ampia) (gamma|varietà|scelta|selezione) di\b", "quanti e quali"),
        (r"\ba 360 gradi\b|\ba tutto tondo\b|\ba 360°", "«completo», oppure che cosa copre"),
        (r"\bsenza soluzione di continuità\b", "descrivi che cosa succede"),
        (r"\b(all'avanguardia|di ultima generazione|di prim'ordine|rivoluzionari[oaie]|innovativ[oaie])\b", "che cosa c'è di nuovo?"),
        (r"\b(arazzo|mosaico|sinfonia|crocevia) (di|del|della|dell')", "metafora da generatore"),
        (r"\bun (vero )?(viaggio|percorso) (di|verso|attraverso|alla scoperta|nel|nella)", "metafora da generatore, se figurata"),
        (r"\b(soluzion[ei]) (su misura|personalizzat[ae]|innovativ[ae]|integrat[ae]|complet[ae])", "quale soluzione?"),
        (r"\bal fine di\b|\ballo scopo di\b", "«per»"),
        (r"\b(potenziare|ottimizzare|massimizzare|valorizzare|elevare)\b", "«migliorare», «aumentare», e di quanto"),
    ],
    "Connettivi e riempitivi": [
        (r"\bè (importante|fondamentale|essenziale|cruciale|bene|utile|doveroso|opportuno) (notare|sottolineare|ricordare|comprendere|evidenziare|precisare|considerare|tenere presente|tenere a mente)", "togli e di' la cosa"),
        (r"\bvale la pena (notare|sottolineare|ricordare|menzionare|evidenziare)", "togli e di' la cosa"),
        (r"\b(va|occorre|bisogna|è da) (detto|precisare|sottolineare|notare|considerare) che\b", "togli e di' la cosa"),
        (r"\bnon è un caso (che|se)\b", "se c'è una causa, scrivila"),
        (r"\b(detto questo|detto ciò|ciò detto|in altre parole|in quest'ottica|in questo contesto|in tal senso)\b", "spesso si può togliere"),
        (r"\b(in aggiunta|oltre a ciò|allo stesso tempo|d'altra parte|d'altro canto)\b", "se non collega niente, togli"),
        (r"\bquell[oaie] che (è|sono|era|erano) (il|lo|la|i|gli|le|l')", "plastismo: togli «quello che è»"),
        (r"\b(andiamo|andremo|vado|andrò|vai|andate) a (vedere|analizzare|scoprire|esplorare|approfondire|illustrare|spiegare|definire|creare|inserire)\b", "usa il verbo senza «andare a»"),
        (r"\b(in termini di|a livello di|dal punto di vista di|per quanto riguarda|per quanto concerne|relativamente a|in merito a)\b", "«su», «di», «per»"),
    ],
    "Chiusure": [
        (r"^\s*(in conclusione|in definitiva|in sintesi|in sostanza|tirando le somme|per concludere|in ultima analisi|per riassumere|ricapitolando)\b", "il riassunto serve davvero?"),
        (r"\b(ciò|quello) che conta davvero\b|\balla fine,? ciò che conta\b", "morale: taglia"),
        (r"\bsolo il tempo (dirà|potrà dire|ci dirà)\b|\bil futuro è (tutto )?da scrivere\b", "taglia"),
        (r"\bnon resta che\b|\bcosa aspetti\?|\bche aspetti\?", "un invito preciso, se serve"),
    ],
    "Voce da assistente": [
        (r"^\s*(certamente|certo|assolutamente|ottima domanda|ottima idea|volentieri)[!,.]", "togli"),
        (r"\becco (il|la|un|una|i|le|a te|qui) .{0,40}(che hai (richiesto|chiesto)|rivist[oa]|aggiornat[oa]|migliorat[oa])", "consegna il testo e basta"),
        (r"\bspero (che )?(questo|ti|vi|le) (ti |vi |le )?(sia|possa|aiut)", "togli"),
        (r"\b(fammi|fatemi|mi faccia) sapere se\b", "togli, salvo in una vera email"),
        (r"\bse hai (altre|ulteriori) domande\b|\bnon esitare a (chiedere|contattarmi)\b", "togli, salvo in una vera email"),
        (r"\bin quanto (modello|intelligenza artificiale|assistente)\b|\bfino al mio ultimo aggiornamento\b", "residuo di chat"),
        (r"\[(nome|cognome|inserire|inserisci|data|azienda|link)[^\]]*\]", "segnaposto dimenticato"),
    ],
    "Vaghezza autorevole": [
        (r"\b(numerosi |molti |diversi |recenti |alcuni )?(studi|ricerche) (dimostrano|mostrano|suggeriscono|indicano|confermano|hanno dimostrato|hanno mostrato)", "quale studio? cita o togli"),
        (r"\b(secondo|stando a) (gli|molti|alcuni|diversi|numerosi) (esperti|studiosi|analisti|osservatori)", "chi? cita o togli"),
        (r"\b(molti|alcuni|diversi) (esperti|studiosi|critici|osservatori) (ritengono|sostengono|affermano|concordano)", "chi? cita o togli"),
        (r"\bsempre più (persone|aziende|italiani|utenti|consumatori|imprese|giovani)\b", "quante? da quando?"),
        (r"\bun numero (sempre )?crescente di\b", "quanti?"),
        (r"\bè (ampiamente|universalmente|generalmente) (riconosciuto|noto|risaputo|accettato)", "da chi?"),
    ],
    "Calchi dall'inglese": [
        (r"\b(assicurati|assicuratevi|si assicuri) di\b", "imperativo diretto: «controlla», «ricordati di»"),
        (r"\b(sentiti|sentitevi|si senta) liber[oaie] di\b", "«puoi», «pure»"),
        (r"\balla fine della giornata\b", "«alla fine», «in fin dei conti» (se non parli della sera)"),
        (r"\b(prenditi|prendetevi|si prenda) il (tuo|vostro|suo) tempo\b", "«fai con calma»"),
        (r"\bsulla stessa pagina\b", "«d'accordo», «allineati»"),
        (r"\bla buona notizia è che\b", "«per fortuna», oppure di' la notizia"),
        (r"\bfa(re|nno|ceva)? senso\b", "«avere senso»"),
        (r"\bnel lungo termine\b|\bnel breve termine\b", "«a lungo termine», «a breve»"),
        (r"\bgrazie per aver condiviso\b", "«grazie»"),
        (r"\bspero che questa (email|mail|e-mail) (ti|la|vi) trovi bene\b", "togli"),
        (r"\b(sono|siamo) eccitat[oaie] (di|per)\b", "«contento», «entusiasta»"),
        (r"\bper favore,? (nota|notate|clicca|cliccate|inserisci|inserite|seleziona|compila)", "nelle istruzioni niente «per favore»"),
        (r"\bops!? qualcosa è andato storto\b", "di' che cosa è successo e che cosa fare"),
        (r"\b(resta|restate|rimani|rimanete) sintonizzat[oi]\b", "«a presto», «ti aggiorniamo»"),
        (r"\bultimo ma non (meno importante|ultimo)\b", "«infine»"),
        (r"\b(prendere|prendi|prendo|preso) una (doccia|foto|pausa)\b", "«fare»"),
        (r"\bpag\w+ attenzione\b", "«fare attenzione», «prestare attenzione»"),
        (r"\b(salvare|salva|salvi|risparmiare) tempo e denaro\b", "formula da volantino; e «save time» è «risparmiare tempo»"),
        (r"\b(salvare|salva|salvi) (tempo|denaro|soldi)\b", "«risparmiare»"),
        (r"\b(spendere|spendi|speso|spendo) (del |il |molto |più |troppo )?tempo\b", "«passare», «dedicare» tempo"),
        (r"\bè qui per restare\b", "«durerà», «non è una moda»"),
    ],
    "Titolese ed esche": [
        (r"\becco (cosa|perché|come|chi|quando|quanto|dove)\b", "se nasconde la notizia, dilla"),
        (r"\bnon (crederai|indovinerai|immaginerai) mai\b", "esca"),
        (r"\b(fa|fanno|ha fatto) impazzire il web\b|\bil web (insorge|si divide|impazzisce)\b|\bla rete (insorge|si divide)\b", "esca"),
        (r"\btutti pazzi per\b", "esca"),
        (r"\bè (bufera|polemica|giallo|allarme|caos|scontro|gelo|boom|bagarre)\b", "che cosa è successo?"),
        (r"\b(clamoroso|incredibile|pazzesco|da brividi|senza parole|choc|shock)\b", "provoca l'emozione con il fatto"),
        (r"\bnessuno (ne parla|te lo dice|ti dice)\b|\bquello che nessuno ti dice\b", "formula logora"),
        (r"\bbrancol\w+ nel buio\b|\bmassimo riserbo\b|\bnell'occhio del ciclone\b|\balle prime luci dell'alba\b|\bcaccia all'uomo\b", "plastismo di cronaca"),
    ],
}

ORTOGRAFIA = [
    (r"\b(perch|poich|affinch|bench|finch|giacch|sicch|cosicch|purch|nonch|granch|anzich)è\b", "accento acuto: -ché"),
    (r"\b(n|s)è\b(?! stess)", "«né», «sé» con l'accento acuto (se non è un nome)"),
    (r"\b(ventitr|trentatr|quarantatr|cinquantatr|sessantatr|settantatr|ottantatr|novantatr)[eè]\b", "«-tré» con l'accento acuto"),
    (r"\bun pò\b|\bun po\b(?!')", "«un po'» con l'apostrofo"),
    (r"\bqual'(è|era|erano)\b", "«qual è» senza apostrofo"),
    (r"\b(perche|poiche|piu|gia|cosi|puo|cioe|pero|percio|sara|citta|qualita|attivita|societa|universita|verita|liberta|possibilita|realta|novita|necessita|lunedi|martedi|mercoledi|giovedi|venerdi)'", "apostrofo al posto dell'accento"),
    (r"\b(qu[ia])[ìà]\b|\bquì\b|\bquà\b", "«qui» e «qua» senza accento"),
    (r"\b(f|s|v|st)à\b|\bsò\b|\bdò\b|\bstò\b|\bfù\b|\bblù\b|\bsù\b", "monosillabo senza accento: fa, sa, va, sta, so, do, sto, fu, blu, su"),
    (r"\bse (avrei|sarei|potrei|dovrei|vorrei|farei|avresti|saresti|potresti|avrebbe|sarebbe|potrebbe|avremmo|saremmo|avrebbero|sarebbero)\b", "dopo «se» ipotetico va il congiuntivo (salvo interrogativa indiretta)"),
    (r"\b(aereoporto|aereoplano|metereolog\w+|pultroppo|propio|propia|avvolte|apposto|daccordo|d'avvero|sopratutto|sopprattutto|accellerare|accellera\w*|eccezzion\w+|coscenz\w+|conoscienz\w+|scenz\w+|ingegnier\w+|redarre|fin'ora|tutt'ora|c'è n'è|un'altro|qual'ora)\b", "ortografia"),
    (r"\b(un') ?(amico|altro|uomo|anno|albero|esempio|errore|elenco|ufficio|italiano|inizio|ordine|obiettivo|aspetto|argomento|evento|utente|articolo|elemento|approccio|ambiente|impegno|incontro|invito|oggetto)\b", "«un» senza apostrofo davanti a maschile"),
    (r"\b(i|dei|nei|sui|ai|dai|due|tre|molti|alcuni|tanti|questi|quei) (films|fans|computers|sports|bars|managers|leaders|clubs|goals|tests|links|posts|files|teams|brands|slogans)\b", "le parole straniere non prendono la -s del plurale"),
]

TIPOGRAFIA = [
    (r"(?<![\w'’])E'(?=\s)", "«È» con l'accento, non «E'»"),
    (r"—", "lineetta lunga all'inglese: prova virgole, due punti o parentesi; se resta, « – » con gli spazi"),
    (r"(?<=\w)–(?=\w)", "lineetta attaccata alle parole: per un inciso vuole gli spazi; per un intervallo usa il trattino"),
    (r"\b[\w'’]+, [\w'’]+(?: [\w'’]+)?, (e|o) ", "virgola prima di «e» o «o» in un elenco? (in italiano di norma no)"),
    (r"!{2,}|\?!|!\?", "punteggiatura da chat"),
    (r"\.{4,}|\.\.(?!\.)(?<!\.\.\.)", "i puntini di sospensione sono tre"),
    (r" [,.;:!?](?=\s|$)", "spazio prima della punteggiatura"),
    (r"(?<=\S)  +(?=\S)", "doppio spazio"),
    (r"\b\d{1,2}(:|\.)\d{2} ?(AM|PM|am|pm|a\.m\.|p\.m\.)", "ore all'italiana: 14:30, o «le 2 del pomeriggio»"),
    (r"(?<=[a-zà-ù0-9,;] )(Lunedì|Martedì|Mercoledì|Giovedì|Venerdì|Sabato|Domenica|Gennaio|Febbraio|Marzo|Aprile|Maggio|Giugno|Luglio|Agosto|Settembre|Ottobre|Novembre|Dicembre)\b", "giorni e mesi in minuscolo"),
    (r"\b\d{1,3}(,\d{3})+(\.\d+)?\b", "numero all'inglese? In italiano 1.250,50"),
    (r"\b(ed) (?![eE])[aiouAIOUàìòù]\w*|\b(ad) (?![aA])(?!esempio|eccezione|opera|ora\b)[eiouEIOU]\w*|\bod \w+", "d eufonica solo tra vocali uguali (salvo «ad esempio»)"),
]

GRAMMATICA_DA_GUARDARE = [
    (r"\bpiuttosto che\b", "corretto solo se vale «anziché», non «oppure»"),
    (r"(?<![\w'’])(Esso|Essa|Essi|Esse|Egli|Ella)\b", "pronome soggetto in disuso: ripeti il nome o sottintendi"),
    (r"(^|[.!?] )(Noi|Tu|Voi) (?!stess|che |e |o |per |non )\w+", "soggetto espresso: serve davvero?"),
    (r"\b(può|possono|potrebbe|potrebbero) (aiutare|contribuire|rivelarsi|risultare|essere utile|fare la differenza)\b", "cautela all'inglese: se aiuta, «aiuta»"),
]


def righe_utili(testo):
    """Restituisce (numero, riga) saltando i blocchi di codice e il frontmatter."""
    dentro_codice = False
    dentro_frontmatter = False
    for n, riga in enumerate(testo.splitlines(), 1):
        nuda = riga.strip()
        if n == 1 and nuda == "---":
            dentro_frontmatter = True
            continue
        if dentro_frontmatter:
            if nuda == "---":
                dentro_frontmatter = False
            continue
        if nuda.startswith("```") or nuda.startswith("~~~"):
            dentro_codice = not dentro_codice
            continue
        if dentro_codice:
            continue
        yield n, riga


def senza_markup(riga):
    """Toglie link, codice in linea e segni di markdown che confondono i controlli."""
    riga = re.sub(r"`[^`]*`", "§", riga)
    riga = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", riga)
    riga = re.sub(r"https?://\S+", " ", riga)
    return riga


def estratto(riga, inizio, fine, margine=30):
    a = max(0, inizio - margine)
    b = min(len(riga), fine + margine)
    pezzo = riga[a:b].strip()
    return ("…" if a > 0 else "") + pezzo + ("…" if b < len(riga) else "")


def cerca(gruppo, righe, flag=re.IGNORECASE):
    trovati = []
    for modello, nota in gruppo:
        rx = re.compile(modello, flag)
        for n, riga in righe:
            for m in rx.finditer(riga):
                trovati.append({"riga": n, "testo": estratto(riga, m.start(), m.end()), "nota": nota})
    trovati.sort(key=lambda t: t["riga"])
    return trovati


def titoli_all_inglese(righe_grezze):
    """Titoli markdown con la maiuscola su quasi tutte le parole."""
    trovati = []
    minuscole_ammesse = {"di", "a", "da", "in", "con", "su", "per", "tra", "fra", "e", "o", "il", "lo", "la", "i",
                         "gli", "le", "un", "una", "del", "della", "dei", "delle", "al", "alla", "nel", "nella"}
    for n, riga in righe_grezze:
        m = re.match(r"^\s{0,3}(#{1,6})\s+(.*)$", riga) or re.match(r"^\s*\*\*([^*]+)\*\*\s*$", riga)
        if not m:
            continue
        titolo = m.group(m.lastindex)
        parole = [p for p in re.findall(r"[A-Za-zÀ-ÿ']+", titolo) if len(p) > 1]
        if len(parole) < 3:
            continue
        resto = [p for p in parole[1:] if p.lower() not in minuscole_ammesse]
        if len(resto) >= 2 and sum(p[0].isupper() for p in resto) / len(resto) >= 0.75:
            if not titolo.isupper():
                trovati.append({"riga": n, "testo": titolo.strip(),
                                "nota": "maiuscole a ogni parola: in italiano solo la prima e i nomi propri"})
    return trovati


def forma(righe_grezze):
    trovati = []
    grassetti = 0
    elenchi_etichetta = 0
    emoji_elenco = 0
    rx_emoji = re.compile("^[\\s\\-*•]*[←-⯿\U0001F300-\U0001FAFF]")
    for n, riga in righe_grezze:
        grassetti += len(re.findall(r"\*\*[^*]+\*\*", riga))
        if re.match(r"^\s*([-*•]|\d+[.)])\s+\*\*[^*]+\*\*\s*[:.–-]", riga):
            elenchi_etichetta += 1
        if rx_emoji.match(riga):
            emoji_elenco += 1
    if elenchi_etichetta >= 3:
        trovati.append({"riga": 0, "testo": f"{elenchi_etichetta} voci di elenco nella forma «**Etichetta**: testo»",
                        "nota": "in un articolo o in una email scrivi un paragrafo"})
    if emoji_elenco >= 3:
        trovati.append({"riga": 0, "testo": f"{emoji_elenco} righe che cominciano con un'emoji",
                        "nota": "emoji come punti elenco"})
    return trovati, grassetti


# Misure prese su 86 articoli di otto testate italiane (settembre-ottobre 2026).
# Vedi references/periodo.md, connettivi.md e impronte.md.
RIFERIMENTO = ("nei giornali letti: 19-31 parole per frase, 3-15% di frasi fino a 6 parole, "
               "17-43% da 30 in su, 1,2-2,3 virgole per frase, 5-12 due punti ogni mille parole")


def conta_parole(t):
    return len(re.findall(r"[A-Za-zÀ-ÿ]+(?:['’][A-Za-zÀ-ÿ]+)?", t))


def statistiche(testo_pulito, grassetti, prosa):
    """Conteggi sul testo intero e misure del passo sulla sola prosa (senza titoli, elenchi, tabelle)."""
    trovati = []
    n_parole = conta_parole(testo_pulito)
    capoversi = [c.strip() for c in re.split(r"\n\s*\n", prosa) if conta_parole(c) >= 2]
    frasi = []
    chiuse_brevi = 0
    capoversi_lunghi = 0
    for c in capoversi:
        f = [x for x in re.split(r"(?<=[.!?…])[\"»”]?\s+(?=[A-ZÀ-Ý«“\"])", c.replace("\n", " ")) if conta_parole(x) >= 1]
        frasi.extend(f)
        if len(f) >= 3:
            capoversi_lunghi += 1
            if conta_parole(f[-1]) <= 8:
                chiuse_brevi += 1
    lunghezze = [conta_parole(f) for f in frasi]
    n_prosa = sum(lunghezze)
    dati = {"parole": n_parole, "frasi": len(lunghezze)}

    def ogni_mille(n, base=None):
        base = n_parole if base is None else base
        return n * 1000 / base if base else 0

    if len(lunghezze) >= 10 and n_prosa >= 150:
        media = statistics.mean(lunghezze)
        dev = statistics.pstdev(lunghezze)
        brevi = 100 * sum(1 for x in lunghezze if x <= 6) / len(lunghezze)
        lunghe = 100 * sum(1 for x in lunghezze if x >= 30) / len(lunghezze)
        testo_prosa = " ".join(frasi)
        virgole = testo_prosa.count(",") / len(lunghezze)
        duepunti = ogni_mille(testo_prosa.count(":"), n_prosa)
        dati.update({"parole_per_frase": round(media, 1), "variazione": round(dev / media, 2) if media else 0,
                     "frasi_fino_a_6_parole_pct": round(brevi), "frasi_da_30_parole_pct": round(lunghe),
                     "virgole_per_frase": round(virgole, 2), "due_punti_ogni_mille": round(duepunti, 1)})
        if media < 17:
            trovati.append({"riga": 0, "testo": f"frasi corte in fila: {media:.0f} parole in media",
                            "nota": "se è un testo da leggere, unisci le frasi che parlano della stessa cosa (" + RIFERIMENTO + ")"})
        if brevi > 15:
            trovati.append({"riga": 0, "testo": f"{brevi:.0f}% di frasi fino a 6 parole",
                            "nota": "la frase breve funziona se è rara e viene dopo un periodo lungo"})
        if lunghe < 10:
            trovati.append({"riga": 0, "testo": f"solo il {lunghe:.0f}% delle frasi arriva a 30 parole",
                            "nota": "mancano i periodi: principale all'inizio, aggiunte in coda"})
        if virgole < 1.0:
            trovati.append({"riga": 0, "testo": f"{virgole:.1f} virgole per frase".replace(".", ","),
                            "nota": "pochi incisi, apposizioni e subordinate"})
        if duepunti > 14:
            trovati.append({"riga": 0, "testo": f"{duepunti:.0f} due punti ogni mille parole",
                            "nota": "tieni quelli che introducono un elenco, una citazione o una conseguenza"})
        if media and dev / media < 0.33:
            trovati.append({"riga": 0, "testo": "frasi di lunghezza molto uniforme",
                            "nota": "alterna periodi lunghi e qualche frase breve"})
        if media > 42:
            trovati.append({"riga": 0, "testo": f"frasi lunghe in media {media:.0f} parole",
                            "nota": "qualche periodo va chiuso prima"})
        basso = testo_prosa.lower().replace("’", "'")
        puo = ogni_mille(len(re.findall(r"\b(?:può|possono|potrebbe|potrebbero)\b", basso)), n_prosa)
        che = ogni_mille(len(re.findall(r"\bche\b", basso)), n_prosa)
        un_una = 100 * sum(1 for f in frasi if re.match(r"[«“\"]?(?:Un|Una|Un')\b", f)) / len(frasi)
        misura = len(re.findall(r"\b(?:forse|probabilmente|però|infatti|proprio|quasi|ormai|insomma|eppure|dunque|un po'|del resto|"
                                r"in realtà|persino|piuttosto|abbastanza|comunque|magari|addirittura|appunto)(?![a-zà-ù])", basso))
        misura_10k = misura * 10000 / n_prosa
        dati.update({"puo_ogni_mille": round(puo, 1), "che_ogni_mille": round(che, 1),
                     "frasi_che_cominciano_con_un_una_pct": round(un_una), "parole_di_misura_ogni_10000": round(misura_10k)})
        if puo > 6:
            trovati.append({"riga": 0, "testo": f"«può», «possono», «potrebbe»: {puo:.0f} ogni mille parole (nei giornali circa 3)",
                            "nota": "se succede, scrivi che succede; se è un'ipotesi, di' di chi"})
        if un_una > 6:
            trovati.append({"riga": 0, "testo": f"{un_una:.0f}% delle frasi comincia con «Un» o «Una» (nei giornali il 2-3%)",
                            "nota": "soggetti generici: parti da una persona, un luogo, una data"})
        if che < 17 and n_prosa >= 300:
            trovati.append({"riga": 0, "testo": f"{che:.0f} «che» ogni mille parole (nei giornali 22-26)",
                            "nota": "poche relative e poche subordinate (nelle pagine di un sito è normale)"})
        if misura_10k < 30 and n_prosa >= 300:
            trovati.append({"riga": 0, "testo": f"quasi nessuna parola che lega o misura ({misura} in {n_prosa} parole)",
                            "nota": "mancano «però», «infatti», «forse», «proprio», «quasi», «ormai»: che rapporto c'è tra una frase e l'altra? (nelle pagine di un sito è normale)"})
        if capoversi_lunghi >= 4 and chiuse_brevi / capoversi_lunghi > 0.35:
            trovati.append({"riga": 0, "testo": f"{chiuse_brevi} capoversi su {capoversi_lunghi} finiscono con una frase breve",
                            "nota": "sentenza a fine capoverso: spesso il capoverso finisce meglio una frase prima"})

    triadi = len(re.findall(r"\b[\w'’]+, [\w'’]+(?: [\w'’]+)? e [\w'’]+", testo_pulito))
    if triadi >= 3 and ogni_mille(triadi) > 6:
        trovati.append({"riga": 0, "testo": f"{triadi} elenchi di tre elementi",
                        "nota": "la triade esce in automatico: conta quanti elementi hai davvero"})
    gerundi = len(re.findall(r", \w+(?:ando|endo)\b", testo_pulito))
    if gerundi >= 3 and ogni_mille(gerundi) > 5:
        trovati.append({"riga": 0, "testo": f"{gerundi} gerundi dopo virgola",
                        "nota": "se sono in coda alla frase e aggiungono effetti non dimostrati, toglili"})
    mente = len(re.findall(r"\b\w{4,}mente\b", testo_pulito))
    if mente >= 5 and ogni_mille(mente) > 15:
        trovati.append({"riga": 0, "testo": f"{mente} avverbi in -mente", "nota": "taglia gli intensificatori"})
    esclamativi = testo_pulito.count("!")
    if esclamativi >= 3 and ogni_mille(esclamativi) > 5:
        trovati.append({"riga": 0, "testo": f"{esclamativi} punti esclamativi", "nota": "uno in un testo è già tanto"})
    lineette = len(re.findall(r" – ", testo_pulito))
    if lineette >= 4 and ogni_mille(lineette) > 8:
        trovati.append({"riga": 0, "testo": f"{lineette} lineette", "nota": "prova virgole o parentesi"})
    if grassetti >= 6 and ogni_mille(grassetti) > 12:
        trovati.append({"riga": 0, "testo": f"{grassetti} grassetti",
                        "nota": "in un testo da leggere il grassetto in testa a ogni capoverso è un segnale"})
    imperativi = len(re.findall(r"(?:^|(?<=[.!?] ))(?:Taglia|Togli|Scrivi|Usa|Evita|Parti|Di'|Scegli|Prova|Guarda|Controlla|Rileggi|Chiediti|Ricorda)\b[^.!?\n]{0,25}[.!]", testo_pulito, re.M))
    if imperativi >= 5 and ogni_mille(imperativi) > 6:
        trovati.append({"riga": 0, "testo": f"{imperativi} imperativi secchi",
                        "nota": "il tono da istruttore va bene in una guida, non in un testo da leggere"})
    return trovati, dati


def analizza(testo):
    grezze = list(righe_utili(testo))
    pulite = [(n, senza_markup(r)) for n, r in grezze]
    testo_pulito = "\n".join(re.sub(r"^\s*(#{1,6}|[-*•>]|\d+[.)])\s+", "", r).replace("**", "").replace("*", "")
                             for _, r in pulite)
    esito = {}
    for categoria, gruppo in FORMULE.items():
        flag = re.IGNORECASE | re.MULTILINE
        esito[categoria] = cerca(gruppo, pulite, flag)
    esito["Ortografia"] = cerca(ORTOGRAFIA, pulite, re.IGNORECASE)
    esito["Tipografia"] = cerca(TIPOGRAFIA, pulite, 0) + titoli_all_inglese(grezze)
    esito["Da guardare"] = cerca(GRAMMATICA_DA_GUARDARE, pulite, 0)
    di_forma, grassetti = forma(grezze)
    prosa = []
    for _, r in pulite:
        if re.match(r"^\s*(#{1,6}\s|\||[-*•]\s|\d+[.)]\s)", r):
            prosa.append("")
        else:
            prosa.append(re.sub(r"^\s*>\s?", "", r).replace("**", "").replace("*", ""))
    di_ritmo, dati = statistiche(testo_pulito, grassetti, "\n".join(prosa))
    esito["Forma e ritmo"] = di_forma + di_ritmo
    esito = {k: v for k, v in esito.items() if v}
    return esito, dati


def stampa(nome, esito, dati):
    totale = sum(len(v) for v in esito.values())
    print(f"\n== {nome} ==")
    riepilogo = f"{dati.get('parole', 0)} parole, {dati.get('frasi', 0)} frasi"
    if "parole_per_frase" in dati:
        riepilogo += (f"\nPasso: {dati['parole_per_frase']} parole per frase, {dati['frasi_fino_a_6_parole_pct']}% fino a 6 parole, "
                      f"{dati['frasi_da_30_parole_pct']}% da 30 in su, {dati['virgole_per_frase']} virgole per frase, "
                      f"{dati['due_punti_ogni_mille']} due punti ogni mille parole"
                      f"\nImpronte: «può» {dati['puo_ogni_mille']} e «che» {dati['che_ogni_mille']} ogni mille parole, "
                      f"{dati['frasi_che_cominciano_con_un_una_pct']}% di frasi che cominciano con «Un/Una», "
                      f"{dati['parole_di_misura_ogni_10000']} parole di legame e misura ogni diecimila")
    print(riepilogo)
    if not totale:
        print("Nessuna segnalazione. Non vuol dire che il testo sia buono: rileggilo ad alta voce.")
        return
    for categoria, trovati in esito.items():
        print(f"\n{categoria} ({len(trovati)})")
        for t in trovati:
            dove = f"riga {t['riga']:>3}" if t["riga"] else "  testo "
            print(f"  {dove}  {t['testo']}")
            print(f"            → {t['nota']}")
    densita = totale * 1000 / max(dati.get("parole", 1), 1)
    print(f"\n{totale} segnalazioni ({densita:.0f} ogni mille parole). Sono indizi: decide chi scrive.")
    if "parole_per_frase" in dati:
        print("Le misure di passo e impronte valgono per i testi da leggere (articoli, saggi, newsletter, pagine), "
              "non per istruzioni, elenchi, dialoghi.")


def main():
    for flusso in (sys.stdout, sys.stderr):
        try:
            flusso.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(description="Segnala i sospetti di sbobba artificiale in un testo italiano.")
    parser.add_argument("file", nargs="*", help="file di testo o markdown; senza argomenti legge da stdin")
    parser.add_argument("--json", action="store_true", help="stampa il risultato in JSON")
    parser.add_argument("--strict", action="store_true", help="esce con codice 1 se ci sono segnalazioni")
    args = parser.parse_args()

    ingressi = []
    if args.file:
        for percorso in args.file:
            try:
                with open(percorso, encoding="utf-8-sig") as f:
                    ingressi.append((percorso, f.read()))
            except OSError as errore:
                print(f"Non riesco a leggere {percorso}: {errore}", file=sys.stderr)
                return 2
            except UnicodeDecodeError:
                print(f"{percorso} non è in UTF-8: salvalo in UTF-8 e riprova.", file=sys.stderr)
                return 2
    else:
        try:
            sys.stdin.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
        ingressi.append(("stdin", sys.stdin.read()))

    risultati = {}
    totale = 0
    for nome, testo in ingressi:
        esito, dati = analizza(testo)
        risultati[nome] = {"statistiche": dati, "segnalazioni": esito}
        totale += sum(len(v) for v in esito.values())
        if not args.json:
            stampa(nome, esito, dati)
    if args.json:
        print(json.dumps(risultati, ensure_ascii=False, indent=2))
    return 1 if (args.strict and totale) else 0


if __name__ == "__main__":
    sys.exit(main())

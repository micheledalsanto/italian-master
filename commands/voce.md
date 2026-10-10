---
description: Ricava una scheda di stile dai testi di un autore, con le misure e con la lettura
argument-hint: "[cartella o file dei testi] [bozza da confrontare]"
---

Ricava con la skill `italian-master` la scheda di stile dell'autore dei testi indicati qui sotto. Servono almeno due o tre testi dello stesso genere: se ce n'è uno solo, dillo e chiedine altri.

$ARGUMENTS

Procedi così:

1. Apri `references/imparare-una-voce.md` della skill e leggi i testi per intero.
2. Se puoi eseguire comandi, misura la voce con `python "${CLAUDE_PLUGIN_ROOT}/skills/italian-master/scripts/controlla.py" --voce` seguito dai file. Se l'utente ha indicato anche una bozza, aggiungi `--confronta` e il file della bozza.
3. Scrivi la scheda. Le misure dicono come è fatta la voce (persona, lunghezza delle frasi, punteggiatura, parole che tornano); il resto si ricava leggendo: come attacca, come chiude, che cosa non fa mai. Ogni osservazione deve essere verificabile sui testi, con un esempio breve quando serve.
4. Proponi all'utente di salvare la scheda nella configurazione della skill, alla voce dei testi di riferimento, e fallo solo se accetta.

Quando c'è una bozza, dopo la scheda di' in che cosa se ne allontana e riscrivi i passi che stonano.

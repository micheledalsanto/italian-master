---
description: Rivede un testo italiano con la skill italian-master e dice che cosa ha cambiato
argument-hint: "[file o testo da rivedere]"
disable-model-invocation: true
---

Carica prima la skill `italian-master` con lo strumento delle skill e leggine le regole, poi rivedi il testo indicato qui sotto. Se è il percorso di un file, leggilo; se non c'è niente, chiedi all'utente di incollare il testo o di indicare il file.

$ARGUMENTS

Procedi così:

1. Leggi la configurazione di tono e pubblico, se esiste, e apri il riferimento del genere a cui il testo appartiene.
2. Se puoi eseguire comandi, lancia `python "${CLAUDE_PLUGIN_ROOT}/skills/italian-master/scripts/controlla.py"` sul testo e tieni conto delle segnalazioni, che sono indizi e non verdetti.
3. Conserva i fatti, il contenuto e la voce dell'autore, compresa la persona con cui si rivolge al lettore. Non aggiungere dati che nell'originale non ci sono.
4. Consegna il testo rivisto e, sotto, poche righe in prosa su che cosa è cambiato e perché, raggruppate per tipo di intervento. Se una frase è vuota, dillo e chiedi il dato che manca.

Se l'utente ha chiesto solo una correzione di bozze, tocca gli errori veri e lascia stare lo stile.

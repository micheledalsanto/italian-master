---
description: Crea o aggiorna il file in cui la skill italian-master legge tono e pubblico
argument-hint: "[progetto | personale]"
---

Aiuta l'utente a compilare la configurazione della skill `italian-master`, cioè il file `italian-master.md` che dice per chi si scrive e con che tono.

$ARGUMENTS

Procedi così:

1. Cerca un file esistente: `.claude/italian-master.md` nel progetto, poi nella cartella personale. Se c'è, leggilo e chiedi che cosa va cambiato.
2. Se manca, parti dal modello che sta in `assets/italian-master.md` dentro la skill. Chiedi se la configurazione vale per questo progetto o per tutti: nel primo caso il file va in `.claude/` nel progetto, nel secondo nella cartella personale.
3. Fai poche domande, una alla volta, e solo su quello che non si capisce dal progetto: chi legge e quanto ne sa, il tono, tu, lei o voi, noi o io, quanto inglese, le eccezioni per tipo di testo. Le voci su cui l'utente non ha una preferenza restano vuote.
4. Se l'utente ha testi suoi da prendere a modello, proponi di ricavarne la scheda di stile.
5. Scrivi il file e mostra in poche righe che cosa contiene.

# Microcopy: i testi delle interfacce

Questo file serve quando il testo sta dentro un'applicazione o un sito e accompagna un'azione: un pulsante, l'etichetta di un campo, un messaggio di errore, una conferma, la schermata che compare quando non c'è ancora niente da mostrare. Sono testi di tre o quattro parole, che nessuno legge per intero e che tutti devono capire al primo sguardo, e per loro le regole sul periodo di `periodo.md` non valgono.

Le indicazioni vengono dalle stringhe di otto applicazioni a codice aperto, contate una per una, e da due guide di stile pubbliche. Le applicazioni non sono nominate e nessuna stringa è riportata: gli esempi sono scritti apposta, per un servizio inventato di prenotazione di visite mediche.

## Indice

1. I testi letti
2. Le misure
3. A chi si parla, e chi parla
4. Pulsanti e comandi
5. Messaggi di errore
6. Conferme
7. Stati vuoti, attese, operazioni riuscite
8. Punteggiatura e maiuscole
9. Le parole
10. I calchi che nelle interfacce vere non ci sono
11. Un esempio
12. In pratica

## 1. I testi letti

Circa quindicimila stringhe, per poco più di centomila parole, scaricate a ottobre 2026 dai file di lingua italiani di otto applicazioni: tre nate in italiano, tutte di servizi pubblici digitali (un'applicazione sanitaria per il telefono, un servizio di notifiche con valore legale, un'area riservata per gli enti), e cinque tradotte dall'inglese da gruppi di volontari o di professionisti italiani (un browser, un programma di messaggistica, un social network, un servizio di archiviazione, un sistema per costruire siti). Le prime dicono come scrive chi progetta un'interfaccia in italiano, le seconde come si è assestato in vent'anni l'italiano del software.

Le due guide sono quella sul linguaggio dei servizi digitali della pubblica amministrazione e quella di un gruppo di localizzazione di software libero. Sono citate in `fonti.md`.

## 2. Le misure

| | Tre applicazioni nate in italiano | Cinque tradotte |
| --- | --- | --- |
| Parole per stringa, in media | da 6 a 12 | da 5 a 7 |
| Stringhe di una, due o tre parole | dal 27 al 57% | dal 36 al 50% |
| Stringhe brevi che finiscono con il punto | 0-2% | 1-10% |
| Frasi di sei parole o più che finiscono con un punto | 62-73% | 51-84% |
| Stringhe con un punto esclamativo | 5-13 ogni mille | 1-15 ogni mille |
| Stringhe che danno del tu | 93-276 ogni mille | 41-143 ogni mille |
| Stringhe che danno del lei o del voi | nessuna, salvo due casi | nessuna, salvo tre casi |

Metà dell'interfaccia, quindi, è fatta di etichette di tre parole al massimo, e l'altra metà di frasi intere che spiegano: nelle applicazioni nate in italiano supera le quindici parole dal 13 al 29% delle stringhe, e la percentuale più alta è quella dell'applicazione sanitaria, che ha più cose da spiegare. Il microcopy non è scrivere corto dappertutto. È scrivere corto dove si agisce e per esteso dove si spiega.

## 3. A chi si parla, e chi parla

**Tu.** In tutte e otto le applicazioni il lettore riceve il tu, comprese le tre dei servizi pubblici, dove ci si aspetterebbe il lei. La guida al linguaggio della pubblica amministrazione chiede proprio questo: forme dirette in seconda persona, «Registrati sul sito» e non «È possibile registrarsi». Il lei resta nelle lettere e nei documenti che lo stesso ente manda (vedi `corrispondenza-formale.md`), e in un'interfaccia si usa solo se il committente lo chiede.

**Oppure l'impersonale, ma per tutta l'interfaccia.** Una parte del software tradotto segue una convenzione più vecchia, che evita di rivolgersi all'utente: imperativo sui pulsanti («Salva») e infinito o forma impersonale nelle spiegazioni («Per continuare, inserire il codice», «Visitare la pagina di aiuto»). È una scelta legittima e ancora diffusa nei programmi per computer. Mescolare le due nella stessa schermata, con «Inserisci il codice» sopra e «Selezionare un file» sotto, è l'errore.

**Noi, quando qualcosa non va.** Nel servizio di notifiche, che è il più curato dei tre italiani, l'applicazione parla in prima persona plurale soprattutto negli errori: non «Impossibile caricare i dati» ma, nella stessa forma, «Non siamo riusciti a caricare i tuoi appuntamenti». Chi legge capisce che l'errore non è suo.

**Le domande dell'utente in prima persona.** Nelle pagine di aiuto i titoli sono le domande come le farebbe chi usa il servizio: «Cosa devo fare?», «Come funziona la delega?». È lo stesso principio di `tono-accogliente.md`.

## 4. Pulsanti e comandi

**Imperativo.** Nelle stringhe brevi delle otto applicazioni i comandi all'imperativo («Salva», «Annulla», «Continua») sono più di mille, e quelli all'infinito («Salvare») meno di quaranta. L'infinito sui pulsanti è un uso che il software italiano ha abbandonato.

**Verbo e oggetto.** Quando sulla schermata c'è più di un'azione, il pulsante dice anche su che cosa agisce: «Prenota la visita», «Scarica il referto». L'articolo si tiene in poco più della metà dei casi e si toglie quando lo spazio è poco («Aggiungi contatto»): vanno bene tutte e due le forme, purché in tutta l'interfaccia sia la stessa.

**Il pulsante ripete il verbo della domanda.** Sotto «Vuoi annullare la prenotazione?» stanno «Annulla la prenotazione» e «Torna indietro», non «Sì» e «No», e nemmeno «Conferma» e «Annulla», che in questo caso si contraddicono.

**I titoli delle finestre sono nomi.** «Nuova prenotazione», «Dati di fatturazione», «Modifica del profilo».

## 5. Messaggi di errore

Un messaggio di errore dice che cosa è successo, e poi che cosa può fare chi legge. Quando è breve le due cose stanno in due frasi, ed è uno dei pochi casi in cui la frase di quattro parole è la forma giusta.

Le formule contate nelle otto applicazioni:

| Formula | Dove si trova | Nota |
| --- | --- | --- |
| «Si è verificato un errore» | In sette su otto | È la formula neutra. Da sola non basta: va seguita da che cosa fare |
| «Non è stato possibile» più infinito | In tutte e otto | Dice la stessa cosa nominando l'azione che non è riuscita |
| «Non siamo riusciti a» più infinito | Nove stringhe ogni mille in una delle italiane, rara altrove | L'applicazione si prende la responsabilità |
| «Impossibile» più infinito | 17-33 ogni mille stringhe in tre tradotte, quasi mai nelle italiane | È l'impronta del software tradotto (*Unable to*, *Cannot*). Si capisce, ma è secca |
| «Riprova», «Riprova più tardi» | In tutte e otto | La chiusura normale. «Più tardi» solo se il problema è del servizio |
| «Qualcosa è andato storto» | Nove volte in tutto, sei nelle italiane | Regge come titolo, se sotto c'è la spiegazione |
| «Ops» | Quattro volte su quindicimila stringhe | Non è l'italiano delle interfacce |

Per i campi di un modulo la forma è nominale e senza punto: «Indirizzo email non valido», «Codice fiscale non valido», «Campo obbligatorio». «Non valido» è la formula di gran lunga più comune, e conviene aggiungere il formato atteso quando l'utente non può indovinarlo: «Data non valida. Scrivila così: 12/03/2027».

Quando l'errore è dell'utente lo si dice senza rimproverare e senza scusarsi: «Hai inserito un codice sbagliato per tre volte. Chiedine uno nuovo e riprova». Quando è del servizio lo si dice chiaramente, perché chi legge non perda tempo a cercare che cosa ha sbagliato: «Il servizio non è disponibile per un problema tecnico. Riprova più tardi».

## 6. Conferme

Si chiede conferma solo per quello che non si può annullare o che ha un costo. Le forme contate sono tre: «Vuoi davvero…?» (33 volte), «Confermi di voler…?» (22, la preferita dalle applicazioni italiane) e «Sei sicuro di voler…?» (20, calco di *Are you sure you want to*, che una delle due guide sconsiglia). La prima e la seconda sono preferibili, e la terza obbliga a scegliere tra «sicuro» e «sicura».

Sotto la domanda va la conseguenza, in una frase: «Vuoi annullare la visita del 12 marzo? Il posto tornerà disponibile per altri pazienti».

## 7. Stati vuoti, attese, operazioni riuscite

**Niente da mostrare.** Le due forme sono «Nessun…» (169 stringhe, in tutte le applicazioni) e «Non hai ancora…» (143). La prima sta bene per i risultati di una ricerca («Nessun risultato per questa ricerca»), la seconda per le cose che l'utente potrebbe aggiungere, e allora dice anche come: «Non hai ancora prenotato nessuna visita. Per farlo, cerca un medico o una prestazione».

**Attesa.** Un nome, con «in corso» o con i puntini: «Caricamento in corso», «Invio…». I puntini di attesa sono un uso dei programmi per computer, e le applicazioni italiane per il web quasi non li hanno.

**Operazione riuscita.** Participio e avverbio, senza soggetto e senza festa: «Prenotazione annullata», «Indirizzo email aggiunto correttamente». «Correttamente» si trova in tutte e otto le applicazioni, «con successo», che ricalca *successfully*, in tre.

## 8. Punteggiatura e maiuscole

- Pulsanti, etichette, voci di menu, titoli e messaggi di un campo non hanno il punto finale.
- Le frasi intere lo hanno in sei o sette casi su dieci. La regola pratica è che una frase sola, in un avviso breve, può farne a meno, e che due frasi di seguito lo vogliono tutte e due. Quello che conta è decidere una volta.
- Il punto esclamativo compare in una stringa su cento o meno. Per un'operazione riuscita non serve.
- La maiuscola va solo alla prima parola e ai nomi propri: «Salva le modifiche», non «Salva Le Modifiche». Le maiuscole a ogni parola sono la traccia più visibile di un'interfaccia tradotta male.
- I nomi dei pulsanti citati in una frase stanno tra virgolette: «Per riprovare premi “Annulla”».

## 9. Le parole

Le scelte su cui le otto applicazioni sono d'accordo, o quasi. Tra parentesi quante volte compare ciascuna forma.

| Si usa | Molto meno | Nota |
| --- | --- | --- |
| Accedi (131), Esci (27) | login (29), logout (9) | «Login» resta come nome: «dati di login» |
| email (200) | e-mail (0), posta elettronica (11) | Senza trattino, e mai «mail» da sola |
| password (207), nome utente (102) | parola d'ordine (12), username (2) | |
| Elimina (295) | Cancella (45) | «Rimuovi» (117) per togliere da un elenco senza distruggere |
| Impostazioni (200) | Preferenze (16) | |
| Scarica (66), Carica (249) | download (35), upload (17) | |
| Continua (67) | Prosegui (25), Avanti (7) | |
| Annulla (85), Chiudi (56) | | «Annulla» interrompe un'azione, «Chiudi» una finestra |
| dispositivo (96), cartella (97) | device (0), directory (23) | |
| link (338), file (455), account (164) | collegamento (28) | Non si traducono |
| Seleziona (276) | Premi (42), Clicca (35), Fai clic (28), Tocca (6) | «Seleziona» vale per il mouse e per il dito |
| Scopri di più (42) | Ulteriori informazioni (24), Maggiori informazioni (14) | |
| facoltativo (12), opzionale (7) | | Tutte e due in uso |

I plurali inglesi restano invariati (i file, i link, gli account), e un termine scelto resta lo stesso in tutta l'interfaccia: se nella prima schermata è «prenotazione», nella terza non diventa «appuntamento».

## 10. I calchi che nelle interfacce vere non ci sono

Un'interfaccia generata in italiano si riconosce da formule che traducono l'inglese parola per parola e che nelle quindicimila stringhe lette mancano del tutto o quasi.

| Calco | Quante volte nel campione | In italiano |
| --- | --- | --- |
| Per favore inserisci, Per favore attendi | 5, tutte nella stessa applicazione | Inserisci, Attendi |
| Ops! Qualcosa è andato storto | «Ops» 4 volte | Che cosa è successo e che cosa fare |
| Congratulazioni!, Complimenti!, Fantastico!, Perfetto! | 3 in tutto | «Prenotazione confermata» |
| Operazione completata con successo | «con successo» 17 volte in 3 applicazioni | «Prenotazione salvata», o «correttamente» |
| Benvenuto a bordo!, Sei tutto pronto! | «Benvenuto» in testa 2 volte | La prima cosa da fare |
| Non esitare a contattarci | Mai | «Hai bisogno di aiuto?», con il recapito |

Una correzione a quello che dice `calchi.md`: «Assicurati di» nelle istruzioni di un'interfaccia non è un segnale. Si trova in sei applicazioni su otto, comprese le italiane, nei casi in cui c'è davvero una condizione da verificare prima di procedere («Assicurati che il telefono sia collegato a Internet»). Resta un calco in un articolo o in una pagina di presentazione.

L'italiano occupa circa un quinto di spazio in più dell'inglese. Quando una stringa non entra si cerca la parola più corta («Invia» e non «Procedi all'invio»), e gli articoli non si tolgono dalle frasi per farle entrare.

## 11. Un esempio

Il compito: i testi della schermata con cui un paziente annulla una visita, e dell'errore che compare se l'annullamento non riesce. La visita è il 12 marzo alle 9:30, e si può annullare senza costi fino al giorno prima.

Versione calcata dall'inglese:

> **Sei Sicuro Di Voler Annullare?**
>
> Per favore nota che questa azione non può essere annullata!
>
> [Sì] [No]
>
> Ops! Qualcosa è andato storto. Per favore riprova più tardi.

Versione scritta in italiano:

> **Vuoi annullare la visita del 12 marzo?**
>
> La visita delle 9:30 sarà cancellata e il posto tornerà disponibile. Fino all'11 marzo l'annullamento è gratuito.
>
> [Annulla la visita] [Torna indietro]
>
> Non siamo riusciti ad annullare la visita. La prenotazione è ancora valida: riprova tra qualche minuto, oppure chiama il centro.

Nella prima versione «annullare» ha due significati nella stessa schermata, i pulsanti non dicono che cosa fanno e l'errore non dice se la visita è stata annullata oppure no, che è la sola cosa che al paziente interessa. Nella seconda ogni stringa risponde a una domanda che chi legge ha in quel momento.

## 12. In pratica

- Prima di scrivere, chiedi o deduci se l'interfaccia dà del tu o usa l'impersonale, e guarda le stringhe che esistono già: i termini e la persona sono quelli.
- Sui pulsanti un verbo all'imperativo, con l'oggetto se le azioni sono più d'una.
- In un errore: che cosa è successo, di chi è la causa quando si sa, che cosa fare adesso.
- In una conferma: la domanda con il verbo dell'azione, la conseguenza, due pulsanti che ripetono i verbi.
- Senza punto le etichette, senza punto esclamativo quasi tutto, maiuscola solo alla prima parola.
- Per ogni stringa, chiediti che cosa vuole sapere in quel momento chi la legge. Di solito è una cosa sola.
- Consegna le stringhe in una tabella o in un elenco con il nome dell'elemento accanto (titolo, testo, pulsante principale, pulsante secondario), e non inventare i dati che cambiano: date, importi e nomi vanno come variabili, tra parentesi graffe.

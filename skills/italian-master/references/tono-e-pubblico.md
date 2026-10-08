# Tono e pubblico: le scelte di chi usa la skill

Il tono e il pubblico di un testo li decide chi lo firma. Questo file spiega dove la skill trova quelle scelte, che cosa vuol dire ciascuna, e come comportarsi quando mancano.

## Indice

1. Dove sta la configurazione
2. Che cosa vale di più
3. I sei toni
4. Lo stesso avviso in sei toni
5. Il pubblico
6. Quando la configurazione manca
7. Quando tono e testo non vanno d'accordo

## 1. Dove sta la configurazione

Prima di scrivere cerca, in quest'ordine, un file `italian-master.md`:

1. nella cartella `.claude/` del progetto in cui stai lavorando;
2. nella cartella `.claude/` della home dell'utente (`~/.claude/italian-master.md`).

Se ci sono tutti e due, per ogni voce vale quella del progetto, e quella personale copre le voci che il progetto lascia vuote. Il modello da compilare è in `assets/italian-master.md`, e si crea con `npx italian-master configura`.

Il file ha sette parti: pubblico, tono, persona, lingua, testi di riferimento, tipi di testo, altre indicazioni. Una voce lasciata vuota, o con l'elenco delle alternative ancora tra parentesi, vale come non compilata.

Negli ambienti in cui non puoi leggere file, la configurazione può arrivare nella conversazione o nelle istruzioni del progetto: trattala allo stesso modo.

## 2. Che cosa vale di più

Quando le indicazioni sono più d'una, vincono nell'ordine:

1. quello che dice la richiesta («scrivilo più formale», «è per i fornitori»);
2. l'eccezione prevista nella configurazione per quel tipo di testo;
3. le voci generali della configurazione;
4. la voce ricavata dai testi di riferimento, per tutto quello che la configurazione non dice;
5. quello che si deduce dal contesto.

La configurazione decide il tono e il pubblico. Le regole della lingua (grammatica, punteggiatura, calchi, periodi) restano quelle della skill con qualunque tono.

## 3. I sei toni

| Tono | Chi parla, e a chi | Com'è fatto | Da leggere |
| --- | --- | --- | --- |
| formale | Uno studio, un'azienda o un ente che scrive a clienti, fornitori, utenti. Lei o voi | Frasi complete, formule di cortesia in apertura e in chiusura, date e scadenze in evidenza, nessuna battuta | `registri.md` |
| cordiale | Una persona che scrive a un'altra con cui lavora. Lei o tu secondo il rapporto | Diretto e breve, un saluto e un grazie, niente formule cerimoniose | `registri.md` |
| accogliente | Chi spiega una cosa a chi non la conosce. Tu, e noi per chi scrive | Parte dalla situazione del lettore, spiega prima di nominare, anticipa le domande | `tono-accogliente.md` |
| giornalistico | Una redazione che informa. Terza persona, o noi | La notizia in apertura, fatti con data e fonte, periodi di venti o trenta parole, nessun appello al lettore | `periodo.md`, `attacchi-e-chiusure.md`, `titoli.md` |
| tecnico | Chi documenta per chi deve fare una cosa. Impersonale, o tu nelle istruzioni | Termini esatti e sempre gli stessi, un'azione per frase, elenchi e titoletti, niente aggettivi di valore | `sintassi-stile.md`, `punteggiatura-tipografia.md` |
| commerciale | Un'azienda che presenta quello che offre. Tu o voi, e noi | Il vantaggio per chi legge detto con un fatto, frasi di una ventina di parole, un invito chiaro alla fine | `siti.md`, `agenzie-digitali.md` |

Il tono dice come si parla, non quanto si gonfia. In ognuno dei sei il difetto è lo stesso: le parole che occupano il posto di un fatto. Il formale gonfio mette due capoversi di cortesie prima delle date, il commerciale gonfio promette «soluzioni innovative», l'accogliente gonfio rassicura tre volte chi non aveva paura.

Se la configurazione descrive il tono con parole sue («formale ma senza formule», «come un collega che spiega»), parti dal tono della tabella più vicino e applica la correzione.

## 4. Lo stesso avviso in sei toni

Il fatto è uno solo: dal 1° marzo l'azienda manda le fatture per email e smette di spedirle per posta.

**Formale**

> Gentili Clienti, desideriamo informarvi che dal 1° marzo le fatture saranno trasmesse esclusivamente in formato elettronico, all'indirizzo di posta indicato in anagrafica. Vi invitiamo a verificarne la correttezza e a comunicarci eventuali variazioni entro il 20 febbraio.

**Cordiale**

> Buongiorno, dal 1° marzo vi manderemo le fatture solo per email, all'indirizzo che ci avete indicato. Se nel frattempo è cambiato, basta rispondere a questo messaggio entro il 20 febbraio.

**Accogliente**

> Dal 1° marzo la fattura ti arriva per email e non più per posta. Non devi fare niente: usiamo l'indirizzo che ci hai dato quando ti sei registrato, e se vuoi cambiarlo puoi farlo dalla tua area personale fino al 20 febbraio.

**Giornalistico**

> Dal 1° marzo l'azienda non spedirà più fatture di carta, e i clienti le riceveranno soltanto per email. Chi vuole cambiare l'indirizzo a cui arrivano ha tempo fino al 20 febbraio.

**Tecnico**

> Dal 1° marzo l'invio cartaceo delle fatture è disattivato. Le fatture sono inviate in PDF all'indirizzo registrato nel campo «Email di fatturazione» dell'anagrafica. Il campo si può modificare fino al 20 febbraio.

**Commerciale**

> Dal 1° marzo ricevi la fattura per email il giorno stesso in cui viene emessa, e le ritrovi tutte nella tua area personale. Controlla che l'indirizzo sia quello giusto: hai tempo fino al 20 febbraio.

In tutte e sei le versioni ci sono la data, la cosa che cambia e la scadenza. Cambiano la persona, le formule e l'ordine in cui le informazioni arrivano.

## 5. Il pubblico

La voce «quanto ne sa» decide che cosa si può dare per conosciuto.

| Pubblico | Termini | Spiegazioni | Esempi |
| --- | --- | --- | --- |
| esperti | Quelli del mestiere, senza spiegarli, anche in inglese | Solo di ciò che è nuovo | Casi e numeri, non paragoni |
| del settore ma non tecnici | Quelli del loro lavoro sì, quelli degli specialisti spiegati alla prima occorrenza | Di come funziona, in breve | Dal loro lavoro |
| non esperti | Parole comuni, e il termine tecnico solo dopo la spiegazione | Di ogni passaggio, senza saltarne | Dalla vita di tutti i giorni |
| misto | Come per i non esperti | In un inciso, che l'esperto salta senza fatica | Uno comune e uno del mestiere |

La voce «chi legge» serve a scegliere gli esempi e a decidere che cosa interessa. A un titolare d'azienda di un nuovo obbligo fiscale importano la scadenza e il costo, al suo commercialista importano l'articolo di legge e i casi di esclusione.

## 6. Quando la configurazione manca

Se il file non c'è, o la voce che serve è vuota, deduci tono e pubblico dalla richiesta: da chi scrive, a chi, per quale occasione. Una comunicazione ai clienti di uno studio è formale anche se nessuno lo dice, e una guida per chi comincia è accogliente.

Fai una domanda solo quando la scelta cambia il testo e dal contesto non si ricava, e in quel caso chiedi le due cose insieme, chi legge e con che tono. Per un testo breve conviene scrivere, e dire in una riga sotto il testo quale tono e quale pubblico hai assunto, così chi legge può correggerti.

Quando ti accorgi che l'utente dà le stesse indicazioni più di una volta, proponigli di salvarle nella configurazione.

## 7. Quando tono e testo non vanno d'accordo

Può succedere che la configurazione dica una cosa e il testo richiesto ne voglia un'altra: tono accogliente con il tu, e una diffida da mandare a un fornitore. In questi casi segui il genere del testo, e dillo in una riga. Un sollecito di pagamento, una risposta a un reclamo, una comunicazione a un ente vogliono il registro formale qualunque sia il tono abituale di chi scrive.

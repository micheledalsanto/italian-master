# Changelog

Le modifiche rilevanti di questa skill, versione per versione. Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/) e i numeri di versione seguono il [versionamento semantico](https://semver.org/lang/it/).

## [1.6.1] - 2026-10-08

### Aggiunto

- In `evals/esegui.py`: l'opzione `--plugin`, per provare un'altra copia della skill e confrontare due versioni sugli stessi casi, e `--mancanti`, che riprende un giro interrotto eseguendo solo i casi senza risposta.

### Corretto

- L'esecutore si accorge quando il piano ha raggiunto il limite di utilizzo. Prima salvava l'avviso del limite come se fosse la risposta e continuava a lanciare sessioni: ora si ferma, segna quelle esecuzioni come non eseguite e dice come riprendere.

## [1.6.0] - 2026-10-08

### Aggiunto

- **La skill si installa anche in Codex**, e negli altri agenti che leggono le Agent Skills dalla cartella `.agents/skills`. L'installatore ha tre opzioni nuove: `--codex` (in `~/.agents/skills`, o in `./.agents/skills` con `--project`), `--tutti` (Claude Code e Codex insieme) e `--claude`, che resta il comportamento predefinito. Valgono anche per `rimuovi`, `configura` e `dove`.
- `agents/openai.yaml`, con il nome e la descrizione breve che Codex mostra nell'elenco delle skill.

### Modificato

- **Niente nella skill dipende più da un agente.** La configurazione di tono e pubblico si cerca nella cartella `.claude/` oppure `.agents/`, del progetto o della home. `SKILL.md` e i riferimenti non nominano comandi di un agente in particolare, e il README dice «l'agente» dove diceva «Claude».
- In `CONTRIBUTING.md`, il criterio corrispondente per chi contribuisce.

### Limiti noti

- L'installazione è stata provata copiando la skill in una cartella `.agents/skills` e verificando la struttura sulla documentazione di Codex. I casi di prova girano ancora solo con Claude Code: la qualità dei testi prodotti dalla skill dentro Codex non è stata misurata.

## [1.5.4] - 2026-10-08

### Modificato

- Nello stesso esempio il nome della disciplina è quello che usa l'autore, «UI design e UX».

## [1.5.3] - 2026-10-08

### Modificato

- In `descrivere-e-raccontare.md`, la correzione di «Le interfacce sono arrivate nel 2017» è quella dell'autore: il mestiere si nomina con il nome della disciplina («mi occupo anche di UI design e UX») e l'oggetto viene dopo, a precisare. La versione di prima, «progetto interfacce», era chiara e non era il modo in cui un designer parla del proprio lavoro.

## [1.5.2] - 2026-10-08

### Aggiunto

- In `descrivere-e-raccontare.md`, **le cose che arrivano da sole**: «Le interfacce sono arrivate nel 2017», in una presentazione di sé, non dice che cosa ha fatto chi scrive. La segnalazione viene da una frase finita sul sito dell'autore della skill. Lo script la segnala tra le cose da guardare.

## [1.5.1] - 2026-10-08

`grammatica.md` e `punteggiatura-tipografia.md` riletti sulle risposte della consulenza della Crusca e sulle pagine di Treccani.

### Modificato

- **Quattro regole erano più rigide della norma**, e avrebbero fatto correggere forme che non sono errori: «mia mamma» e «mio papà» (comuni fuori dalla Toscana, dove vale «la mia mamma»), il partitivo dopo una preposizione («con degli amici», sconsigliato ma ammesso), «anche se» con il congiuntivo quando introduce un'ipotesi («anche se piovesse»), e il condizionale dopo «se», che è corretto in più casi della sola interrogativa indiretta.
- **La lineetta lunga.** `punteggiatura-tipografia.md` diceva che in italiano non si usa. La norma distingue solo il trattino dalla lineetta, e alcuni editori usano quella lunga, con gli spazi, per incisi e dialoghi. Quello che in italiano non esiste è la lineetta lunga attaccata alle parole e messa a ogni pausa. Nei testi scritti dalla skill la regola pratica non cambia.
- Il punto fermo dopo le virgolette è la norma prevalente, e l'uso di alcuni editori di metterlo dentro non si corregge.

### Aggiunto

- In `grammatica.md`: l'accordo con il lei rivolto a un uomo («lei è stato gentile», ma «l'ho vista ieri»), l'articolo davanti alle cifre («l'8 marzo», «l'11», «l'80%»), «ce l'ho» e «gliel'ho», «sia… sia» e «sia… che», i verbi di moto usati con un oggetto («scendi il cane»), i saluti scritti uniti e alcune locuzioni che si scrivono staccate.
- In `controlla.py`: «c'è l'ho» e l'articolo non eliso davanti a 8, 11 e 80.
- In `fonti.md`, le voci consultate per la revisione.

## [1.5.0] - 2026-10-08

### Aggiunto

- **`newsletter.md`**: come sono fatte tredici newsletter italiane d'autore e di redazione (136 numeri, circa trecentomila parole). Copre il titolo e il sottotitolo, i quattro modi di cominciare un numero, la persona, il corpo con le rubriche fisse, il blocco di chiusura, e una sezione su come le stesse forme si applicano alla newsletter di un negozio o di uno studio, con i difetti dei numeri generati.
- In `registri.md`, una nota sui **canali di enti e aziende**, da tredici canali pubblici di messaggistica: metà scrive testo piano, metà mette un'emoji in quasi ogni post.

### Modificato

- **L'emoji a inizio riga non è più indicata come sempre sbagliata**: in cinque canali su tredici è l'uso normale. Si guarda che cosa fa il canale.
- In `titoli.md`, la frase sugli oggetti delle newsletter d'autore ha ora le misure.

### Limiti noti

- Le newsletter di negozi, studi e piccole aziende non hanno archivi pubblici da leggere in serie: la sezione che le riguarda applica le forme osservate nelle altre.
- I post di LinkedIn e di Instagram richiedono l'accesso e non sono stati letti. Le indicazioni su quelle piattaforme restano quelle di prima, non misurate.

## [1.4.0] - 2026-10-08

### Aggiunto

- **`microcopy.md`**: i testi delle interfacce. Parte dalle stringhe di otto applicazioni a codice aperto, tre nate in italiano e cinque tradotte (circa quindicimila stringhe e centomila parole), e da due guide di stile pubbliche. Copre la persona, i pulsanti, i messaggi di errore, le conferme, gli stati vuoti, la punteggiatura, il lessico su cui le applicazioni sono d'accordo e i calchi che nelle interfacce vere non compaiono, con un esempio di riscrittura.
- Un caso di prova sui testi di una schermata, che passa in due esecuzioni su due.

### Modificato

- **Il tu anche nelle interfacce dei servizi pubblici.** `registri.md` indicava il lei per banche, sanità e pubblica amministrazione. Nelle otto applicazioni lette il lei non compare, comprese le tre dei servizi pubblici, e le linee guida per i servizi digitali della pubblica amministrazione chiedono la seconda persona. Il lei resta nelle lettere e nei documenti.
- In `calchi.md`, le alternative a «Sei sicuro di voler eliminare?» e a «Ops! Qualcosa è andato storto» sono quelle che le applicazioni italiane usano.
- «Assicurati di» nelle istruzioni di un'interfaccia non è più indicato come calco: si trova in sei applicazioni su otto, dove c'è una condizione da verificare.

## [1.3.1] - 2026-10-08

### Aggiunto

- In `SKILL.md`, **tre regole in testa alla pagina**: nel testo entrano solo i fatti forniti, prima di scrivere si apre il riferimento del genere, si consegna il testo con poche righe sotto. Sono le indicazioni che nelle prove si perdevano più spesso quando stavano in mezzo alle altre.
- **Il commento al fatto** tra i segnali dello slop gonfio: la frase che dopo ogni dato ne spiega il significato («segno che in tanti ci tenevano», «una cifra che racconta da sola…»), e che compare quando c'è una lunghezza da raggiungere e i fatti sono finiti. È descritto in `ai-slop.md`, e `descrivere-e-raccontare.md` dice che cosa fare quando i fatti non bastano per la misura richiesta.
- In `slop-asciutto.md`, il primo passo per uscirne: **separare i fatti dalle sentenze** prima di unire le frasi, perché una sentenza fusa in un periodo continua a non dire niente.
- In `calchi.md`, le formule di entusiasmo e di congedo dei post tradotti: «non potevamo essere più contenti», «restate con noi», «siamo entusiasti di annunciare».
- In `controlla.py`, la categoria «Commento al fatto», i tre calchi qui sopra e la riga di annuncio («Ecco il testo riscritto:»).
- In `evals/esegui.py`, l'opzione `--ripeti`, che esegue lo stesso caso più volte e dice quante volte passa.

### Modificato

- **Chi scrive dice «io» oppure «noi»**, e non passa dall'uno all'altro nella stessa lettera.
- **Date, ore, prezzi e misure sempre in cifre**: nelle prove uscivano «centoventi euro» e «dalle nove all'una».
- Lo script si lancia sulla risposta intera, note comprese.

### Limiti noti

- Le prove sono fatte con Sonnet, un'esecuzione per caso o tre per i casi più difficili, e lo stesso caso passa in un'esecuzione e fallisce in quella dopo. Con la 1.3.0 passano i controlli automatici otto o nove casi su tredici, e con questa versione il numero non è cresciuto in modo misurabile. Della 1.2.0 non c'è una misura pulita, perché il primo giro è stato eseguito dentro la repo e le sessioni di prova ne leggevano la memoria.
- Negli articoli scritti da appunti il commento ai fatti è sparito e il testo esce più corto della misura richiesta, dichiarandolo, in tre esecuzioni su tre. Restano due difetti che le modifiche di questa versione non hanno tolto: la lineetta lunga nelle note per l'utente, in circa metà delle esecuzioni, e qualche circostanza inventata negli stessi articoli, più piccola di prima ma presente in quasi tutte.

## [1.3.0] - 2026-10-08

### Aggiunto

- **`evals/esegui.py`**: esegue i casi di prova, ciascuno in una sessione nuova di Claude Code con la skill caricata dalla repo, e valuta le risposte. Controlla se la skill si è attivata, quali riferimenti ha aperto, le segnalazioni di `controlla.py` e i controlli dichiarati in ogni caso (che cosa deve esserci, che cosa non deve esserci, le misure del passo). Le risposte restano in `evals/risultati/`, perché i controlli automatici dicono se un testo è sbagliato e non se è buono.
- **Sette casi di prova nuovi**, che coprono le parti aggiunte nella 1.2.0: l'avviso ai clienti chiesto alla buona, la spiegazione per una bambina, l'attacco di un racconto fantastico, la pagina di un'agenzia, la configurazione del progetto, la riscrittura di un testo a frasette, la guida per chi non è del mestiere. I casi sono ora tredici, e tutti hanno i loro controlli.
- In `SKILL.md`, la sezione **«Come si consegna»**. Nelle prove quasi tutte le risposte cominciavano con «Ecco la mail» o «Ecco il testo», e le note per l'utente avevano le lineette lunghe e le etichette in grassetto che la skill toglie dai testi. Ora il testo viene per primo, e le righe che lo accompagnano seguono le stesse regole.

### Modificato

- **«Non inventare» comprende le circostanze.** Nelle prove i numeri venivano rispettati, ma tra un fatto e l'altro comparivano dettagli che nessuno aveva fornito: come si era svolto un lavoro, chi aveva promosso una raccolta, entro quando pagare una fattura. `SKILL.md` e `descrivere-e-raccontare.md` ora li nominano, dicono che un dato si può ricavare da quelli forniti se il conto torna, e che il dato indispensabile che manca diventa un segnaposto segnalato. `corrispondenza-formale.md` lo ripete per le scadenze.
- **Nelle revisioni resta la persona dell'originale.** Un testo che dava del tu non passa al lei se nessuno lo chiede. E una sentenza dello slop asciutto allungata in un periodo resta una sentenza: al suo posto vanno i fatti forniti dall'utente.
- La descrizione della skill nomina le correzioni di bozze di poche righe, per le quali nelle prove non si attivava.

## [1.2.0] - 2026-10-08

### Aggiunto

- **`tono-accogliente.md`**: come accompagnare lettori non esperti. Parte dal confronto tra dodici siti italiani di guide, divulgazione e servizi e un sito di divulgazione generato, che dà del tu una volta ogni mille parole contro le sette-diciannove dei primi. Copre l'attacco dalla situazione del lettore, la voce di chi spiega, le domande anticipate, i paragoni con le cose di casa, il termine tecnico dopo la spiegazione, i titoli che si direbbero a voce e gli eccessi da evitare.
- In `descrivere-e-raccontare.md`, i titoli calcati dall'inglese.
- **Dieci libri di saggistica letti su Liber Liber** (Gobetti, Croce, Panzini, Mantegazza, Savinio, Brancati, circa 425.000 parole), che con i siti delle agenzie portano il campione a quasi un milione di parole. In `modelli.md` ci sono tre pagine nuove: il ritratto di una persona (Gobetti), la spiegazione di un'idea (Croce), il diario di chi divaga (Panzini). In `periodo.md` e in `connettivi.md` ci sono le misure della prosa saggistica.
- In `controlla.py`, due controlli nuovi: la fila di frasi che cominciano con un verbo in «-iamo» e le formule «risultati concreti e misurabili» e «ciò che conta davvero».
- **Tono e pubblico li decide chi usa la skill.** Un file `italian-master.md`, nella cartella `.claude/` del progetto o in quella personale, dice chi legge, quanto ne sa, quale tono usare (formale, cordiale, accogliente, giornalistico, tecnico, commerciale) e come rivolgersi al lettore. La skill lo legge prima di scrivere. Il modello si crea con `npx italian-master configura`, e il nuovo riferimento `tono-e-pubblico.md` descrive i sei toni con lo stesso avviso scritto in ciascuno.
- **`narrativa-fantastica.md`**: fantasy, fiaba e fantastico quotidiano. Parte da ventisei racconti italiani contemporanei e da quattro raccolte di fiabe e novelle (Capuana, Perodi, Boito), e copre le misure del racconto, gli attacchi, il mondo mostrato dalle cose, i nomi, il dialogo, i tempi, con quattro attacchi di esempio e gli stampi da evitare.
- **`scrivere-per-bambini.md`**: come si scrive per chi ha tra i sei e gli undici anni. Le regole sul periodo si rovesciano (una frase, un'idea), e il file dà le misure ricavate da tre lezioni per un bambino di otto anni, le indicazioni su parole, spiegazioni e voce, lo stesso capoverso scritto per due età e un esempio intero. «Bambini» entra tra i pubblici della configurazione.
- In `controlla.py`, l'indice di leggibilità Gulpease.
- **`corrispondenza-formale.md`**: avvisi, lettere e comunicazioni a clienti, fornitori, pazienti e utenti. Distingue il formale sobrio da quello gonfio e da quello tolto, descrive la struttura di una comunicazione, dà le formule per funzione e sei lettere modello (chiusura, cambio di sede, listino, sollecito, reclamo, nuovi orari).
- In `controlla.py`, l'opzione `--bambini`.
- **`agenzie-digitali.md`**: come scrivono dodici agenzie digitali e di marketing italiane, estratte a caso e lette nelle pagine di presentazione, nei casi studio e nel blog (circa 78.000 parole). Copre la fila di frasi in «-iamo», le parole che promettono concretezza, i difetti dei casi studio, i due tipi di articolo dei blog, i titoli e l'inglese del mestiere, con un esempio di riscrittura.

### Modificato

- **Il registro formale non è più trattato come un difetto.** Nelle comunicazioni a clienti, fornitori e utenti le formule di cortesia e forme come «al fine di» sono indicate come normali, e il difetto da evitare è gonfiarle. Cambiano `registri.md`, `sintassi-stile.md`, `ai-slop.md` e il suggerimento dello script.
- **Nuovo esempio di riscrittura**: una mail di chiusura estiva al posto della presentazione del bar, nel README, in `ai-slop.md` e in `slop-asciutto.md`.
- **«AI slop» al posto di «sbobba artificiale».** La skill usa ora il termine originale in tutti i file. Di conseguenza `sbobba.md` è diventato `ai-slop.md` e `sbobba-asciutta.md` è diventato `slop-asciutto.md`: chi aveva un link ai vecchi nomi deve aggiornarlo.
- **Due segnali ridimensionati.** «Soltanto» e il numero basso di «che» non bastano da soli: Gobetti usa il primo quasi quanto i testi generati e ha pochi «che» in frasi di trenta parole. `connettivi.md` e `impronte.md` ora lo dicono.

## [1.1.0] - 2026-10-07

### Aggiunto

- **Installazione con npx.** `npx github:micheledalsanto/italian-master` copia la skill nella cartella delle skill di Claude Code (`~/.claude/skills`, oppure `.claude/skills` del progetto con `--project`), la aggiorna se c'è già e la toglie con `rimuovi`. Lo script non ha dipendenze e non sovrascrive una cartella che non riconosce come questa skill, a meno di `--force`.
- `package.json`, con i metadati per un'eventuale pubblicazione su npm.

## [1.0.0] - 2026-10-07

Prima versione pubblica.

### Che cosa contiene

- **`SKILL.md`**: i principi per scrivere in italiano naturale, tre liste di segnali da rileggere (slop gonfio, slop asciutto, impronte grammaticali) e il metodo per scrivere da zero, rivedere, correggere le bozze, titolare, tradurre e imparare una voce.
- **Diciotto riferimenti**, che Claude apre solo quando servono:
  - sulla frase e sul testo: `periodo.md`, `connettivi.md`, `sintassi-stile.md`, `attacchi-e-chiusure.md`, `descrivere-e-raccontare.md`
  - sui difetti della scrittura generata: `ai-slop.md`, `slop-asciutto.md`, `impronte.md`, `calchi.md`
  - sulla norma: `grammatica.md`, `punteggiatura-tipografia.md`
  - sui generi: `registri.md`, `siti.md`, `titoli.md`, `modi-di-dire.md`
  - sui modelli e sul metodo: `modelli.md`, `imparare-una-voce.md`, `fonti.md`
- **`scripts/controlla.py`**: uno script senza dipendenze che segnala formule, errori di ortografia e segnali tipografici, e misura il passo delle frasi e alcune impronte grammaticali confrontandoli con quelli dei giornali.
- **Sei casi di prova** in `evals/evals.json`.
- **Manifest del plugin e del marketplace** per l'installazione in Claude Code.

### Su che cosa si basa

- Circa mezzo milione di parole lette e contate: 86 articoli di otto testate italiane online, le *Lettere dal carcere* di Gramsci e opere d'autore di pubblico dominio (Pavese, Svevo, Pirandello, Verga, Serao, Deledda, Tozzi, De Amicis, Vamba, Collodi, Artusi).
- Dieci siti di aziende ed enti italiani di settori diversi, estratti a caso da un elenco di venti settori.
- Un campione di testi generati, usato per il confronto.
- Le indicazioni dell'Accademia della Crusca e di Treccani per la norma, e la tradizione della scrittura chiara (Calvino, Eco, Serianni, Sabatini, Castellani Pollidori, Carrada) per lo stile.
- Le correzioni di un lettore madrelingua ai testi prodotti durante lo sviluppo.

### Le scelte principali, e che cosa è cambiato durante lo sviluppo

- **Periodi al posto delle frasette.** La prima stesura raccomandava una prosa breve e «asciutta», secondo i manuali di scrittura inglesi. Il confronto con i giornali ha mostrato che la prosa italiana da leggere ha frasi di venti o trenta parole, e la skill ora insegna a costruirle.
- **Due tipi di AI slop.** Oltre a quello gonfio, la skill descrive lo stile a frasi corte, due punti a effetto e sentenze finali che un modello produce quando gli si chiede di evitare il primo.
- **Meno divieti.** Molte forme indicate all'inizio come segnali di scrittura artificiale («sempre più», il passivo, i gerundi, gli avverbi in -mente, i possessivi) nei giornali sono comuni. Sono state tolte dalle liste e raccolte tra i falsi allarmi.
- **Misure per genere.** I controlli su connettivi e relative valgono per articoli e saggi, e non per le pagine di un sito, dove i connettivi quasi non compaiono.
- **Il gergo di mestiere resta.** I termini che chi fa un lavoro dice in inglese non vengono tradotti quando il testo è rivolto a chi quel lavoro lo conosce.
- **Descrivere e raccontare.** Un riferimento dedicato alla scrittura da zero: coerenza dei tempi verbali, grado di precisione adatto al genere, accostamenti di parole che esistono davvero, frasi che si capiscono da sole.

### Che cosa non contiene

- Nessuna frase presa da giornali o siti, che non sono nominati. Gli esempi di quel tipo sono scritti apposta, con fatti inventati.
- Le sole citazioni testuali sono brevi passi di opere uscite prima del 1930.

### Limiti noti

- È italiano d'Italia, e non copre le varietà regionali se non per cenni.
- Il campione di testi generati è piccolo (circa 16.600 parole, da due fonti), quindi le misure che lo riguardano valgono come indizio.
- Lo script segnala indizi e non giudica: un testo senza segnalazioni può essere mediocre.
- I casi di prova sono scritti ma non ancora eseguiti in modo sistematico con e senza la skill.

[1.1.0]: https://github.com/micheledalsanto/italian-master/releases/tag/v1.1.0
[1.0.0]: https://github.com/micheledalsanto/italian-master/releases/tag/v1.0.0

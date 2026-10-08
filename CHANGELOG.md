# Changelog

Le modifiche rilevanti di questa skill, versione per versione. Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/) e i numeri di versione seguono il [versionamento semantico](https://semver.org/lang/it/).

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

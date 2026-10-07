# Changelog

Le modifiche rilevanti di questa skill, versione per versione. Il formato segue [Keep a Changelog](https://keepachangelog.com/it/1.1.0/) e i numeri di versione seguono il [versionamento semantico](https://semver.org/lang/it/).

## [1.0.0] - 2026-10-07

Prima versione pubblica.

### Che cosa contiene

- **`SKILL.md`**: i principi per scrivere in italiano naturale, tre liste di segnali da rileggere (sbobba gonfia, sbobba asciutta, impronte grammaticali) e il metodo per scrivere da zero, rivedere, correggere le bozze, titolare, tradurre e imparare una voce.
- **Diciotto riferimenti**, che Claude apre solo quando servono:
  - sulla frase e sul testo: `periodo.md`, `connettivi.md`, `sintassi-stile.md`, `attacchi-e-chiusure.md`, `descrivere-e-raccontare.md`
  - sui difetti della scrittura generata: `sbobba.md`, `sbobba-asciutta.md`, `impronte.md`, `calchi.md`
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
- **Due sbobbe.** Oltre a quella gonfia, la skill descrive lo stile a frasi corte, due punti a effetto e sentenze finali che un modello produce quando gli si chiede di evitare la prima.
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

[1.0.0]: https://github.com/micheledalsanto/italian-master/releases/tag/v1.0.0

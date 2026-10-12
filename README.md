# Italian master

[![Versione](https://img.shields.io/github/package-json/v/micheledalsanto/italian-master?label=versione&color=2ea44f)](CHANGELOG.md)
[![Licenza MIT](https://img.shields.io/github/license/micheledalsanto/italian-master?label=licenza&color=blue)](LICENSE)

L'italiano di chi scrive per mestiere, genere per genere e con i soli fatti che gli vengono dati. Una skill per Claude, per Codex e per gli altri agenti che leggono le Agent Skills.

*An agent skill (Claude, Codex) for natural Italian writing: grammar, syntax, tone, verb tenses, idioms, headlines. The skill is written in Italian. [Read this README in English](README.en.md).*

## La stessa richiesta, tre risposte

La richiesta è la stessa per tutti e tre i testi: una mail per dire ai clienti di uno studio che la chiusura estiva va dall'11 al 24 agosto, che chi ha adempimenti in quel periodo deve farsi sentire entro il 31 luglio e che per le urgenze risponde Paola al cellulare.

Senza la skill:

> **Oggetto: Aggiornamento Importante Sulla Nostra Chiusura Estiva**
>
> Gentile Cliente,
>
> speriamo che questa email ti trovi bene! In un periodo dell'anno in cui il riposo diventa fondamentale, desideriamo informarLa che il nostro team si prenderà una meritata pausa — per tornare più carico che mai. Non si tratta solo di una chiusura: è un'occasione per ricaricare le energie, rinnovarci e offrirti un servizio ancora migliore.

Senza la skill, chiedendo di essere più asciutti:

> **Oggetto: Ad agosto chiudiamo. Ecco cosa cambia.**
>
> Chiudiamo. Due settimane. Dall'11 al 24 agosto.
>
> Niente panico: le urgenze restano coperte. Il resto può aspettare. A settembre si riparte.

Con la skill:

> **Oggetto: Chiusura estiva dello Studio dall'11 al 24 agosto**
>
> Gentili Clienti,
>
> desideriamo informarvi che lo Studio resterà **chiuso per la pausa estiva dall'11 al 24 agosto compresi**. Le attività riprenderanno regolarmente a partire dal **25 agosto**.
>
> Al fine di garantire una corretta gestione delle pratiche e il rispetto delle relative scadenze, invitiamo coloro che hanno adempimenti previsti durante il periodo di chiusura a **contattarci entro il 31 luglio**, così da consentirci di provvedere con il necessario anticipo.
>
> Per eventuali urgenze durante il periodo di chiusura, sarà possibile contattare Paola al numero di cellulare riportato in firma.
>
> Ringraziandovi per la collaborazione, cogliamo l'occasione per augurarvi una serena estate.
>
> **Cordiali saluti,**
>
> Lo Staff dello Studio

Il primo testo dà del tu e del lei nella stessa frase e non riporta nessuno dei dati della richiesta. Il secondo dice le date, ma con il tono di uno slogan, e non spiega al cliente che cosa deve fare. Il terzo è la comunicazione che uno studio manda davvero ai suoi clienti: registro formale, date, scadenza per le pratiche, contatto per le urgenze.

## Perché succede

Chi chiede a un modello un testo in italiano riceve quasi sempre una pagina senza errori che nessun italiano scriverebbe. Comincia con «In un mondo sempre più», mette tre aggettivi dove ne basterebbe uno, ha le maiuscole a ogni parola del titolo e le lineette lunghe dell'inglese. Se poi gli si chiede di essere più asciutto, il modello passa a frasette di cinque parole con una battuta in fondo, e il testo si riconosce lo stesso.

Questa skill dà al modello quello che sa un buon redattore: dove si sbaglia davvero la grammatica, come si costruisce un periodo che non suona tradotto, quando dare del tu, del lei o del voi, come si fa un titolo, quale tempo verbale vuole un racconto. Gli chiede anche di non aggiungere niente ai fatti che riceve, per cui un testo con pochi dati esce più corto e sotto dice che cosa manca. Le indicazioni vengono da testi veri, letti e contati: giornali, siti di aziende e di agenzie, saggi, lettere.

## Come lavora

- **Misure prese su testi italiani.** Quanto è lunga una frase in un quotidiano, quanti due punti ci sono in un articolo, quali tempi verbali usa un romanzo, come comincia una newsletter: le indicazioni vengono da circa cinque milioni di parole contate, e ogni riferimento dice su quali testi è stato fatto.
- **Regole per genere.** Una mail a un cliente, la home di un sito, il messaggio di errore di un'applicazione, un articolo e un racconto vogliono cose diverse. Il contrasto e la triade che in un articolo sono un difetto in un claim sono normali, e la skill lo dice caso per caso, insieme all'elenco dei falsi allarmi.
- **Solo i fatti ricevuti.** Niente numeri, nomi, citazioni o circostanze verosimili aggiunti per dare colore. Se i dati sono pochi il testo esce più corto.
- **Due difetti, non uno.** Oltre allo slop gonfio c'è quello asciutto, a frasette e sentenze, che nasce quando si cerca di evitare il primo.
- **Il registro di chi firma.** Uno studio, un'azienda e un ente scrivono in modo formale e completo, e la skill non scambia l'informalità per naturalezza.

## Che cosa le puoi chiedere

Non serve invocarla, perché si attiva da sola quando chiedi un testo in italiano, come in questi esempi.

- «Riscrivi questa pagina "Chi siamo", suona finta.»
- «Dammi dieci titoli per questo articolo, niente clickbait.»
- «Scrivi una mail di sollecito all'architetto Ferraris, ci diamo del lei.»
- «Scrivi la hero section della home: siamo una falegnameria di Udine, facciamo mobili su misura dal 1961.»
- «Correggi solo gli errori, non toccare lo stile.»
- «Traduci questo post in italiano, non deve sembrare una traduzione.»
- «Leggi questi tre numeri della mia newsletter e scrivi il prossimo con la stessa voce.»

In Claude Code puoi anche chiamarla in modo esplicito: `/italian-master:italian-master` se l'hai installata come plugin, `/italian-master` se l'hai copiata a mano. In Codex si chiama con `$italian-master`.

Il plugin porta con sé tre comandi per i lavori più lunghi:

| Comando | Che cosa fa |
| --- | --- |
| `/italian-master:rivedi` | Rivede un file o un testo incollato e dice che cosa ha cambiato |
| `/italian-master:voce` | Ricava la scheda di stile di un autore dai suoi testi, con le misure, e la confronta con una bozza |
| `/italian-master:configura` | Crea o aggiorna il file di tono e pubblico, con poche domande |

### Genere per genere

Ogni genere ha il suo riferimento, con le misure prese sui testi di quel genere. L'agente legge sempre [`SKILL.md`](skills/italian-master/SKILL.md) e apre gli altri file solo quando servono.

| Che cosa scrivi | Su che cosa è misurato | Dove sta |
| --- | --- | --- |
| Email, avvisi, lettere a clienti e fornitori | circa cinquanta comunicazioni formali | [`corrispondenza-formale`](skills/italian-master/references/corrispondenza-formale.md), [`registri`](skills/italian-master/references/registri.md) |
| Home, claim, «Chi siamo», pagine di servizio | dieci siti di aziende ed enti, dodici di agenzie | [`siti`](skills/italian-master/references/siti.md), [`agenzie-digitali`](skills/italian-master/references/agenzie-digitali.md) |
| Schede prodotto | 1.138 schede di dieci negozi online | [`schede-prodotto`](skills/italian-master/references/schede-prodotto.md) |
| Annunci a pagamento | 904 inserzioni di 732 inserzionisti | [`annunci`](skills/italian-master/references/annunci.md) |
| Newsletter | 136 numeri di tredici newsletter | [`newsletter`](skills/italian-master/references/newsletter.md) |
| Articoli, post, guide, titoli | ottantasei articoli di otto testate, sessantuno pagine di tredici siti | [`periodo`](skills/italian-master/references/periodo.md), [`connettivi`](skills/italian-master/references/connettivi.md), [`attacchi-e-chiusure`](skills/italian-master/references/attacchi-e-chiusure.md), [`titoli`](skills/italian-master/references/titoli.md), [`testi-per-la-ricerca`](skills/italian-master/references/testi-per-la-ricerca.md), [`descrivere-e-raccontare`](skills/italian-master/references/descrivere-e-raccontare.md) |
| Spiegazioni per chi non è del mestiere, e per i bambini | dodici siti che spiegano o accompagnano | [`tono-accogliente`](skills/italian-master/references/tono-accogliente.md), [`scrivere-per-bambini`](skills/italian-master/references/scrivere-per-bambini.md) |
| Testi di un'interfaccia | quindicimila stringhe di otto applicazioni | [`microcopy`](skills/italian-master/references/microcopy.md) |
| Racconti | venti romanzi per dialogo e scena, ventidue libri per i tempi verbali, ventisei racconti e quattro raccolte di fiabe | [`narrativa`](skills/italian-master/references/narrativa.md), [`narrativa-fantastica`](skills/italian-master/references/narrativa-fantastica.md), [`tempi-verbali`](skills/italian-master/references/tempi-verbali.md), [`modelli`](skills/italian-master/references/modelli.md) |
| Tesi, saggi, articoli accademici | quarantacinque articoli di nove riviste | [`scrittura-accademica`](skills/italian-master/references/scrittura-accademica.md) |
| Traduzioni verso l'italiano | elenchi di calchi, falsi amici e modi di dire | [`calchi`](skills/italian-master/references/calchi.md), [`modi-di-dire`](skills/italian-master/references/modi-di-dire.md) |
| Revisioni e correzioni di bozze | le risposte della Crusca e di Treccani, e testi generati per il confronto | [`ai-slop`](skills/italian-master/references/ai-slop.md), [`slop-asciutto`](skills/italian-master/references/slop-asciutto.md), [`impronte`](skills/italian-master/references/impronte.md), [`grammatica`](skills/italian-master/references/grammatica.md), [`punteggiatura-tipografia`](skills/italian-master/references/punteggiatura-tipografia.md), [`sintassi-stile`](skills/italian-master/references/sintassi-stile.md) |
| Testi con la tua voce e il tuo tono | i testi che le dai da leggere | [`imparare-una-voce`](skills/italian-master/references/imparare-una-voce.md), [`tono-e-pubblico`](skills/italian-master/references/tono-e-pubblico.md) |

## Installarla

### Con npx

È il modo più rapido, e non richiede di clonare la repo. Serve Node 18 o successivo.

```bash
npx github:micheledalsanto/italian-master
```

Il comando copia la skill in `~/.claude/skills/italian-master`, dove Claude Code la trova da solo, e rilanciato la aggiorna.

```bash
npx github:micheledalsanto/italian-master --codex     # per Codex (~/.agents/skills)
npx github:micheledalsanto/italian-master --tutti     # per Claude Code e per Codex
npx github:micheledalsanto/italian-master --project   # solo nel progetto corrente (.claude/skills, o .agents/skills con --codex)
npx github:micheledalsanto/italian-master rimuovi     # la toglie
npx github:micheledalsanto/italian-master --help      # tutte le opzioni
```

### Con skills.sh

Chi usa il comando `skills` di [skills.sh](https://skills.sh), che installa le skill da GitHub per Claude Code, Codex, Cursor e altri agenti, può fare così:

```bash
npx skills add micheledalsanto/italian-master
```

### Claude Code, come plugin

Dentro una sessione di Claude Code:

```
/plugin marketplace add micheledalsanto/italian-master
/plugin install italian-master@italian-master
```

Oppure dal terminale:

```bash
claude plugin marketplace add micheledalsanto/italian-master
claude plugin install italian-master@italian-master
```

Per installarla da una copia locale della repo, senza passare da GitHub, al posto di `micheledalsanto/italian-master` si indica il percorso della cartella:

```bash
claude plugin marketplace add ./italian-master
claude plugin install italian-master@italian-master
```

Per provarla in una sola sessione senza installarla: `claude --plugin-dir ./italian-master`.

### Claude Code, a mano

Copia la cartella della skill tra le tue skill personali:

```bash
git clone https://github.com/micheledalsanto/italian-master.git
cp -r italian-master/skills/italian-master ~/.claude/skills/
```

Per usarla solo in un progetto, copiala in `.claude/skills/` dentro il progetto.

### Codex e altri agenti

Codex cerca le skill in `.agents/skills`, nella cartella del progetto e nella home. Con npx:

```bash
npx github:micheledalsanto/italian-master --codex             # ~/.agents/skills/italian-master
npx github:micheledalsanto/italian-master --codex --project   # ./.agents/skills/italian-master
```

Oppure a mano:

```bash
git clone https://github.com/micheledalsanto/italian-master.git
mkdir -p ~/.agents/skills && cp -r italian-master/skills/italian-master ~/.agents/skills/
```

Riavvia Codex. La skill si attiva da sola quando chiedi un testo in italiano, e si chiama in modo esplicito con `$italian-master` oppure da `/skills`. La cartella `.agents/skills` è letta anche da altri agenti che seguono lo stesso formato, e per una cartella diversa c'è `--dir`.

### Claude.ai e app desktop

1. Scarica la repo e crea uno zip della cartella `skills/italian-master` (lo zip deve contenere la cartella `italian-master` con dentro `SKILL.md`).
2. In Claude apri le impostazioni, vai alla sezione delle skill e carica lo zip.

## Tono e pubblico, decisi da te

Per chi scrivi e con che tono lo decidi tu, una volta, in un file di configurazione. La skill lo legge prima di scrivere.

```bash
npx github:micheledalsanto/italian-master configura            # per tutti i tuoi progetti (~/.claude/italian-master.md)
npx github:micheledalsanto/italian-master configura --project  # solo per il progetto corrente (.claude/italian-master.md)
npx github:micheledalsanto/italian-master configura --codex    # per Codex (~/.agents/italian-master.md)
```

Il comando crea un modello da compilare. Le voci sono queste, e quelle che lasci vuote la skill le decide dal contesto della richiesta.

| Voce | Che cosa ci scrivi |
| --- | --- |
| Pubblico | Chi legge e quanto ne sa: esperti, del settore ma non tecnici, non esperti, misto, bambini (con l'età) |
| Tono | Formale, cordiale, accogliente, giornalistico, tecnico o commerciale, oppure una descrizione tua |
| Persona | Tu, lei o voi per il lettore; noi, io o la forma impersonale per chi scrive |
| Lingua | Quanto inglese, parole da usare e da evitare |
| Testi di riferimento | I testi da cui la skill deve imparare la tua voce |
| Tipi di testo | Le eccezioni: «newsletter: accogliente, tu», «comunicazioni ai clienti: formale, voi» |

Quello che chiedi in una singola richiesta vale più della configurazione, e se ci sono sia il file del progetto sia quello personale vale il primo. Il file sta fuori dalla cartella della skill, quindi un aggiornamento non lo tocca. Se hai installato la skill a mano o su Claude.ai, copia il modello da [`assets/italian-master.md`](skills/italian-master/assets/italian-master.md), oppure incolla le tue scelte nelle istruzioni del progetto.

## Controllare un testo da riga di comando

`controlla.py` cerca in un testo le formule, gli errori e i segnali tipografici più comuni, e ne misura il passo (parole per frase, frasi brevi, periodi lunghi, virgole, due punti) confrontandolo con quello di giornali e riviste. Calcola anche l'indice di leggibilità Gulpease. Usa solo la libreria standard e richiede Python 3.8 o successivo.

```bash
python skills/italian-master/scripts/controlla.py bozza.md
```

```
== bozza.md ==
63 parole, 5 frasi

Falso contrasto (1)
  riga   5  …r tornare più carico che mai. Non si tratta solo di una chiusura: è un'occasio…
            → scrivi la parte affermativa

Calchi dall'inglese (1)
  riga   5  speriamo che questa email ti trovi bene! In un periodo dell'anno in c…
            → togli

Tipografia (2)
  riga   5  …i prenderà una meritata pausa — per tornare più carico che ma…
            → lineetta lunga all'inglese: prova virgole, due punti o parentesi; se resta, « – » con gli spazi
  riga   1  Aggiornamento Importante Sulla Nostra Chiusura Estiva
            → maiuscole a ogni parola: in italiano solo la prima e i nomi propri

4 segnalazioni (63 ogni mille parole). Sono indizi: decide chi scrive.
```

Opzioni: `--json` per l'uscita strutturata, `--strict` per uscire con codice 1 se ci sono segnalazioni (utile in una pipeline), `--bambini` per i testi destinati ai bambini, dove le frasi corte sono giuste e si controlla la leggibilità.

Lo stesso script misura una voce. Dati tre o più testi dello stesso autore, stampa una scheda con la persona di chi scrive e quella del lettore, il passo delle frasi e dei capoversi, la punteggiatura, i legami preferiti e quelli assenti, le parole che tornano. Con `--confronta` dice in quali misure una bozza si allontana da quella voce.

```bash
python skills/italian-master/scripts/controlla.py --voce post1.md post2.md post3.md --confronta bozza.md
```

Lo script non riconosce i testi generati e non vede i fatti inventati. Segnala abitudini di scrittura deboli, chiunque le abbia, e un testo che non riceve segnalazioni può essere comunque mediocre.

## Fonti e limiti

Dall'Accademia della Crusca e da Treccani per la norma, e dalla tradizione della scrittura chiara per lo stile (Calvino, Eco, Serianni, Sabatini, Castellani Pollidori, Carrada). Le misure vengono da circa cinque milioni di parole lette e contate: articoli di otto testate italiane online, dieci siti di aziende ed enti, dodici siti di agenzie digitali, tredici newsletter, le schede prodotto di dieci negozi online, novecento inserzioni, le stringhe di otto applicazioni, articoli di riviste accademiche, racconti fantastici, lettere, saggi, fiabe, romanzi, memorie, teatro e altre opere di pubblico dominio. L'elenco completo è in [`fonti.md`](skills/italian-master/references/fonti.md).

La skill non contiene testi altrui. Giornali e siti non sono nominati e nessuna loro frase è riportata: gli esempi sono scritti apposta, con fatti inventati. Le sole citazioni testuali sono brevi passi di opere uscite prima del 1930.

- È italiano d'Italia. Non copre l'italiano della Svizzera né le varietà regionali, se non per qualche cenno.
- La lingua cambia: quello che oggi è un calco domani sarà nei dizionari. Dove l'uso è in movimento la skill lo dice.
- I segnali dell'AI slop cambiano con i modelli. Il catalogo va tenuto aggiornato, ed è il motivo per cui la repo è pubblica.
- La skill lavora sui fatti che riceve. Se la richiesta ne dà pochi il testo esce corto, e nessuna regola lo riempie al posto di chi ha qualcosa da dire.

## Contribuire, versioni, licenza

Segnalazioni, correzioni e nuovi esempi sono benvenuti: le indicazioni sono in [`CONTRIBUTING.md`](CONTRIBUTING.md).

La versione corrente è la 1.16.0. Le modifiche sono elencate nel [CHANGELOG](CHANGELOG.md).

La licenza è la [MIT](LICENSE).

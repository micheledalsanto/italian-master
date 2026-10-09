# Italian master

Una skill per scrivere in italiano come scrive un italiano bravo, contro l'AI slop. Funziona con Claude, con Codex e con gli altri agenti che leggono le Agent Skills.

*An agent skill (Claude, Codex) for natural Italian writing: grammar, syntax, tone, idioms, headlines. The skill and its documentation are in Italian. [English summary below](#english).*

## Il problema

Chi chiede a un modello un testo in italiano riceve quasi sempre una pagina senza errori che nessun italiano scriverebbe. Comincia con «In un mondo sempre più», mette tre aggettivi dove ne basterebbe uno, ha le maiuscole a ogni parola del titolo e le lineette lunghe dell'inglese. Se poi gli si chiede di essere più asciutto, il modello passa a frasette di cinque parole con una battuta in fondo, e il testo si riconosce lo stesso.

Questa skill dà al modello quello che sa un buon redattore: dove si sbaglia davvero la grammatica, come si costruisce un periodo che non suona tradotto, quando dare del tu, del lei o del voi, come si fa un titolo. Le indicazioni vengono da testi veri, letti e contati: giornali, siti di aziende e di agenzie, saggi, lettere.

## Prima e dopo

La richiesta è la stessa per tutti e tre i testi: una mail per dire ai clienti di uno studio che ad agosto si chiude due settimane.

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
> desideriamo informarvi che lo Studio resterà **chiuso per la pausa estiva dall’11 al 24 agosto compresi**. Le attività riprenderanno regolarmente a partire dal **25 agosto**.
>
> Al fine di garantire una corretta gestione delle pratiche e il rispetto delle relative scadenze, invitiamo coloro che hanno adempimenti previsti durante il periodo di chiusura a **contattarci entro il 31 luglio**, così da consentirci di provvedere con il necessario anticipo.
>
> Per eventuali urgenze durante il periodo di chiusura, sarà possibile contattare Paola al numero di cellulare riportato in firma.
>
> Ringraziandovi per la collaborazione, cogliamo l’occasione per augurarvi una serena estate.
>
> **Cordiali saluti,**
>
> Lo Staff dello Studio

Il primo testo dà del tu e del lei nella stessa frase e non dice le date. Il secondo le dice, ma con il tono di uno slogan, e non spiega al cliente che cosa deve fare. Il terzo è la comunicazione che uno studio manda davvero ai suoi clienti: registro formale, date, scadenza per le pratiche, contatto per le urgenze.

## Che cosa contiene

| File | Contenuto |
| --- | --- |
| [`SKILL.md`](skills/italian-master/SKILL.md) | I principi, i segnali da rileggere, il metodo di lavoro |
| [`references/tono-e-pubblico.md`](skills/italian-master/references/tono-e-pubblico.md) | I sei toni, lo stesso avviso scritto in ciascuno, che cosa cambia secondo il pubblico, e come si applica la configurazione |
| [`references/periodo.md`](skills/italian-master/references/periodo.md) | Come sono fatte le frasi italiane, con misure prese da giornali e libri |
| [`references/descrivere-e-raccontare.md`](skills/italian-master/references/descrivere-e-raccontare.md) | Descrivere un progetto, raccontare un percorso, scrivere da appunti: tempi verbali, grado di precisione, gergo di mestiere, accostamenti di parole |
| [`references/tono-accogliente.md`](skills/italian-master/references/tono-accogliente.md) | Come accompagnare lettori non esperti: da dove cominciare, il tu, le domande, i paragoni, i titoli |
| [`references/slop-asciutto.md`](skills/italian-master/references/slop-asciutto.md) | Lo stile a frasette che nasce quando si evita l'AI slop |
| [`references/modelli.md`](skills/italian-master/references/modelli.md) | Pagine di Svevo, Pirandello, Collodi, Artusi, Serao, Vamba, Gobetti, Croce e Panzini annotate, e modelli di attacco |
| [`references/connettivi.md`](skills/italian-master/references/connettivi.md) | I connettivi e le parole che misurano, con le frequenze nei giornali e nei testi generati |
| [`references/attacchi-e-chiusure.md`](skills/italian-master/references/attacchi-e-chiusure.md) | Come cominciano e come finiscono gli articoli veri, con esempi costruiti |
| [`references/impronte.md`](skills/italian-master/references/impronte.md) | I segni grammaticali che restano dopo aver tolto le formule, e i falsi allarmi |
| [`references/ai-slop.md`](skills/italian-master/references/ai-slop.md) | Catalogo dei segnali di scrittura artificiale in italiano, con le alternative |
| [`references/sintassi-stile.md`](skills/italian-master/references/sintassi-stile.md) | Antilingua, nominalizzazioni, frase, capoverso, logica |
| [`references/calchi.md`](skills/italian-master/references/calchi.md) | Calchi dall'inglese, falsi amici, anglicismi |
| [`references/grammatica.md`](skills/italian-master/references/grammatica.md) | Accenti, apostrofi, congiuntivo, pronomi, reggenze, femminili professionali |
| [`references/punteggiatura-tipografia.md`](skills/italian-master/references/punteggiatura-tipografia.md) | Virgole, virgolette, lineette, maiuscole, numeri, date |
| [`references/siti.md`](skills/italian-master/references/siti.md) | Come scrivono dieci siti italiani di settori diversi, senza nomi: che cosa funziona e che cosa no |
| [`references/microcopy.md`](skills/italian-master/references/microcopy.md) | I testi delle interfacce: misure su quindicimila stringhe di otto applicazioni, formule per errori, conferme e stati vuoti, lessico, calchi |
| [`references/newsletter.md`](skills/italian-master/references/newsletter.md) | Come sono fatte tredici newsletter italiane: titolo e sottotitolo, aperture, persona, chiusure, e che cosa cambia per la newsletter di un'attività |
| [`references/agenzie-digitali.md`](skills/italian-master/references/agenzie-digitali.md) | Come scrivono dodici agenzie digitali e di marketing: presentazioni, casi studio, blog, inglese del mestiere |
| [`references/narrativa-fantastica.md`](skills/italian-master/references/narrativa-fantastica.md) | Fantasy, fiaba e fantastico quotidiano: misure su ventisei racconti e quattro raccolte di fiabe, attacchi, dialoghi, stampi da evitare |
| [`references/scrivere-per-bambini.md`](skills/italian-master/references/scrivere-per-bambini.md) | Come si scrive per chi ha tra i sei e gli undici anni: frasi, parole, modo di spiegare, indice di leggibilità |
| [`references/corrispondenza-formale.md`](skills/italian-master/references/corrispondenza-formale.md) | Avvisi, lettere e comunicazioni a clienti e fornitori: struttura, formule per funzione, sei lettere modello |
| [`references/registri.md`](skills/italian-master/references/registri.md) | Tu, lei, voi; email, social, siti, pubblica amministrazione, narrativa |
| [`references/titoli.md`](skills/italian-master/references/titoli.md) | Titoli giornalistici e web, oggetti di email, attacchi, il titolese da evitare |
| [`references/modi-di-dire.md`](skills/italian-master/references/modi-di-dire.md) | Modi di dire, proverbi, espressioni del parlato, equivalenti degli idiomi inglesi |
| [`references/imparare-una-voce.md`](skills/italian-master/references/imparare-una-voce.md) | Come ricavare una scheda di stile dai testi di riferimento dell'utente |
| [`references/fonti.md`](skills/italian-master/references/fonti.md) | Bibliografia e fonti |
| [`scripts/controlla.py`](skills/italian-master/scripts/controlla.py) | Script che segnala i sospetti più comuni in un testo |

L'agente legge sempre `SKILL.md` e apre gli altri file solo quando servono.

## Installazione

### Con npx

È il modo più rapido, e non richiede di clonare la repo. Serve Node 18 o successivo.

```bash
npx github:micheledalsanto/italian-master
```

Il comando copia la skill in `~/.claude/skills/italian-master`, dove Claude Code la trova da solo. Rilanciato, la aggiorna.

```bash
npx github:micheledalsanto/italian-master --codex     # per Codex (~/.agents/skills)
npx github:micheledalsanto/italian-master --tutti     # per Claude Code e per Codex
npx github:micheledalsanto/italian-master --project   # solo nel progetto corrente (.claude/skills, o .agents/skills con --codex)
npx github:micheledalsanto/italian-master rimuovi     # la toglie
npx github:micheledalsanto/italian-master --help      # tutte le opzioni
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

## Come si usa

Non serve invocarla: si attiva da sola quando chiedi un testo in italiano. Qualche esempio.

- «Riscrivi questa pagina "Chi siamo", suona finta.»
- «Dammi dieci titoli per questo articolo, niente clickbait.»
- «Scrivi una mail di sollecito all'architetto Ferraris, ci diamo del lei.»
- «Correggi solo gli errori, non toccare lo stile.»
- «Traduci questo post in italiano, non deve sembrare una traduzione.»
- «Leggi questi tre numeri della mia newsletter e scrivi il prossimo con la stessa voce.»

In Claude Code puoi anche chiamarla in modo esplicito: `/italian-master:italian-master` se l'hai installata come plugin, `/italian-master` se l'hai copiata a mano. In Codex si chiama con `$italian-master`.

## Tono e pubblico

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

## Lo script di controllo

`controlla.py` cerca in un testo le formule, gli errori e i segnali tipografici più comuni, e ne misura il passo (parole per frase, frasi brevi, periodi lunghi, virgole, due punti) confrontandolo con quello di giornali e riviste. Calcola anche l'indice di leggibilità Gulpease. Solo libreria standard, Python 3.8 o successivo.

```bash
python skills/italian-master/scripts/controlla.py bozza.md
```

```
== bozza.md ==
62 parole, 4 frasi

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

4 segnalazioni (65 ogni mille parole). Sono indizi: decide chi scrive.
```

Opzioni: `--json` per l'uscita strutturata, `--strict` per uscire con codice 1 se ci sono segnalazioni (utile in una pipeline), `--bambini` per i testi destinati ai bambini, dove le frasi corte sono giuste e si controlla la leggibilità.

Non è un rilevatore di testi generati e non pretende di esserlo. Segnala abitudini di scrittura deboli, chiunque le abbia.

## Da dove vengono le regole

Dall'Accademia della Crusca e da Treccani per la norma, e dalla tradizione della scrittura chiara per lo stile (Calvino, Eco, Serianni, Sabatini, Castellani Pollidori, Carrada). Le misure vengono da quasi due milioni di parole lette e contate: articoli di otto testate italiane online, dieci siti di aziende ed enti, dodici siti di agenzie digitali, tredici newsletter, le stringhe di otto applicazioni, racconti fantastici, lettere, saggi, fiabe e opere d'autore di pubblico dominio. L'elenco completo è in [`fonti.md`](skills/italian-master/references/fonti.md).

La skill non contiene testi altrui. Giornali e siti non sono nominati e nessuna loro frase è riportata: gli esempi sono scritti apposta, con fatti inventati. Le sole citazioni testuali sono brevi passi di opere uscite prima del 1930.

## Limiti

- È italiano d'Italia. Non copre l'italiano della Svizzera né le varietà regionali, se non per qualche cenno.
- La lingua cambia: quello che oggi è un calco domani sarà nei dizionari. Dove l'uso è in movimento la skill lo dice.
- I segnali dell'AI slop cambiano con i modelli. Il catalogo va tenuto aggiornato, ed è il motivo per cui la repo è pubblica.
- Nessuna regola sostituisce l'avere qualcosa da dire.

## Contribuire

Segnalazioni, correzioni e nuovi esempi sono benvenuti. Vedi [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Versioni

La versione corrente è la 1.8.1. Le modifiche sono elencate nel [CHANGELOG](CHANGELOG.md).

## Licenza

[MIT](LICENSE).

---

<a name="english"></a>

## English

Italian master is an agent skill that makes Claude, Codex and other Agent Skills-compatible agents write Italian the way a skilled native writer does. It targets the patterns that make generated Italian text instantly recognisable: English calques, Title Case headings, em dashes, automatic triads, «non è solo X, è Y» constructions, inflated vocabulary, bureaucratic phrasing.

It covers grammar and spelling doubts, punctuation and typography conventions, syntax and logic, register (tu/lei/voi), idioms and proverbs with their English equivalents, headlines and email subject lines, and a workflow for learning a voice from reference texts. A small Python linter flags the most common tells.

Install in Claude Code:

```
/plugin marketplace add micheledalsanto/italian-master
/plugin install italian-master@italian-master
```

Install in Codex (copies the skill to `~/.agents/skills`):

```bash
npx github:micheledalsanto/italian-master --codex
```

The skill triggers on any request whose output is Italian text, including requests written in English.

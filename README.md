# Italian master

Una skill per Claude che scrive in italiano come scrive un italiano bravo. Contro l'AI slop.

*A Claude skill for natural Italian writing: grammar, syntax, tone, idioms, headlines. The skill and its documentation are in Italian. [English summary below](#english).*

## Il problema

I testi generati in italiano si riconoscono in due righe. Sono corretti e vuoti: pensati in inglese e tradotti parola per parola, pieni di «in un mondo sempre più», di triadi di aggettivi, di «non si tratta solo di X, ma di Y», di Titoli Con Le Maiuscole Ovunque e di lineette lunghe che in italiano non si usano.

Questa skill insegna a Claude le cose che un buon redattore italiano sa: la grammatica dove si sbaglia davvero, la sintassi che non suona tradotta, i registri (tu, lei, voi), i modi di dire, come si fa un titolo che viene aperto senza imbrogliare.

## Prima e dopo

Senza la skill:

> **Scopri Il Segreto Di Una Colazione Perfetta**
>
> In un mondo sempre più frenetico, la colazione rappresenta molto più di un semplice pasto: è un vero e proprio rituale. Non si tratta solo di caffè — si tratta di un'esperienza. I nostri cornetti sono freschi, fragranti e irresistibili, garantendo un momento di puro piacere.

Con la skill:

> **Il bar di via Roma**
>
> Siamo aperti dalle sei del mattino, e la prima cosa che facciamo è infornare i cornetti, che prepariamo noi con il burro e che verso le sei e mezza sono pronti. Di solito per le dieci non ne resta nessuno, quindi chi ci tiene a quello alla crema farebbe bene a non arrivare tardi. Per chi la mattina preferisce il salato ci sono toast, focaccia e uova, e il caffè è quello di una torrefazione di Trieste.
>
> Ci trovate al numero 12, tutti i giorni fino alle sette di sera tranne il lunedì.

C'è anche un secondo modo di sbagliare, che la skill tratta a parte: la prosa «asciutta» a frasette da dieci parole, con i due punti a effetto, che i modelli producono quando gli si chiede di evitare l'AI slop. Un articolo di giornale ha in media ventisei parole per frase, e la skill insegna a costruire periodi di quella misura.

## Che cosa contiene

| File | Contenuto |
| --- | --- |
| [`SKILL.md`](skills/italian-master/SKILL.md) | I principi, i segnali da rileggere, il metodo di lavoro |
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
| [`references/agenzie-digitali.md`](skills/italian-master/references/agenzie-digitali.md) | Come scrivono dodici agenzie digitali e di marketing: presentazioni, casi studio, blog, inglese del mestiere |
| [`references/registri.md`](skills/italian-master/references/registri.md) | Tu, lei, voi; email, social, siti, pubblica amministrazione, narrativa |
| [`references/titoli.md`](skills/italian-master/references/titoli.md) | Titoli giornalistici e web, oggetti di email, attacchi, il titolese da evitare |
| [`references/modi-di-dire.md`](skills/italian-master/references/modi-di-dire.md) | Modi di dire, proverbi, espressioni del parlato, equivalenti degli idiomi inglesi |
| [`references/imparare-una-voce.md`](skills/italian-master/references/imparare-una-voce.md) | Come ricavare una scheda di stile dai testi di riferimento dell'utente |
| [`references/fonti.md`](skills/italian-master/references/fonti.md) | Bibliografia e fonti |
| [`scripts/controlla.py`](skills/italian-master/scripts/controlla.py) | Script che segnala i sospetti più comuni in un testo |

Claude legge sempre `SKILL.md` e apre gli altri file solo quando servono.

## Installazione

### Con npx

È il modo più rapido, e non richiede di clonare la repo. Serve Node 18 o successivo.

```bash
npx github:micheledalsanto/italian-master
```

Il comando copia la skill in `~/.claude/skills/italian-master`, dove Claude Code la trova da solo. Rilanciato, la aggiorna.

```bash
npx github:micheledalsanto/italian-master --project   # solo nel progetto corrente (.claude/skills)
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

In Claude Code puoi anche chiamarla in modo esplicito: `/italian-master:italian-master` se l'hai installata come plugin, `/italian-master` se l'hai copiata a mano.

## Lo script di controllo

`controlla.py` cerca in un testo le formule, gli errori e i segnali tipografici più comuni, e ne misura il passo (parole per frase, frasi brevi, periodi lunghi, virgole, due punti) confrontandolo con quello di giornali e riviste. Solo libreria standard, Python 3.8 o successivo.

```bash
python skills/italian-master/scripts/controlla.py bozza.md
```

```
== bozza.md ==
131 parole, 10 frasi, 13.1 parole per frase

Aperture a tappeto (2)
  riga   3  In un mondo sempre più frenetico, la colazione rappr…
            → parti dal fatto
Tipografia (6)
  riga   1  Scopri Il Segreto Di Una Colazione Perfetta
            → maiuscole a ogni parola: in italiano solo la prima e i nomi propri
...
20 segnalazioni (153 ogni mille parole). Sono indizi: decide chi scrive.
```

Opzioni: `--json` per l'uscita strutturata, `--strict` per uscire con codice 1 se ci sono segnalazioni (utile in una pipeline).

Non è un rilevatore di testi generati e non pretende di esserlo. Segnala abitudini di scrittura deboli, chiunque le abbia.

## Da dove vengono le regole

Dall'Accademia della Crusca e da Treccani per la norma, e dalla tradizione della scrittura chiara per lo stile (Calvino, Eco, Serianni, Sabatini, Castellani Pollidori, Carrada). Le misure vengono da quasi un milione di parole lette e contate: articoli di otto testate italiane online, dieci siti di aziende ed enti, dodici siti di agenzie digitali, lettere, saggi e opere d'autore di pubblico dominio. L'elenco completo è in [`fonti.md`](skills/italian-master/references/fonti.md).

La skill non contiene testi altrui. Giornali e siti non sono nominati e nessuna loro frase è riportata: gli esempi sono scritti apposta, con fatti inventati. Le sole citazioni testuali sono brevi passi di opere uscite prima del 1930.

## Limiti

- È italiano d'Italia. Non copre l'italiano della Svizzera né le varietà regionali, se non per qualche cenno.
- La lingua cambia: quello che oggi è un calco domani sarà nei dizionari. Dove l'uso è in movimento la skill lo dice.
- I segnali dell'AI slop cambiano con i modelli. Il catalogo va tenuto aggiornato, ed è il motivo per cui la repo è pubblica.
- Nessuna regola sostituisce l'avere qualcosa da dire.

## Contribuire

Segnalazioni, correzioni e nuovi esempi sono benvenuti. Vedi [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Versioni

La versione corrente è la 1.1.0. Le modifiche sono elencate nel [CHANGELOG](CHANGELOG.md).

## Licenza

[MIT](LICENSE).

---

<a name="english"></a>

## English

Italian master is a Claude skill that makes Claude write Italian the way a skilled native writer does. It targets the patterns that make generated Italian text instantly recognisable: English calques, Title Case headings, em dashes, automatic triads, «non è solo X, è Y» constructions, inflated vocabulary, bureaucratic phrasing.

It covers grammar and spelling doubts, punctuation and typography conventions, syntax and logic, register (tu/lei/voi), idioms and proverbs with their English equivalents, headlines and email subject lines, and a workflow for learning a voice from reference texts. A small Python linter flags the most common tells.

Install in Claude Code:

```
/plugin marketplace add micheledalsanto/italian-master
/plugin install italian-master@italian-master
```

The skill triggers on any request whose output is Italian text, including requests written in English.

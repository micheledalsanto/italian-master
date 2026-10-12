# Italian master

[![Version](https://img.shields.io/github/package-json/v/micheledalsanto/italian-master?label=version&color=2ea44f)](CHANGELOG.md)
[![MIT license](https://img.shields.io/github/license/micheledalsanto/italian-master?label=license&color=blue)](LICENSE)

Italian as professionals write it, genre by genre, using only the facts it is given. An agent skill for Claude, Codex and other Agent Skills-compatible agents.

*The skill itself, its reference files and the changelog are written in Italian. [Leggi questo README in italiano](README.md).*

## One request, three answers

All three texts answer the same request: an email telling the clients of a professional firm that the office is closed from 11 to 24 August, that anyone with deadlines in that period should get in touch by 31 July, and that Paola answers her mobile for urgent matters.

Without the skill:

> **Oggetto: Aggiornamento Importante Sulla Nostra Chiusura Estiva**
>
> Gentile Cliente,
>
> speriamo che questa email ti trovi bene! In un periodo dell'anno in cui il riposo diventa fondamentale, desideriamo informarLa che il nostro team si prenderà una meritata pausa — per tornare più carico che mai. Non si tratta solo di una chiusura: è un'occasione per ricaricare le energie, rinnovarci e offrirti un servizio ancora migliore.

Without the skill, after asking for something more concise:

> **Oggetto: Ad agosto chiudiamo. Ecco cosa cambia.**
>
> Chiudiamo. Due settimane. Dall'11 al 24 agosto.
>
> Niente panico: le urgenze restano coperte. Il resto può aspettare. A settembre si riparte.

With the skill:

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

The first text mixes the informal *tu* and the formal *Lei* in one sentence, a calque of English "you", and contains none of the facts in the request. The second gives the dates, but in the voice of a slogan, and does not tell clients what they have to do. The third is what an Italian firm actually sends: formal register, dates, the deadline, a contact for urgent matters.

## Why it happens

Ask a model for a text in Italian and you usually get a page with no mistakes that no Italian would write. It opens with «In un mondo sempre più», uses three adjectives where one would do, capitalises every word of the headline and keeps the English em dash. Ask it to be more concise and it switches to five-word sentences with a punchline at the end, which is just as easy to spot.

This skill gives the model what a good Italian editor knows: where grammar really goes wrong, how to build a sentence that does not sound translated, when to use *tu*, *lei* or *voi*, how to write a headline, which verb tense a story needs. It also tells the model to add nothing to the facts it is given, so a text with little data comes out shorter and says what is missing. The guidance comes from real texts that were read and counted: newspapers, company and agency websites, essays, letters, novels.

## How it works

- **Measurements taken on Italian texts.** How long a sentence is in a newspaper, how many colons an article has, which tenses a novel uses, how a newsletter opens: the guidance comes from about five million counted words, and each reference file says which texts it is based on.
- **Rules by genre.** An email to a client, a website home page, an app's error message, an article and a short story need different things. A contrast or a triad that is a flaw in an article is normal in a tagline, and the skill says so case by case, with a list of false alarms.
- **Only the facts provided.** No numbers, names, quotes or plausible circumstances added for colour. If there is little data, the text comes out shorter.
- **Two flaws, not one.** Besides inflated slop there is the clipped kind, made of short sentences and one-liners, which appears when a model tries to avoid the first.
- **The register of whoever signs.** A firm, a company or an institution writes formally and in full, and the skill does not mistake informality for naturalness.

## What you can ask for

There is nothing to invoke: the skill triggers on any request whose output is Italian text, including requests written in English. A few examples:

- "Rewrite this About page in Italian, it sounds fake."
- "Give me ten Italian headlines for this article, no clickbait."
- "Write a payment reminder to architetto Ferraris, we use the formal *lei*."
- "Translate this post into Italian, it must not read like a translation."
- «Correggi solo gli errori, non toccare lo stile.»
- «Leggi questi tre numeri della mia newsletter e scrivi il prossimo con la stessa voce.»

In Claude Code you can also call it explicitly: `/italian-master:italian-master` if installed as a plugin, `/italian-master` if copied by hand.

The plugin ships three commands for the longer jobs:

| Command | What it does |
| --- | --- |
| `/italian-master:rivedi` | Revises a file or a pasted text and says what it changed |
| `/italian-master:voce` | Builds an author's style sheet from their texts, with measurements, and compares a draft against it |
| `/italian-master:configura` | Creates or updates the tone and audience file, asking a few questions |

### Genre by genre

Each genre has its own reference file, with measurements taken on texts of that genre. The agent always reads [`SKILL.md`](skills/italian-master/SKILL.md) and opens the other files only when they are needed.

| What you write | What it was measured on | Where it lives |
| --- | --- | --- |
| Emails, notices, letters to clients and suppliers | about fifty formal communications | [`corrispondenza-formale`](skills/italian-master/references/corrispondenza-formale.md), [`registri`](skills/italian-master/references/registri.md) |
| Home pages, taglines, wordplay, About pages, service pages | ten company and institution websites, twelve agency websites | [`giochi-di-parole`](skills/italian-master/references/giochi-di-parole.md), [`siti`](skills/italian-master/references/siti.md), [`agenzie-digitali`](skills/italian-master/references/agenzie-digitali.md) |
| Product pages | 1,138 pages from ten online shops | [`schede-prodotto`](skills/italian-master/references/schede-prodotto.md) |
| Paid ads | 904 ads by 732 advertisers | [`annunci`](skills/italian-master/references/annunci.md) |
| Newsletters | 136 issues of thirteen newsletters | [`newsletter`](skills/italian-master/references/newsletter.md) |
| Articles, posts, guides, headlines | eighty-six articles from eight publications, sixty-one pages from thirteen sites | [`periodo`](skills/italian-master/references/periodo.md), [`connettivi`](skills/italian-master/references/connettivi.md), [`attacchi-e-chiusure`](skills/italian-master/references/attacchi-e-chiusure.md), [`titoli`](skills/italian-master/references/titoli.md), [`testi-per-la-ricerca`](skills/italian-master/references/testi-per-la-ricerca.md), [`descrivere-e-raccontare`](skills/italian-master/references/descrivere-e-raccontare.md) |
| Explanations for non-experts and for children | twelve sites that explain or guide | [`tono-accogliente`](skills/italian-master/references/tono-accogliente.md), [`scrivere-per-bambini`](skills/italian-master/references/scrivere-per-bambini.md) |
| Interface copy | fifteen thousand strings from eight applications | [`microcopy`](skills/italian-master/references/microcopy.md) |
| Fiction | twenty novels for dialogue and scene, twenty-two books for verb tenses, twenty-six short stories and four fairy-tale collections | [`narrativa`](skills/italian-master/references/narrativa.md), [`narrativa-fantastica`](skills/italian-master/references/narrativa-fantastica.md), [`tempi-verbali`](skills/italian-master/references/tempi-verbali.md), [`modelli`](skills/italian-master/references/modelli.md) |
| Theses, essays, journal articles | forty-five articles from nine journals | [`scrittura-accademica`](skills/italian-master/references/scrittura-accademica.md) |
| Translations into Italian | lists of calques, false friends and idioms | [`calchi`](skills/italian-master/references/calchi.md), [`modi-di-dire`](skills/italian-master/references/modi-di-dire.md) |
| Revisions and proofreading | the Crusca and Treccani answers, and generated texts for comparison | [`ai-slop`](skills/italian-master/references/ai-slop.md), [`slop-asciutto`](skills/italian-master/references/slop-asciutto.md), [`impronte`](skills/italian-master/references/impronte.md), [`grammatica`](skills/italian-master/references/grammatica.md), [`punteggiatura-tipografia`](skills/italian-master/references/punteggiatura-tipografia.md), [`sintassi-stile`](skills/italian-master/references/sintassi-stile.md) |
| Texts in your own voice and tone | the texts you give it to read | [`imparare-una-voce`](skills/italian-master/references/imparare-una-voce.md), [`tono-e-pubblico`](skills/italian-master/references/tono-e-pubblico.md) |

## Installing it

### With npx

The quickest way, with no need to clone the repository. Requires Node 18 or later.

```bash
npx github:micheledalsanto/italian-master
```

The command copies the skill to `~/.claude/skills/italian-master`, where Claude Code picks it up automatically. Run it again to update.

```bash
npx github:micheledalsanto/italian-master --codex     # for Codex (~/.agents/skills)
npx github:micheledalsanto/italian-master --tutti     # for both Claude Code and Codex
npx github:micheledalsanto/italian-master --project   # current project only (.claude/skills, or .agents/skills with --codex)
npx github:micheledalsanto/italian-master rimuovi     # uninstall
npx github:micheledalsanto/italian-master --help      # all options (in Italian)
```

### With skills.sh

If you use the `skills` CLI from [skills.sh](https://skills.sh), which installs skills from GitHub for Claude Code, Codex, Cursor and other agents:

```bash
npx skills add micheledalsanto/italian-master
```

### Claude Code, as a plugin

Inside a Claude Code session:

```
/plugin marketplace add micheledalsanto/italian-master
/plugin install italian-master@italian-master
```

Or from the terminal:

```bash
claude plugin marketplace add micheledalsanto/italian-master
claude plugin install italian-master@italian-master
```

To install from a local copy of the repository, pass the folder path instead of `micheledalsanto/italian-master`. To try it for a single session without installing: `claude --plugin-dir ./italian-master`.

### Claude Code, by hand

```bash
git clone https://github.com/micheledalsanto/italian-master.git
cp -r italian-master/skills/italian-master ~/.claude/skills/
```

For a single project, copy it to `.claude/skills/` inside the project.

### Codex and other agents

Codex looks for skills in `.agents/skills`, in the project folder and in the home directory.

```bash
npx github:micheledalsanto/italian-master --codex             # ~/.agents/skills/italian-master
npx github:micheledalsanto/italian-master --codex --project   # ./.agents/skills/italian-master
```

Or by hand:

```bash
git clone https://github.com/micheledalsanto/italian-master.git
mkdir -p ~/.agents/skills && cp -r italian-master/skills/italian-master ~/.agents/skills/
```

Restart Codex. The skill can be called explicitly with `$italian-master` or from `/skills`. Other agents that follow the same format read `.agents/skills` too, and `--dir` installs to any other folder.

### Claude.ai and the desktop app

1. Download the repository and zip the `skills/italian-master` folder (the zip must contain the `italian-master` folder with `SKILL.md` inside).
2. In Claude, open the settings, go to the skills section and upload the zip.

## Tone and audience, your call

You decide once who you write for and in what tone, in a configuration file that the skill reads before writing.

```bash
npx github:micheledalsanto/italian-master configura            # for all your projects (~/.claude/italian-master.md)
npx github:micheledalsanto/italian-master configura --project  # current project only (.claude/italian-master.md)
npx github:micheledalsanto/italian-master configura --codex    # for Codex (~/.agents/italian-master.md)
```

The command creates a template to fill in. The template is in Italian, and whatever you leave empty the skill works out from the request.

| Entry | What goes in it |
| --- | --- |
| Pubblico (audience) | Who reads and how much they know: experts, people in the field but not technical, non-experts, mixed, children (with their age) |
| Tono (tone) | Formal, cordial, welcoming, journalistic, technical or commercial, or your own description |
| Persona (person) | *Tu*, *lei* or *voi* for the reader; *noi*, *io* or the impersonal form for the writer |
| Lingua (language) | How much English, words to use and to avoid |
| Testi di riferimento (reference texts) | The texts the skill should learn your voice from |
| Tipi di testo (text types) | Exceptions: «newsletter: accogliente, tu», «comunicazioni ai clienti: formale, voi» |

What you ask for in a single request overrides the configuration, and a project file overrides the personal one. The file lives outside the skill folder, so updates do not touch it. If you installed the skill by hand or on Claude.ai, copy the template from [`assets/italian-master.md`](skills/italian-master/assets/italian-master.md).

## Checking a text from the command line

`controlla.py` looks for the most common stock phrases, errors and typographic tells in a text, and measures its pace (words per sentence, short sentences, long periods, commas, colons) against Italian newspapers and magazines. It also computes the Gulpease readability index. It uses only the standard library and needs Python 3.8 or later. Its output is in Italian.

```bash
python skills/italian-master/scripts/controlla.py bozza.md
```

Options: `--json` for structured output, `--strict` to exit with code 1 when there are findings (useful in a pipeline), `--bambini` for texts written for children.

The same script measures a voice. Given three or more texts by the same author, it prints a sheet with the writer's and the reader's grammatical person, the pace of sentences and paragraphs, punctuation, the connectives the author prefers and the ones they never use, and recurring words. With `--confronta` it says where a draft departs from that voice.

```bash
python skills/italian-master/scripts/controlla.py --voce post1.md post2.md post3.md --confronta bozza.md
```

The script does not detect generated text and does not see invented facts. It flags weak writing habits, whoever has them, and a text with no findings can still be mediocre.

## Sources and limits

From the Accademia della Crusca and Treccani for the norm, and from the Italian tradition of clear writing for style (Calvino, Eco, Serianni, Sabatini, Castellani Pollidori, Carrada). The measurements come from about five million words that were read and counted: articles from eight Italian online publications, ten company and institution websites, twelve digital agency websites, thirteen newsletters, the product pages of ten online shops, nine hundred ads, the strings of eight applications, academic journal articles, fantastic fiction, letters, essays, fairy tales, novels, memoirs, plays and other public-domain works. The full list is in [`fonti.md`](skills/italian-master/references/fonti.md).

The skill contains no third-party text. Newspapers and websites are not named and none of their sentences is reproduced: the examples were written for the skill, with invented facts. The only verbatim quotations are short passages from works published before 1930.

- It is the Italian of Italy. It does not cover Swiss Italian or regional varieties, except in passing.
- Language changes: today's calque will be in tomorrow's dictionaries. Where usage is shifting, the skill says so.
- The tells of AI slop change with the models. The catalogue has to be kept up to date, which is why the repository is public.
- The skill works with the facts it is given. If the request has few, the text comes out short, and no rule can fill it in for someone who has nothing to say.

## Contributing, versions, license

Reports, corrections and new examples are welcome: the guidelines are in [`CONTRIBUTING.md`](CONTRIBUTING.md) (in Italian).

The current version is 1.17.0. Changes are listed in the [CHANGELOG](CHANGELOG.md) (in Italian).

The license is [MIT](LICENSE).

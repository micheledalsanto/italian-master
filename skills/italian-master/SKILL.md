---
name: italian-master
description: Scrive, riscrive e corregge testi in italiano naturale, come li scriverebbe un italiano che sa scrivere, eliminando l'AI slop, i calchi dall'inglese, il burocratese e le frasi fatte. Copre grammatica, ortografia, punteggiatura, sintassi, logica del testo, tono e registro (tu/lei/voi), modi di dire e proverbi, titoli giornalistici, titoli web e social, oggetti di email e newsletter. Usa questa skill ogni volta che l'output finale è un testo in italiano destinato a essere letto da persone: articoli, post, newsletter, email, landing page, copy, microcopy, comunicati, descrizioni prodotto, discorsi, traduzioni verso l'italiano, revisioni e "umanizzazioni" di testi che suonano finti, anche quando l'utente non nomina la skill e anche quando scrive in inglese ma vuole un testo italiano. Use it for any Italian-language writing, editing, proofreading, headline or translation-into-Italian task.
---

# Italian master

Questa skill serve a scrivere in italiano come scrive una persona che la lingua la conosce bene e che ha in mente qualcuno a cui rivolgersi.

Un testo generato si riconosce in due modi, e bisogna guardarsi da entrambi. Il primo è l'AI slop che tutti conoscono, quello gonfio, fatto di «in un mondo sempre più», di triadi di aggettivi e di conclusioni che ripetono quanto si è appena detto. Il secondo viene fuori proprio quando si cerca di evitare il primo, ed è una prosa a frasi corte e nette, piena di due punti a effetto e di sentenze in fondo ai capoversi, che un lettore italiano riconosce altrettanto in fretta perché nessuno, in Italia, scrive un articolo o una lettera così. Chiamiamola slop asciutto.

Tra le due c'è l'italiano che si legge sui giornali fatti bene e nei libri che durano, e che è fatto in buona parte di periodi di venti o trenta parole, legati tra loro da un «perché», da un «anche se», da un «però» messo al posto giusto.

## Prima di scrivere

**Cerca la configurazione di chi usa la skill.** Il tono e il pubblico li decide l'utente, in un file `italian-master.md` che sta nella cartella `.claude/` del progetto oppure in quella della sua home (`~/.claude/`). Se c'è, leggilo prima di ogni altra cosa: dice chi legge e quanto ne sa, quale tono usare (formale, cordiale, accogliente, giornalistico, tecnico, commerciale), se dare del tu, del lei o del voi, e quali testi prendere a modello. Quello che dice la richiesta vale più della configurazione, e la configurazione vale più di quello che dedurresti da solo. Se il file manca, deduci tono e pubblico dal contesto e, sotto un testo breve, di' in una riga che cosa hai assunto. I sei toni, lo stesso avviso scritto in ciascuno e che cosa cambia secondo il pubblico sono in `references/tono-e-pubblico.md`.

Conviene poi avere chiare quattro cose, e se la richiesta non le dice si deducono dal contesto, lasciando all'utente solo le domande da cui dipende davvero il testo.

1. **Chi legge**, perché da questo dipendono il registro e le parole che si possono dare per conosciute.
2. **Che cosa deve capire o fare alla fine.** Se non si riesce a dirlo in una frase, il testo non è ancora pronto per essere scritto.
3. **Tu, lei o voi**, scelti una volta e mantenuti fino in fondo, dato che mescolarli è l'errore più tipico di chi traduce «you» (vedi `references/registri.md`).
4. **Se il testo si legge o si consulta.** Un articolo, una newsletter, una pagina di presentazione o una lettera si leggono dall'inizio alla fine e vogliono una prosa che accompagni. Un avviso, una pagina di istruzioni, un'interfaccia o una scheda si consultano, e lì servono frasi brevi, elenchi e titoletti. Le pagine di un sito stanno a metà strada, con frasi di una ventina di parole e pochi connettivi (vedi `references/siti.md`).

## Come si scrive in italiano

**Scrivi periodi, non frasette.** In un testo da leggere la frase normale ha tra le venti e le trenta parole e contiene una principale con una o due subordinate, oppure un inciso che precisa. Gli articoli di un quotidiano online ben scritto hanno in media ventisei parole per frase, e le frasi sotto le sei parole sono due su cento. La regola delle frasi brevi viene dai manuali inglesi e, applicata all'italiano, produce un testo che ha il suono di una traduzione. Per costruire un periodo che resti leggibile si mette la principale all'inizio e si allunga in coda, con le relative, le apposizioni, i gerundi e i connettivi che l'italiano mette a disposizione. Gli strumenti, con esempi presi da testi veri, sono in `references/periodo.md`, che va letto prima di qualunque testo più lungo di poche righe.

**Tieni la frase breve per quando serve.** Una frase di cinque parole dopo due periodi lunghi ha molta forza, mentre tre frasi brevi di fila, o una in fondo a ogni capoverso, sono soltanto un singhiozzo. In una pagina ce ne può stare una, raramente due.

**Lega i fatti tra loro.** Quando due frasi vicine parlano della stessa cosa, quasi sempre la seconda è una subordinata della prima, e conviene scriverla come tale. I connettivi che servono sono quelli comuni e che impegnano a un rapporto preciso («perché», «quindi», «anche se», «però», «invece», «infatti», «anzi»), e in italiano stanno più spesso dentro la frase, dopo il primo elemento e tra due virgole, che in testa. «Inoltre», «infine» e «in conclusione» in apertura di capoverso non collegano niente. Il repertorio, con le frequenze misurate sui giornali, è in `references/connettivi.md`.

**Pensa la frase in italiano.** Molto AI slop nasce da frasi inglesi rivestite di parole italiane, come «assicurati di», «quando si tratta di», «fare la differenza», «portare al livello successivo». La domanda utile è come direbbe la stessa cosa una persona a voce, e la risposta di solito ha un verbo diverso. L'elenco dei calchi è in `references/calchi.md`. Questo non vuol dire tradurre tutto: i termini che chi fa un mestiere dice in inglese (landing page, call to action, brand, packaging) restano in inglese quando si scrive per chi quel mestiere lo conosce.

**Usa accostamenti che esistono.** Una coppia di parole può essere corretta e non essere italiano, come «una comunicazione gridata». Se un accostamento non lo si è mai sentito, va preso quello più comune, oppure lasciata la parola dell'originale. Tra una ripetizione e un sinonimo che non si usa, è meglio la ripetizione.

**Usa le parole che significano qualcosa.** Calvino chiamava «terrore semantico» la fuga davanti alle parole concrete, per cui si scrive «recarsi» invece di andare ed «effettuare» invece di fare. Oggi le parole di fuga sono «soluzioni», «realtà», «tematiche», «a 360 gradi», e sul versante dei verbi «rappresenta», «costituisce» e «si configura come», che quasi sempre stanno per «è». Questo non significa infilare un dettaglio concreto in ogni riga, cosa che dà al testo il tono di uno spot. Significa non nascondere un fatto dietro una parola vaga quando il fatto lo si conosce.

**Lascia fare alla grammatica italiana.** Il soggetto si sottintende («Abbiamo deciso», non «Noi abbiamo deciso»), il possessivo si toglie con le parti del corpo e le cose ovvie («ha messo le mani in tasca»), gli aggettivi che giudicano stanno di norma dopo il nome, e «esso», «essa», «egli» non si usano quasi più. L'ordine delle parole è libero e serve a dare rilievo: «il contratto lo firmiamo martedì» non dice la stessa cosa di «martedì firmiamo il contratto».

**Fatti sentire, nel modo che il genere consente.** In un saggio, in una newsletter, in un post o in una pagina di presentazione chi scrive può dire «io» o «noi», avere un parere e chiamarlo parere, ammettere di non essere sicuro. In un testo di cronaca la prima persona non c'è, e al suo posto ci sono le persone di cui si parla, con nome, qualifica e parole citate. La prosa vera è piena di parole che misurano la certezza e il peso di quello che si dice, come «di solito», «quasi», «in buona parte», «mi pare», «probabilmente», «proprio», «magari», e un testo in cui ogni affermazione è ugualmente categorica suona scritto da nessuno. L'ironia e l'understatement sono risorse dell'italiano e si possono usare, quando il contesto lo permette.

**Racconta i fatti al passato e con i loro nomi.** Il testo generato tende a un presente senza tempo e a soggetti generici («Un assistente può…», «Una risposta può…»), mentre chi scrive di cose accadute usa il passato prossimo, l'imperfetto e anche il remoto, e mette come soggetto persone e cose determinate. «Può» va riservato ai casi in cui c'è davvero un'incertezza, dicendo di chi è. Vedi `references/impronte.md`.

**Comincia dal fatto e finisci quando hai finito.** Negli articoli veri la prima frase contiene già una data, un nome o un numero, e l'ultima è quasi sempre un'informazione in più, non una morale. Vedi `references/attacchi-e-chiusure.md`.

**Accompagna chi non è del mestiere.** Quando il testo spiega qualcosa a persone non esperte, si comincia dalla situazione o dal dubbio del lettore, gli si dà del tu, ci si fa vedere con un «vediamo» o un «ti spiego», si mettono le sue domande nei punti in cui gli verrebbero e il termine tecnico arriva dopo la spiegazione. Anche i titoli devono essere frasi che si direbbero a voce. Vedi `references/tono-accogliente.md`.

**Non inventare.** Un numero, un nome, un orario o una citazione che l'utente non ha fornito non si aggiungono per rendere il testo più vivo. Se serve un dato che manca, lo si chiede, oppure si scrive la frase senza.

Per i passi d'autore da cui prendere il ritmo, `references/modelli.md`. Per lo scioglimento di frasi burocratiche e nominali, `references/sintassi-stile.md`.

## Che cosa rileggere

I segnali dello slop gonfio, il cui catalogo completo con le alternative è in `references/ai-slop.md`:

- aperture che partono dal mondo o dall'epoca («In un mondo sempre più…», «Nel panorama odierno…»)
- il falso contrasto («Non è solo X, è Y»)
- la triade automatica di aggettivi, vantaggi o verbi
- la coda di gerundi («…, garantendo qualità e contribuendo a…»)
- i verbi da brochure (sbloccare, potenziare, navigare, abbracciare, immergersi)
- le chiusure che riassumono («In conclusione», «In definitiva»)
- la voce da assistente («Ecco…», «Certamente!», «Spero ti sia utile»)
- la vaghezza autorevole («studi dimostrano», «secondo gli esperti»)
- la tipografia inglese: Maiuscole A Ogni Parola, lineette lunghe, virgola prima di «e» negli elenchi, grassetti sparsi

I segnali dello slop asciutto, descritti in `references/slop-asciutto.md`:

- frasi quasi tutte sotto le quindici parole, e nessun periodo lungo
- due punti usati per fare effetto, tre volte più frequenti che in un giornale
- una frase breve e sentenziosa in fondo a ogni capoverso
- il «non è X, è Y» in formato ridotto («È un tic, non uno stile»)
- dettagli concreti messi per colore, e gli elenchi di tre oggetti
- imperativi secchi rivolti al lettore («Taglia.», «Parti dal fatto.»)
- un'etichetta in grassetto in testa a ogni capoverso, in un testo che non è una guida
- nessun «forse», nessun inciso, nessuna parentesi, nessuno che dica «io»

Le impronte che restano anche senza formule, misurate in `references/impronte.md`:

- «può» e «possono» in quasi ogni frase
- frasi che cominciano con «Un» o «Una» seguiti da un soggetto generico
- solo verbi al presente, anche quando si parla di cose accadute
- poche relative, cioè pochi «che» e pochi «cui»
- nessun «forse», «infatti», «però», «proprio», «quasi», «ormai»
- nessuna persona citata con nome e parole sue

Nessuna di queste liste è un elenco di divieti, perché ognuna di queste forme ha i suoi usi legittimi, e diventano un segnale quando si accumulano. Vale anche il contrario: molte cose che passano per segnali («sempre più», il passivo, i gerundi, gli avverbi in -mente, «negli ultimi anni») nei giornali sono comunissime, e l'elenco di questi falsi allarmi è nello stesso `references/impronte.md`.

## Che cosa ti viene chiesto

**Scrivere da zero, descrivere, raccontare.** Prima di scrivere si elencano i fatti disponibili e quelli che mancano, e si decide qual è la cosa principale. Una descrizione dice nella prima frase che cos'è la cosa, e un racconto tiene lo stesso tempo verbale finché non arriva a oggi. Vedi `references/descrivere-e-raccontare.md`. Il testo si consegna senza premesse del tipo «Ecco il testo richiesto» e senza commenti in coda, salvo quando c'è da segnalare un dato mancante o una scelta che l'utente deve confermare.

**Rivedere o "umanizzare" un testo.** Si conservano il contenuto, i fatti e la voce dell'autore, e si corregge la lingua. Sotto il testo rivisto vanno poche righe su che cosa è cambiato e perché, scritte in prosa e raggruppate per tipo di intervento. Se una frase è vuota conviene dirlo e proporre di toglierla, o chiedere il dato che manca, perché riscrivere il vuoto con parole migliori produce solo un vuoto più elegante.

**Correggere le bozze.** Si toccano solo gli errori veri (ortografia, accenti, concordanze, punteggiatura, reggenze) e si lascia stare lo stile, a meno che la richiesta lo comprenda. Vedi `references/grammatica.md` e `references/punteggiatura-tipografia.md`.

**Titoli, oggetti, attacchi.** Vedi `references/titoli.md`. Si propongono più varianti da angoli diversi, indicando quale si sceglierebbe, e ogni titolo promette solo quello che il testo mantiene.

**Tradurre verso l'italiano.** Si traduce il senso, ricostruendo i periodi come li costruirebbe chi scrive in italiano, dato che la sintassi a frasi brevi dell'originale inglese è la prima cosa che tradisce una traduzione. Vedi `references/calchi.md` e, per le espressioni idiomatiche, `references/modi-di-dire.md`.

**Imparare una voce.** Quando l'utente indica dei testi di riferimento, vanno letti prima di scrivere, ricavandone una scheda di stile secondo `references/imparare-una-voce.md`. La voce dell'utente prevale sulle preferenze di questa skill.

## Rilettura finale

Prima di consegnare un testo da leggere conviene controllare, nell'ordine:

- se le frasi hanno lunghezze diverse e se la maggior parte supera le quindici parole
- se ci sono coppie di frasi brevi che andrebbero fuse in una
- se ogni «due punti» introduce davvero un elenco, una citazione o una conseguenza
- se l'ultima frase di ogni capoverso è lì per dire qualcosa o per fare effetto
- se tu, lei e voi sono coerenti dall'inizio alla fine
- accenti e apostrofi («perché», «è», «È», «un po'», «qual è»), maiuscole solo a inizio titolo, numeri e date all'italiana
- se ogni dato presente nel testo viene dall'utente o da una fonte
- se i fatti accaduti sono raccontati al passato, con soggetti determinati e senza salti di tempo verbale
- se ogni frase riscritta si capisce da sola, e se gli accostamenti di parole sono di quelli che si sentono dire
- se, letto ad alta voce, sembra detto da qualcuno

Lo script `scripts/controlla.py`, dove è possibile eseguirlo, segnala le formule più comuni e misura il passo delle frasi confrontandolo con quello dei testi veri:

```bash
python scripts/controlla.py testo.md
```

Le sue segnalazioni sono indizi da valutare, e un testo che non ne riceve può essere comunque mediocre.

## Quando leggere i riferimenti

| File | Quando |
| --- | --- |
| `references/tono-e-pubblico.md` | Per applicare la configurazione dell'utente, o per scegliere tono e pubblico quando manca |
| `references/periodo.md` | Prima di ogni testo da leggere più lungo di poche righe |
| `references/descrivere-e-raccontare.md` | Per descrivere un progetto o un prodotto, raccontare un percorso, scrivere partendo da appunti |
| `references/tono-accogliente.md` | Quando il testo deve guidare lettori non esperti: divulgazione, guide, lezioni, titoli di sezioni |
| `references/slop-asciutto.md` | Quando il testo esce a frasette, o dopo aver ripulito un testo dalle formule |
| `references/modelli.md` | Prima di un testo lungo, per prendere il passo da pagine vere |
| `references/connettivi.md` | Quando le frasi stanno una accanto all'altra senza legarsi, o il testo è tutto ugualmente sicuro |
| `references/attacchi-e-chiusure.md` | Per la prima e l'ultima frase di un articolo, di un post, di una newsletter |
| `references/impronte.md` | In rilettura, per i segni che restano dopo aver tolto le formule, e per non proibire cose normali |
| `references/ai-slop.md` | Per rivedere un testo che suona artificiale |
| `references/sintassi-stile.md` | Per sciogliere frasi burocratiche, nominali, passive |
| `references/calchi.md` | Per tradurre dall'inglese, o se il testo parla di tecnologia, lavoro, marketing |
| `references/grammatica.md` | Per un dubbio di ortografia, accenti, congiuntivo, pronomi, reggenze, femminili professionali |
| `references/punteggiatura-tipografia.md` | Per virgole, virgolette, lineette, maiuscole, numeri, date |
| `references/siti.md` | Per la pagina di un sito: home, chi siamo, valori, schede, avvisi. Con esempi da dieci siti italiani |
| `references/agenzie-digitali.md` | Per il sito, i casi studio o il blog di un'agenzia, di uno studio, di un consulente o di un'azienda di servizi digitali |
| `references/registri.md` | Per scegliere il tono di email, post, comunicazioni pubbliche, messaggi a un cliente |
| `references/titoli.md` | Per titoli, sottotitoli, oggetti di email, attacchi |
| `references/modi-di-dire.md` | Per usare un proverbio o un'espressione idiomatica, o tradurne una |
| `references/imparare-una-voce.md` | Quando l'utente fornisce testi da cui imparare uno stile |
| `references/fonti.md` | Per sapere da dove vengono queste indicazioni |

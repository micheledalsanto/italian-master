# Imparare una voce dai testi

Le regole di questa skill descrivono l'italiano scritto bene in generale. Ma ogni testata, ogni marchio e ogni persona ha un suo modo. Quando l'utente indica dei testi di riferimento («scrivi come questa newsletter», «questo è il nostro blog», «ti incollo tre miei post»), leggili prima di scrivere e ricava da lì le scelte di stile.

## Quando farlo

- L'utente dà link, file o testi incollati come modello.
- L'utente chiede di scrivere «con la mia voce» o «nello stile di».
- Devi continuare un lavoro esistente: il quarto post di un account, una pagina in più di un sito, il capitolo successivo.
- Nel progetto esiste già una scheda di stile (vedi sotto): leggila e seguila.

## Come leggere

Servono almeno due o tre testi, meglio cinque, dello stesso genere di quello da scrivere. Un solo testo insegna i tic di quel testo, non la voce.

Se i testi sono online, recuperali con gli strumenti disponibili. Se non riesci a leggerli (pagina a pagamento, accesso negato), dillo all'utente e chiedi di incollarli: non ricostruire uno stile a memoria fingendo di averlo letto.

Leggi cercando le scelte, cioè i punti in cui l'autore avrebbe potuto fare diversamente.

**Persona e rapporto con il lettore**

- Io, noi o impersonale? Tu, lei o voi?
- Si rivolge al lettore direttamente? Gli fa domande?
- Quanta distanza: confidenziale, cordiale, professionale, istituzionale?

**Frase**

- Lunghezza tipica e quanto varia. Conta le parole di una decina di frasi.
- Subordinate o frasi accostate? Incisi? Frasi nominali?
- Come comincia le frasi: dal soggetto, da un complemento, da una congiunzione («E», «Ma»)?

**Lessico**

- Parole ricorrenti, espressioni tipiche, eventuali parole che l'autore evita.
- Anglicismi: quanti e quali.
- Gergo di settore: spiegato o dato per scontato?
- Registro: alto, medio, colloquiale. Parolacce, regionalismi?

**Punteggiatura e forma**

- Virgolette: caporali o alte?
- Lineette, punto e virgola, due punti, parentesi: li usa?
- Punti esclamativi, puntini, emoji.
- Lunghezza dei capoversi. Titoletti, elenchi, grassetti.
- Come scrive numeri, date, ore.

**Struttura**

- Come attacca: dal fatto, da un aneddoto, da una domanda?
- Come chiude: sul fatto, con una battuta, con un invito?
- Come titola.

**Tono**

- Ironia, serietà, calore, polemica.
- Che cosa non fa mai.

## Misurare, quando si può

Se i testi sono in file e si possono eseguire comandi, lo script della skill conta quello che a occhio si stima male: la persona di chi scrive e quella del lettore, la lunghezza media delle frasi e dei capoversi, la quota di frasi brevi e di periodi lunghi, la punteggiatura, i legami che l'autore usa di più e quelli che non usa mai, le parole che tornano.

```bash
python scripts/controlla.py --voce post1.md post2.md post3.md
python scripts/controlla.py --voce post1.md post2.md post3.md --confronta bozza.md
```

Il secondo comando dice in quali misure la bozza si allontana dalla voce, e va lanciato prima di consegnare un testo scritto «con la voce di». Sotto le 1.500 parole di campione le misure sono indicative. Le cifre vanno nella scheda accanto a quello che si ricava leggendo, e non lo sostituiscono: dicono che l'autore scrive frasi di ventidue parole e non usa mai «inoltre», non perché una sua pagina si legge volentieri.

## La scheda di stile

Riassumi quello che hai trovato in una scheda breve, da tenere davanti mentre scrivi. Deve contenere osservazioni verificabili, non aggettivi: «frasi di 8-15 parole, quasi mai subordinate» è utile, «stile fresco e dinamico» no.

```markdown
# Voce: [nome della testata, del marchio o dell'autore]

Fonti lette: [elenco dei testi, con data]

## In una riga
[Chi parla, a chi, con che atteggiamento]

## Persona e registro
- [io/noi, tu/lei/voi, registro]

## Frase e ritmo
- [lunghezza, costruzioni tipiche]

## Lessico
- Usa: [...]
- Evita: [...]

## Punteggiatura e forma
- [virgolette, lineette, emoji, capoversi, numeri]

## Struttura
- Attacco: [...]
- Chiusura: [...]
- Titoli: [...]

## Tre frasi tipiche
> [citazioni brevi, testuali, che fanno sentire la voce]

## Non fa mai
- [...]
```

Se l'utente lavora in un progetto con dei file e vuole riusare la voce, proponi di salvare la scheda in `voci/<nome>.md` nella sua cartella di lavoro. Alle richieste successive, se trovi una cartella `voci/`, leggi la scheda pertinente prima di scrivere.

## Imitare senza copiare

- Si imita il modo, non le frasi. Non riusare periodi, immagini o battute dei testi letti.
- Le citazioni nella scheda servono a te come diapason. Nel testo nuovo non devono comparire.
- Se la voce è di un autore riconoscibile e l'utente non è quell'autore, non produrre testi che possano essere scambiati per suoi e fatti circolare come tali. Scrivere «alla maniera di» per esercizio, parodia dichiarata o ispirazione va bene.

## Quando la voce e le regole si scontrano

La voce dell'utente vince sulle preferenze di stile di questa skill. Se il marchio usa le emoji, dà del tu a tutti, ama gli anglicismi o le frasi di tre parole, si scrive così.

Restano ferme due cose:

1. **La correttezza.** Un errore di ortografia o di grammatica non è uno stile. Se i testi di riferimento ne contengono di sistematici («qual'è», «un pò», «perchè»), non riprodurli e segnalalo all'utente con tatto.
2. **L'AI slop.** Se i testi di riferimento ne sono pieni, non imitarlo alla cieca. Di' all'utente che cosa hai notato e chiedi se vuole mantenere quel tono o approfittarne per ripulirlo.

## Imparare leggendo, in generale

La skill non contiene testi altrui: contiene regole ricavate da chi ha studiato come scrivono gli italiani. Per orientarsi tra i modelli, l'elenco ragionato è in `fonti.md`. In breve, chi vuole un orecchio per l'italiano contemporaneo ben scritto può leggere, a seconda del genere:

- per la chiarezza espositiva: un quotidiano online che spiega le notizie, una buona rivista di approfondimento, le voci di un'enciclopedia
- per la saggistica che si fa leggere: Primo Levi, Natalia Ginzburg, Italo Calvino delle *Lezioni americane*, Umberto Eco delle *Bustine di Minerva*, Leonardo Sciascia
- per il parlato messo sulla pagina: Natalia Ginzburg di *Lessico famigliare*, Gianni Rodari, i dialoghi di Fruttero e Lucentini
- per la norma e i dubbi: le risposte della consulenza linguistica dell'Accademia della Crusca

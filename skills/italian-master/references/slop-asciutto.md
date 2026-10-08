# Lo slop asciutto

Quando a un modello si chiede di evitare le formule della scrittura artificiale, non comincia a scrivere come una persona. Passa a un secondo stile, più difficile da nominare e altrettanto riconoscibile: frasi corte e nette, due punti a effetto, un dettaglio concreto per riga, una sentenza in fondo a ogni capoverso. Ha l'aria della prosa «pulita» dei manuali di scrittura americani e del copywriting minimalista, e un lettore italiano lo fiuta quanto il primo, perché nessuno in Italia scrive un articolo o una lettera in quel modo.

Gli esempi di questo file vengono in buona parte dalla prima versione di questa skill e dai testi che aveva prodotto. Li lascio perché sono veri.

## Indice

1. I segnali
2. Perché succede
3. Come uscirne
4. Un esempio

## 1. I segnali

**Frasette in fila.** Soggetto, verbo, complemento, punto, per tutto il testo. La media sta intorno alle dodici parole per frase, quando un articolo di giornale ne ha in media ventisei, e quasi nessuna frase supera le trenta. Vedi le misure in `periodo.md`.

> Il caffè è una miscela di una torrefazione di Trieste. C'è anche il salato. Siamo in via Roma 12.

**I due punti a effetto.** Usati per creare una piccola attesa prima della seconda metà della frase, anche dove basterebbe una virgola o un «perché». Nei giornali i due punti sono sette o otto ogni mille parole, nella prosa asciutta venticinque.

> Il criterio non è abbassare il registro: è scegliere la parola più precisa.

**La sentenza a fine capoverso.** Ogni paragrafo si chiude con una frase breve che suona come una massima e che si potrebbe ricamare su un cuscino.

> «Andare» non è meno elegante di «recarsi»: è solo più onesto.
>
> Un buon finale è spesso solo il punto in cui hai smesso di avere cose da dire.

**La negazione che corregge, in formato ridotto.** Il «non è X, è Y» dello slop classico sopravvive accorciato, e spesso proprio nella sentenza finale.

> Non è un errore, è un modo di legare.
>
> È un tic, non uno stile.

**Il dettaglio concreto di fabbrica.** Un orario, un indirizzo, un ingrediente, una cifra tonda, messi lì perché «il concreto funziona». Quando sono inventati sono falsi, e quando sono veri ma scelti per fare colore danno al testo il tono di uno spot.

> Li facciamo noi, ogni mattina, con il burro. Alle sei e mezza sono pronti.

**L'elenco di tre cose concrete.** La triade di aggettivi è stata sostituita da una triade di oggetti, che è la stessa triade.

> Proviamo gli strumenti su lavori di tutti i giorni: una mail, un verbale, due preventivi da confrontare.

**L'imperativo secco e il tu da istruttore.** Ordini di una o due parole rivolti al lettore, uno dopo l'altro.

> Taglia. Di' la cosa. Parti dal fatto.

**L'etichetta in grassetto seguita dalla spiegazione.** Ogni capoverso comincia con tre parole in neretto e un punto. In una guida da consultare ha senso, e questo file lo fa. In un articolo, in una lettera o in un report scritto per essere letto è l'impronta digitale del generatore.

**Le simmetrie.** «Prima» e «Dopo», «Ora» e «Meglio», «Che cosa è cambiato», ripetuti identici per ogni esempio, e capoversi tutti della stessa lunghezza.

**Le anafore pubblicitarie.** «Niente premesse. Niente commenti.» «Senza stress, senza sprechi.» «Chi, quanto, quando, dove.»

**Nessuna esitazione.** Mancano «forse», «quasi», «un po'», «in genere», «mi pare», «del resto», «a dire il vero», mancano gli incisi e le parentesi, e manca chiunque dica «io». Tutte le affermazioni hanno lo stesso grado di sicurezza, che è il massimo, e una persona che scrive non è mai così certa di tutto.

**Il vocabolario del pulito.** Poche parole che tornano di continuo perché sono quelle con cui il modello parla della buona scrittura: «la cosa», «il fatto», «davvero», «basta», «e basta», «preciso», «concreto», «vero», «asciutto», «il lettore». In un testo di duemila parole «la cosa» può comparire venti volte.

## 2. Perché succede

Le istruzioni contro l'AI slop sono quasi tutte divieti: non gonfiare, non girarci intorno, non usare quel verbo. Un modello che le rispetta toglie, e quello che resta dopo aver tolto è una prosa scarna che somiglia ai consigli da cui è partita. In più quei consigli vengono dalla tradizione del *plain English*, che prescrive frasi brevi e parole semplici per una lingua in cui la subordinazione pesa più che in italiano. Applicati alla lettera, producono un italiano che ha la sintassi dell'inglese e il lessico dell'italiano, cioè un calco, solo più difficile da vedere perché non sta nelle parole.

C'è poi un equivoco sul concreto. Calvino chiedeva parole che significassero qualcosa, e non di disseminare in ogni frase un orario e un nome di via. Il dettaglio serve quando è quello che il lettore vuole sapere, e in un testo normale la maggior parte delle frasi non ne contiene nessuno.

## 3. Come uscirne

**Unire.** Rileggi cercando le coppie di frasi brevi che si possono fondere in una con un «che», un «perché», un «anche se», un «e». Se due frasi parlano della stessa cosa, quasi sempre la seconda era una subordinata della prima.

**Togliere i due punti.** Per ognuno chiediti se introduce davvero un elenco, una citazione o una conseguenza. Se serve solo a staccare la seconda metà della frase, va sostituito con una virgola, con un connettivo oppure riscrivendo la frase.

**Cancellare l'ultima frase del capoverso** quando è breve e sentenziosa. Il capoverso di solito finisce meglio una frase prima.

**Rimettere le misure.** Dove hai scritto una cosa più netta di quanto sai, rimetti «di solito», «in buona parte», «mi sembra», «per quanto ne so». Non è debolezza, perché chi legge si fida di più di chi distingue quello che sa da quello che pensa.

**Rimettere qualcuno.** Un testo è scritto da una persona o da una redazione, che possono dire «io» o «noi», avere una preferenza, ricordare un caso, ammettere di non essere sicuri.

**Rompere la simmetria.** Se tre esempi hanno la stessa forma, uno va raccontato in modo diverso. Se ogni paragrafo ha un'etichetta, toglile e lascia che sia la prima frase a dire di che cosa si parla.

**Contare.** Lo script `scripts/controlla.py` misura parole per frase, frasi brevi, periodi lunghi, virgole e due punti, e li confronta con le misure dei testi veri. In un testo da leggere la media deve stare sopra le diciotto parole e le frasi sotto le sei devono essere poche.

Un'avvertenza per evitare il difetto opposto. Uscire dalla prosa asciutta non vuol dire tornare al periodo gonfio dello slop classico, con i suoi «inoltre» e i suoi «svolge un ruolo fondamentale». La frase lunga che serve è quella che lega dei fatti, e il modello da tenere in mente è un buon articolo di giornale, non una circolare.

## 4. Un esempio

Il compito era riscrivere la presentazione di un bar, a partire da un testo pieno di formule. Questi dati li aveva forniti il proprietario: i cornetti sono fatti in casa con il burro e sfornati alle 6:30, verso le dieci di solito sono finiti, il caffè viene da una torrefazione di Trieste, il bar è in via Roma 12 ed è aperto dalle 6 alle 19, chiuso il lunedì.

Versione asciutta:

> **I cornetti escono dal forno alle 6:30**
>
> Li facciamo noi, ogni mattina, con il burro. Alle sei e mezza sono pronti e di solito alle dieci sono finiti: se ci tieni a quello alla crema, passa presto.
>
> Il caffè è una miscela di una torrefazione di Trieste. C'è anche il salato, per chi la mattina il dolce non lo regge: toast, focaccia, uova.
>
> Siamo in via Roma 12, aperti dalle 6 alle 19, chiusi il lunedì.

Versione scritta come la scriverebbe il proprietario:

> **Il bar di via Roma**
>
> Siamo aperti dalle sei del mattino, e la prima cosa che facciamo è infornare i cornetti, che prepariamo noi con il burro e che verso le sei e mezza sono pronti. Di solito per le dieci non ne resta nessuno, quindi chi ci tiene a quello alla crema farebbe bene a non arrivare tardi. Per chi la mattina preferisce il salato ci sono toast, focaccia e uova, e il caffè è quello di una torrefazione di Trieste.
>
> Ci trovate al numero 12, tutti i giorni fino alle sette di sera tranne il lunedì.

La seconda versione contiene le stesse informazioni e nessuna in più, ma sembra detta da qualcuno. I fatti sono legati tra loro («e la prima cosa che facciamo», «quindi chi ci tiene»), c'è un voi rivolto ai clienti come lo userebbe un barista, e il titolo è il nome con cui il posto è conosciuto in paese. Non è un testo memorabile, e non deve esserlo: è la pagina di un bar.

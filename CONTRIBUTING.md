# Contribuire

Questa skill migliora se chi scrive in italiano per mestiere ci mette le mani.

## Che cosa serve di più

- **Nuovi segnali di sbobba.** Formule che vedi comparire nei testi generati e che qui mancano. Cambiano a ogni generazione di modelli.
- **Calchi e falsi amici** non ancora elencati.
- **Correzioni.** Se una regola è sbagliata, troppo rigida o superata dall'uso, segnalalo con una fonte.
- **Casi di prova.** Richieste reali in cui la skill ha prodotto un testo debole.
- **Registri e generi poco coperti:** scrittura scientifica, legale, per la scuola, per il teatro, sottotitoli, doppiaggio.

## Come proporre una modifica

1. Apri una issue per discutere le modifiche grandi. Per le piccole basta una pull request.
2. Modifica i file in `skills/italian-master/`.
3. Se aggiungi una formula allo script, provala su un testo vero e controlla che non scatti su frasi innocenti.
4. Descrivi nella pull request che cosa hai cambiato e perché.
5. Aggiungi una riga al `CHANGELOG.md`, sotto la prossima versione.

## Criteri

**Una regola ha bisogno di una fonte o di un'evidenza.** Per la norma: Crusca, Treccani, una grammatica di riferimento, un dizionario dell'uso. Per i segnali di scrittura generata: più esempi reali, non un'impressione. Aggiungi la fonte in `references/fonti.md` se è nuova.

**Descrivi, non proibire.** Quasi nessuna parola è sbagliata in sé. Spiega quando diventa un problema e che cosa fare al suo posto. Le liste di parole vietate producono testi contorti.

**Ogni segnale ha un'alternativa.** Non basta dire «evita»: di' che cosa scrivere, o che la cosa giusta è tagliare.

**Solo esempi scritti apposta.** Non si incollano frasi di giornali, siti, libri sotto diritti o testi di altri, nemmeno brevi, e non si nominano le testate o le aziende da cui viene un'osservazione. Di quello che si è letto si descrive la forma, e l'esempio si costruisce con fatti inventati. Fanno eccezione i passi di opere uscite prima del 1930, che sono libere ovunque.

**Niente dati inventati negli esempi presentati come veri.** Se un esempio contiene un numero o un nome di fantasia, deve essere chiaro che è un esempio.

**La skill deve fare quello che predica.** I file sono scritti in italiano chiaro: titoli con la sola iniziale maiuscola, niente lineette lunghe, niente grassetti a pioggia, niente triadi automatiche. Prima di aprire la pull request passa il tuo testo allo script:

```bash
python skills/italian-master/scripts/controlla.py skills/italian-master/SKILL.md
```

Nei file di riferimento molte segnalazioni sono inevitabili, perché contengono gli esempi da evitare. In `SKILL.md` e nel `README.md` dovrebbero essere vicine a zero.

**Tieni `SKILL.md` corto.** È il file che Claude legge ogni volta. I dettagli vanno nei riferimenti, e `SKILL.md` dice quando aprirli.

## Struttura

```
.claude-plugin/          manifest del plugin e del marketplace
bin/italian-master.js    installatore per npx
package.json             metadati del pacchetto npm
skills/italian-master/
  SKILL.md               principi e metodo
  references/            approfondimenti, letti quando servono
  scripts/controlla.py   controllo automatico
evals/evals.json         casi di prova
```

## Provare le modifiche

In Claude Code, dalla cartella della repo:

```bash
claude plugin validate .
claude --plugin-dir .
```

Poi prova le richieste in `evals/evals.json` e confronta il risultato con quello atteso.

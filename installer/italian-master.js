#!/usr/bin/env node
'use strict';

// Installa la skill Italian master nella cartella delle skill di Claude Code, di Codex
// e degli altri agenti che leggono le Agent Skills (.agents/skills).
// Nessuna dipendenza: solo la libreria standard di Node.

const fs = require('fs');
const os = require('os');
const path = require('path');

const NOME = 'italian-master';
const SORGENTE = path.join(__dirname, '..', 'skills', NOME);
const pkg = require('../package.json');

const AIUTO = `Italian master ${pkg.version}
Skill per Claude, Codex e gli altri agenti che scrive, riscrive e corregge testi in italiano naturale.

Uso:
  npx ${NOME} [installa] [opzioni]   installa o aggiorna la skill
  npx ${NOME} rimuovi [opzioni]      toglie la skill
  npx ${NOME} configura [opzioni]    crea il file in cui scegli tono e pubblico
  npx ${NOME} dove [opzioni]         mostra la cartella di destinazione

Opzioni:
  --claude          per Claude Code (~/.claude/skills), è il default
  --codex           per Codex e gli agenti che leggono .agents/skills (~/.agents/skills)
  --tutti           per tutti e due
  --project, -p     installa nel progetto corrente (./.claude/skills o ./.agents/skills)
  --global, -g      installa per il tuo utente, è il default
  --dir <cartella>  installa in una cartella di skill a tua scelta
  --force, -f       sovrascrive anche una cartella che non sembra questa skill
  --help, -h        mostra questo aiuto
  --version, -v     mostra la versione

Esempi:
  npx ${NOME}
  npx ${NOME} --codex
  npx ${NOME} --tutti --project
  npx ${NOME} configura --project
  npx ${NOME} rimuovi
`;

function leggiArgomenti(argv) {
  const o = { comando: 'installa', ambito: 'global', agenti: ['claude'], dir: null, force: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--help' || a === '-h') o.comando = 'aiuto';
    else if (a === '--version' || a === '-v') o.comando = 'versione';
    else if (a === '--project' || a === '-p') o.ambito = 'project';
    else if (a === '--global' || a === '-g') o.ambito = 'global';
    else if (a === '--claude') o.agenti = ['claude'];
    else if (a === '--codex' || a === '--agents') o.agenti = ['agents'];
    else if (a === '--tutti' || a === '--all') o.agenti = ['claude', 'agents'];
    else if (a === '--force' || a === '-f') o.force = true;
    else if (a === '--dir') {
      o.dir = argv[++i];
      if (!o.dir) throw new Error('--dir vuole il percorso di una cartella.');
    } else if (['installa', 'install', 'aggiorna', 'update'].includes(a)) o.comando = 'installa';
    else if (['rimuovi', 'remove', 'uninstall'].includes(a)) o.comando = 'rimuovi';
    else if (['dove', 'where'].includes(a)) o.comando = 'dove';
    else if (['configura', 'config', 'configure'].includes(a)) o.comando = 'configura';
    else throw new Error(`Argomento non riconosciuto: ${a}`);
  }
  return o;
}

// Le cartelle di skill in cui lavorare: una per agente scelto, oppure quella indicata con --dir.
// Claude Code legge .claude/skills; Codex e gli altri agenti leggono .agents/skills.
function cartelleSkill(o) {
  if (o.dir) return [path.resolve(o.dir)];
  return o.agenti.map((agente) => {
    const nome = agente === 'claude' ? '.claude' : '.agents';
    if (o.ambito === 'project') return path.join(process.cwd(), nome, 'skills');
    const base = agente === 'claude' && process.env.CLAUDE_CONFIG_DIR
      ? process.env.CLAUDE_CONFIG_DIR
      : path.join(os.homedir(), nome);
    return path.join(base, 'skills');
  });
}

// Vero se la cartella contiene già questa skill (e quindi si può aggiornare o togliere senza --force).
function eQuestaSkill(dest) {
  try {
    const testo = fs.readFileSync(path.join(dest, 'SKILL.md'), 'utf8');
    return /^name:\s*italian-master\s*$/m.test(testo);
  } catch (e) {
    return false;
  }
}

function contaFile(dir) {
  let n = 0;
  for (const v of fs.readdirSync(dir, { withFileTypes: true })) {
    n += v.isDirectory() ? contaFile(path.join(dir, v.name)) : 1;
  }
  return n;
}

function installa(o) {
  if (!fs.existsSync(path.join(SORGENTE, 'SKILL.md'))) {
    throw new Error('Non trovo i file della skill dentro il pacchetto.');
  }
  for (const cartella of cartelleSkill(o)) {
    const dest = path.join(cartella, NOME);
    const esisteva = fs.existsSync(dest);
    if (esisteva && !eQuestaSkill(dest) && !o.force) {
      throw new Error(`${dest} esiste già e non sembra questa skill. Usa --force per sovrascriverla.`);
    }
    if (esisteva) fs.rmSync(dest, { recursive: true, force: true });
    fs.mkdirSync(dest, { recursive: true });
    fs.cpSync(SORGENTE, dest, { recursive: true });
    console.log(`${esisteva ? 'Skill aggiornata' : 'Skill installata'}: ${dest}`);
    console.log(`Versione ${pkg.version}, ${contaFile(dest)} file.`);
  }
  console.log('');
  console.log('Apri una nuova sessione: la skill si attiva da sola quando chiedi un testo in italiano.');
  console.log('Per chiamarla in modo esplicito: /italian-master in Claude Code, $italian-master in Codex.');
}

function rimuovi(o) {
  for (const cartella of cartelleSkill(o)) {
    const dest = path.join(cartella, NOME);
    if (!fs.existsSync(dest)) {
      console.log(`Niente da togliere: ${dest} non esiste.`);
      continue;
    }
    if (!eQuestaSkill(dest) && !o.force) {
      throw new Error(`${dest} non sembra questa skill. Usa --force per toglierla comunque.`);
    }
    fs.rmSync(dest, { recursive: true, force: true });
    console.log(`Skill tolta: ${dest}`);
  }
}

// Copia il modello di configurazione accanto alla cartella delle skill, dove un aggiornamento non lo tocca.
function configura(o) {
  const modello = path.join(SORGENTE, 'assets', `${NOME}.md`);
  for (const cartella of cartelleSkill(o)) {
    const dest = path.join(path.dirname(cartella), `${NOME}.md`);
    if (fs.existsSync(dest) && !o.force) {
      console.log(`La configurazione esiste già: ${dest}`);
      console.log('Aprila e modificala. Per ripartire dal modello vuoto usa --force.');
      continue;
    }
    fs.mkdirSync(path.dirname(dest), { recursive: true });
    fs.copyFileSync(modello, dest);
    console.log(`Configurazione creata: ${dest}`);
    console.log('Aprila e scrivi per chi scrivi e con che tono. Le voci lasciate vuote le decide la skill dal contesto.');
  }
}

function main() {
  const o = leggiArgomenti(process.argv.slice(2));
  if (o.comando === 'aiuto') return void console.log(AIUTO);
  if (o.comando === 'versione') return void console.log(pkg.version);
  if (o.comando === 'dove') return void cartelleSkill(o).forEach((c) => console.log(path.join(c, NOME)));
  if (o.comando === 'rimuovi') return rimuovi(o);
  if (o.comando === 'configura') return configura(o);
  return installa(o);
}

try {
  main();
} catch (e) {
  console.error(`Errore: ${e.message}`);
  console.error(`Per l'aiuto: npx ${NOME} --help`);
  process.exit(1);
}

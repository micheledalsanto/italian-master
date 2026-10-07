#!/usr/bin/env node
'use strict';

// Installa la skill Italian master nella cartella delle skill di Claude Code.
// Nessuna dipendenza: solo la libreria standard di Node.

const fs = require('fs');
const os = require('os');
const path = require('path');

const NOME = 'italian-master';
const SORGENTE = path.join(__dirname, '..', 'skills', NOME);
const pkg = require('../package.json');

const AIUTO = `Italian master ${pkg.version}
Skill per Claude che scrive, riscrive e corregge testi in italiano naturale.

Uso:
  npx ${NOME} [installa] [opzioni]   installa o aggiorna la skill
  npx ${NOME} rimuovi [opzioni]      toglie la skill
  npx ${NOME} dove [opzioni]         mostra la cartella di destinazione

Opzioni:
  --project, -p     installa nel progetto corrente (./.claude/skills)
  --global, -g      installa per il tuo utente (~/.claude/skills), è il default
  --dir <cartella>  installa in una cartella di skill a tua scelta
  --force, -f       sovrascrive anche una cartella che non sembra questa skill
  --help, -h        mostra questo aiuto
  --version, -v     mostra la versione

Esempi:
  npx ${NOME}
  npx ${NOME} --project
  npx ${NOME} rimuovi
`;

function leggiArgomenti(argv) {
  const o = { comando: 'installa', ambito: 'global', dir: null, force: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--help' || a === '-h') o.comando = 'aiuto';
    else if (a === '--version' || a === '-v') o.comando = 'versione';
    else if (a === '--project' || a === '-p') o.ambito = 'project';
    else if (a === '--global' || a === '-g') o.ambito = 'global';
    else if (a === '--force' || a === '-f') o.force = true;
    else if (a === '--dir') {
      o.dir = argv[++i];
      if (!o.dir) throw new Error('--dir vuole il percorso di una cartella.');
    } else if (['installa', 'install', 'aggiorna', 'update'].includes(a)) o.comando = 'installa';
    else if (['rimuovi', 'remove', 'uninstall'].includes(a)) o.comando = 'rimuovi';
    else if (['dove', 'where'].includes(a)) o.comando = 'dove';
    else throw new Error(`Argomento non riconosciuto: ${a}`);
  }
  return o;
}

function cartellaSkill(o) {
  if (o.dir) return path.resolve(o.dir);
  if (o.ambito === 'project') return path.join(process.cwd(), '.claude', 'skills');
  const base = process.env.CLAUDE_CONFIG_DIR || path.join(os.homedir(), '.claude');
  return path.join(base, 'skills');
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
  const dest = path.join(cartellaSkill(o), NOME);
  const esisteva = fs.existsSync(dest);
  if (esisteva && !eQuestaSkill(dest) && !o.force) {
    throw new Error(`${dest} esiste già e non sembra questa skill. Usa --force per sovrascriverla.`);
  }
  if (esisteva) fs.rmSync(dest, { recursive: true, force: true });
  fs.mkdirSync(dest, { recursive: true });
  fs.cpSync(SORGENTE, dest, { recursive: true });
  console.log(`${esisteva ? 'Skill aggiornata' : 'Skill installata'}: ${dest}`);
  console.log(`Versione ${pkg.version}, ${contaFile(dest)} file.`);
  console.log('');
  console.log('Apri una nuova sessione di Claude Code: la skill si attiva da sola quando chiedi un testo in italiano,');
  console.log('oppure la chiami con /italian-master.');
}

function rimuovi(o) {
  const dest = path.join(cartellaSkill(o), NOME);
  if (!fs.existsSync(dest)) {
    console.log(`Niente da togliere: ${dest} non esiste.`);
    return;
  }
  if (!eQuestaSkill(dest) && !o.force) {
    throw new Error(`${dest} non sembra questa skill. Usa --force per toglierla comunque.`);
  }
  fs.rmSync(dest, { recursive: true, force: true });
  console.log(`Skill tolta: ${dest}`);
}

function main() {
  const o = leggiArgomenti(process.argv.slice(2));
  if (o.comando === 'aiuto') return void console.log(AIUTO);
  if (o.comando === 'versione') return void console.log(pkg.version);
  if (o.comando === 'dove') return void console.log(path.join(cartellaSkill(o), NOME));
  if (o.comando === 'rimuovi') return rimuovi(o);
  return installa(o);
}

try {
  main();
} catch (e) {
  console.error(`Errore: ${e.message}`);
  console.error(`Per l'aiuto: npx ${NOME} --help`);
  process.exit(1);
}

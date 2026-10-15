"""Prove del pacchetto: quello che finisce nel commit deve restare leggibile da chi lo scarica.

Gli analizzatori dei cataloghi di plugin rifiutano un commit che contenga file di servizio
del sistema operativo (.DS_Store, Thumbs.db, __MACOSX), collegamenti simbolici, sottomoduli,
file speciali o una cartella troppo grande. Queste prove lo verificano prima della pubblicazione.
"""

import shutil
import subprocess
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GIT = shutil.which("git")

# Modi che git assegna a un file normale: tutto il resto è un collegamento simbolico (120000),
# un sottomodulo (160000) o un file speciale.
MODI_AMMESSI = {"100644", "100755"}

NOMI_DI_SERVIZIO = (
    ".ds_store",
    "thumbs.db",
    "desktop.ini",
    ".appledouble",
    ".spotlight-v100",
    ".trashes",
)

# Lo spazio di una cartella di plugin: un margine ampio sui limiti dei cataloghi.
LIMITE_PACCHETTO = 20 * 1024 * 1024
LIMITE_FILE = 2 * 1024 * 1024

# Estensioni dei file che si leggono come testo: lì i fine riga contano.
ESTENSIONI_DI_TESTO = {".md", ".py", ".js", ".json", ".yaml", ".yml", ".txt"}


def git(*argomenti, testo=True, ingresso=None):
    return subprocess.run([GIT, *argomenti], input=ingresso, capture_output=True, cwd=REPO,
                          text=testo, encoding="utf-8" if testo else None)


def versionati():
    """Percorso, modo e dimensione di ogni file nell'indice: in CI è il commit pubblicato,
    in locale è quello che sta per entrare nel commit."""
    elenco = git("ls-files", "-s")
    if elenco.returncode != 0:
        return []
    voci = []
    for riga in elenco.stdout.splitlines():
        intestazione, percorso = riga.split("\t", 1)
        modo, oggetto, _stadio = intestazione.split()
        voci.append((percorso, modo, oggetto))
    misura = git("cat-file", "--batch-check=%(objectsize)", ingresso="\n".join(o for _p, _m, o in voci))
    dimensioni = [int(d) if d.isdigit() else 0 for d in misura.stdout.split()]
    if len(dimensioni) != len(voci):
        dimensioni = [0] * len(voci)
    return [(percorso, modo, dimensione) for (percorso, modo, _o), dimensione in zip(voci, dimensioni)]


@unittest.skipUnless(GIT and (REPO / ".git").exists(), "serve il deposito git")
class Pacchetto(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file = versionati()
        if not cls.file:
            raise unittest.SkipTest("nessun file versionato da controllare")

    def test_nessun_file_di_servizio(self):
        trovati = [percorso for percorso, _modo, _dimensione in self.file
                   if Path(percorso).name.lower() in NOMI_DI_SERVIZIO
                   or any(parte.lower() in ("__macosx", ".appledouble") for parte in Path(percorso).parts)
                   or Path(percorso).name.startswith("._")]
        self.assertEqual(trovati, [], "file di servizio del sistema operativo nel commit")

    def test_solo_file_normali(self):
        strani = [(percorso, modo) for percorso, modo, _dimensione in self.file if modo not in MODI_AMMESSI]
        self.assertEqual(strani, [], "collegamenti simbolici, sottomoduli o file speciali nel commit")

    def test_nessun_sottomodulo(self):
        self.assertFalse((REPO / ".gitmodules").exists(), ".gitmodules: i cataloghi non raggiungono i sottomoduli")

    def test_fine_riga_unix(self):
        # Con i fine riga di Windows il frontmatter di SKILL.md non viene letto e la skill non si carica.
        colpevoli = [percorso for percorso, _modo, _dimensione in self.file
                     if Path(percorso).suffix.lower() in ESTENSIONI_DI_TESTO
                     and b"\r\n" in git("cat-file", "blob", f":{percorso}", testo=False).stdout]
        self.assertEqual(colpevoli, [], "fine riga di Windows nei file versionati")

    def test_dimensioni(self):
        grossi = [(percorso, dimensione) for percorso, _modo, dimensione in self.file if dimensione > LIMITE_FILE]
        self.assertEqual(grossi, [], "file troppo grandi per una cartella di plugin")
        self.assertLess(sum(dimensione for _p, _m, dimensione in self.file), LIMITE_PACCHETTO,
                        "il pacchetto è troppo grande")


if __name__ == "__main__":
    unittest.main()

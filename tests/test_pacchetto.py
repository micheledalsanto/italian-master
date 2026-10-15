"""Prove del pacchetto: quello che finisce nel commit deve restare leggibile da chi lo scarica.

L'analizzatore del catalogo dei plugin rifiuta un commit che contenga file di servizio del
sistema operativo (.DS_Store, Thumbs.db, desktop.ini, __MACOSX), collegamenti simbolici,
sottomoduli, file speciali, nomi che non valgono su Windows o su macOS, file troppo grandi o
un .gitattributes che riscrive il contenuto dei file. Quando si ferma non dice quale causa sia,
quindi le prove le controllano tutte prima della pubblicazione.
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

# Limiti del catalogo: oltre i 256 KiB un file che non sia un'immagine o un carattere
# tipografico manda la versione in lettura a una persona, e oltre 512 file anche.
LIMITE_FILE = 256 * 1024
LIMITE_NUMERO_FILE = 512
LIMITE_PACCHETTO = 20 * 1024 * 1024
ESTENSIONI_BINARIE_AMMESSE = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".woff", ".woff2", ".ttf", ".otf"}

# Attributi che riscrivono il contenuto dei file: con uno di questi l'analizzatore non apre il commit.
ATTRIBUTI_VIETATI = ("export-ignore", "export-subst", "filter", "text", "eol", "ident", "working-tree-encoding")

# Nomi riservati su Windows: un file che si chiama così non si può scaricare.
NOMI_RISERVATI = {"con", "prn", "aux", "nul", *(f"com{n}" for n in range(1, 10)), *(f"lpt{n}" for n in range(1, 10))}

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
        grossi = [(percorso, dimensione) for percorso, _modo, dimensione in self.file
                  if dimensione > LIMITE_FILE and Path(percorso).suffix.lower() not in ESTENSIONI_BINARIE_AMMESSE]
        self.assertEqual(grossi, [], "file oltre i 256 KiB: la versione finisce in lettura a una persona")
        self.assertLessEqual(len(self.file), LIMITE_NUMERO_FILE, "troppi file per una cartella di plugin")
        self.assertLess(sum(dimensione for _p, _m, dimensione in self.file), LIMITE_PACCHETTO,
                        "il pacchetto è troppo grande")

    def test_nessun_attributo_che_riscrive_i_file(self):
        # Un .gitattributes con text, eol, filter o export-ignore ferma l'analizzatore del catalogo
        # senza dire perché: i fine riga li tiene a posto test_fine_riga_unix, non un attributo.
        for percorso, _modo, _dimensione in self.file:
            if Path(percorso).name != ".gitattributes":
                continue
            testo = git("cat-file", "blob", f":{percorso}").stdout
            righe = [r for r in testo.splitlines() if r.strip() and not r.lstrip().startswith("#")]
            for riga in righe:
                pezzi = riga.split(maxsplit=1)
                attributi = pezzi[1] if len(pezzi) > 1 else ""
                for attributo in ATTRIBUTI_VIETATI:
                    with self.subTest(file=percorso, riga=riga):
                        self.assertNotIn(attributo, attributi)

    def test_nomi_validi_su_windows_e_su_macos(self):
        problemi = []
        for percorso, _modo, _dimensione in self.file:
            for parte in Path(percorso).parts:
                radice = parte.split(".")[0].lower()
                if ":" in parte or parte != parte.rstrip(". ") or radice in NOMI_RISERVATI:
                    problemi.append(percorso)
        self.assertEqual(problemi, [], "nomi che non valgono su Windows o su macOS")
        minuscoli = [percorso.lower() for percorso, _modo, _dimensione in self.file]
        doppioni = sorted({p for p in minuscoli if minuscoli.count(p) > 1})
        self.assertEqual(doppioni, [], "due nomi che differiscono solo per le maiuscole")


if __name__ == "__main__":
    unittest.main()

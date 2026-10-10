"""Prove dell'installatore per npx. Servono Node 18 o successivo e una cartella temporanea."""

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
INSTALLATORE = REPO / "installer" / "italian-master.js"
NODE = shutil.which("node")


@unittest.skipUnless(NODE, "node non è installato")
class Installatore(unittest.TestCase):
    def setUp(self):
        self.lavoro = Path(tempfile.mkdtemp(prefix="italian-master-prova-"))
        # Le prove installano solo nella cartella di un progetto finto, mai nella home di chi le lancia.
        (self.lavoro / "progetto").mkdir()

    def tearDown(self):
        shutil.rmtree(self.lavoro, ignore_errors=True)

    def lancia(self, *argomenti):
        return subprocess.run([NODE, str(INSTALLATORE), *argomenti], capture_output=True, text=True, encoding="utf-8",
                              cwd=self.lavoro / "progetto")

    def test_versione(self):
        r = self.lancia("--version")
        self.assertEqual(r.returncode, 0)
        self.assertRegex(r.stdout.strip(), r"^\d+\.\d+\.\d+$")

    def test_installa_nel_progetto_e_rimuove(self):
        dest = self.lavoro / "progetto" / ".claude" / "skills" / "italian-master"
        self.assertEqual(self.lancia("--project").returncode, 0)
        self.assertTrue((dest / "SKILL.md").exists())
        self.assertTrue((dest / "references" / "periodo.md").exists())
        self.assertTrue((dest / "scripts" / "controlla.py").exists())
        self.assertEqual(list(dest.rglob("__pycache__")), [])
        self.assertIn("aggiornata", self.lancia("--project").stdout)
        self.assertEqual(self.lancia("rimuovi", "--project").returncode, 0)
        self.assertFalse(dest.exists())

    def test_codex_nel_progetto(self):
        self.assertEqual(self.lancia("--codex", "--project").returncode, 0)
        self.assertTrue((self.lavoro / "progetto" / ".agents" / "skills" / "italian-master" / "SKILL.md").exists())

    def test_cartella_a_scelta(self):
        altrove = self.lavoro / "altrove"
        self.assertEqual(self.lancia("--dir", str(altrove)).returncode, 0)
        self.assertTrue((altrove / "italian-master" / "SKILL.md").exists())

    def test_non_sovrascrive_una_cartella_estranea(self):
        estranea = self.lavoro / "progetto" / ".claude" / "skills" / "italian-master"
        estranea.mkdir(parents=True)
        (estranea / "SKILL.md").write_text("---\nname: altra-cosa\n---\n", encoding="utf-8")
        self.assertNotEqual(self.lancia("--project").returncode, 0)
        self.assertEqual(self.lancia("--project", "--force").returncode, 0)

    def test_configura(self):
        self.assertEqual(self.lancia("configura", "--project").returncode, 0)
        self.assertTrue((self.lavoro / "progetto" / ".claude" / "italian-master.md").exists())

    def test_argomento_sconosciuto(self):
        self.assertNotEqual(self.lancia("--boh").returncode, 0)


if __name__ == "__main__":
    unittest.main()

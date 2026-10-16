"""Prove del benchmark e del suo grafico, senza lanciare sessioni. Si lanciano con: python -m unittest discover tests"""

import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "evals"))
import benchmark  # noqa: E402
import grafico_benchmark  # noqa: E402

ESEMPIO = {"casi": 12, "ripetizioni": 2, "modello": "sonnet", "giudice": "opus", "aggiornato": "2026-10-16",
           "senza": {"formule_ogni_mille": 6.4},
           "versioni": [{"versione": "1.0.0", "quota": 0.58, "formule_ogni_mille": 4.1},
                        {"versione": "1.18.6", "quota": 0.83, "formule_ogni_mille": 1.4}]}


class Formule(unittest.TestCase):
    def test_conta_le_formule(self):
        trovate, parole = benchmark.formule("Nel panorama odierno, non è solo un prodotto: è un viaggio.")
        self.assertGreater(trovate, 0)
        self.assertGreater(parole, 5)

    def test_le_citazioni_non_contano(self):
        trovate, _ = benchmark.formule("Ho tolto «nel panorama odierno» e «non è solo un prodotto».")
        self.assertEqual(trovate, 0)


class Grafico(unittest.TestCase):
    def test_svg_valido_in_due_lingue(self):
        with tempfile.TemporaryDirectory() as cartella:
            percorso = Path(cartella) / "benchmark.svg"
            grafico_benchmark.disegna(ESEMPIO, percorso)
            for file, parola in ((percorso, "alla pari"), (percorso.with_suffix(".en.svg"), "even")):
                testo = file.read_text(encoding="utf-8")
                ET.fromstring(testo)
                self.assertIn(parola, testo)
                self.assertIn("prefers-color-scheme: dark", testo)

    def test_una_sola_versione(self):
        esiti = dict(ESEMPIO, versioni=ESEMPIO["versioni"][-1:])
        ET.fromstring(grafico_benchmark.svg(esiti, "it"))

    def test_esiti_della_repo(self):
        esiti = REPO / "evals" / "benchmark" / "esiti.json"
        if esiti.exists():
            ET.fromstring(grafico_benchmark.svg(json.loads(esiti.read_text(encoding="utf-8")), "it"))


class Casi(unittest.TestCase):
    def test_casi_fissi(self):
        casi = json.loads(benchmark.CASI.read_text(encoding="utf-8"))["evals"]
        self.assertEqual(len({c["name"] for c in casi}), len(casi))
        for caso in casi:
            self.assertTrue(caso["prompt"] and caso["expected_output"])


if __name__ == "__main__":
    unittest.main()

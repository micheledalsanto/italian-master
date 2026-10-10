"""Prove di controlla.py. Si lanciano dalla radice della repo con: python -m unittest discover tests"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "skills" / "italian-master" / "scripts" / "controlla.py"
sys.path.insert(0, str(SCRIPT.parent))
import controlla  # noqa: E402


def categorie(testo, **opzioni):
    esito, _ = controlla.analizza(testo, **opzioni)
    return esito


def note(testo):
    return " | ".join(t["nota"] for trovati in categorie(testo).values() for t in trovati)


# Un capoverso di prosa con periodi legati, ripetuto quanto basta per le misure di passo.
PERIODO = ("Quando il consiglio comunale ha approvato il progetto, a marzo, nessuno pensava che i lavori sarebbero "
           "durati più di un anno, anche perché l'impresa aveva promesso di finire prima dell'estate. Poi però sono "
           "arrivati i ritardi nelle forniture, e la biblioteca è rimasta chiusa fino a ottobre. ")
PROSA = "\n\n".join(PERIODO * 2 for _ in range(6))

FRASETTE = "\n\n".join("Chiudiamo. Due settimane. Dall'11 al 24 agosto. Niente panico. Le urgenze restano coperte. "
                       "Il resto può aspettare. A settembre si riparte." for _ in range(10))


class Formule(unittest.TestCase):
    def test_apertura_a_tappeto(self):
        self.assertIn("Aperture a tappeto", categorie("In un mondo sempre più connesso, comunicare bene è fondamentale."))

    def test_falso_contrasto(self):
        self.assertIn("Falso contrasto", categorie("Non si tratta solo di una chiusura: è un'occasione per ripartire."))

    def test_lineetta_lunga(self):
        self.assertIn("lineetta lunga", note("Il team si prenderà una pausa — per tornare più carico."))

    def test_maiuscole_all_inglese(self):
        self.assertIn("maiuscole a ogni parola", note("# Aggiornamento Importante Sulla Nostra Chiusura Estiva\n\nTesto."))

    def test_titolo_italiano_non_segnalato(self):
        self.assertNotIn("maiuscole a ogni parola", note("# Chiusura estiva dello Studio dall'11 al 24 agosto\n\nTesto."))

    def test_ortografia(self):
        esito = categorie("Qual'è il problema? Ne parliamo tra un pò, perchè ora non posso.")
        self.assertGreaterEqual(len(esito.get("Ortografia", [])), 2)

    def test_frase_pulita_senza_segnalazioni(self):
        self.assertEqual(categorie("Lo studio resterà chiuso dall'11 al 24 agosto e riaprirà lunedì 25."), {})


class CodiceEFrontmatter(unittest.TestCase):
    def test_il_codice_non_viene_controllato(self):
        testo = "Ecco il comando.\n\n```\necho \"In un mondo sempre più — veloce\"\n```\n"
        self.assertNotIn("Aperture a tappeto", categorie(testo))

    def test_il_frontmatter_non_viene_controllato(self):
        testo = "---\ntitolo: In un mondo sempre più connesso\n---\n\nLo studio riapre lunedì."
        self.assertEqual(categorie(testo), {})


class Passo(unittest.TestCase):
    def test_prosa_a_periodi(self):
        esito, dati = controlla.analizza(PROSA)
        self.assertGreater(dati["parole_per_frase"], 20)
        self.assertNotIn("frasi corte in fila", " ".join(t["testo"] for t in esito.get("Forma e ritmo", [])))

    def test_frasette(self):
        esito, dati = controlla.analizza(FRASETTE)
        self.assertLess(dati["parole_per_frase"], 8)
        testi = " ".join(t["testo"] for t in esito.get("Forma e ritmo", []))
        self.assertIn("frasi corte in fila", testi)
        self.assertIn("frasi fino a 6 parole", testi)

    def test_bambini_ammette_le_frasi_corte(self):
        esito, _ = controlla.analizza(FRASETTE, bambini=True)
        testi = " ".join(t["testo"] for t in esito.get("Forma e ritmo", []))
        self.assertNotIn("frasi corte in fila", testi)

    def test_gulpease_tra_zero_e_cento(self):
        _, dati = controlla.analizza(PROSA)
        self.assertTrue(0 <= dati["gulpease"] <= 100)

    def test_testo_breve_senza_misure_di_passo(self):
        _, dati = controlla.analizza("Due righe soltanto. Niente di più.")
        self.assertNotIn("parole_per_frase", dati)


class Voce(unittest.TestCase):
    def test_persona_e_lettore(self):
        testo = "\n\n".join("Ti scrivo perché ho una novità che ti riguarda, e credo che ti farà piacere saperla prima degli altri. "
                            "Da lunedì ho deciso di aprire anche il sabato, così se vuoi passare con calma mi trovi fino alle sette."
                            for _ in range(8))
        dati = controlla.profilo_voce(testo)
        self.assertGreater(dati["io_ogni_mille"], dati["noi_ogni_mille"])
        self.assertGreater(dati["tu_ogni_mille"], 20)
        self.assertEqual(dati["virgolette"], "nessuna")

    def test_la_bozza_a_frasette_si_allontana(self):
        voce, bozza = controlla.profilo_voce(PROSA), controlla.profilo_voce(FRASETTE)
        diversi = [chiave for chiave, _, relativa, assoluta in controlla.MISURE_VOCE
                   if abs(bozza.get(chiave, 0) - voce.get(chiave, 0)) >= assoluta
                   and abs(bozza.get(chiave, 0) - voce.get(chiave, 0)) >= relativa * max(abs(voce.get(chiave, 0)), 1)]
        self.assertIn("parole_per_frase", diversi)

    def test_la_voce_confrontata_con_se_stessa(self):
        voce = controlla.profilo_voce(PROSA)
        diversi = [c for c, _, r, a in controlla.MISURE_VOCE if abs(voce.get(c, 0) - voce.get(c, 0)) >= a]
        self.assertEqual(diversi, [])


class RigaDiComando(unittest.TestCase):
    def lancia(self, *argomenti, ingresso=None):
        return subprocess.run([sys.executable, str(SCRIPT), *argomenti], input=ingresso, capture_output=True,
                              text=True, encoding="utf-8")

    def test_json_da_stdin(self):
        r = self.lancia("--json", ingresso="In un mondo sempre più veloce.")
        self.assertEqual(r.returncode, 0)
        self.assertIn("segnalazioni", json.loads(r.stdout)["stdin"])

    def test_strict_esce_con_uno(self):
        self.assertEqual(self.lancia("--strict", ingresso="In un mondo sempre più veloce.").returncode, 1)
        self.assertEqual(self.lancia("--strict", ingresso="Lo studio riapre lunedì 25 agosto.").returncode, 0)

    def test_file_inesistente(self):
        self.assertEqual(self.lancia("non-esiste.md").returncode, 2)

    def test_confronta_vuole_voce(self):
        self.assertEqual(self.lancia("--confronta", "bozza.md", ingresso="Testo.").returncode, 2)

    def test_i_file_della_skill_non_fanno_cadere_lo_script(self):
        for percorso in sorted((REPO / "skills" / "italian-master").rglob("*.md")):
            with self.subTest(file=percorso.name):
                self.assertEqual(self.lancia(str(percorso)).returncode, 0)


class Skill(unittest.TestCase):
    """La skill deve restare leggibile da chi interpreta lo YAML in modo rigoroso, e i rimandi devono esistere."""

    def setUp(self):
        self.cartella = REPO / "skills" / "italian-master"
        self.testo = (self.cartella / "SKILL.md").read_text(encoding="utf-8")

    def test_intestazione(self):
        righe = self.testo.split("\n")
        self.assertEqual(righe[0], "---")
        self.assertEqual(righe[1], "name: italian-master")
        self.assertRegex(righe[2], r'^description: ".+"$')
        self.assertNotIn('"', righe[2][len('description: "'):-1])
        self.assertEqual(righe[3], "---")
        self.assertNotIn("\r", self.testo)

    def test_i_riferimenti_citati_esistono(self):
        import re
        for nome in sorted(set(re.findall(r"`((?:references|scripts|assets)/[\w.-]+)`", self.testo))):
            with self.subTest(file=nome):
                self.assertTrue((self.cartella / nome).exists())

    def test_ogni_riferimento_ha_una_riga_nella_tabella(self):
        for percorso in sorted((self.cartella / "references").glob("*.md")):
            with self.subTest(file=percorso.name):
                self.assertIn(f"| `references/{percorso.name}` |", self.testo)

    def test_versioni_allineate(self):
        pacchetto = json.loads((REPO / "package.json").read_text(encoding="utf-8"))["version"]
        plugin = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
        self.assertEqual(pacchetto, plugin)
        self.assertIn(f"La versione corrente è la {pacchetto}.", (REPO / "README.md").read_text(encoding="utf-8"))
        self.assertIn(f"The current version is {pacchetto}.", (REPO / "README.en.md").read_text(encoding="utf-8"))
        self.assertIn(f"## [{pacchetto}]", (REPO / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_casi_di_prova_validi(self):
        import re
        casi = json.loads((REPO / "evals" / "evals.json").read_text(encoding="utf-8"))["evals"]
        self.assertEqual(len({c["id"] for c in casi}), len(casi))
        for caso in casi:
            for chiave in ("deve", "non_deve"):
                for modello in (caso.get("controlli") or {}).get(chiave, []):
                    with self.subTest(caso=caso["name"], modello=modello):
                        re.compile(modello)


if __name__ == "__main__":
    unittest.main()

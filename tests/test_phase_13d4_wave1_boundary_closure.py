from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
M080_PATH = REPO_ROOT / "skills" / "system_intelligence" / "M-080-shorts-generator.py"
M047_PATH = REPO_ROOT / "skills" / "script_intelligence_army" / "M-047-thumbnail-psychology-engine.py"
SARASWATI_PATH = REPO_ROOT / "directors" / "distribution" / "saraswati.md"
KRISHNA_PATH = REPO_ROOT / "directors" / "supreme_vision" / "krishna.md"


def load_module(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Phase13D4Wave1BoundaryClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.m080 = load_module(M080_PATH, "m080_shorts_generator")
        cls.m047 = load_module(M047_PATH, "m047_thumbnail_psychology_engine")

    def test_m080_blocks_film_route_as_content_shortform_only(self) -> None:
        result = self.m080.run(
            {
                "route_id": "FILM_SCREENPLAY_GENERATION",
                "dossier_id": "DOSSIER-FILM-M080",
            }
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["skill_id"], "M-080")
        self.assertFalse(result["cinema_core_authority"])
        self.assertTrue(result["content_shortform_only"])

    def test_m080_preserves_script_generation_shortform_behavior(self) -> None:
        result = self.m080.run(
            {
                "route_id": "SCRIPT_GENERATION",
                "dossier_id": "DOSSIER-SCRIPT-M080",
            }
        )

        self.assertEqual(result["status"], "success")
        self.assertFalse(result["payload"]["result"]["cinema_core_authority"])
        self.assertTrue(result["payload"]["result"]["content_shortform_only"])

    def test_m047_blocks_film_route_without_downstream_authorization(self) -> None:
        result = self.m047.run(
            {
                "route_id": "FILM_SCREENPLAY_GENERATION",
                "dossier_id": "DOSSIER-FILM-M047",
            }
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["skill_id"], "M-047")
        self.assertFalse(result["cinema_core_authority"])
        self.assertTrue(result["downstream_packaging_only"])

    def test_m047_allows_only_authorized_downstream_packaging_after_film_packet(self) -> None:
        result = self.m047.run(
            {
                "route_id": "FILM_SCREENPLAY_GENERATION",
                "film_packet_ready": True,
                "downstream_packaging_authorized": True,
                "dossier_id": "DOSSIER-FILM-M047-DOWNSTREAM",
            }
        )

        self.assertEqual(result["status"], "success")
        self.assertFalse(result["payload"]["result"]["cinema_core_authority"])
        self.assertTrue(result["payload"]["result"]["downstream_packaging_only"])

    def test_director_boundary_markers_remain_present(self) -> None:
        saraswati = SARASWATI_PATH.read_text(encoding="utf-8")
        krishna = KRISHNA_PATH.read_text(encoding="utf-8")

        self.assertIn("PHASE 13D_1 CINEMA PRE-PRODUCTION BOUNDARY", saraswati)
        self.assertIn("cinema_core_authority: false", saraswati)
        self.assertIn("downstream_release_authority: true", saraswati)
        self.assertIn("script_generation_preserved: true", saraswati)

        self.assertIn("PHASE 13D_1 CINEMA PRE-PRODUCTION ORCHESTRATION BOUNDARY", krishna)
        self.assertIn("cinema_preproduction_orchestrator: true", krishna)
        self.assertIn("film_screenplay_generation_core_owner: false", krishna)
        self.assertIn("downstream_packaging_is_not_cinema_core: true", krishna)


if __name__ == "__main__":
    unittest.main()

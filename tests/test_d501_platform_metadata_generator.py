from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
D501_PATH = REPO_ROOT / "skills" / "publishing" / "D-501-platform-metadata-generator.py"


def load_d501_module():
    spec = importlib.util.spec_from_file_location("d501_platform_metadata_generator", D501_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load D-501 module from {D501_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class D501CinemaBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.d501 = load_d501_module()

    def test_blocks_film_route_without_downstream_authorization(self) -> None:
        result = self.d501.run(
            {
                "route_id": "FILM_SCREENPLAY_GENERATION",
                "dossier_id": "DOSSIER-FILM-001",
            }
        )

        self.assertEqual(result["status"], "blocked")
        self.assertFalse(result["cinema_core_authority"])
        self.assertTrue(result["downstream_packaging_only"])
        self.assertIn("film_packet_ready=true", result["required_before_use"])
        self.assertIn("downstream_packaging_authorized=true", result["required_before_use"])

    def test_blocks_film_route_mode_without_downstream_authorization(self) -> None:
        result = self.d501.run(
            {
                "route_mode": "film_screenplay_generation",
                "dossier_id": "DOSSIER-FILM-002",
            }
        )

        self.assertEqual(result["status"], "blocked")
        self.assertEqual(result["route_id"], "FILM_SCREENPLAY_GENERATION")
        self.assertFalse(result["cinema_core_authority"])
        self.assertTrue(result["downstream_packaging_only"])

    def test_allows_authorized_downstream_packaging_after_film_packet(self) -> None:
        result = self.d501.run(
            {
                "route_id": "FILM_SCREENPLAY_GENERATION",
                "film_packet_ready": True,
                "downstream_packaging_authorized": True,
                "dossier_id": "DOSSIER-FILM-003",
                "content_title": "River of Witnesses",
                "primary_topic": "docudrama release prep",
                "target_platforms": ["youtube"],
            }
        )

        self.assertEqual(result["status"], "CREATED")
        self.assertEqual(result["skill_id"], "D-501")
        payload_status = result["payload"]["status"]
        self.assertFalse(payload_status["cinema_core_authority"])
        self.assertTrue(payload_status["downstream_packaging_only"])

    def test_preserves_script_generation_metadata_behavior(self) -> None:
        result = self.d501.run(
            {
                "route_id": "SCRIPT_GENERATION",
                "dossier_id": "DOSSIER-SCRIPT-001",
                "content_title": "Creator Strategy",
                "primary_topic": "content route preservation",
                "target_platforms": ["youtube", "instagram"],
            }
        )

        self.assertEqual(result["status"], "CREATED")
        raw_metadata = result["payload"]["evidence"]["raw_metadata"]
        self.assertEqual(sorted(raw_metadata), ["instagram", "youtube"])
        self.assertFalse(result["payload"]["status"]["cinema_core_authority"])
        self.assertTrue(result["payload"]["status"]["downstream_packaging_only"])


if __name__ == "__main__":
    unittest.main()

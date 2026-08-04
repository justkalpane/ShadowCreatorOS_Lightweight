from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "validators" / "validate_ffmpeg_log.py"
GOLD_FIXTURE = ROOT / "tests" / "shadow_runtime" / "fixtures" / "batch8i" / "gold" / "gold_ffmpeg_filtergraph_governance_crf18_bt709_lanczos_minimal.json"
BAD_FIXTURE = ROOT / "tests" / "shadow_runtime" / "fixtures" / "batch8i" / "bad" / "bad_ffmpeg_filtergraph_missing_bt709.json"


def run_validator(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


class FfmpegProductionFlagsTests(unittest.TestCase):
    def test_help(self) -> None:
        result = run_validator("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("usage:", result.stdout)

    def test_gold_fixture_passes(self) -> None:
        result = run_validator(str(GOLD_FIXTURE))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"actual_result": "PASS"', result.stdout)

    def test_bad_fixture_fails(self) -> None:
        result = run_validator(str(BAD_FIXTURE))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('"actual_result": "FAIL"', result.stdout)


if __name__ == "__main__":
    unittest.main()

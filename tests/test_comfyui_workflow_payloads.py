from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "validators" / "validate_comfyui_output.py"
GOLD_FIXTURE = ROOT / "tests" / "shadow_runtime" / "fixtures" / "batch8i" / "gold" / "gold_c18_comfyui_failure_state_timeout_carried_forward.json"
BAD_FIXTURE = ROOT / "tests" / "shadow_runtime" / "fixtures" / "batch8i" / "bad" / "bad_c18_comfyui_failure_state_missing_workflow_json.json"


def run_validator(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


class ComfyuiWorkflowPayloadTests(unittest.TestCase):
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

"""Artifact-bound duration validator for the film screenplay runtime proof."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet, screenplay_text
except ModuleNotFoundError:  # pragma: no cover - direct file execution fallback
    REPO_ROOT = Path(__file__).resolve().parents[3]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet, screenplay_text


PHASE = "13D_F3"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = True
GOVERNED_RUNTIME_PROOF_CLAIMED = False


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_duration",
        "phase": PHASE,
        "status": status,
        "passed": passed,
        "enforced": True,
        "runtime_behavior_changed": RUNTIME_BEHAVIOR_CHANGED,
        "route_selector_modified": ROUTE_SELECTOR_MODIFIED,
        "validator_bound_to_runtime": VALIDATOR_BOUND_TO_RUNTIME,
        "governed_runtime_proof_claimed": GOVERNED_RUNTIME_PROOF_CLAIMED,
        "errors": errors or [],
        "message": message,
    }


def validate(payload: dict[str, Any]) -> dict[str, Any]:
    packet = load_screenplay_packet(payload)
    expected_minutes = payload.get("duration_minutes", packet.get("duration_minutes"))
    text = screenplay_text(packet, payload)
    errors: list[str] = []

    if expected_minutes != 5:
        errors.append(f"duration_minutes must be 5, got {expected_minutes!r}")

    if packet.get("estimated_duration_minutes") not in (None, 5):
        errors.append("estimated_duration_minutes must be 5 or omitted")

    if text and packet.get("word_count"):
        if packet["word_count"] < 240:
            errors.append("screenplay is too short for a five-minute proof")

    if errors:
        return _result("VALIDATION_FAILED", False, "Film duration validation failed.", errors)

    return _result("VALIDATION_PASSED", True, "Film duration validation passed.")

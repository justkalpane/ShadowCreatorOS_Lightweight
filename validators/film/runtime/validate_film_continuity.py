"""Artifact-bound continuity validator for the film screenplay runtime proof."""

from __future__ import annotations

import sys
from typing import Any

from pathlib import Path

try:
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet
except ModuleNotFoundError:  # pragma: no cover - direct file execution fallback
    REPO_ROOT = Path(__file__).resolve().parents[3]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


PHASE = "13D_F3"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = True
GOVERNED_RUNTIME_PROOF_CLAIMED = False


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_continuity",
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
    scene_breakdown = packet.get("scene_breakdown") or []
    continuity_notes = packet.get("continuity_notes") or []
    errors: list[str] = []

    if not isinstance(scene_breakdown, list) or len(scene_breakdown) < 3:
        errors.append("at least 3 scenes are required")

    if not isinstance(continuity_notes, list) or not continuity_notes:
        errors.append("continuity_notes are required")

    if isinstance(scene_breakdown, list):
        scene_numbers = [item.get("scene_number") for item in scene_breakdown if isinstance(item, dict)]
        if scene_numbers != sorted(scene_numbers):
            errors.append("scene numbers must be sequential")

    if errors:
        return _result("VALIDATION_FAILED", False, "Film continuity validation failed.", errors)

    return _result("VALIDATION_PASSED", True, "Film continuity validation passed.")

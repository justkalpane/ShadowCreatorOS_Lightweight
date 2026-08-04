"""Artifact-bound scene card validator for the film screenplay runtime proof."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet
except ModuleNotFoundError:  # pragma: no cover - direct file execution fallback
    REPO_ROOT = Path(__file__).resolve().parents[3]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


PHASE = "13D_F6"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = True
GOVERNED_RUNTIME_PROOF_CLAIMED = False

REQUIRED_FIELDS = {
    "scene_number",
    "slugline",
    "location",
    "time_of_day",
    "characters_present",
    "scene_objective",
    "conflict",
    "turning_point",
    "emotional_value_start",
    "emotional_value_end",
    "visual_motif",
    "dialogue_subtext_goal",
    "continuity_dependencies",
}


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_scene_cards",
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
    scene_cards = packet.get("scene_cards") or []
    errors: list[str] = []

    if not isinstance(scene_cards, list) or len(scene_cards) < 3:
        errors.append("at least 3 scene cards are required")
        return _result("VALIDATION_FAILED", False, "Film scene card validation failed.", errors)

    scene_numbers: list[int] = []
    all_text = " ".join(str(card) for card in scene_cards).lower()
    for index, card in enumerate(scene_cards, start=1):
        if not isinstance(card, dict):
            errors.append(f"scene card {index} must be an object")
            continue
        missing = REQUIRED_FIELDS - set(card)
        if missing:
            errors.append(f"scene card {index} missing fields: {', '.join(sorted(missing))}")
        for field in ("scene_objective", "conflict", "turning_point", "emotional_value_start", "emotional_value_end"):
            if not isinstance(card.get(field), str) or not card.get(field).strip():
                errors.append(f"scene card {index} missing non-empty {field}")
        deps = card.get("continuity_dependencies")
        if not isinstance(deps, list) or not deps:
            errors.append(f"scene card {index} missing continuity_dependencies")
        number = card.get("scene_number")
        if not isinstance(number, int) or number < 1:
            errors.append(f"scene card {index} must have a positive scene_number")
        else:
            scene_numbers.append(number)

    if scene_numbers != sorted(scene_numbers):
        errors.append("scene cards must be ordered by scene_number")
    for required_term in ("pressure", "restraint", "repair"):
        if required_term not in all_text:
            errors.append(f"scene cards missing required {required_term} scene")
    if "toddler" not in all_text and "toddlers" not in all_text:
        errors.append("scene cards must preserve toddler stakes")

    if errors:
        return _result("VALIDATION_FAILED", False, "Film scene card validation failed.", errors)
    return _result("VALIDATION_PASSED", True, "Film scene card validation passed.")

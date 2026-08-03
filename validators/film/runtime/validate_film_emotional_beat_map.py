"""Artifact-bound emotional beat validator for the film screenplay runtime proof."""

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

DEFAULT_REQUIRED_BEATS = [
    "opening_image",
    "setup",
    "pressure_trigger",
    "internal_anger",
    "visible_restraint",
    "self_awareness",
    "repair_choice",
    "closing_image",
]

REQUIRED_BEAT_FIELDS = {
    "beat_id",
    "scene_number",
    "character_action",
    "emotional_state_before",
    "emotional_state_after",
    "story_function",
    "stakes_change",
}

BEAT_FAMILIES = [
    "opening_image",
    "setup",
    "pressure_trigger",
    "secondary_pressure",
    "internal_anger",
    "visible_restraint",
    "restraint_under_fire",
    "self_awareness",
    "deepened_self_awareness",
    "midpoint_reversal",
    "repair_choice",
    "closing_image",
]


def _normalize_beat_id(beat_id: str) -> str:
    for family in sorted(BEAT_FAMILIES, key=len, reverse=True):
        if beat_id == family or beat_id.startswith(family):
            return family
    return beat_id


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_emotional_beat_map",
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
    beat_map = packet.get("emotional_beat_map") or packet.get("beat_sheet") or []
    required_beats = (
        packet.get("genre_grammar_report", {}).get("required_beats")
        or DEFAULT_REQUIRED_BEATS
    )
    scene_breakdown = packet.get("scene_breakdown") or []
    errors: list[str] = []

    if not isinstance(beat_map, list) or not beat_map:
        errors.append("emotional_beat_map is required")
        return _result("VALIDATION_FAILED", False, "Film emotional beat validation failed.", errors)

    ordered_ids: list[str] = []
    beats_by_id: dict[str, dict[str, Any]] = {}
    normalized_ids: set[str] = set()
    for index, beat in enumerate(beat_map, start=1):
        if not isinstance(beat, dict):
            errors.append(f"beat {index} must be a structured object")
            continue

        missing_fields = REQUIRED_BEAT_FIELDS - set(beat)
        if missing_fields:
            errors.append(f"beat {beat.get('beat_id', index)!r} missing fields: {', '.join(sorted(missing_fields))}")

        beat_id = beat.get("beat_id")
        if not isinstance(beat_id, str) or not beat_id:
            errors.append(f"beat {index} missing beat_id")
            continue
        normalized = _normalize_beat_id(beat_id)
        if normalized not in set(required_beats) | {
            "setup",
            "internal_anger",
            "visible_restraint",
            "restraint_under_fire",
            "self_awareness",
            "deepened_self_awareness",
            "repair_choice",
            "midpoint_reversal",
            "secondary_pressure",
        }:
            errors.append(f"unexpected beat_id: {beat_id}")
            continue
        if beat_id in beats_by_id:
            errors.append(f"duplicate beat_id: {beat_id}")
            continue

        scene_number = beat.get("scene_number")
        if not isinstance(scene_number, int) or scene_number < 1:
            errors.append(f"beat {beat_id} must have a positive scene_number")

        for field in ("character_action", "emotional_state_before", "emotional_state_after", "story_function", "stakes_change"):
            if not isinstance(beat.get(field), str) or not beat.get(field).strip():
                errors.append(f"beat {beat_id} must include non-empty {field}")

        ordered_ids.append(normalized)
        beats_by_id[beat_id] = beat
        normalized_ids.add(normalized)

    missing_ids = [beat_id for beat_id in required_beats if beat_id not in normalized_ids]
    if missing_ids:
        errors.append(f"missing beat_ids: {', '.join(missing_ids)}")

    if ordered_ids:
        cursor = 0
        for beat_id in ordered_ids:
            if cursor < len(required_beats) and beat_id == required_beats[cursor]:
                cursor += 1
        if cursor != len(required_beats):
            errors.append("emotional_beat_map must preserve the required beat order")

    if not errors:
        scene_numbers = [beats_by_id[beat_id]["scene_number"] for beat_id in required_beats]
        if scene_numbers != sorted(scene_numbers):
            errors.append("beat scene ordering does not satisfy the required progression")

        final_scene = len(scene_breakdown) if isinstance(scene_breakdown, list) and scene_breakdown else max(scene_numbers)
        if "closing_image" in beats_by_id and beats_by_id["closing_image"]["scene_number"] != final_scene:
            errors.append("closing_image must occur in the final scene")

    if errors:
        return _result("VALIDATION_FAILED", False, "Film emotional beat validation failed.", errors)

    return _result("VALIDATION_PASSED", True, "Film emotional beat validation passed.")

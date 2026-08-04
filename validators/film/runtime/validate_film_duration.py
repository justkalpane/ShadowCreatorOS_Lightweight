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
    scene_cards = packet.get("scene_cards") or []
    sequence_count = len((packet.get("sequence_structure") or {}).get("sequences") or [])
    format_name = str(packet.get("format", "")).lower()
    errors: list[str] = []

    if expected_minutes in (None, "", 0):
        errors.append("duration_minutes is required")

    if packet.get("estimated_duration_minutes") not in (None, expected_minutes):
        errors.append("estimated_duration_minutes must match duration_minutes")

    if "feature" in format_name or (isinstance(expected_minutes, int) and expected_minutes >= 80):
        if expected_minutes < 80:
            errors.append("feature_film duration must be at least 80 minutes")
        if len(scene_cards) < 12:
            errors.append("feature-length proof requires at least 12 scene cards")
        if sequence_count < 6:
            errors.append("feature-length proof requires at least 6 sequences")
        if text and packet.get("word_count") and packet["word_count"] < 700:
            errors.append("screenplay is too short for a feature-length stress proof")
    elif "series" in format_name or "episode" in format_name or (isinstance(expected_minutes, int) and expected_minutes >= 40):
        if len(scene_cards) < 8:
            errors.append("expanded proof requires at least 8 scene cards")
        if sequence_count < 4:
            errors.append("expanded proof requires at least 4 sequences")
        if text and packet.get("word_count") and packet["word_count"] < 420:
            errors.append("screenplay is too short for an expanded-form proof")
    else:
        if expected_minutes != 5:
            errors.append(f"duration_minutes must be 5 for short-form proof, got {expected_minutes!r}")
        if text and packet.get("word_count") and packet["word_count"] < 240:
            errors.append("screenplay is too short for a five-minute proof")

    if errors:
        return _result("VALIDATION_FAILED", False, "Film duration validation failed.", errors)

    return _result("VALIDATION_PASSED", True, "Film duration validation passed.")

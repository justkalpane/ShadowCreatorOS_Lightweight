"""Validate emotional escalation depth."""

from __future__ import annotations

from typing import Any

from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


def validate(payload: dict[str, Any]) -> dict[str, Any]:
    packet = load_screenplay_packet(payload)
    depth = (packet.get("cinema_depth_packet") or {}).get("emotional_depth") or {}
    errors: list[str] = []
    scene_states = depth.get("scene_emotional_state") or []
    turns = depth.get("emotional_turning_points") or []
    flags = depth.get("flatline_risk_flags") or []
    if len(scene_states) < 3:
        errors.append("emotional depth requires at least 3 scene states")
    if len(turns) < 2:
        errors.append("emotional depth requires at least 2 emotional turning points")
    if flags:
        errors.extend(flags)
    act_map = depth.get("act_emotional_progression") or {}
    if any(details.get("flatline") for details in act_map.values() if isinstance(details, dict)):
        errors.append("one or more acts are emotionally flat")
    return {"validator": "validate_emotional_escalation", "passed": not errors, "status": "VALIDATION_PASSED" if not errors else "VALIDATION_FAILED", "errors": errors}

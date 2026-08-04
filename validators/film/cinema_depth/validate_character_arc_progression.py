"""Validate character arc progression depth."""

from __future__ import annotations

from typing import Any

from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


def validate(payload: dict[str, Any]) -> dict[str, Any]:
    packet = load_screenplay_packet(payload)
    depth = (packet.get("cinema_depth_packet") or {}).get("character_depth") or {}
    arc = depth.get("character_arc_map") or {}
    decisions = depth.get("decision_progression") or []
    errors: list[str] = []
    if not depth.get("want_need_gap"):
        errors.append("want and need must differ")
    if arc.get("transformation_start") == arc.get("transformation_end"):
        errors.append("character arc is static")
    if not any(item.get("behavior_shift") for item in decisions[-3:]):
        errors.append("late character decisions do not show behavioral change")
    if len(depth.get("flaw_pressure_points") or []) < 1:
        errors.append("flaw is not pressured by the story")
    return {"validator": "validate_character_arc_progression", "passed": not errors, "status": "VALIDATION_PASSED" if not errors else "VALIDATION_FAILED", "errors": errors}

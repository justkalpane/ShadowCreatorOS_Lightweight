"""Validate scene logic depth."""

from __future__ import annotations

from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


def validate(payload):
    packet = load_screenplay_packet(payload)
    depth = (packet.get("cinema_depth_packet") or {}).get("scene_logic_depth") or {}
    errors = []
    scene_logic = depth.get("scene_logic_map") or []
    if len(scene_logic) < 3:
        errors.append("scene logic depth requires at least 3 scenes")
    for item in scene_logic:
        if not item.get("objective") or not item.get("conflict") or not item.get("turning_point") or not item.get("consequence"):
            errors.append(f"scene {item.get('scene_number')} lacks full logic chain")
    errors.extend(depth.get("duplicate_conflict_flags") or [])
    errors.extend(depth.get("summary_scene_flags") or [])
    if len(depth.get("cause_effect_links") or []) < max(1, len(scene_logic) - 1):
        errors.append("scene chain lacks cause/effect continuity")
    return {"validator": "validate_scene_logic_depth", "passed": not errors, "status": "VALIDATION_PASSED" if not errors else "VALIDATION_FAILED", "errors": errors}

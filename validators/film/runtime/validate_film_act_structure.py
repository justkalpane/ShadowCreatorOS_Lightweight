from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, require_fields, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    acts = data.get("act_structure") or {}
    scene_cards = data.get("scene_cards") or []
    errors = require_fields(
        acts,
        [
            "act_one",
            "act_two",
            "act_three",
            "act_one_setup",
            "act_one_inciting_pressure",
            "act_two_escalation",
            "midpoint_shift_or_reversal",
            "act_three_choice",
            "resolution",
            "scene_mapping",
            "stakes_progression",
        ],
    )
    midpoint = str(acts.get("midpoint_shift_or_reversal", "")).lower()
    if not midpoint:
        errors.append("missing_midpoint")
    scene_mapping = acts.get("scene_mapping") or {}
    if not scene_cards or not all(beat_id in scene_mapping for beat_id in [*(acts.get("act_one") or []), *(acts.get("act_two") or []), *(acts.get("act_three") or [])]):
        errors.append("act_without_scene_mapping")
    stakes = acts.get("stakes_progression") or {}
    if len({stakes.get("start"), stakes.get("middle"), stakes.get("end")}) < 2:
        errors.append("no_stakes_change")
    if "choice" not in str(acts.get("act_three_choice", "")).lower() and "repair" not in str(acts.get("resolution", "")).lower():
        errors.append("resolution_without_choice")
    return result("validate_film_act_structure", not errors, errors)

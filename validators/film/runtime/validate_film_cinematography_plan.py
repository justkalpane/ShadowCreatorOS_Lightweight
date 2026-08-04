from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, require_fields, result


def validate(payload: dict) -> dict:
    plan = packet(payload).get("cinematography_plan") or {}
    errors = require_fields(
        plan,
        [
            "shot_types",
            "close_up_grammar",
            "wide_shot_grammar",
            "rule_of_thirds",
            "symmetry",
            "negative_space",
            "foreground_background_layering",
            "lens_intent",
            "camera_movement_motivation",
            "lighting_mood",
            "color_contrast",
            "visual_rhythm",
            "shot_progression",
        ],
    )
    progression = plan.get("shot_progression") or []
    if not isinstance(progression, list) or len(progression) < 3:
        errors.append("shot progression must cover at least 3 scenes")
    if not contains_any(str(plan.get("lens_intent", "")).lower(), ["lens", "natural", "compressed", "intimacy", "normal"]):
        errors.append("cinematography_without_lens_intent")
    if not all(isinstance(item, dict) and item.get("scene_number") and item.get("shot_type") and item.get("camera_reason") for item in progression):
        errors.append("shot_progression_not_scene_mapped")
    if not contains_any(str(plan.get("camera_movement_motivation", "")).lower(), ["emotion", "threat", "repair", "approach", "pressure"]):
        errors.append("camera_movement_without_story_reason")
    return result("validate_film_cinematography_plan", not errors, errors)

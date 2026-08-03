from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, require_fields, result


def validate(payload: dict) -> dict:
    visual = packet(payload).get("visual_language") or {}
    errors = require_fields(
        visual,
        [
            "visual_grammar",
            "staging",
            "blocking",
            "scene_intention",
            "emotional_framing",
            "camera_motivation",
            "reveal_design",
            "silence_design",
            "visual_metaphor",
            "frame_power_dynamics",
            "scene_visual_mapping",
        ],
    )
    mapping = visual.get("scene_visual_mapping") or []
    if not mapping or not all(isinstance(item, dict) and item.get("scene_number") and item.get("visual_strategy") for item in mapping):
        errors.append("visual_language_not_scene_mapped")
    if not contains_any(str(visual.get("silence_design", "")).lower(), ["silence", "pause", "held"]):
        errors.append("visual_language_only_keywords")
    return result("validate_film_visual_language", not errors, errors)

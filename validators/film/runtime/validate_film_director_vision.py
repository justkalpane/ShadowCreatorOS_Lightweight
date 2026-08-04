from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, require_fields, result


def validate(payload: dict) -> dict:
    vision = packet(payload).get("director_vision") or {}
    errors = require_fields(
        vision,
        [
            "director_note",
            "mood_map",
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
        ],
    )
    intentions = vision.get("scene_direction_map") or vision.get("scene_intention") or []
    if not isinstance(intentions, list) or len(intentions) < 3:
        errors.append("director vision must include scene intentions for at least 3 scenes")
    if intentions and not all(isinstance(item, dict) and "scene_number" in item and "objective" in item for item in intentions):
        errors.append("no_scene_visual_mapping")
    if not contains_any(str(vision.get("camera_motivation", "")).lower(), ["emotion", "pressure", "threat", "tender"]):
        errors.append("camera_without_motivation")
    if not contains_any(str(vision.get("blocking", "")).lower(), ["distance", "proximity", "approach", "retreat", "restraint"]):
        errors.append("blocking_not_tied_to_emotion")
    return result("validate_film_director_vision", not errors, errors)

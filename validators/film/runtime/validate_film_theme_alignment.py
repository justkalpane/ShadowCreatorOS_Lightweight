from __future__ import annotations

import json

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    theme = str(data.get("theme") or data.get("concept_note", {}).get("theme") or "").lower()
    beat_text = json.dumps(data.get("beat_sheet") or []).lower()
    screenplay = str(data.get("screenplay", "")).lower()
    final_image = json.dumps((data.get("treatment") or {}).get("ending_image", "")).lower()
    character_arc = json.dumps(data.get("character_arc") or {}).lower()
    scene_cards = json.dumps(data.get("scene_cards") or []).lower()
    errors = []
    if not theme:
        errors.append("theme missing")
    theme_terms = [term for term in theme.replace(".", " ").split() if len(term) > 5][:4]
    if not any(term in json.dumps(data.get("premise_test") or {}).lower() for term in theme_terms):
        errors.append("theme_only_in_metadata")
    if not contains_any(beat_text, theme_terms + ["restraint", "repair", "trust", "fear"]):
        errors.append("theme_not_in_beats")
    if not contains_any(character_arc, ["midpoint", "repair", "choice", "transform"]):
        errors.append("theme not tested through character arc")
    if not contains_any(final_image, theme_terms + ["repair", "hope", "trust", "care", "tender", "protected", "calm", "close", "joined"]):
        errors.append("theme_not_resolved")
    if not (
        contains_any(screenplay, ["repair", "pause", "trust", "care", "threat", "love", "tender"])
        or contains_any(scene_cards, ["repair", "pause", "trust", "care", "threat", "love", "tender"])
        or contains_any(character_arc, ["repair", "trust", "tender", "transform"])
    ) or "lecture" in screenplay:
        errors.append("theme_contradicted_by_character_action")
    return result("validate_film_theme_alignment", not errors, errors)

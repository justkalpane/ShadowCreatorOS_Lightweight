from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import (
    contains_any,
    non_empty_string,
    packet,
    require_fields,
    result,
)


GENERIC_PHRASES = ["be strong", "never give up", "believe in yourself", "life is hard"]


def validate(payload: dict) -> dict:
    data = packet(payload)
    premise = data.get("premise_test") or {}
    concept = data.get("concept_note") or {}
    errors = require_fields(
        premise,
        ["premise", "protagonist", "external_goal", "internal_need", "central_conflict", "stakes", "theme", "genre", "dramatic_question"],
    )
    premise_text = str(premise.get("premise", "")).lower()
    theme_text = str(premise.get("theme", "")).lower()
    if not non_empty_string(premise.get("external_goal")):
        errors.append("external goal missing or empty")
    if not non_empty_string(premise.get("internal_need")):
        errors.append("internal need missing or empty")
    if not contains_any(premise_text, ["must", "protect", "choose", "face"]):
        errors.append("premise must describe a dramatic obligation")
    if not contains_any(premise_text, ["conflict", "pressure", "anger", "threat", "distance", "fear"]) and not contains_any(
        str(premise.get("central_conflict", "")).lower(),
        ["anger", "pressure", "threat", "distance", "fear"],
    ):
        errors.append("premise_without_conflict")
    if not contains_any(str(premise.get("stakes", "")).lower(), ["child", "children", "toddler", "family", "trust", "love", "safety", "danger"]):
        errors.append("premise_without_stakes")
    if not any(phrase in premise_text for phrase in theme_text.split()[:3] if phrase) and not contains_any(theme_text, premise_text.split()):
        errors.append("premise_not_matching_theme")
    if any(phrase in premise_text for phrase in GENERIC_PHRASES):
        errors.append("generic_premise")
    if concept and premise.get("genre") != concept.get("genre"):
        errors.append("premise genre does not match concept note")
    return result("validate_film_premise", not errors, errors)

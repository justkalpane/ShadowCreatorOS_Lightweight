from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, result


VAGUE_TERMS = ["be better", "find strength", "change everything", "believe again"]


def validate(payload: dict) -> dict:
    data = packet(payload)
    logline = str(data.get("logline") or data.get("concept_note", {}).get("logline") or "")
    treatment = data.get("treatment") or {}
    screenplay = str(data.get("screenplay", ""))
    lowered = logline.lower()
    errors = []
    if len(logline.split()) < 12:
        errors.append("logline is too short")
    if not contains_any(lowered, [str(data.get("character_list", [{}])[0].get("name", "")).lower(), "parent", "lover", "guardian", "teacher"]):
        errors.append("logline missing protagonist identity")
    if not contains_any(lowered, ["must", "tries to", "has to", "protect", "save", "repair"]):
        errors.append("logline_without_goal")
    if not contains_any(lowered, ["against", "before", "when", "while", "threat", "pressure", "fear", "distance"]):
        errors.append("logline_without_obstacle")
    if not contains_any(lowered, ["trust", "family", "safety", "love", "danger", "stakes", "children"]):
        errors.append("logline_without_stakes")
    if data.get("genre", "").replace("_", " ") not in lowered and not contains_any(lowered, ["thriller", "romance", "drama", "crime", "horror"]):
        errors.append("logline missing genre signal")
    if any(term in lowered for term in VAGUE_TERMS):
        errors.append("logline is vague motivational prose")
    if treatment and not contains_any(lowered, [str(treatment.get("stakes", "")).lower(), str(treatment.get("central_conflict", "")).split()[0].lower()]):
        errors.append("logline_not_matching_packet")
    if screenplay and not contains_any(screenplay.lower(), [word for word in lowered.split() if len(word) > 5][:4]):
        errors.append("logline does not echo screenplay action")
    return result("validate_film_logline", not errors, errors)

from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import result


def validate(payload: dict) -> dict:
    packets = payload.get("packets") or []
    errors = []
    if len(packets) < 3:
        errors.append("three lane packets required")
        return result("validate_film_lane_voice_differentiation", False, errors)

    screenplays = {packet.get("genre"): packet.get("screenplay", "").lower() for packet in packets}
    if len(set(screenplays.values())) != len(screenplays):
        errors.append("same narration rhythm reused")
    if all("don't fix" in text or "next time" in text for text in screenplays.values()):
        errors.append("same dialogue rhythm reused")
    if "motivational_drama" in screenplays and "worksheet" not in screenplays["motivational_drama"]:
        errors.append("motivational voice missing domestic micro-pressure")
    if "thriller" in screenplays and "valve" not in screenplays["thriller"]:
        errors.append("thriller voice missing tactical threat vocabulary")
    if "romance" in screenplays and "anniversary" not in screenplays["romance"]:
        errors.append("romance voice missing relational wound vocabulary")
    if all("repair" in text for text in screenplays.values()):
        errors.append("same repair language removed insufficiently")
    return result("validate_film_lane_voice_differentiation", not errors, errors)

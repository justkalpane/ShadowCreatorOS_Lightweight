from __future__ import annotations

from collections import Counter

from validators.film.runtime.preproduction_validator_utils import result


FORBIDDEN_SHARED_PHRASES = {
    "moves through the scene with subtext",
    "present without becoming explanatory prose",
    "chooses pause",
    "the room keeps that choice",
}


def _closing_line(packet: dict) -> str:
    lines = (packet.get("screenplay") or "").strip().splitlines()
    return lines[-1].strip().lower() if lines else ""


def validate(payload: dict) -> dict:
    packets = payload.get("packets") or []
    errors = []
    if len(packets) < 2:
        errors.append("at least two packets are required for template comparison")
        return result("validate_film_template_reuse", False, errors)

    scene_counts = [len(packet.get("scene_cards", [])) for packet in packets]
    if len(set(scene_counts)) == 1:
        errors.append("all revised outputs share the same scene count")

    closing_lines = [_closing_line(packet) for packet in packets]
    if len(set(closing_lines)) != len(closing_lines):
        errors.append("closing cadence is reused across outputs")

    phrase_hits = Counter()
    for packet in packets:
        screenplay = (packet.get("screenplay") or "").lower()
        for phrase in FORBIDDEN_SHARED_PHRASES:
            if phrase in screenplay:
                phrase_hits[phrase] += 1
    repeated_phrases = [phrase for phrase, count in phrase_hits.items() if count >= 2]
    if repeated_phrases:
        errors.append("shared template phrases detected: " + ", ".join(sorted(repeated_phrases)))

    if len(packets) == 3:
        genres = [packet.get("genre") or packet.get("premise_test", {}).get("genre") for packet in packets]
        if len(set(genres)) == 3:
            objective_heads = []
            for packet in packets:
                objective = (packet.get("scene_cards") or [{}])[0].get("scene_objective", "")
                objective_heads.append(" ".join(objective.lower().split()[:4]))
            if len(set(objective_heads)) == 1:
                errors.append("genre-specific openings collapse into the same objective shape")

    return result("validate_film_template_reuse", not errors, errors)

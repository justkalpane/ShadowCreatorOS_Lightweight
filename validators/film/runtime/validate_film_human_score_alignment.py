from __future__ import annotations

from tools.film_runtime.quality.film_quality_score_engine import analyze_template_reuse
from validators.film.runtime.preproduction_validator_utils import result


def validate(payload: dict) -> dict:
    report = payload.get("quality_score_report") or {}
    packet = payload.get("preproduction_packet") or payload.get("packet") or {}
    estimated_human = payload.get("estimated_human_score", report.get("estimated_human_score"))
    errors = []

    if estimated_human is None:
        errors.append("estimated_human_score missing")
        return result("validate_film_human_score_alignment", False, errors)

    overall = report.get("overall_score")
    if not isinstance(overall, (int, float)):
        errors.append("overall_score missing")
        return result("validate_film_human_score_alignment", False, errors)

    if overall - float(estimated_human) > 1.5:
        errors.append("engine score exceeds estimated human score by more than 1.5")

    template = analyze_template_reuse(packet) if packet else {}
    if template.get("template_phrase_hits") and overall > 6.5:
        errors.append("template-heavy output cannot score above 6.5")
    if len(template.get("repeated_sentence_starts", {})) >= 2 and overall > 6.5:
        errors.append("repeated sentence pattern cannot score above 6.5")

    weak_visual = report.get("score_dimensions", {}).get("visual_embodiment", 10) < 6
    weak_dialogue = report.get("score_dimensions", {}).get("dialogue_subtext_depth", 10) < 6
    generic_output = report.get("score_dimensions", {}).get("cinematic_embodiment", 10) < 6
    if weak_visual and overall > 6.5:
        errors.append("weak visual embodiment cannot score above 6.5")
    if weak_dialogue and overall > 6.5:
        errors.append("weak dialogue subtext cannot score above 6.5")
    if generic_output and overall > 6.0:
        errors.append("generic output cannot score above 6.0")

    return result("validate_film_human_score_alignment", not errors, errors)

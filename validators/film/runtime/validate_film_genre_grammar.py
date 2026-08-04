from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, result


REQUIRED_GENRES = {
    "motivational_drama",
    "social_drama",
    "thriller",
    "horror",
    "romance",
    "comedy",
    "crime",
    "action",
    "mythology_fantasy",
    "mass_commercial",
    "short_film",
    "feature_film",
    "web_series",
}


def validate(payload: dict) -> dict:
    report = packet(payload).get("genre_grammar_report") or {}
    current_map = report.get("current_genre_rule_map") or {}
    available = set(report.get("available_genres") or [])
    errors = []
    if not REQUIRED_GENRES.issubset(available):
        errors.append("multi-genre rule registry is incomplete")
    for key in [
        "story_logic",
        "scene_logic",
        "pacing_logic",
        "character_logic",
        "visual_logic",
        "negative_rules",
        "required_beats",
        "required_scene_functions",
        "validator_hooks",
    ]:
        if key not in current_map:
            errors.append(f"current genre rule map missing {key}")
    if report.get("genre") not in available:
        errors.append("invalid_genre")
    if not report.get("required_beats") or not report.get("required_scene_functions"):
        errors.append("missing required genre rule group")
    if not report.get("passed"):
        errors.append("current genre grammar must pass")
    return result("validate_film_genre_grammar", not errors, errors)

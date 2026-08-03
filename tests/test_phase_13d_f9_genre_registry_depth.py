import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.preproduction.genre_grammar_engine import load_genre_registry, validate_genre_grammar
from validators.film.runtime import validate_film_genre_grammar


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


def load_payload(name: str) -> dict:
    return json.loads((ROOT / f"tests/fixtures/film/{name}").read_text(encoding="utf-8"))


def test_genre_registry_depth():
    registry = load_genre_registry()
    genres = registry["genres"]
    assert REQUIRED_GENRES.issubset(set(genres))
    for genre_name, rules in genres.items():
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
            assert key in rules, f"{genre_name} missing {key}"

    payload = load_payload("f9_payload_thriller_short.json")
    parsed = {
        "genre": payload["genre"],
        "theme": payload["theme"],
        "pressure_trigger": payload["emotional_pressure_trigger"],
        "stakes": payload["stakes"],
        "setting": payload["setting"],
    }
    beat_sheet = [
        {"beat_id": "opening_image", "story_function": "setup threat"},
        {"beat_id": "pressure_trigger", "story_function": "threat pressure"},
        {"beat_id": "midpoint_reversal", "story_function": "reversal"},
        {"beat_id": "repair_choice", "story_function": "choice"},
        {"beat_id": "closing_image", "story_function": "quiet aftermath"},
    ]
    scene_cards = [
        {"scene_objective": "setup suspicion", "conflict": "threat pressure", "turning_point": "reversal", "visual_motif": "shadowed practical-light thriller realism"},
        {"scene_objective": "contain the threat", "conflict": "panic", "turning_point": "choice", "visual_motif": "shadowed practical-light thriller realism"},
        {"scene_objective": "quiet aftermath", "conflict": "fear", "turning_point": "repair", "visual_motif": "shadowed practical-light thriller realism"},
    ]
    report = validate_genre_grammar(parsed, beat_sheet, scene_cards)
    assert report["passed"] is True
    invalid = validate_genre_grammar({"genre": "invalid_genre"}, beat_sheet, scene_cards)
    assert invalid["passed"] is False
    broken = {"preproduction_packet": {"genre_grammar_report": dict(report)}}
    del broken["preproduction_packet"]["genre_grammar_report"]["current_genre_rule_map"]["required_scene_functions"]
    assert validate_film_genre_grammar.validate(broken)["passed"] is False


if __name__ == "__main__":
    test_genre_registry_depth()
    print("phase_13d_f9_genre_registry_depth_ok")

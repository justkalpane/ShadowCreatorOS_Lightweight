"""Genre grammar checks for cinema preproduction."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTRY_PATH = REPO_ROOT / "registries/film/film_genre_rules.yaml"


def load_genre_registry() -> dict[str, Any]:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def _text_blob(parsed: dict[str, Any], beat_sheet: list[dict[str, Any]], scene_cards: list[dict[str, Any]]) -> str:
    return " ".join(
        [
            parsed.get("genre", ""),
            parsed.get("theme", ""),
            parsed.get("pressure_trigger", ""),
            parsed.get("stakes", ""),
            " ".join(beat.get("beat_id", "") for beat in beat_sheet),
            " ".join(beat.get("story_function", "") for beat in beat_sheet),
            " ".join(card.get("scene_objective", "") for card in scene_cards),
            " ".join(card.get("conflict", "") for card in scene_cards),
            " ".join(card.get("turning_point", "") for card in scene_cards),
            " ".join(card.get("visual_motif", "") for card in scene_cards),
        ]
    ).lower()


def _scene_function_hits(parsed: dict[str, Any], scene_cards: list[dict[str, Any]], required_scene_functions: list[str]) -> dict[str, bool]:
    text = " ".join(
        [
            parsed.get("theme", ""),
            " ".join(card.get("scene_objective", "") for card in scene_cards),
            " ".join(card.get("conflict", "") for card in scene_cards),
            " ".join(card.get("turning_point", "") for card in scene_cards),
        ]
    ).lower()
    alias_map = {
        "setup": ["setup", "opening", "warm", "establish", "show affection"],
        "pressure": ["pressure", "threat", "fear", "fragile"],
        "restraint": ["restraint", "pause", "contain", "tactical"],
        "repair": ["repair", "tender", "reconnect", "trust"],
        "suspicion": ["suspicion", "threat", "unease"],
        "reversal": ["reversal", "pivot", "reveal", "dangerous", "realizes"],
        "choice": ["choice", "decides", "return"],
        "approach": ["approach", "affection", "invite"],
        "retreat": ["retreat", "distance", "withdrawal"],
        "confession": ["confession", "honesty", "seen"],
    }
    hits = {}
    for name in required_scene_functions:
        aliases = alias_map.get(name.lower(), [name.lower()])
        hits[name] = any(alias in text for alias in aliases)
    return hits


def _genre_checks(parsed: dict[str, Any], beat_sheet: list[dict[str, Any]], scene_cards: list[dict[str, Any]], rules: dict[str, Any]) -> dict[str, bool]:
    text = _text_blob(parsed, beat_sheet, scene_cards)
    beat_ids = {beat.get("beat_id") for beat in beat_sheet}
    scene_cards_count = len(scene_cards)
    scene_function_hits = _scene_function_hits(parsed, scene_cards, rules.get("required_scene_functions", []))
    objectives = " ".join(card.get("scene_objective", "") for card in scene_cards).lower()
    visuals = " ".join(card.get("visual_motif", "") for card in scene_cards).lower()
    checks = {
        "required_beats_present": all(beat in beat_ids for beat in rules.get("required_beats", [])),
        "required_scene_functions_present": all(scene_function_hits.values()) if scene_function_hits else True,
        "negative_rules_avoided": not any(term.replace("_", " ") in text for term in rules.get("negative_rules", [])),
        "visual_logic_bound": bool(rules.get("visual_logic")) and bool(visuals.strip()),
        "scene_count_supports_duration": scene_cards_count >= 3,
    }

    genre = parsed.get("genre", "")
    if genre == "motivational_drama":
        checks.update(
            {
                "grounded_realism": bool(parsed.get("setting")),
                "internal_conflict": "anger" in text or "internal" in text,
                "visible_restraint": "restraint" in text or "pause" in text,
                "emotional_repair": "repair" in text,
                "earned_hope": "hope" in text or "soft" in text,
            }
        )
    elif genre == "thriller":
        checks.update(
            {
                "pressure_escalates": "pressure" in text or "suspicion" in text or "threat" in text,
                "reversal_present": "reversal" in text or "reveal" in text or "pivot" in text,
                "fear_logic_present": "fear" in text or "danger" in text or "panic" in text,
            }
        )
    elif genre == "romance":
        checks.update(
            {
                "relationship_pressure_present": "relationship" in text or "trust" in text or "love" in text,
                "vulnerability_present": "vulnerab" in text or "confession" in text or "tender" in text,
                "emotional_exchange_present": "mirror" in text or "support" in text or "repair" in text,
            }
        )
    else:
        checks["genre_story_logic_bound"] = bool(rules.get("story_logic")) and any(
            token in text for token in str(rules.get("story_logic", "")).lower().split()[:3]
        )
    return checks


def validate_genre_grammar(parsed: dict[str, Any], beat_sheet: list[dict[str, Any]], scene_cards: list[dict[str, Any]]) -> dict[str, Any]:
    registry = load_genre_registry()
    genres = registry.get("genres", {})
    current_genre = parsed.get("genre", "motivational_drama")
    if current_genre not in genres:
        return {
            "genre": current_genre,
            "registry_id": registry.get("registry_id"),
            "available_genres": sorted(genres),
            "current_genre_rule_map": {},
            "rules": [],
            "checks": {"genre_registered": False},
            "required_beats": [],
            "required_scene_functions": [],
            "scene_function_hits": {},
            "validator_hooks": [],
            "passed": False,
            "message": f"{current_genre} grammar failed",
        }

    current_rules = genres[current_genre]
    checks = _genre_checks(parsed, beat_sheet, scene_cards, current_rules)
    scene_function_hits = _scene_function_hits(parsed, scene_cards, current_rules.get("required_scene_functions", []))
    return {
        "genre": current_genre,
        "registry_id": registry.get("registry_id"),
        "available_genres": sorted(genres),
        "current_genre_rule_map": current_rules,
        "rules": sorted(set(current_rules.get("required_beats", []) + current_rules.get("required_scene_functions", []))),
        "checks": checks,
        "required_beats": current_rules.get("required_beats", []),
        "required_scene_functions": current_rules.get("required_scene_functions", []),
        "scene_function_hits": scene_function_hits,
        "validator_hooks": current_rules.get("validator_hooks", current_rules.get("required_validator_hooks", [])),
        "passed": bool(current_rules) and all(checks.values()),
        "message": f"{current_genre} grammar passed" if bool(current_rules) and all(checks.values()) else f"{current_genre} grammar failed",
    }

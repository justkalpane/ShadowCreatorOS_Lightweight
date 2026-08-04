"""Cinema-depth feature density analysis."""

from __future__ import annotations

from typing import Any


def build_feature_density_report(parsed: dict[str, Any], scene_cards: list[dict[str, Any]], sequence_structure: dict[str, Any]) -> dict[str, Any]:
    duration = int(parsed.get("duration_minutes", 5))
    macro_scene_count = len(scene_cards)
    sub_scene_count = sum(len(card.get("sub_scene_cards", [])) for card in scene_cards)
    sequence_count = len((sequence_structure.get("sequences") or []))
    minimum_scene_count_required = 36 if parsed.get("format_family") == "feature_film" else 8 if parsed.get("format_family") == "web_series" else 3
    feature_thinness_flags = []
    if parsed.get("format_family") == "feature_film":
        if macro_scene_count < 12:
            feature_thinness_flags.append("feature mode requires at least 12 macro scenes")
        if sub_scene_count < 36:
            feature_thinness_flags.append("feature mode requires at least 36 sub-scenes")
        if sequence_count < 6:
            feature_thinness_flags.append("feature mode requires at least 6 sequences")
    runtime_density_score = round((sub_scene_count or macro_scene_count) / max(1, duration / 3), 2)
    sequence_density_score = round(sequence_count / max(1, duration / 20), 2)
    middle_act_density_risk = parsed.get("format_family") == "feature_film" and sequence_count < 8
    if middle_act_density_risk:
        feature_thinness_flags.append("middle act density risk")
    return {
        "runtime_density_score": runtime_density_score,
        "minimum_scene_count_required": minimum_scene_count_required,
        "actual_scene_count": macro_scene_count,
        "actual_sub_scene_count": sub_scene_count,
        "sequence_density_score": sequence_density_score,
        "middle_act_density_risk": middle_act_density_risk,
        "feature_thinness_flags": feature_thinness_flags,
    }

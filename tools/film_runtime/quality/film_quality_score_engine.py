"""F13 calibrated film-quality scoring with human-readable penalties."""

from __future__ import annotations

from collections import Counter
from typing import Any


GENERIC_PHRASES = {
    "a person learns to do better",
    "someone has a hard day",
    "they want to be better",
    "everything is probably fine now",
    "we will be better tomorrow",
}

TEMPLATE_PHRASES = {
    "moves through the scene with subtext",
    "moves through",
    "the scene keeps",
    "present without becoming explanatory prose",
    "chooses pause",
    "the room keeps that choice",
}

GENERIC_EMOTION_TERMS = {
    "hard",
    "better",
    "upset",
    "calm",
    "angry",
    "sad",
    "good",
    "bad",
}

GENRE_SIGNATURES = {
    "motivational_drama": {"repair", "toddlers", "kitchen", "trust", "quiet", "home", "worksheet"},
    "thriller": {"threat", "gas", "hiss", "stairwell", "danger", "valve", "panic"},
    "romance": {"distance", "touch", "anniversary", "rain", "vulnerability", "pride", "tenderness"},
}

SCORE_DIMENSIONS = [
    "premise_strength",
    "logline_strength",
    "theme_dramatization",
    "character_arc_depth",
    "opposing_force_pressure",
    "relationship_function",
    "stakes_escalation",
    "scene_conflict_density",
    "midpoint_strength",
    "ending_payoff",
    "dialogue_subtext",
    "visual_motivation",
    "cinematography_intent",
    "genre_integrity",
    "continuity_integrity",
    "revision_readiness",
    "cinematic_embodiment",
    "dialogue_subtext_depth",
    "scene_vividness",
    "genre_specific_voice",
    "template_reuse_penalty",
    "visual_embodiment",
    "emotional_specificity",
]


def _text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip().lower()
    return str(value).strip().lower()


def _contains_any(text: str, terms: set[str] | list[str]) -> bool:
    return any(term in text for term in terms)


def _clamp(score: float) -> int:
    return max(0, min(10, int(round(score))))


def _band(score: float) -> str:
    if score <= 3:
        return "FAIL_WEAK_FILM"
    if score <= 5:
        return "NEEDS_MAJOR_REWRITE"
    if score <= 7:
        return "WORKABLE_DRAFT"
    if score <= 9:
        return "STRONG_DRAFT"
    return "EXCELLENT"


def _sentence_starts(screenplay: str) -> Counter[str]:
    starts: list[str] = []
    for raw_line in screenplay.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("int.") or line.startswith("ext.") or line.startswith("title:") or line.startswith("theme:"):
            continue
        words = line.split()
        if len(words) >= 3:
            starts.append(" ".join(words[:3]))
    return Counter(starts)


def analyze_template_reuse(packet: dict[str, Any]) -> dict[str, Any]:
    screenplay = _text(packet.get("screenplay"))
    scene_cards = packet.get("scene_cards", [])
    scene_objectives = [_text(card.get("scene_objective")) for card in scene_cards]
    conflicts = [_text(card.get("conflict")) for card in scene_cards if _text(card.get("conflict"))]
    starts = _sentence_starts(screenplay)
    repeated_starts = {start: count for start, count in starts.items() if count >= 3}
    phrase_hits = {phrase: screenplay.count(phrase) for phrase in TEMPLATE_PHRASES if screenplay.count(phrase) >= 2}
    closing_line = screenplay.splitlines()[-1].strip().lower() if screenplay.splitlines() else ""
    return {
        "scene_count": len(scene_cards),
        "repeated_sentence_starts": repeated_starts,
        "template_phrase_hits": phrase_hits,
        "same_conflict_repeated": len(set(conflicts)) <= 2 if conflicts else True,
        "same_objective_shape": len(set(scene_objectives)) <= 2 if scene_objectives else True,
        "closing_cadence_generic": any(term in closing_line for term in ["chooses pause", "quieter than before", "keeps that choice"]),
    }


def estimate_human_readable_quality(packet: dict[str, Any], score_dimensions: dict[str, int]) -> float:
    screenplay = _text(packet.get("screenplay"))
    template = analyze_template_reuse(packet)
    scene_cards = packet.get("scene_cards", [])
    expressive_keys = [
        "dialogue_subtext",
        "cinematic_embodiment",
        "dialogue_subtext_depth",
        "scene_vividness",
        "genre_specific_voice",
        "visual_embodiment",
        "emotional_specificity",
    ]
    expressive_average = sum(score_dimensions[key] for key in expressive_keys) / len(expressive_keys)
    structural_average = sum(
        score_dimensions[key]
        for key in ["premise_strength", "logline_strength", "character_arc_depth", "scene_conflict_density", "ending_payoff"]
    ) / 5
    base = (0.65 * expressive_average) + (0.35 * structural_average)
    penalty = 0.0
    penalty += 0.6 * len(template["template_phrase_hits"])
    penalty += 0.45 * len(template["repeated_sentence_starts"])
    if template["same_conflict_repeated"]:
        penalty += 0.5
    if template["same_objective_shape"]:
        penalty += 0.5
    if template["closing_cadence_generic"]:
        penalty += 0.4
    if "scene objective:" in screenplay:
        penalty += 0.2
    if screenplay.count("TITLE:") >= 1 and screenplay.count("THEME:") >= 1:
        penalty += 0.4
    if score_dimensions["logline_strength"] < 5:
        penalty += 0.8
    if score_dimensions["cinematic_embodiment"] < 7:
        penalty += 0.5
    if score_dimensions["genre_specific_voice"] < 7:
        penalty += 0.6
    if score_dimensions["visual_embodiment"] < 7:
        penalty += 0.5
    if score_dimensions["emotional_specificity"] < 7:
        penalty += 0.7
    if all(len(card.get("dialogue_lines", [])) <= 2 for card in scene_cards):
        penalty += 0.4
    return round(max(0.0, base - penalty), 1)


def score_packet(packet: dict[str, Any]) -> dict[str, Any]:
    premise = packet.get("premise_test", {})
    genre = _text(packet.get("genre") or premise.get("genre") or packet.get("quality_benchmark_source_payload", {}).get("genre"))
    theme = _text(packet.get("theme") or premise.get("theme"))
    logline = _text(packet.get("logline"))
    beats = packet.get("beat_sheet", [])
    scene_cards = packet.get("scene_cards", [])
    arc = packet.get("character_arc", {})
    relationship = (packet.get("relationship_map", {}).get("relationships") or [{}])[0]
    visual = packet.get("visual_language", {})
    cinematography = packet.get("cinematography_plan", {})
    genre_report = packet.get("genre_grammar_report", {})
    continuity = packet.get("continuity_bible", {})
    cinema_depth = packet.get("cinema_depth_packet", {})
    screenplay = _text(packet.get("screenplay"))
    source_payload = packet.get("quality_benchmark_source_payload") or {}
    template = analyze_template_reuse(packet)
    emotional_depth = cinema_depth.get("emotional_depth", {})
    character_depth = cinema_depth.get("character_depth", {})
    scene_logic_depth = cinema_depth.get("scene_logic_depth", {})
    dialogue_depth = cinema_depth.get("dialogue_depth", {})
    genre_depth = cinema_depth.get("genre_depth", {})
    continuity_depth = cinema_depth.get("continuity_depth", {})
    feature_density = cinema_depth.get("feature_density", {})

    scores: dict[str, int] = {}

    premise_text = _text(premise.get("premise"))
    premise_score = 9
    if premise_text in GENERIC_PHRASES or premise_text.startswith("a person ") or premise_text.startswith("someone "):
        premise_score -= 5
    if not _contains_any(premise_text, ["must", "protect", "choose", "face", "keep", "save", "return"]):
        premise_score -= 2
    if not _text(premise.get("stakes")):
        premise_score -= 3
    if not _text(premise.get("central_conflict")) or _text(premise.get("central_conflict")) in {"a problem", "issues", "tension"}:
        premise_score -= 2
    if theme and theme.split()[0] not in premise_text:
        premise_score -= 1
    scores["premise_strength"] = _clamp(premise_score)

    logline_score = 9
    if len(logline.split()) < 10 or logline in GENERIC_PHRASES or "someone" in logline:
        logline_score -= 4
    if not _contains_any(logline, ["must", "before", "against", "protect", "save", "repair", "move"]):
        logline_score -= 2
    if not _contains_any(logline, ["trust", "love", "safety", "danger", "family", "threat", "distance"]):
        logline_score -= 2
    if logline.endswith(".") and len(set(logline.split())) < 8:
        logline_score -= 1
    scores["logline_strength"] = _clamp(logline_score)

    theme_score = 9
    beat_text = " ".join(_text(beat.get("story_function")) for beat in beats)
    if theme and theme.split()[0] not in screenplay and theme.split()[0] not in beat_text:
        theme_score -= 4
    if "without dramatizing the theme" in beat_text:
        theme_score -= 4
    if not _contains_any(screenplay, ["repair", "choice", "trust", "truth", "love", "safety", "danger", "distance"]):
        theme_score -= 2
    scores["theme_dramatization"] = _clamp(theme_score)

    arc_score = 9
    if _text(arc.get("want")) == _text(arc.get("need")):
        arc_score -= 4
    if _text(arc.get("transformation_start")) == _text(arc.get("transformation_end")):
        arc_score -= 3
    if not _text(arc.get("moral_dilemma")) or not _contains_any(_text(arc.get("moral_dilemma")), ["or", "versus", "protect", "betray", "trust", "fear", "distance"]):
        arc_score -= 2
    if not arc.get("emotional_continuity_by_scene"):
        arc_score -= 2
    scores["character_arc_depth"] = _clamp(arc_score)

    force_score = 9
    force_text = _text(packet.get("opposing_force", {}).get("opposing_force") or arc.get("opposing_force"))
    if force_text in {"a problem", "issue", "tension", ""}:
        force_score -= 5
    if not any(_contains_any(_text(card.get("conflict")), ["anger", "threat", "distance", "fear", "danger", "clock", "pressure", "shame"]) for card in scene_cards):
        force_score -= 3
    scores["opposing_force_pressure"] = _clamp(force_score)

    relation_score = 9
    if _contains_any(_text(relationship.get("mirror_function")), ["decorative", "pleasant company", "fill the scene"]):
        relation_score -= 5
    if not _text(relationship.get("conflict_source")) or _contains_any(_text(relationship.get("conflict_source")), ["little difficult", "same page", "minor issue"]):
        relation_score -= 2
    if not any(_contains_any(_text(card.get("dialogue_subtext_goal")), ["mirror", "subtext", "care", "fear", "repair", "wound"]) for card in scene_cards):
        relation_score -= 2
    scores["relationship_function"] = _clamp(relation_score)

    stakes_score = 9
    stake_lines = [_text(beat.get("stakes_change")) for beat in beats]
    if len(set(stake_lines)) < 3:
        stakes_score -= 5
    if not any(_contains_any(line, ["child", "toddler", "trust", "safety", "danger", "love", "distance"]) for line in stake_lines):
        stakes_score -= 2
    if emotional_depth.get("flatline_risk_flags"):
        stakes_score -= 2
    scores["stakes_escalation"] = _clamp(stakes_score)

    conflict_score = 9
    conflicts = [_text(card.get("conflict")) for card in scene_cards]
    if not conflicts or len([c for c in conflicts if c]) < max(1, len(scene_cards) - 1):
        conflict_score -= 4
    if all(c == conflicts[0] for c in conflicts if c):
        conflict_score -= 3
    if any(_contains_any(c, ["little difficult", "very little resists", "no real resistance"]) for c in conflicts):
        conflict_score -= 2
    if scene_logic_depth.get("duplicate_conflict_flags"):
        conflict_score -= 2
    if scene_logic_depth.get("summary_scene_flags"):
        conflict_score -= 2
    scores["scene_conflict_density"] = _clamp(conflict_score)

    midpoint_score = 9
    midpoint = _text(packet.get("act_structure", {}).get("midpoint_shift_or_reversal"))
    if not midpoint or _contains_any(midpoint, ["continues without", "nothing meaningfully changes", "keeps going"]):
        midpoint_score -= 6
    if midpoint and not _contains_any(midpoint, ["realizes", "admits", "discovers", "sees", "recognizes"]):
        midpoint_score -= 1
    if emotional_depth.get("act_emotional_progression", {}).get("act_two", {}).get("flatline"):
        midpoint_score -= 2
    scores["midpoint_strength"] = _clamp(midpoint_score)

    ending_score = 9
    final_card = scene_cards[-1] if scene_cards else {}
    if _contains_any(_text(final_card.get("scene_objective")), ["say everything will be okay", "call it resolved"]):
        ending_score -= 4
    if not _contains_any(screenplay, ["repair", "relieved", "softly", "safe", "tenderness", "truth", "quiet", "listen"]):
        ending_score -= 2
    if _contains_any(_text(packet.get("character_arc", {}).get("transformation_end")), ["slightly calmer", "mostly waiting"]):
        ending_score -= 3
    if template["closing_cadence_generic"]:
        ending_score -= 2
    scores["ending_payoff"] = _clamp(ending_score)

    dialogue_score = 9
    dialogue_text = " ".join(_text(line.get("line")) for card in scene_cards for line in card.get("dialogue_lines", []))
    if _contains_any(dialogue_text, ["we will be better tomorrow", "i feel bad and you feel bad", "i am upset because i am upset"]):
        dialogue_score -= 4
    if all(_contains_any(_text(card.get("dialogue_subtext_goal")), ["say the exact feeling", "say the feeling directly"]) for card in scene_cards if scene_cards):
        dialogue_score -= 4
    if dialogue_depth.get("same_voice_risk_flags"):
        dialogue_score -= 2
    if dialogue_depth.get("generic_dialogue_flags"):
        dialogue_score -= 2
    scores["dialogue_subtext"] = _clamp(dialogue_score)

    visual_score = 9
    mapping = visual.get("scene_visual_mapping") or []
    if not mapping or any(not _text(item.get("visual_strategy")) or "plain coverage" in _text(item.get("visual_strategy")) for item in mapping):
        visual_score -= 4
    if not _text(visual.get("visual_metaphor")):
        visual_score -= 3
    if feature_density.get("feature_thinness_flags") and packet.get("format_family") == "feature_film":
        visual_score -= 1
    scores["visual_motivation"] = _clamp(visual_score)

    camera_score = 9
    if not _text(cinematography.get("lens_intent")) or "basic coverage" in _text(cinematography.get("lens_intent")):
        camera_score -= 4
    progression = cinematography.get("shot_progression") or []
    if not progression or any(_text(item.get("camera_reason")) in {"coverage", "none", ""} for item in progression):
        camera_score -= 3
    scores["cinematography_intent"] = _clamp(camera_score)

    genre_score = 9
    if genre_report and not genre_report.get("passed"):
        genre_score -= 4
    current_map = genre_report.get("current_genre_rule_map") or {}
    if genre_report and (not current_map or not current_map.get("required_scene_functions")):
        genre_score -= 3
    if genre and not _contains_any(screenplay, GENRE_SIGNATURES.get(genre, set())):
        genre_score -= 3
    if genre_depth.get("genre_failure_flags"):
        genre_score -= 3
    scores["genre_integrity"] = _clamp(genre_score)

    continuity_score = 9
    if not continuity.get("timeline") or not continuity.get("location_continuity"):
        continuity_score -= 3
    if not continuity.get("toddler_stakes_continuity"):
        continuity_score -= 2
    if not continuity.get("character_emotional_state_by_scene"):
        continuity_score -= 2
    if continuity_depth.get("unresolved_thread_flags"):
        continuity_score -= 2
    scores["continuity_integrity"] = _clamp(continuity_score)

    readiness_score = 9
    if not source_payload:
        readiness_score -= 3
    if len([score for score in scores.values() if score < 5]) > 4:
        readiness_score -= 2
    if not scene_cards or not beats:
        readiness_score -= 3
    scores["revision_readiness"] = _clamp(readiness_score)

    cinematic_score = 8
    if len(template["template_phrase_hits"]) >= 2:
        cinematic_score -= 4
    if "scene objective:" in screenplay:
        cinematic_score -= 2
    if not any(card.get("action_lines") for card in scene_cards):
        cinematic_score -= 2
    if emotional_depth.get("flatline_risk_flags"):
        cinematic_score -= 2
    if feature_density.get("feature_thinness_flags"):
        cinematic_score -= 2
    scores["cinematic_embodiment"] = _clamp(cinematic_score)

    dialogue_depth_score = 8
    explanatory_phrases = [
        "i feel",
        "i am trying",
        "this is the version",
        "i know what this is now",
        "i can come back",
        "i see the threat clearly now",
    ]
    if sum(screenplay.count(phrase) for phrase in explanatory_phrases) >= 2:
        dialogue_depth_score -= 4
    if not any(len(card.get("dialogue_lines", [])) >= 2 for card in scene_cards):
        dialogue_depth_score -= 2
    if all("really" not in _text(card.get("dialogue_subtext_goal")) and "asking" not in _text(card.get("dialogue_subtext_goal")) for card in scene_cards):
        dialogue_depth_score -= 1
    if dialogue_depth.get("same_voice_risk_flags"):
        dialogue_depth_score -= 2
    if len(dialogue_depth.get("subtext_map") or []) < 2:
        dialogue_depth_score -= 2
    scores["dialogue_subtext_depth"] = _clamp(dialogue_depth_score)

    vividness_score = 8
    visual_motifs = [_text(card.get("visual_motif")) for card in scene_cards]
    if len(set(v for v in visual_motifs if v)) < max(2, len(scene_cards) // 2):
        vividness_score -= 3
    if not any(_contains_any(" ".join(card.get("action_lines", [])).lower(), ["wrist", "breath", "glass", "floor", "coat", "towel", "window", "valve"]) for card in scene_cards):
        vividness_score -= 2
    if packet.get("format_family") == "feature_film" and feature_density.get("actual_sub_scene_count", 0) < 36:
        vividness_score -= 2
    scores["scene_vividness"] = _clamp(vividness_score)

    genre_voice_score = 8
    signature_hits = sum(1 for term in GENRE_SIGNATURES.get(genre, set()) if term in screenplay)
    if signature_hits < 3:
        genre_voice_score -= 4
    if genre == "thriller" and not _contains_any(screenplay, ["hiss", "valve", "stairwell", "threat", "panic"]):
        genre_voice_score -= 2
    if genre == "romance" and not _contains_any(screenplay, ["distance", "touch", "anniversary", "pride", "tender"]):
        genre_voice_score -= 2
    if genre == "motivational_drama" and not _contains_any(screenplay, ["toddlers", "repair", "kitchen", "worksheet", "home"]):
        genre_voice_score -= 2
    if genre_depth.get("genre_failure_flags"):
        genre_voice_score -= 2
    scores["genre_specific_voice"] = _clamp(genre_voice_score)

    template_penalty_score = 10
    template_penalty_score -= min(5, len(template["template_phrase_hits"]) * 2)
    template_penalty_score -= min(3, len(template["repeated_sentence_starts"]))
    if template["same_conflict_repeated"]:
        template_penalty_score -= 1
    if template["same_objective_shape"]:
        template_penalty_score -= 1
    if scene_logic_depth.get("duplicate_conflict_flags"):
        template_penalty_score -= 1
    scores["template_reuse_penalty"] = _clamp(template_penalty_score)

    visual_embodiment_score = 8
    scene_map_text = " ".join(_text(item.get("visual_strategy")) for item in mapping)
    if _contains_any(scene_map_text, ["plain coverage", "ordinary coverage", "basic romantic coverage"]):
        visual_embodiment_score -= 4
    if not any(_contains_any(_text(item.get("visual_strategy")), ["frame", "shadow", "reflect", "angle", "low", "close", "light"]) for item in mapping):
        visual_embodiment_score -= 2
    scores["visual_embodiment"] = _clamp(visual_embodiment_score)

    emotional_specificity_score = 8
    if sum(screenplay.count(term) for term in GENERIC_EMOTION_TERMS) > max(6, len(scene_cards) * 2):
        emotional_specificity_score -= 3
    if not any(_contains_any(" ".join(card.get("action_lines", [])).lower(), ["jaw", "wrist", "breath", "shoulder", "touch", "knuckles", "thumb"]) for card in scene_cards):
        emotional_specificity_score -= 2
    if not _contains_any(screenplay, ["ashamed", "cornered", "tentative", "disciplined", "exposed", "relieved", "bare"]):
        emotional_specificity_score -= 2
    if emotional_depth.get("flatline_risk_flags"):
        emotional_specificity_score -= 2
    scores["emotional_specificity"] = _clamp(emotional_specificity_score)

    structural_keys = [
        "premise_strength",
        "theme_dramatization",
        "character_arc_depth",
        "opposing_force_pressure",
        "relationship_function",
        "stakes_escalation",
        "scene_conflict_density",
        "midpoint_strength",
        "ending_payoff",
        "genre_integrity",
        "continuity_integrity",
    ]
    expressive_keys = [
        "dialogue_subtext",
        "visual_motivation",
        "cinematography_intent",
        "cinematic_embodiment",
        "dialogue_subtext_depth",
        "scene_vividness",
        "genre_specific_voice",
        "template_reuse_penalty",
        "visual_embodiment",
        "emotional_specificity",
    ]
    structural_average = sum(scores[key] for key in structural_keys) / len(structural_keys)
    expressive_average = sum(scores[key] for key in expressive_keys) / len(expressive_keys)
    low_dimension_count = len([score for score in scores.values() if score < 6])
    calibration_penalty = 0.18 * low_dimension_count
    calibration_penalty += 0.35 * len(template["template_phrase_hits"])
    calibration_penalty += 0.25 * len(template["repeated_sentence_starts"])
    if template["same_conflict_repeated"]:
        calibration_penalty += 0.3
    if template["same_objective_shape"]:
        calibration_penalty += 0.3
    if template["closing_cadence_generic"]:
        calibration_penalty += 0.25
    calibration_penalty += 0.4 * len(emotional_depth.get("flatline_risk_flags") or [])
    calibration_penalty += 0.35 * len(scene_logic_depth.get("duplicate_conflict_flags") or [])
    calibration_penalty += 0.25 * len(dialogue_depth.get("same_voice_risk_flags") or [])
    calibration_penalty += 0.2 * len(continuity_depth.get("unresolved_thread_flags") or [])
    if feature_density.get("feature_thinness_flags"):
        calibration_penalty += 0.8
    raw_overall = round(max(0.0, (0.4 * structural_average) + (0.6 * expressive_average) - calibration_penalty), 1)

    defect_list = [key for key, value in scores.items() if value < 6]
    highest_risk_area = min(scores, key=scores.get)
    estimated_human_score = estimate_human_readable_quality(packet, scores)
    overall_cap = 8.8
    if emotional_depth.get("flatline_risk_flags"):
        overall_cap = min(overall_cap, 5.5)
    if character_depth and not character_depth.get("arc_completion_status"):
        overall_cap = min(overall_cap, 5.5)
    if dialogue_depth.get("same_voice_risk_flags"):
        overall_cap = min(overall_cap, 5.8)
    if feature_density.get("feature_thinness_flags"):
        overall_cap = min(overall_cap, 5.2)
    if genre_depth.get("genre_failure_flags"):
        overall_cap = min(overall_cap, 5.8)
    if continuity_depth.get("unresolved_thread_flags"):
        overall_cap = min(overall_cap, 5.9)
    overall_score = round(min(raw_overall, estimated_human_score + 0.7, overall_cap), 1)
    recommended_actions = [
        {"area": defect, "action": defect.replace("_", " ") + " needs targeted revision"}
        for defect in defect_list
    ]
    return {
        "score_dimensions": scores,
        "overall_score": overall_score,
        "quality_band": _band(overall_score),
        "defect_list": defect_list,
        "highest_risk_area": highest_risk_area,
        "recommended_revision_actions": recommended_actions,
        "estimated_human_score": estimated_human_score,
        "human_calibration_gap": round(overall_score - estimated_human_score, 1),
        "template_signals": template,
    }


def render_quality_score_markdown(label: str, report: dict[str, Any]) -> str:
    lines = [f"# {label}", ""]
    for key, value in report["score_dimensions"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            f"- overall_score: {report['overall_score']}",
            f"- quality_band: {report['quality_band']}",
            f"- estimated_human_score: {report.get('estimated_human_score')}",
            f"- human_calibration_gap: {report.get('human_calibration_gap')}",
            f"- highest_risk_area: {report['highest_risk_area']}",
            "- defect_list:",
        ]
    )
    for defect in report["defect_list"]:
        lines.append(f"  - {defect}")
    return "\n".join(lines) + "\n"

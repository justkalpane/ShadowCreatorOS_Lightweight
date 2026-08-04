"""Cinema-depth dialogue voice and subtext analysis."""

from __future__ import annotations

from collections import Counter
from typing import Any


GENERIC_MENTOR_LINES = {
    "we can do better",
    "everything will be okay",
    "you just need to be calm",
    "let's be honest now",
}


def _fingerprint(lines: list[str]) -> dict[str, Any]:
    joined = " ".join(lines).strip()
    words = joined.split()
    return {
        "line_count": len(lines),
        "avg_words_per_line": round(len(words) / max(1, len(lines)), 2),
        "question_count": joined.count("?"),
        "hesitation_count": sum(joined.count(marker) for marker in ["...", "—", "--"]),
        "address_count": sum(1 for word in words if word.istitle()),
        "keyword_stems": Counter(word.lower().strip(".,!?;:'\"") for word in words).most_common(5),
    }


def build_dialogue_voice_map(scene_cards: list[dict[str, Any]]) -> dict[str, Any]:
    voices: dict[str, list[str]] = {}
    dialogue_pressure_points = []
    generic_dialogue_flags = []
    exposition_dump_flags = []
    subtext_map = []
    for card in scene_cards:
        scene_number = card.get("scene_number")
        for line in card.get("dialogue_lines", []):
            speaker = line.get("speaker")
            text = str(line.get("line", "")).strip()
            voices.setdefault(speaker, []).append(text)
            if any(phrase in text.lower() for phrase in GENERIC_MENTOR_LINES):
                generic_dialogue_flags.append(f"scene {scene_number} generic dialogue from {speaker}")
            if len(text.split()) > 20:
                exposition_dump_flags.append(f"scene {scene_number} exposition risk from {speaker}")
            lowered = text.lower()
            subtext_markers = [
                "not",
                "fine",
                "okay",
                "sure",
                "isn't",
                "don't",
                "didn't",
                "before i",
                "if i",
                "not yet",
                "stay",
                "hear me",
                "look at you",
                "being right",
            ]
            if (
                any(marker in lowered for marker in subtext_markers)
                or text.endswith("?")
                or "..." in text
                or len(text.split()) <= 14 and any(word in lowered for word in ["room", "quiet", "stay", "right", "safe"])
            ):
                subtext_map.append({"scene_number": scene_number, "speaker": speaker, "line": text, "subtext_strength": "high"})
        dialogue_pressure_points.append(
            {
                "scene_number": scene_number,
                "pressure": card.get("conflict"),
                "subtext_goal": card.get("dialogue_subtext_goal"),
            }
        )

    fingerprints = {speaker: _fingerprint(lines) for speaker, lines in voices.items()}
    same_voice_risk_flags = []
    speakers = list(fingerprints)
    for idx, left in enumerate(speakers):
        for right in speakers[idx + 1:]:
            lf = fingerprints[left]
            rf = fingerprints[right]
            if (
                abs(lf["avg_words_per_line"] - rf["avg_words_per_line"]) < 1.5
                and abs(lf["question_count"] - rf["question_count"]) <= 1
                and {stem for stem, _ in lf["keyword_stems"]} == {stem for stem, _ in rf["keyword_stems"]}
            ):
                same_voice_risk_flags.append(f"{left} and {right} sound interchangeable")

    return {
        "dialogue_voice_map": dialogue_pressure_points,
        "character_voice_fingerprints": fingerprints,
        "subtext_map": subtext_map,
        "dialogue_pressure_points": dialogue_pressure_points,
        "same_voice_risk_flags": same_voice_risk_flags,
        "generic_dialogue_flags": generic_dialogue_flags,
        "exposition_dump_flags": exposition_dump_flags,
    }

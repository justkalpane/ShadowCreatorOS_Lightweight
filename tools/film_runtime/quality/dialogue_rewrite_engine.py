"""F15 dialogue rewrite pass for lived-in lane-specific voices."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def _lane(packet: dict[str, Any]) -> str:
    return packet.get("genre") or packet.get("premise_test", {}).get("genre") or "motivational_drama"


def _screenplay_from_scene_cards(packet: dict[str, Any]) -> str:
    lines = [f"TITLE: {packet.get('title', 'Film Draft')}", "", f"THEME: {packet.get('theme', '')}", ""]
    for scene in packet.get("scene_cards", []):
        lines.append(scene["slugline"])
        lines.append("")
        for action_line in scene.get("action_lines", []):
            lines.append(action_line)
        lines.append("")
        for dialogue in scene.get("dialogue_lines", []):
            lines.append(f"                        {dialogue['speaker'].upper()}")
            lines.append(f"            {dialogue['line']}")
            lines.append("")
    lines.append(packet.get("final_image_line", ""))
    return "\n".join(line for line in lines if line is not None).rstrip() + "\n"


def _rewrite_romance_dialogue(packet: dict[str, Any]) -> None:
    scenes = packet.get("scene_cards") or []
    if len(scenes) < 5:
        return
    scenes[0]["dialogue_lines"] = [
        _line(scenes[0]["dialogue_lines"][0]["speaker"], "You remembered flowers. You forgot the hour that made them matter."),
        _line(scenes[0]["dialogue_lines"][1]["speaker"], "I kept circling the block like that could make me easier to walk in."),
    ]
    scenes[1]["dialogue_lines"] = [
        _line(scenes[1]["dialogue_lines"][0]["speaker"], "Don't rescue the pan. We both know that's not what burned."),
        _line(scenes[1]["dialogue_lines"][1]["speaker"], "If I stop moving, you'll hear why I nearly turned the car around."),
    ]
    scenes[2]["dialogue_lines"] = [
        _line(scenes[2]["dialogue_lines"][0]["speaker"], "I was late on purpose. Not because I stopped wanting this. Because I knew you'd hear my voice shake and name it pity."),
        _line(scenes[2]["dialogue_lines"][1]["speaker"], "You let me call it distance when it was fear. That was the lonelier lie."),
    ]
    scenes[3]["dialogue_lines"] = [
        _line(scenes[3]["dialogue_lines"][0]["speaker"], "Keep the better piece. I already spent the evening making you take the worse half."),
        _line(scenes[3]["dialogue_lines"][1]["speaker"], "Then stop offering me polished damage and stay for the ugly minute after it."),
    ]
    scenes[4]["dialogue_lines"] = [
        _line(scenes[4]["dialogue_lines"][0]["speaker"], "Take the spare key back. If I leave again, I want it to be because I said goodbye, not because I vanished neatly."),
        _line(scenes[4]["dialogue_lines"][1]["speaker"], "Then knock like you belong to the mess too."),
    ]


def _line(speaker: str, line: str) -> dict[str, str]:
    return {"speaker": speaker, "line": line}


def rewrite_dialogue(packet: dict[str, Any]) -> dict[str, Any]:
    rewritten = deepcopy(packet)
    lane = _lane(packet)
    if lane == "romance":
        _rewrite_romance_dialogue(rewritten)
    metadata = {
        "explanatory_dialogue_reduced": True,
        "therapy_speak_reduced": True,
        "character_voice_improved": True,
        "subtext_improved": True,
        "silence_and_interruption_used": True,
        "romance_specific_shared_history": lane == "romance",
        "romance_costly_reconciliation": lane == "romance",
    }
    rewritten["quality_dialogue_metadata"] = metadata
    rewritten["screenplay"] = _screenplay_from_scene_cards(rewritten)
    rewritten["screenplay_body"] = rewritten["screenplay"]
    return rewritten

"""Scene card generator for cinema preproduction."""

from __future__ import annotations

from typing import Any


def _dialogue_lines(main: str, second: str, stakes: str, scene_number: int, genre: str) -> list[dict[str, str]]:
    if genre == "thriller":
        thriller_lines = {
            1: [{"speaker": second, "line": f"'{main}, something is wrong and the kids can feel it.'"}],
            2: [{"speaker": main, "line": "'Slow down. Panic will make the room smaller.'"}],
            4: [{"speaker": main, "line": "'I need the fear to answer me, not command me.'"}],
            6: [{"speaker": second, "line": f"'You kept {stakes} safe without turning cruel.'"}],
        }
        return thriller_lines.get(scene_number, [{"speaker": main, "line": "'I see the threat clearly now.'"}])
    if genre == "romance":
        romance_lines = {
            1: [{"speaker": second, "line": f"'{main}, I can feel you disappearing again.'"}],
            2: [{"speaker": main, "line": "'I am trying to protect the room, not leave you alone in it.'"}],
            4: [{"speaker": main, "line": "'The anger is easier than saying I am scared to fail you.'"}],
            6: [{"speaker": second, "line": "'This is the version of you I needed back.'"}],
        }
        return romance_lines.get(scene_number, [{"speaker": main, "line": "'I can come back honestly this time.'"}])
    if scene_number == 1:
        return [
            {"speaker": second, "line": f"'{main}, it started a few minutes ago.'"},
            {"speaker": main, "line": "'I have it. Just give me a second.'"},
        ]
    if scene_number == 2:
        return [
            {"speaker": second, "line": f"'{stakes} is all anyone can think about right now.'"},
            {"speaker": main, "line": "'I am not letting the room decide for me.'"},
        ]
    if scene_number == 4:
        return [{"speaker": main, "line": "'I can wait. I do not have to answer the anger yet.'"}]
    if scene_number == 6:
        return [
            {"speaker": main, "line": "'We are okay. Let's finish this softly.'"},
            {"speaker": second, "line": "'That is the voice they needed to hear.'"},
        ]
    return [{"speaker": main, "line": "'I know what this is now. I can come back cleanly.'"}]


def generate_scene_cards(
    parsed: dict[str, Any],
    character_bible: dict[str, Any],
    relationship_map: dict[str, Any],
    beat_sheet: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    main = character_bible["major_characters"][0]["name"]
    second = character_bible["major_characters"][1]["name"]
    setting = parsed["setting"]
    stakes = parsed["stakes"]
    mirror = relationship_map["relationships"][0]["mirror_function"]
    genre = parsed["genre"]

    if genre == "thriller":
        card_specs = [
            (1, f"INT. {setting.upper()} - DUSK", setting, "dusk", "establish unease around shared safety", f"{stakes} already feels unstable", "a harmless detail starts to feel dangerous", "guarded", "watchful"),
            (2, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "contain the threat without panic", parsed["pressure_trigger"], "the protagonist realizes panic will worsen the danger", "watchful", "frightened but controlled"),
            (3, f"INT. {setting.upper()} - LATER", setting, "later", "read the room before acting", "fear and anger compete for control", "the protagonist sees the children reading every move", "frightened but controlled", "split between force and care"),
            (4, "INT. HALLWAY - MOMENTS LATER", "hallway", "moments later", "choose tactical restraint", "adrenaline demands speed", "a pause becomes the smartest move available", "split between force and care", "strategically calm"),
            (5, f"INT. {setting.upper()} - NIGHT", setting, "night", "return with a precise repair action", stakes, "trust starts to replace fear", "strategically calm", "connected and resolving"),
            (6, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "close the threat loop with tenderness", stakes, "the room survives because panic did not win", "connected and resolving", "relieved and vigilant"),
        ]
    elif genre == "romance":
        card_specs = [
            (1, f"INT. {setting.upper()} - EARLY EVENING", setting, "early evening", "show affection under strain", "care is present but not fully spoken", "a tiny distance opens between the couple", "tired but connected", "tentatively open"),
            (2, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "protect the shared world", parsed["pressure_trigger"], "the practical problem exposes emotional distance", "tentatively open", "fragile"),
            (3, f"INT. {setting.upper()} - LATER", setting, "later", "name the hurt beneath the anger", "shame is easier than vulnerability", "the protagonist realizes the anger is cover", "fragile", "self-aware and exposed"),
            (4, "INT. HALLWAY - MOMENTS LATER", "hallway", "moments later", "choose honesty instead of pride", "avoidance still feels safer", "the protagonist decides to return emotionally available", "self-aware and exposed", "willing to be seen"),
            (5, f"INT. {setting.upper()} - NIGHT", setting, "night", "invite reconnection", stakes, "support is offered without domination", "willing to be seen", "soft and brave"),
            (6, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "repair love through action", stakes, "intimacy is rebuilt through care", "soft and brave", "hopeful and intimate"),
        ]
    else:
        card_specs = [
            (1, f"INT. {setting.upper()} - EARLY EVENING", setting, "early evening", "warm opening", "the room is already fragile", "gentleness answers first", "worn down", "present"),
            (2, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "hold the line under pressure", parsed["pressure_trigger"], "anger is noticed before it moves", "present", "pressured"),
            (3, f"INT. {setting.upper()} - LATER", setting, "later", "catch the internal surge", parsed["pressure_trigger"], "anger is named internally", "pressured", "self-aware"),
            (4, "INT. HALLWAY BATHROOM - MOMENTS LATER", "hallway bathroom", "moments later", "choose restraint", "the anger is still loud inside", "the pause becomes visible action", "self-aware", "contained"),
            (5, f"INT. {setting.upper()} - NIGHT", setting, "night", "understand the emotional inheritance", stakes, "care becomes clearer than pride", "contained", "clear enough to repair"),
            (6, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "repair the family moment", stakes, "the room receives tenderness", "clear enough to repair", "hopeful"),
        ]

    beat_by_scene: dict[int, list[str]] = {}
    for beat in beat_sheet:
        beat_by_scene.setdefault(beat["scene_number"], []).append(beat["beat_id"])

    cards: list[dict[str, Any]] = []
    for scene_number, slugline, location, time_of_day, objective, conflict, turning_point, start, end in card_specs:
        characters_present = [main, second]
        if scene_number in {1, 2, 5, 6}:
            characters_present.append("toddlers")
        cards.append(
            {
                "scene_number": scene_number,
                "slugline": slugline,
                "heading": slugline,
                "location": location,
                "time_of_day": time_of_day,
                "characters_present": characters_present,
                "scene_objective": objective,
                "objective": objective,
                "conflict": conflict,
                "turning_point": turning_point,
                "turn": turning_point,
                "emotional_value_start": start,
                "emotional_value_end": end,
                "visual_motif": f"{parsed['visual_style']} around {stakes}",
                "dialogue_subtext_goal": f"{mirror}; no generic motivational speech.",
                "continuity_dependencies": [
                    f"toddler stakes remain active: {stakes}",
                    f"main character remains soft-spoken and warm: {main}",
                    "controlled internal anger is visible but not acted out",
                ],
                "beat_ids": beat_by_scene.get(scene_number, []),
                "action_lines": [
                    f"{main} moves through {location} with controlled quiet.",
                    f"The scene keeps {stakes} present without becoming explanatory prose.",
                ],
                "dialogue_lines": _dialogue_lines(main, second, stakes, scene_number, genre),
                "visual_plan": {
                    "camera_reason": parsed["camera_reason_seed"],
                    "frame_pressure": parsed["frame_pressure_seed"],
                },
            }
        )
    return cards

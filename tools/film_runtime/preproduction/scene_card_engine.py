"""Scene card generator for cinema preproduction."""

from __future__ import annotations

from typing import Any


def _story_scale(parsed: dict[str, Any]) -> str:
    format_name = str(parsed.get("format", "")).lower()
    duration = int(parsed.get("duration_minutes", 5))
    if "feature" in format_name or duration >= 80:
        return "feature"
    if "series" in format_name or "episode" in format_name or duration >= 40:
        return "expanded"
    return "short"


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
    scale = _story_scale(parsed)

    if scale == "feature":
        if genre == "thriller":
            card_specs = [
                (1, f"INT. {setting.upper()} - LATE AFTERNOON", setting, "late afternoon", "seed unease inside the domestic world", f"{stakes} already feels unstable", "a minor detail suggests the night will turn dangerous", "guarded", "watchful"),
                (2, f"INT. {setting.upper()} - DUSK", setting, "dusk", "show the threat touching the relationship", "fear starts to govern speech and movement", "the couple realizes the danger is no longer hypothetical", "watchful", "coiled"),
                (3, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "contain the threat without panic", parsed["pressure_trigger"], "the protagonist understands panic will make the room more dangerous", "coiled", "frightened but controlled"),
                (4, "INT. ENTRYWAY - MOMENTS LATER", "entryway", "moments later", "keep the children shielded while options shrink", "every choice now carries physical and emotional risk", "the protagonist sees fear turning toward anger", "frightened but controlled", "split between force and care"),
                (5, "INT. HALLWAY - NIGHT", "hallway", "night", "stop escalation before it becomes cruelty", "adrenaline demands force", "restraint becomes the only way to preserve trust", "split between force and care", "tactically contained"),
                (6, "INT. KITCHEN - NIGHT", "kitchen", "night", "understand the deeper cost of failure", "the household pressure exposes what the children are learning", "the threat becomes moral as well as immediate", "tactically contained", "clear-eyed and burdened"),
                (7, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "reframe the crisis around protection, not control", stakes, "the protagonist realizes what kind of memory this night could become", "clear-eyed and burdened", "strategically calm"),
                (8, "INT. APARTMENT CORRIDOR - NIGHT", "apartment corridor", "night", "survive renewed pressure after the insight", parsed["pressure_trigger"], "the room is tested again before it can settle", "strategically calm", "under siege but deliberate"),
                (9, "INT. KITCHEN - LATER", "kitchen", "later", "hold the new behavior under pressure", "the family still needs action while fear remains close", "the protagonist narrows every move to protection", "under siege but deliberate", "disciplined and exact"),
                (10, "INT. BALCONY THRESHOLD - LATER", "balcony threshold", "later", "restore trust with the emotional mirror", "distance with the partner threatens the repair", "the protagonist chooses connection over solitary control", "disciplined and exact", "emotionally available"),
                (11, "INT. CHILDREN'S ROOM - PRE-DAWN", "children's room", "pre-dawn", "repair the household through precise care", stakes, "trust begins to displace fear inside the room", "emotionally available", "connected and resolving"),
                (12, "INT. BEDROOM DOORWAY - PRE-DAWN", "bedroom doorway", "pre-dawn", "close the aftermath with earned vigilance", stakes, "the family settles because panic did not rule the night", "connected and resolving", "relieved and vigilant"),
            ]
        elif genre == "romance":
            card_specs = [
                (1, f"INT. {setting.upper()} - LATE AFTERNOON", setting, "late afternoon", "show practiced tenderness under strain", "affection exists but the distance is already growing", "a small domestic detail reveals emotional drift", "tired but connected", "tentatively open"),
                (2, f"INT. {setting.upper()} - DUSK", setting, "dusk", "expose the wound inside routine", "shared duty hides unspoken hurt", "the couple feels the evening tilt toward silence", "tentatively open", "fragile"),
                (3, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "force intimacy under stress", parsed["pressure_trigger"], "the practical problem makes emotional distance impossible to ignore", "fragile", "defensive"),
                (4, "INT. KITCHEN - NIGHT", "kitchen", "night", "translate pride into visible misread", "both partners start protecting themselves instead of the bond", "the protagonist feels shame beneath the anger", "defensive", "guarded and ashamed"),
                (5, "INT. HALLWAY - NIGHT", "hallway", "night", "interrupt the scene before it hardens", "hurt wants to become coldness", "the protagonist chooses restraint over the clean wound of withdrawal", "guarded and ashamed", "contained but aching"),
                (6, "INT. BATHROOM MIRROR - NIGHT", "bathroom mirror", "night", "recognize the inherited fear inside the silence", "the self-image of being right blocks tenderness", "the protagonist understands what the distance is costing the partner", "contained but aching", "self-aware and exposed"),
                (7, "INT. BALCONY - NIGHT", "balcony", "night", "reverse the meaning of the silence", stakes, "the couple can now read the same moment from opposite emotional angles", "self-aware and exposed", "willing to be seen"),
                (8, "INT. LIVING ROOM - LATER", "living room", "later", "carry vulnerability back into the shared space", parsed["pressure_trigger"], "the ordinary world still demands action before comfort", "willing to be seen", "unsteady but reaching"),
                (9, "INT. CHILDREN'S ROOM - LATER", "children's room", "later", "let care become the language of repair", stakes, "small acts begin doing what explanation could not", "unsteady but reaching", "soft and brave"),
                (10, "INT. SINK AREA - LATER", "sink area", "later", "show the cost of reconnection", "the protagonist must surrender the protection of being right", "repair becomes costly and specific", "soft and brave", "ready to risk honesty"),
                (11, "INT. BEDTIME CORRIDOR - NIGHT", "bedtime corridor", "night", "rebuild intimacy through action first", stakes, "the partner waits to see whether the change is real", "ready to risk honesty", "emotionally reunited"),
                (12, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "land intimacy with cost absorbed", stakes, "closeness returns because someone chose vulnerability over pride", "emotionally reunited", "hopeful and intimate"),
            ]
        else:
            card_specs = [
                (1, f"INT. {setting.upper()} - LATE AFTERNOON", setting, "late afternoon", "open with family warmth already under pressure", "the room is fragile before anyone names it", "care answers first", "worn down", "present"),
                (2, f"INT. {setting.upper()} - DUSK", setting, "dusk", "show the domestic world as emotional inheritance", "the toddlers are already reading the adults", "a routine problem begins carrying emotional weight", "present", "quietly responsible"),
                (3, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "hold the line under pressure", parsed["pressure_trigger"], "anger is noticed before it moves", "quietly responsible", "pressured"),
                (4, "INT. KITCHEN - NIGHT", "kitchen", "night", "show the pressure widening through the household", "every practical task now risks becoming a moral test", "the protagonist feels inherited anger pressing for release", "pressured", "self-aware"),
                (5, "INT. HALLWAY BATHROOM - NIGHT", "hallway bathroom", "night", "interrupt the pattern visibly", "the anger is still loud inside", "the pause becomes the first changed action", "self-aware", "contained"),
                (6, "INT. LIVING ROOM - NIGHT", "living room", "night", "understand what the children are learning", stakes, "the conflict turns from household mess to emotional legacy", "contained", "clear enough to repair"),
                (7, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "change what the night means", stakes, "the protagonist realizes memory is the real battleground", "clear enough to repair", "burdened but lucid"),
                (8, "INT. KITCHEN - LATER", "kitchen", "later", "survive renewed practical pressure", parsed["pressure_trigger"], "insight is tested by fresh friction", "burdened but lucid", "strained but deliberate"),
                (9, "INT. HALLWAY - LATER", "hallway", "later", "hold the changed behavior while still exhausted", "care now requires effort rather than instinct", "the protagonist chooses slow action over inherited force", "strained but deliberate", "steady under load"),
                (10, "INT. DOORWAY - LATER", "doorway", "later", "prepare repair instead of explanation", stakes, "the family needs a changed action more than a speech", "steady under load", "emotionally available"),
                (11, "INT. CHILDREN'S ROOM - PRE-BED", "children's room", "pre-bed", "return with tenderness", stakes, "the room receives action that feels safer than words", "emotionally available", "connected and softened"),
                (12, "INT. KITCHEN TABLE - NIGHT", "kitchen table", "night", "close with earned hope", stakes, "the home feels quieter because the pattern broke", "connected and softened", "hopeful and settled"),
            ]
    elif scale == "expanded":
        if genre == "thriller":
            card_specs = [
                (1, f"INT. {setting.upper()} - DUSK", setting, "dusk", "establish unease around shared safety", f"{stakes} already feels unstable", "a harmless detail starts to feel dangerous", "guarded", "watchful"),
                (2, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "show the threat touching the relationship", "fear starts to shrink every decision", "the couple realizes the danger is active now", "watchful", "coiled"),
                (3, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "contain the threat without panic", parsed["pressure_trigger"], "the protagonist realizes panic will worsen the danger", "coiled", "frightened but controlled"),
                (4, f"INT. {setting.upper()} - LATER", setting, "later", "read the room before acting", "fear and anger compete for control", "the protagonist sees the children reading every move", "frightened but controlled", "split between force and care"),
                (5, "INT. HALLWAY - MOMENTS LATER", "hallway", "moments later", "choose tactical restraint", "adrenaline demands speed", "a pause becomes the smartest move available", "split between force and care", "strategically calm"),
                (6, f"INT. {setting.upper()} - NIGHT", setting, "night", "turn tactical calm into emotional clarity", stakes, "the real risk becomes what panic teaches the family", "strategically calm", "contained and deliberate"),
                (7, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "return with a precise repair action", stakes, "trust starts to replace fear", "contained and deliberate", "connected and resolving"),
                (8, "INT. ENTRYWAY - NIGHT", "entryway", "night", "close the threat loop with tenderness", stakes, "the room survives because panic did not win", "connected and resolving", "relieved and vigilant"),
            ]
        elif genre == "romance":
            card_specs = [
                (1, f"INT. {setting.upper()} - EARLY EVENING", setting, "early evening", "show affection under strain", "care is present but not fully spoken", "a tiny distance opens between the couple", "tired but connected", "tentatively open"),
                (2, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "show shared history and pressure", "memory and duty rub against each other", "the protagonist protects the moment instead of naming the fear", "tentatively open", "fragile"),
                (3, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "protect the shared world", parsed["pressure_trigger"], "the practical problem exposes emotional distance", "fragile", "defensive"),
                (4, f"INT. {setting.upper()} - LATER", setting, "later", "name the hurt beneath the anger", "shame is easier than vulnerability", "the protagonist realizes the anger is cover", "defensive", "self-aware and exposed"),
                (5, "INT. HALLWAY - MOMENTS LATER", "hallway", "moments later", "choose honesty instead of pride", "avoidance still feels safer", "the protagonist decides to return emotionally available", "self-aware and exposed", "willing to be seen"),
                (6, f"INT. {setting.upper()} - NIGHT", setting, "night", "invite reconnection through behavior", stakes, "support is offered without domination", "willing to be seen", "soft and brave"),
                (7, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "repair love through action", stakes, "intimacy is rebuilt through care", "soft and brave", "emotionally reunited"),
                (8, "INT. BALCONY - NIGHT", "balcony", "night", "land earned intimacy", stakes, "the night resolves distance through chosen tenderness", "emotionally reunited", "hopeful and intimate"),
            ]
        else:
            card_specs = [
                (1, f"INT. {setting.upper()} - EARLY EVENING", setting, "early evening", "warm opening", "the room is already fragile", "gentleness answers first", "worn down", "present"),
                (2, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "define family stakes inside the room", stakes, "the toddlers become the emotional center of the space", "present", "quietly responsible"),
                (3, f"INT. {setting.upper()} - CONTINUOUS", setting, "continuous", "hold the line under pressure", parsed["pressure_trigger"], "anger is noticed before it moves", "quietly responsible", "pressured"),
                (4, f"INT. {setting.upper()} - LATER", setting, "later", "catch the internal surge", parsed["pressure_trigger"], "anger is named internally", "pressured", "self-aware"),
                (5, "INT. HALLWAY BATHROOM - MOMENTS LATER", "hallway bathroom", "moments later", "choose restraint", "the anger is still loud inside", "the pause becomes visible action", "self-aware", "contained"),
                (6, f"INT. {setting.upper()} - NIGHT", setting, "night", "understand the emotional inheritance", stakes, "care becomes clearer than pride", "contained", "clear enough to repair"),
                (7, "INT. CHILDREN'S ROOM - NIGHT", "children's room", "night", "repair the family moment", stakes, "the room receives tenderness", "clear enough to repair", "connected and softened"),
                (8, "INT. KITCHEN TABLE - NIGHT", "kitchen table", "night", "close with earned hope", stakes, "the home stays softer than the pressure wanted", "connected and softened", "hopeful"),
            ]
    elif genre == "thriller":
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
        if scene_number in {1, 2, 5, 6, 7, 8, 9, 11, 12}:
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
                    "visual_strategy": f"{parsed['visual_style']} shaped by {objective}",
                },
            }
        )
    return cards

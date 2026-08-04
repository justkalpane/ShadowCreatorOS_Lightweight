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
            1: [
                {"speaker": second, "line": f"'{main}, listen. The wall is talking before we are.'"},
                {"speaker": main, "line": "'Then keep the kids with you and let me hear it.'"},
            ],
            2: [
                {"speaker": main, "line": "'Not fast. Fast is how we miss the leak.'"},
                {"speaker": second, "line": "'You mean the hiss, right? Say the word.'"},
            ],
            3: [
                {"speaker": main, "line": "'I heard it. If they see my face, we lose the room.'"},
            ],
            4: [
                {"speaker": second, "line": "'You go quiet when you want to break something.'"},
                {"speaker": main, "line": "'Then keep me useful, not loud.'"},
            ],
            5: [
                {"speaker": main, "line": "'I can force it open, or I can keep them breathing. Not both.'"},
            ],
            6: [
                {"speaker": second, "line": "'They were watching your hands, not the leak.'"},
                {"speaker": main, "line": "'Then my hands stay steady.'"},
            ],
            7: [
                {"speaker": main, "line": "'Carry the blanket first. I will carry the fear.'"},
            ],
            8: [
                {"speaker": second, "line": "'It came back.'"},
                {"speaker": main, "line": "'I know. This time it finds us ready.'"},
            ],
            9: [
                {"speaker": main, "line": "'The room shrinks when I rush. So I won't rush.'"},
            ],
            10: [
                {"speaker": second, "line": "'You do not have to win this night alone.'"},
                {"speaker": main, "line": "'I know. Stay where I can hear you.'"},
            ],
            11: [
                {"speaker": main, "line": f"'We kept {stakes} alive. Now we keep the memory gentle.'"},
            ],
            12: [
                {"speaker": second, "line": "'You never raised the room above them.'"},
            ],
        }
        return thriller_lines.get(scene_number, [{"speaker": main, "line": "'Not yet. Let the room show me the next move.'"}])
    if genre == "romance":
        romance_lines = {
            1: [
                {"speaker": second, "line": f"'{main}, you put the cups back like you're leaving.'"},
                {"speaker": main, "line": "'I put them where I could reach them in the dark.'"},
            ],
            2: [
                {"speaker": second, "line": "'You always become helpful when you don't want to answer me.'"},
                {"speaker": main, "line": "'That isn't... fair. It isn't wrong either.'"},
            ],
            3: [
                {"speaker": main, "line": "'Hold the bucket. If I look at you right now, I'll say it badly.'"},
            ],
            4: [
                {"speaker": second, "line": "'You missed one dinner and built a fortress out of it.'"},
                {"speaker": main, "line": "'Because being late felt smaller than being known.'"},
            ],
            5: [
                {"speaker": main, "line": "'If I say sorry too cleanly, you'll hear me hiding in it.'"},
            ],
            6: [
                {"speaker": second, "line": "'I wasn't asking for perfect. I was asking for you to stay in the room.'"},
            ],
            7: [
                {"speaker": main, "line": "'I kept thinking silence looked safer on me.'"},
                {"speaker": second, "line": "'It only made me guess at the worst version of you.'"},
            ],
            8: [
                {"speaker": second, "line": "'Then don't explain it. Hand me the towels and stay.'"},
            ],
            9: [
                {"speaker": main, "line": "'She'll remember who reached first. Let it be me.'"},
            ],
            10: [
                {"speaker": main, "line": "'I moved your father's mug so I would not have to see what I turned into.'"},
                {"speaker": second, "line": "'Put it back, then. Not for him. For us.'"},
            ],
            11: [
                {"speaker": main, "line": "'I don't need to be right tonight. I need to be here.'"},
            ],
            12: [
                {"speaker": second, "line": "'Now I can believe you stayed.'"},
            ],
        }
        return romance_lines.get(scene_number, [{"speaker": main, "line": "'Not yet. Let me do one true thing before I talk.'"}])
    if scene_number == 1:
        return [
            {"speaker": second, "line": f"'{main}, it started a few minutes ago.'"},
            {"speaker": main, "line": "'Give me one second to arrive better than I was.'"},
        ]
    if scene_number == 2:
        return [
            {"speaker": second, "line": f"'{stakes} is all anyone can feel right now.'"},
            {"speaker": main, "line": "'Then they get my calm first, not my temper.'"},
        ]
    if scene_number == 3:
        return [
            {"speaker": main, "line": "'I felt it before I named it. That part has to change.'"},
        ]
    if scene_number == 4:
        return [{"speaker": main, "line": "'I can let the first version of me pass by.'"}]
    if scene_number == 5:
        return [{"speaker": main, "line": "'This isn't patience yet. It's the minute before it.'"}]
    if scene_number == 6:
        return [
            {"speaker": main, "line": "'Let them remember the fix, not the fear.'"},
            {"speaker": second, "line": "'That's the part they needed from you.'"},
        ]
    if scene_number == 7:
        return [{"speaker": main, "line": "'They don't need a lesson. They need a softer room.'"}]
    if scene_number == 8:
        return [{"speaker": second, "line": "'It came back smaller. So do better smaller too.'"}]
    if scene_number == 9:
        return [{"speaker": main, "line": "'I can finish the job without making myself the problem.'"}]
    if scene_number == 10:
        return [{"speaker": second, "line": "'You don't have to explain it while you're finally doing it right.'"}]
    if scene_number == 11:
        return [{"speaker": main, "line": "'Sleep first. I'll keep the rest of it.'"}]
    if scene_number == 12:
        return [{"speaker": second, "line": "'You stayed gentle all the way through.'"}]
    return [{"speaker": main, "line": "'The room doesn't need my old answer anymore.'"}]


def _dialogue_subtext_goal(genre: str, mirror: str) -> str:
    if genre == "thriller":
        return f"{mirror}; fear must be spoken sideways through tactical choices and restraint."
    if genre == "romance":
        return f"{mirror}; longing, misread intention, and apology-by-action should sit under the lines."
    return f"{mirror}; no generic motivational speech."


def _visual_motif(parsed: dict[str, Any], genre: str, scene_number: int, stakes: str, location: str) -> str:
    style = parsed["visual_style"]
    if genre == "thriller":
        motifs = {
            1: "vent grille shadow across family light",
            2: "flicker-cut faces and narrowing corridor depth",
            3: "hiss source hidden beyond child-height eyeline",
            4: "doorway silhouette under pressure framing",
            5: "hand versus latch in negative space",
            6: "wet steel sink and watched hands",
            7: "blanket shield around sleeping breath",
            8: "returning corridor shadow with sharper edges",
            9: "careful kitchen geometry under low light",
            10: "threshold intimacy inside emergency posture",
            11: "small hands, soft lamp, post-crisis stillness",
            12: "pre-dawn relief held at the bedroom frame",
        }
        return f"{style}; {motifs.get(scene_number, f'pressure image around {stakes} in {location}')}"
    if genre == "romance":
        motifs = {
            1: "misplaced cups revealing emotional drift",
            2: "folded towels as avoidance choreography",
            3: "rain leak forcing shared physical space",
            4: "kitchen counter as pride barrier",
            5: "hallway narrowness trapping the almost-exit",
            6: "mirror split between self-image and tenderness",
            7: "double reflection before eye contact",
            8: "wet towels passed hand to hand",
            9: "blanket smoothing as surrogate apology",
            10: "old mug restored with changed meaning",
            11: "bedtime corridor closing the distance by inches",
            12: "shoulders touching before speech catches up",
        }
        return f"{style}; {motifs.get(scene_number, f'intimacy image around {stakes} in {location}')}"
    motifs = {
        1: "bent worksheet and spill left half-noticed",
        2: "steel bowl rhythm under a lowered voice",
        3: "doorframe pause before entry",
        4: "sink edge under a tightening hand",
        5: "mirror breath and inherited shoulders",
        6: "damp towel becoming visible repair",
        7: "toddler-height room rebuilt by hand",
        8: "small relapse answered through sequence",
        9: "quiet floorboards after interrupted anger",
        10: "crooked photo set straight without speech",
        11: "page turn replacing the sharpest sound",
        12: "repair-shop hum receding beneath low light",
    }
    return f"{style}; {motifs.get(scene_number, f'care image around {stakes} in {location}')}"


def _action_lines(main: str, second: str, location: str, stakes: str, objective: str, genre: str, scene_number: int) -> list[str]:
    if genre == "thriller":
        thriller_actions = {
            1: [f"{main} stops at the corridor vent, one hand lifted for quiet.", f"{second} follows his eyes to the wall before looking at the children."],
            2: [f"{main} crosses {location} without wasting a step.", "A power flicker strips the room to outlines and breathing."],
            3: ["The hiss becomes undeniable.", f"{main} kneels to child height before moving anyone."],
            4: [f"{main} squares himself in the doorway instead of charging through it.", f"{second} shifts a child behind her hip and waits for his next signal."],
            5: ["His hand reaches for force, then settles on precision instead.", "The room changes because he refuses to feed it panic."],
            6: [f"{second} watches {main}'s hands steady before his face does.", "The danger is now moral as much as practical."],
            7: [f"{main} lifts the child like fragile evidence, not luggage.", f"The blanket becomes a shield around {stakes}."],
            8: ["The sound returns sharper than before.", f"{main} answers it with a plan instead of heat."],
            9: [f"In {location}, every movement is measured against breath and distance.", "No one mistakes calm for passivity now."],
            10: [f"{second} stays in the threshold so {main} can hear another heartbeat besides his own.", "Connection becomes part of the survival plan."],
            11: [f"{main} rebuilds the room with ordinary care: blanket, water, light, breath.", "The children start following his calm instead of the noise."],
            12: ["Nothing is solved forever, but the night has been carried without cruelty.", "Relief arrives carefully, as if it still has to earn the room."],
        }
        return thriller_actions.get(scene_number, [f"{main} moves through {location} with deliberate restraint.", f"{objective.capitalize()} lands as behavior, not explanation."])
    if genre == "romance":
        romance_actions = {
            1: [f"{second} notices one cup turned backward on the drying rack.", f"{main} fixes it before admitting he remembers why it matters."],
            2: [f"{main} keeps folding towels that do not need folding.", f"{second} lets the silence sit long enough to make it answerable."],
            3: ["Rain pushes through the ceiling seam and into their old argument.", f"They work side by side without touching, close enough to feel the absence."],
            4: [f"{main} leans on the counter as if standing still could count as honesty.", f"{second} wipes the same spot twice rather than rescue him from the moment."],
            5: ["He almost leaves, then stays where she can see the choice happen.", "The hallway narrows until pride has nowhere graceful to hide."],
            6: [f"In the mirror, {main} sees how distance has been posing as control.", f"{second}'s voice stays quiet enough to make defense feel childish."],
            7: ["They stand close at the balcony glass and look at different reflections first.", "The silence changes from punishment to invitation."],
            8: [f"{main} takes the wet towels from {second} without turning it into a speech.", "Shared labor becomes the first honest sentence of the night."],
            9: [f"He smooths the child's blanket the way {second} always does.", "Care begins to replace apology."],
            10: [f"{main} returns the old mug to its usual place and leaves his hand there a beat too long.", "The object changes meaning because he lets it accuse him first."],
            11: ["He chooses presence over being right while nothing dramatic rewards him for it.", "That cost is what makes tenderness believable."],
            12: ["Their shoulders meet before either of them names what survived.", "Intimacy returns as a smaller, truer gesture than a perfect confession."],
        }
        return romance_actions.get(scene_number, [f"{main} moves through {location} with visible hesitation.", f"{objective.capitalize()} becomes a lived domestic beat."])
    motivational_actions = {
        1: [f"{main} sets down a school worksheet already marked with a bent corner.", f"{second} watches him miss the spill on the counter the first time.", "A spoon rattles against a steel bowl in the next room and nobody flinches yet."],
        2: [f"{second} keeps one toddler busy with a spoon and a steel bowl.", f"{main} answers the noise by lowering his voice instead of raising it.", "His thumb stays pressed to the edge of the counter until the urge to snap passes."],
        3: [f"The pressure lands in the room before anyone names it.", f"{main} pauses at the doorframe long enough to choose how he will enter.", "His breath changes first; that is how the room knows which version of him arrived."],
        4: [f"In {location}, his hand tightens on the sink before it opens again.", "The old reflex arrives first; the better one arrives second and stays.", "Water taps the metal basin with the patience he is trying to borrow."],
        5: [f"{main} studies his own face in the mirror like he has inherited it from someone he loves and fears.", "Breath returns before language does.", "His shoulders drop a fraction, enough to change the next room."],
        6: [f"{second} notices the children watching him more carefully than the mess.", f"He starts cleaning what frightened them instead of defending himself.", "A damp towel moves through his hands like an apology he cannot rush."],
        7: [f"{main} kneels until the room is built to toddler height.", f"The repair begins where the memory will begin.", "Blanket, worksheet, cup, breath: he puts everything back in the order safety needs."],
        8: [f"The interruption returns, smaller but meaner.", f"{main} answers it with sequence instead of force.", "He closes one cupboard softly before opening the next, as if teaching his own hands."],
        9: [f"He finishes the practical task without spending his temper on it.", "The room feels new because the pattern doesn't complete itself.", "Even the floorboards seem quieter when no one has to brace for him."],
        10: [f"{second} leaves space for an apology that has not earned words yet.", f"{main} fills that space with care first.", "He rights the crooked photo by the switchplate and leaves it straight this time."],
        11: [f"He reads low and steady while small hands unclench around the blanket.", "Safety becomes visible before anyone names it.", "The last sharp sound in the apartment is only the page turning."],
        12: [f"The apartment is still imperfect, but not dangerous in the old way.", f"{main} leaves the light on low and the night softer than he found it.", "The repair shop hum beneath the floor now sounds like distance instead of pressure."],
    }
    return motivational_actions.get(scene_number, [f"{main} moves through {location} with controlled quiet.", f"{stakes} stays visible through behavior rather than explanation."])


def _build_feature_subscenes(card: dict[str, Any], main: str, second: str) -> list[dict[str, Any]]:
    base_location = card["location"]
    objective = card["scene_objective"]
    conflict = card["conflict"]
    turn = card["turning_point"]
    start = card["emotional_value_start"]
    end = card["emotional_value_end"]
    return [
        {
            "sub_scene_number": f"{card['scene_number']}.1",
            "location": base_location,
            "objective": f"prepare pressure inside {objective}",
            "conflict": f"the first edge of {conflict.lower()}",
            "turning_point": f"{main} notices the first crack in the room",
            "emotional_shift": f"{start} -> more exposed",
        },
        {
            "sub_scene_number": f"{card['scene_number']}.2",
            "location": base_location,
            "objective": f"complicate {objective}",
            "conflict": conflict,
            "turning_point": turn,
            "emotional_shift": f"more exposed -> pressured choice",
        },
        {
            "sub_scene_number": f"{card['scene_number']}.3",
            "location": base_location,
            "objective": f"carry consequence toward the next scene for {second}",
            "conflict": f"after {turn.lower()}, trust must survive {conflict.lower()}",
            "turning_point": f"the room leaves the scene in a new state: {end}",
            "emotional_shift": f"pressured choice -> {end}",
        },
    ]


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
                "visual_motif": _visual_motif(parsed, genre, scene_number, stakes, location),
                "dialogue_subtext_goal": _dialogue_subtext_goal(genre, mirror),
                "continuity_dependencies": [
                    f"toddler stakes remain active: {stakes}",
                    f"main character remains soft-spoken and warm: {main}",
                    "controlled internal anger is visible but not acted out",
                ],
                "scene_consequence": f"{turning_point} changes the room from {start} to {end}",
                "next_scene_dependency": f"the next scene must respond to {turning_point.lower()}",
                "beat_ids": beat_by_scene.get(scene_number, []),
                "action_lines": _action_lines(main, second, location, stakes, objective, genre, scene_number),
                "dialogue_lines": _dialogue_lines(main, second, stakes, scene_number, genre),
                "visual_plan": {
                    "camera_reason": parsed["camera_reason_seed"],
                    "frame_pressure": parsed["frame_pressure_seed"],
                    "visual_strategy": f"{parsed['visual_style']} shaped by {objective}",
                },
            }
        )
    if scale == "feature":
        for card in cards:
            card["sub_scene_cards"] = _build_feature_subscenes(card, main, second)
    return cards

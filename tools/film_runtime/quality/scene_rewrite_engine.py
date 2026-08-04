"""F13 scene-level cinematic rewrite engine."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def _payload(packet: dict[str, Any]) -> dict[str, Any]:
    return deepcopy(packet.get("quality_benchmark_source_payload") or {})


def _genre(packet: dict[str, Any]) -> str:
    return (
        packet.get("genre")
        or packet.get("premise_test", {}).get("genre")
        or _payload(packet).get("genre")
        or "motivational_drama"
    )


def _names(packet: dict[str, Any]) -> tuple[str, str]:
    payload = _payload(packet)
    main = payload.get("main_character_name") or packet.get("character_arc", {}).get("protagonist") or "Ari"
    second = payload.get("second_character_name") or ((packet.get("character_bible", {}).get("major_characters") or [{}, {}])[1].get("name")) or "Mina"
    return main, second


def _setting(packet: dict[str, Any]) -> str:
    payload = _payload(packet)
    return payload.get("setting") or packet.get("world_bible", {}).get("locations", ["domestic home"])[0]


def _stakes(packet: dict[str, Any]) -> str:
    payload = _payload(packet)
    return payload.get("toddler_stakes_detail") or packet.get("premise_test", {}).get("stakes", "family trust is at risk")


def _theme(packet: dict[str, Any]) -> str:
    return packet.get("premise_test", {}).get("theme") or _payload(packet).get("theme", "")


def _title(packet: dict[str, Any]) -> str:
    lane = _genre(packet)
    main, _ = _names(packet)
    setting = _setting(packet)
    if lane == "thriller":
        return f"{main} Before the Hiss Reaches {setting.title()}"
    if lane == "romance":
        return f"{main} on the Night the Dinner Burned"
    return f"{main} and the Spill Before Bed"


def _final_image_line(packet: dict[str, Any], final_card: dict[str, Any]) -> str:
    lane = _genre(packet)
    main, second = _names(packet)
    motif = final_card["visual_motif"]
    if lane == "thriller":
        return (
            f"FINAL IMAGE: {motif}; {main} leaves the toy truck upright on the stoop, "
            f"and {second} lets the night's silence stay silence instead of fear."
        )
    if lane == "romance":
        return (
            f"FINAL IMAGE: {motif}; {main} leaves the spare key in {second}'s palm instead of pocketing escape again, "
            "and they look at the same reflection before either one dares to touch the glass."
        )
    return (
        f"FINAL IMAGE: {motif}; {main} and {second} finish the room in a quieter rhythm, "
        "and the children fall asleep inside that new tempo."
    )


def _logline(packet: dict[str, Any]) -> str:
    lane = _genre(packet)
    main, second = _names(packet)
    setting = _setting(packet)
    premise = packet.get("premise_test", {})
    stakes = premise.get("stakes") or _stakes(packet)
    conflict = premise.get("central_conflict") or _payload(packet).get("emotional_pressure_trigger") or "pressure rises"
    if lane == "thriller":
        return (
            f"In this thriller, {main} must get the children clear of {setting} before {conflict} and the family's "
            f"own panic turn {stakes} into catastrophe."
        )
    if lane == "romance":
        return (
            f"In this romance drama, {main} must cross the emotional distance inside {setting} before {conflict} "
            f"and a long habit of silence cost {second} the trust to stay open for {stakes}."
        )
    return (
        f"{main} must protect the toddlers inside {setting} before spilled milk and {conflict}, because two toddlers "
        "are watching whether the adult will choose care or anger, and the children will learn either trust or fear in this motivational drama."
    )


def _line(speaker: str, line: str) -> dict[str, str]:
    return {"speaker": speaker, "line": line}


def _scene(
    number: int,
    slugline: str,
    location: str,
    time_of_day: str,
    characters: list[str],
    objective: str,
    conflict: str,
    turning_point: str,
    emotional_start: str,
    emotional_end: str,
    visual_motif: str,
    subtext_goal: str,
    continuity: list[str],
    action_lines: list[str],
    dialogue_lines: list[dict[str, str]],
    visual_strategy: str,
    camera_reason: str,
) -> dict[str, Any]:
    return {
        "scene_number": number,
        "slugline": slugline,
        "heading": slugline,
        "location": location,
        "time_of_day": time_of_day,
        "characters_present": characters,
        "scene_objective": objective,
        "objective": objective,
        "conflict": conflict,
        "turning_point": turning_point,
        "turn": turning_point,
        "emotional_value_start": emotional_start,
        "emotional_value_end": emotional_end,
        "visual_motif": visual_motif,
        "dialogue_subtext_goal": subtext_goal,
        "continuity_dependencies": continuity,
        "action_lines": action_lines,
        "dialogue_lines": dialogue_lines,
        "visual_plan": {
            "visual_strategy": visual_strategy,
            "camera_reason": camera_reason,
            "frame_pressure": emotional_end,
        },
    }


def _motivational_scenes(packet: dict[str, Any]) -> list[dict[str, Any]]:
    main, second = _names(packet)
    stakes = _stakes(packet)
    raw_setting = _setting(packet)
    setting = raw_setting.upper()
    return [
        _scene(
            1,
            f"INT. {setting} - EARLY EVENING",
            _setting(packet),
            "early evening",
            [main, second, "toddler_1", "toddler_2"],
            "keep the room from tipping into panic before the toddlers memorize the wrong lesson",
            "milk floods the worksheets while a work call vibrates unanswered in a back pocket",
            "the older toddler stops crying and studies the protagonist's face instead",
            "compressed",
            "warned",
            "white milk cutting across homework lines",
            "the partner is really asking whether the protagonist is still emotionally present",
            ["spilled milk still on floor", stakes],
            [
                f"{main} catches the carton before it reaches the table edge, but the notebooks are already soaked.",
                f"{second} holds a dish towel without stepping in yet, holding a quiet pause long enough for the toddlers to look from the puddle to {main}'s jaw.",
            ],
            [
                _line(second, "Don't fix the floor first if you're about to leave us in the room alone."),
                _line(main, "I'm staying. Hand me the towels, not the verdict."),
            ],
            "keep the spill low in frame so the toddlers' line of sight and the adult hands occupy the same tension",
            "show that the protagonist's first victory is small physical control, not verbal wisdom",
        ),
        _scene(
            2,
            "INT. BATHROOM SINK - MOMENTS LATER",
            "bathroom sink",
            "moments later",
            [main],
            "bleed off the first surge before it reaches the children",
            "anger wants privacy, but the sound of the toddlers outside keeps the responsibility immediate",
            "the protagonist sees a milk streak on the wrist and realizes the room will remember the next ten seconds",
            "flooded",
            "contained",
            "water over knuckles that still want to clench",
            "the line is really about shame, not logistics",
            ["wet cuff", "toddlers audible from hallway"],
            [
                f"{main} braces both palms on the sink until the porcelain stops shaking under them.",
                "Off-screen, a toy clatters and one toddler asks if anyone is angry.",
            ],
            [
                _line(main, "No. I'm late, I'm embarrassed, and that's not the same thing."),
            ],
            "stay close on breath, wrist, and faucet rather than the whole room",
            "make restraint visible as action rather than as a speech about calmness",
        ),
        _scene(
            3,
            f"INT. {setting} DOORWAY - CONTINUOUS",
            f"{raw_setting} doorway",
            "continuous",
            [main, second],
            "return before silence hardens into distance",
            "the partner is cleaning alone and the toddlers are now helping in the wrong way",
            f"{second} quietly says the children are copying the protagonist's face, not the instructions",
            "guarded",
            "exposed",
            "small hands pushing towels into the spill",
            "the partner is offering a mirror, not an accusation",
            ["toddlers now kneeling by spill", "the worksheets are salvageable if dried now"],
            [
                f"{main} stops in the doorway when the younger toddler presses a towel into the milk as if rehearsing adulthood.",
                f"{second} keeps working without looking up, which lands harder than if they had snapped.",
            ],
            [
                _line(second, "They're copying your face, not your words."),
                _line(main, "Then I owe them a different face before I owe anyone an explanation."),
            ],
            "let the doorway divide the protagonist from the family for a beat before the decision to step back in",
            "turn the midpoint into a behavior note that collapses the protagonist's excuses",
        ),
        _scene(
            4,
            f"INT. {setting} - NIGHT",
            raw_setting,
            "night",
            [main, second, "toddler_1", "toddler_2"],
            "repair the room through labor, not apology theater",
            "the spill is manageable now, but trust will only settle if the protagonist joins the mess humbly",
            "the protagonist kneels lower than the toddlers and asks them for help instead of order",
            "ashamed",
            "tender",
            "knees on tile beside tiny socks",
            "the words are really an apology to the partner, disguised as instruction to the children",
            ["fresh towels", "one worksheet corner still dry"],
            [
                f"{main} drops to the floor, folds the dry corners away from the milk, and lets the toddlers pass towels one at a time.",
                f"{second} watches the hands, waiting through one quiet beat before trusting the voice.",
            ],
            [
                _line(main, "We clean the part we made, and we stay kind while we do it."),
                _line(second, "That's the first useful thing anyone has said in here."),
            ],
            "favor low angles that keep adult and child hands in the same geography",
            "show repair as a shared task that restores the family's emotional temperature",
        ),
        _scene(
            5,
            "INT. CHILDREN'S ROOM - LATER",
            "children's room",
            "later",
            [main, second, "toddler_1", "toddler_2"],
            "close the lesson with a bedtime ritual that proves change happened",
            "the children still expect the earlier tension to return",
            "one toddler relaxes only after the protagonist slows the final line into a whisper",
            "fragile",
            "safe",
            "night-light glow on newly dried worksheets by the door",
            "the partner needs evidence that repair can hold after the mess is gone",
            ["worksheets drying in hallway", "children now quiet enough for story"],
            [
                f"{main} smooths a blanket corner with the same care used to blot the ruined paper, holding one pause before the final tuck-in.",
                f"{second} places the rescued worksheet by the night-light where tomorrow can find it.",
            ],
            [
                _line(main, "I was loud before I ever raised my voice. I'm done with that for tonight."),
                _line(second, "Good. Let them remember your hands slower than the spill."),
            ],
            "end on a domestic image that holds the repair without announcing victory",
            "earn hope by letting the body language soften before the dialogue does",
        ),
    ]


def _thriller_scenes(packet: dict[str, Any]) -> list[dict[str, Any]]:
    main, second = _names(packet)
    raw_setting = _setting(packet)
    setting = raw_setting.upper()
    stakes = _stakes(packet)
    return [
        _scene(
            1,
            f"INT. {setting} - DUSK",
            raw_setting,
            "dusk",
            [main, second, "toddler_1", "toddler_2"],
            "read the first abnormal sign before the family normalizes it away",
            "a faint gas smell arrives just as the lights shiver and one toddler starts coughing",
            "the protagonist kills the wall fan instead of switching on another light",
            "uneasy",
            "focused",
            "the corridor light blinking like a bad pulse",
            "the partner is really asking whether the protagonist trusts instinct or appearances",
            [stakes, "electricity unstable"],
            [
                f"{main} sniffs once, holds a beat at the light switch, then reaches past it and kills the fan.",
                f"{second} gathers the toddlers without asking why, which tells us this has happened before in smaller forms.",
            ],
            [
                _line(second, "You smelled it too."),
                _line(main, "Enough to stop pretending it's nothing."),
            ],
            "start with cramped practical shadows and an interrupted airflow cue",
            "establish that precision begins with refusing a reflexive bad move",
        ),
        _scene(
            2,
            "INT. KITCHEN THRESHOLD - CONTINUOUS",
            "kitchen threshold",
            "continuous",
            [main, second],
            "confirm the threat without feeding it oxygen",
            "a burner clicks uselessly while the power flickers and the smell thickens near the floor",
            "the protagonist spots a kettle pushed against the wrong knob by a toy truck",
            "focused",
            "alarmed",
            "stainless steel reflecting an unstable blue pilot spark",
            "the partner needs a plan, not reassurance",
            ["fan off", "children held back from kitchen"],
            [
                f"{main} crouches instead of rushing in, holding still long enough for the eyes to travel from the toy truck to the skewed burner knob.",
                f"{second} grips the toddler carrier tight enough to hear the plastic creak.",
            ],
            [
                _line(main, "Don't touch the switches. Back everyone to the stairwell."),
                _line(second, "Tell me this is fixable while we move, not before."),
            ],
            "keep the threat near the floor and the faces higher, forcing spatial awareness into the blocking",
            "turn exposition into instructions shaped by immediate survival",
        ),
        _scene(
            3,
            "INT. STAIRWELL LANDING - MOMENTS LATER",
            "stairwell landing",
            "moments later",
            [main, second, "toddler_1", "toddler_2"],
            "buy time without letting fear spread to the children",
            "the younger toddler starts to cry harder when the adults move too fast",
            "the protagonist slows down long enough to steady the child, even though the clock is running",
            "urgent",
            "disciplined",
            "a shoe abandoned on the step",
            "the partner hears whether calm is real or performed",
            ["kitchen threat confirmed", "toddlers coughing lightly"],
            [
                f"{main} lifts one child, then stops halfway down the stairs when the other locks up instead of following.",
                "The smell reaches the landing a half-second later, as if punishing the pause.",
            ],
            [
                _line(main, "Look at me, not the dark. We move when your breathing catches mine."),
                _line(second, "You're wasting seconds. I know. Keep going."),
            ],
            "build suspense by letting the pause be tactically expensive but necessary",
            "prove the thriller pressure through conflicting correct choices",
        ),
        _scene(
            4,
            "INT. UTILITY NOOK - LATER",
            "utility nook",
            "later",
            [main],
            "find the real source instead of fixing the nearest symptom",
            "the obvious burner problem hides a second leak at the flex line",
            "the protagonist hears the soft hiss only after killing every other noise",
            "disciplined",
            "certain",
            "a flashlight beam trembling over braided metal",
            "the line is really about inherited panic habits versus earned attention",
            ["family staged on landing", "power still unstable"],
            [
                f"{main} pockets the phone before it can ring, then listens harder than the room wants to be listened to.",
                "The hiss is tiny, humiliatingly easy to miss, and suddenly the whole space reorganizes around it.",
            ],
            [
                _line(main, "It wasn't the flame. It was the line pretending to be harmless."),
            ],
            "make the midpoint a revelation of hidden cause, not just stronger fear",
            "give the protagonist a discovery earned through sensory discipline",
        ),
        _scene(
            5,
            "INT. SERVICE HALL - CONTINUOUS",
            "service hall",
            "continuous",
            [main, second],
            "coordinate the shutoff without collapsing into cross-talk",
            "the partner wants to help immediately, but one wrong motion could spread the risk",
            "the protagonist delegates one precise task and trusts it",
            "certain",
            "shared",
            "emergency valve painted over three times",
            "the partner needs to be treated as competent, not protected from truth",
            ["source located", "family waiting on landing"],
            [
                f"{main} points with two fingers instead of grabbing, making the job small enough to survive adrenaline.",
                f"{second} strips paint from the valve lip with a key while holding eye contact for the count.",
            ],
            [
                _line(main, "On three, turn once and stop if it bites back."),
                _line(second, "Good. Give me the real job or get out of my way."),
            ],
            "stress hands, hardware, and count rhythm over faces for this beat",
            "show that shared competence is the thriller's emotional repair",
        ),
        _scene(
            6,
            "EXT. APARTMENT STOOP - NIGHT",
            "apartment stoop",
            "night",
            [main, second, "toddler_1", "toddler_2"],
            "get the children fully clear before relief turns sloppy",
            "the younger toddler reaches back toward the building as if the danger were already over",
            "the protagonist finally allows a full breath only after hearing the hiss die inside",
            "shaken",
            "relieved",
            "streetlight halo against exhaled breath",
            "the partner is really checking whether the protagonist can come back from tactical mode gently",
            ["valve turned", "family outside but not calm yet"],
            [
                f"{main} keeps one hand on the doorframe until the silence inside feels different from the silence of shock.",
                f"{second} wraps a coat around both toddlers in one motion, as if bundling the danger out of them.",
            ],
            [
                _line(second, "Now you can tell me you're scared."),
                _line(main, "I was. I just needed the fear to wait its turn."),
            ],
            "release the frame into open air only after the threat is actually reduced",
            "let the emotional exhale arrive as a consequence of solved action",
        ),
        _scene(
            7,
            "EXT. APARTMENT STOOP - LATER",
            "apartment stoop",
            "later",
            [main, second, "toddler_1", "toddler_2"],
            "end with consequence and competence, not a magic reset",
            "the building is safe now, but the children still need a story for what happened",
            "the protagonist explains the response in child-sized language rather than pretending nothing happened",
            "relieved",
            "steady",
            "the toy truck set upside down on the stoop step",
            "the partner needs evidence that precision can return to tenderness",
            ["gas leak contained", "children wrapped in coats"],
            [
                f"{main} turns the toy truck over and sets it beside the toddler's boot like a promise that small mistakes can be found in time.",
                f"{second} leans into the silence now that it no longer feels dangerous.",
            ],
            [
                _line(main, "The house told us the truth in a whisper. We listened before it had to shout."),
                _line(second, "That is how I want them to remember tonight."),
            ],
            "end on an object that once caused danger but now carries memory and control",
            "make the final beat consequence-aware instead of purely comforting",
        ),
    ]


def _romance_scenes(packet: dict[str, Any]) -> list[dict[str, Any]]:
    main, second = _names(packet)
    raw_setting = _setting(packet)
    setting = raw_setting.upper()
    stakes = _stakes(packet)
    return [
        _scene(
            1,
            f"INT. {setting} - EARLY EVENING",
            raw_setting,
            "early evening",
            [main, second],
            "save the anniversary ritual before distance hardens into habit",
            "a burned pan and an unanswered text expose how long tenderness has been delayed",
            "the partner blows out a candle before the protagonist can pretend not to notice",
            "careful",
            "bruised",
            "rain streaking the window behind the blue sugar bowl from their first rental",
            "the partner is really asking whether absence has become the protagonist's preferred defense and whether shared rituals still mean anything",
            ["anniversary dinner half-ruined", stakes],
            [
                f"{main} steps in with florist paper damp from the rain, stopping in a held beat when the smell of scorched butter and the half-set anniversary table reach the door before {second}'s eyes do.",
                f"{second} pinches out the candle with wet fingers, then straightens the blue sugar bowl they kept from their first one-room rental before sliding the blackened pan off the flame.",
            ],
            [
                _line(second, "You never miss the apology. It's the hour before it that goes dark."),
                _line(main, "I wasn't hiding from tonight. I was trying not to ruin it worse."),
            ],
            "frame the unused celebration details as witnesses rather than decoration",
            "open with relational failure embedded in objects, not explained in backstory",
        ),
        _scene(
            2,
            "INT. KITCHEN COUNTER - CONTINUOUS",
            "kitchen counter",
            "continuous",
            [main, second],
            "keep the argument from slipping into the old familiar script",
            "the protagonist wants to solve the meal while the partner wants the truth under the meal",
            "the partner stops the protagonist from scraping the pan clean and makes them look up",
            "defensive",
            "cornered",
            "charred edge of bread beside the old chipped tea glass they only use on anniversaries",
            "the dialogue is really about abandonment, not dinner, and about who keeps pretending objects are easier than memory",
            ["flowers still in hand", "smoke smell in apartment", "anniversary tea glass still untouched"],
            [
                f"{main} reaches for the pan towel-first, using the movement like a shield, then halts when the chipped tea glass catches against a plate with the sound of an old argument.",
                f"{second} stops the wrist with two fingers and leaves the hand there a beat longer than anger requires, then lets go before the touch can become mercy.",
            ],
            [
                _line(second, "Don't fix the pan to spare yourself the rest of this."),
                _line(main, "If I stand still, you'll hear what I almost said in the car."),
            ],
            "keep touch brief and charged so the scene plays through restraint",
            "make subtext ride through interrupted practical action",
        ),
        _scene(
            3,
            "INT. WINDOW ALCOVE - LATER",
            "window alcove",
            "later",
            [main, second],
            "turn the fight from irritation toward the real wound",
            "the protagonist fears saying the truth will confirm the partner's worst reading",
            "the protagonist admits absence was a form of shame, not indifference",
            "cornered",
            "bare",
            "condensation cut by one thumb through the window fog while their reflections refuse to meet",
            "the confession is really a request not to be mistaken for someone colder than they are, and the partner's reply is really about years of being left to translate silence alone",
            ["dinner abandoned", "rain louder now", "sugar bowl still on table behind them"],
            [
                f"{main} clears a strip in the window fog with the side of a thumb and sees both reflections split by rain before daring to speak to the glass first.",
                f"{second} folds the ruined napkin into a tighter square, then sets it beside the sugar bowl like proof that small saved things can still accuse.",
            ],
            [
                _line(main, "I kept arriving late so you wouldn't have to watch me come apart up close."),
                _line(second, "You decided for me that distance would feel kinder. It didn't."),
            ],
            "use reflection and weather to literalize misread intention becoming clarity",
            "give the midpoint an emotional reversal that changes what the conflict is about",
        ),
        _scene(
            4,
            "INT. DINING TABLE - NIGHT",
            "dining table",
            "night",
            [main, second],
            "rebuild intimacy through a new shared action instead of a solved speech",
            "they can still fall back into eloquent apology unless one of them risks awkward tenderness",
            "the protagonist serves the salvageable pieces first to the partner, not to self-protective order",
            "bare",
            "tentative",
            "one good plate beside one ruined one and the spare key left in plain sight",
            "the offer is really about staying in the conversation after shame has been named, and about surrendering the old escape route before anyone asks",
            ["confession made", "rain continues outside", "spare key in protagonist pocket"],
            [
                f"{main} scrapes the one salvageable piece onto {second}'s plate first, then sets the spare key on the tablecloth instead of keeping it turned inside a fist.",
                f"{second} notices the key before the plate and does not touch either until the silence proves {main} will stay in it.",
            ],
            [
                _line(main, "I know how to arrive with flowers. I don't know how to arrive while I'm still ashamed."),
                _line(second, "Start there. Not polished. Just here."),
            ],
            "favor table geometry and hand placement over coverage of faces delivering lines",
            "make reconciliation tentative and behavioral before it becomes verbal",
        ),
        _scene(
            5,
            "INT. LIVING ROOM WINDOW - LATER",
            "living room window",
            "later",
            [main, second],
            "end with intimacy that feels lived, not declared",
            "forgiveness is possible, but only if the new honesty survives an unguarded quiet",
            "the partner leans in first only after the protagonist stays still instead of filling the silence",
            "tentative",
            "earned",
            "two reflections finally sharing one pane of glass while the spare key changes hands",
            "the partner needs proof that vulnerability will not be answered by retreat, and the protagonist needs to give up leaving neatly before being believed",
            ["table half-cleared together", "rain now softer", "spare key now visible between them"],
            [
                f"{main} stands beside {second} at the window without reaching first, then leaves the spare key in {second}'s open palm and holds still instead of asking for a promise.",
                f"{second} takes the damp florist paper from {main}'s hand, pauses over the water glass meant for wine, and closes fingers over the key only after looking at their joined reflection instead of at the floor.",
            ],
            [
                _line(second, "Next time, don't send the silence in your place."),
                _line(main, "Then next time I'll knock while I'm still a mess."),
            ],
            "close on proximity and reflected light rather than a verbal declaration of closure",
            "earn reconciliation by making stillness feel newly trustworthy",
        ),
    ]


def _scene_sets(packet: dict[str, Any]) -> list[dict[str, Any]]:
    genre = _genre(packet)
    if genre == "thriller":
        return _thriller_scenes(packet)
    if genre == "romance":
        return _romance_scenes(packet)
    return _motivational_scenes(packet)


def _screenplay_from_scenes(packet: dict[str, Any], scenes: list[dict[str, Any]]) -> str:
    theme = _theme(packet)
    title = _title(packet)
    lines = [f"TITLE: {title}", "", f"THEME: {theme}", ""]
    for scene in scenes:
        lines.append(scene["slugline"])
        lines.append("")
        for action_line in scene.get("action_lines", []):
            lines.append(action_line)
        lines.append("")
        for dialogue in scene.get("dialogue_lines", []):
            lines.append(f"                        {dialogue['speaker'].upper()}")
            lines.append(f"            {dialogue['line']}")
            lines.append("")
    final_card = scenes[-1]
    lines.append(_final_image_line(packet, final_card))
    return "\n".join(lines).rstrip() + "\n"


def _beat_sheet(packet: dict[str, Any], scenes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    genre = _genre(packet)
    beat_ids = {
        "motivational_drama": [
            "opening_image",
            "pressure_trigger",
            "self_awareness",
            "repair_choice",
            "closing_image",
        ],
        "thriller": [
            "opening_image",
            "pressure_trigger",
            "escalation",
            "midpoint_reveal",
            "tactical_choice",
            "containment",
            "closing_image",
        ],
        "romance": [
            "opening_image",
            "pressure_trigger",
            "wound_reveal",
            "misread_intention",
            "vulnerable_return",
            "closing_image",
        ],
    }.get(genre, ["opening_image", "pressure_trigger", "midpoint_shift", "repair_choice", "closing_image"])
    beats = []
    stakes_anchor = _stakes(packet)
    for beat_id, scene in zip(beat_ids, scenes):
        beats.append(
            {
                "beat_id": beat_id,
                "scene_number": scene["scene_number"],
                "story_function": scene["scene_objective"],
                "character_action": scene["action_lines"][0],
                "emotional_state_before": scene["emotional_value_start"],
                "emotional_state_after": scene["emotional_value_end"],
                "stakes_change": f"{stakes_anchor}; {scene['turning_point']}",
            }
        )
    return beats


def _sequence_structure(packet: dict[str, Any], scenes: list[dict[str, Any]]) -> dict[str, Any]:
    genre = _genre(packet)
    if genre == "thriller":
        groups = [(1, 2, "detect the threat"), (3, 5, "contain the threat"), (6, 7, "absorb the consequence")]
    elif genre == "romance":
        groups = [(1, 2, "expose the wound"), (3, 3, "reverse the misunderstanding"), (4, 5, "earn reconnection")]
    else:
        groups = [(1, 2, "fracture the room"), (3, 4, "recognize and repair"), (5, 5, "seal the lesson")]
    sequences = []
    for index, (start, end, objective) in enumerate(groups, start=1):
        selected = [scene for scene in scenes if start <= scene["scene_number"] <= end]
        sequences.append(
            {
                "sequence_id": f"sequence_{index}",
                "objective": objective,
                "function": objective,
                "conflict": selected[0]["conflict"],
                "turning_point": selected[-1]["turning_point"],
                "scene_numbers": [scene["scene_number"] for scene in selected],
                "output_scene_numbers": [scene["scene_number"] for scene in selected],
            }
        )
    return {"sequences": sequences}


def rewrite_packet(packet: dict[str, Any]) -> dict[str, Any]:
    rewritten = deepcopy(packet)
    scenes = _scene_sets(packet)
    rewritten["title"] = _title(packet)
    rewritten["logline"] = _logline(packet)
    rewritten["scene_cards"] = scenes
    rewritten["beat_sheet"] = _beat_sheet(packet, scenes)
    rewritten["sequence_structure"] = _sequence_structure(packet, scenes)
    rewritten.setdefault("act_structure", {})
    rewritten["act_structure"]["scene_mapping"] = {
        "act_one": [scene["scene_number"] for scene in scenes[:2]],
        "act_two": [scene["scene_number"] for scene in scenes[2:-1]],
        "act_three": [scenes[-1]["scene_number"]],
    }
    rewritten["act_structure"]["midpoint_shift_or_reversal"] = scenes[len(scenes) // 2]["turning_point"]
    rewritten["act_structure"]["resolution"] = scenes[-1]["turning_point"]
    rewritten["act_structure"]["stakes_progression"] = {
        "start": scenes[0]["conflict"],
        "middle": scenes[len(scenes) // 2]["conflict"],
        "end": scenes[-1]["conflict"],
    }
    rewritten.setdefault("visual_language", {})
    rewritten["visual_language"]["scene_visual_mapping"] = [
        {
            "scene_number": scene["scene_number"],
            "visual_strategy": scene["visual_plan"]["visual_strategy"],
            "blocking_reason": scene["visual_plan"]["camera_reason"],
            "visual_motif": scene["visual_motif"],
        }
        for scene in scenes
    ]
    rewritten["visual_language"]["visual_metaphor"] = scenes[-1]["visual_motif"]
    rewritten["visual_language"]["emotional_framing"] = f"{_genre(packet)} scenes escalate through physical behavior before explanation"
    rewritten.setdefault("cinematography_plan", {})
    rewritten["cinematography_plan"]["shot_progression"] = [
        {
            "scene_number": scene["scene_number"],
            "shot_type": "close-up" if scene["scene_number"] in {2, 3, len(scenes)} else "medium-wide",
            "camera_reason": scene["visual_plan"]["camera_reason"],
            "shot_intent": scene["visual_plan"]["visual_strategy"],
        }
        for scene in scenes
    ]
    rewritten["cinematography_plan"]["lens_intent"] = {
        "motivational_drama": "stay close enough to catch restraint before it becomes speech",
        "thriller": "move from cramped medium space into tactical close detail as the threat clarifies",
        "romance": "favor intimate mids and reflective close detail that expose distance as spatial behavior",
    }.get(_genre(packet), "story-led cinematic framing")
    rewritten["cinematography_plan"]["camera_movement_motivation"] = scenes[0]["visual_plan"]["camera_reason"]
    rewritten["final_image_line"] = _final_image_line(packet, scenes[-1])
    rewritten["screenplay"] = _screenplay_from_scenes(packet, scenes)
    rewritten["screenplay_body"] = rewritten["screenplay"]
    rewritten["quality_scene_rewrite_metadata"] = {
        "genre": _genre(packet),
        "scene_count": len(scenes),
        "rewrite_intent": {
            "motivational_drama": "quiet domestic repair through action",
            "thriller": "threat escalation through tactical behavior",
            "romance": "relational wound and earned vulnerability through subtext",
        }.get(_genre(packet), "cinematic specificity"),
    }
    return rewritten

"""Structured beat sheet generator for cinema preproduction."""

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


def _beat(
    beat_id: str,
    scene_number: int,
    story_function: str,
    character_action: str,
    before: str,
    after: str,
    stakes_change: str,
) -> dict[str, Any]:
    return {
        "beat_id": beat_id,
        "scene_number": scene_number,
        "story_function": story_function,
        "character_action": character_action,
        "emotional_state_before": before,
        "emotional_state_after": after,
        "stakes_change": stakes_change,
    }


def generate_beat_sheet(parsed: dict[str, Any], character_bible: dict[str, Any]) -> list[dict[str, Any]]:
    main = character_bible["major_characters"][0]["name"]
    second = character_bible["major_characters"][1]["name"]
    setting = parsed["setting"]
    pressure = parsed["pressure_trigger"]
    stakes = parsed["stakes"]
    scale = _story_scale(parsed)

    if scale == "feature":
        if parsed["genre"] == "thriller":
            beats = [
                ("opening_image", 1, "seed instability before the reveal", f"{main} notices a fracture in the safety of {setting}.", "guarded", "watchful", f"{stakes} feels exposed before the threat is named."),
                ("setup", 2, "anchor shared vulnerability", f"{second} keeps the emotional stakes visible while {main} scans for control.", "watchful", "coiled", "The domestic world is now part of the threat geometry."),
                ("pressure_trigger", 3, "turn unease into active danger", f"{pressure.capitalize()} forces the room out of denial.", "coiled", "frightened but controlled", "Private anxiety becomes a public emergency."),
                ("internal_anger", 4, "show fear mutating into force", f"{main} feels fear harden into anger as options narrow.", "frightened but controlled", "split between force and care", "The danger is no longer just external."),
                ("visible_restraint", 5, "use restraint to prevent escalation", f"{main} slows the room instead of matching its panic.", "split between force and care", "tactically contained", "Restraint becomes an active survival choice."),
                ("self_awareness", 6, "recognize the inherited pattern", f"{main} sees how panic could become another legacy inside the family.", "tactically contained", "clear-eyed and burdened", "The threat acquires generational cost."),
                ("midpoint_reversal", 7, "reveal the deeper cost of the wrong move", f"{main} realizes the real danger is what fear will teach the children if he breaks now.", "clear-eyed and burdened", "strategically calm", "The story pivots from crisis response to moral authorship."),
                ("secondary_pressure", 8, "renew external pressure after the insight", f"The consequences of {pressure} intensify before the room can settle.", "strategically calm", "under siege but deliberate", "The new clarity is immediately tested."),
                ("restraint_under_fire", 9, "hold the line under renewed pressure", f"{main} protects the room by narrowing every move to what matters most.", "under siege but deliberate", "disciplined and exact", "Calm now costs effort, not just intention."),
                ("deepened_self_awareness", 10, "turn discipline into connection", f"{main} understands what must be repaired with {second}, not just solved.", "disciplined and exact", "emotionally available", "The story can now move toward trust, not just safety."),
                ("repair_choice", 11, "act on the deeper understanding", f"{main} makes a repair move that protects {stakes} and includes {second}.", "emotionally available", "connected and resolving", "Trust begins to outrun threat."),
                ("closing_image", 12, "land aftermath with earned vigilance", f"The family settles with {stakes} protected and fear no longer running the room.", "connected and resolving", "relieved and vigilant", "Care proves stronger than panic."),
            ]
        elif parsed["genre"] == "romance":
            beats = [
                ("opening_image", 1, "establish closeness already under pressure", f"{main} and {second} move through {setting} with practiced tenderness and hidden strain.", "tired but connected", "tentatively open", f"{stakes} lives inside their shared routine."),
                ("setup", 2, "show the wound inside the ordinary world", f"{main} protects the evening without naming the deeper relational bruise.", "tentatively open", "fragile", "The relationship already carries unsaid debt."),
                ("pressure_trigger", 3, "force intimacy under stress", f"{pressure.capitalize()} makes emotional avoidance impossible.", "fragile", "defensive", "Practical strain now threatens emotional trust."),
                ("internal_anger", 4, "show the anger beneath tenderness", f"{main} feels pride and hurt beginning to replace warmth.", "defensive", "guarded and ashamed", "The romance can now break in a specifically relational way."),
                ("visible_restraint", 5, "stop the scene from hardening into cruelty", f"{main} chooses softness before the hurt becomes another habit.", "guarded and ashamed", "contained but aching", "Restraint preserves the possibility of return."),
                ("self_awareness", 6, "name the hidden wound", f"{main} recognizes what old fear is really driving the distance from {second}.", "contained but aching", "self-aware and exposed", "The conflict becomes intimate rather than procedural."),
                ("midpoint_reversal", 7, "reverse the meaning of the distance", f"{main} realizes the silence is not strength but abandonment seen from {second}'s side.", "self-aware and exposed", "willing to be seen", "The story pivots from self-protection to relational risk."),
                ("secondary_pressure", 8, "let the world press the wound again", f"The shared world demands action before either partner feels fully ready.", "willing to be seen", "unsteady but reaching", "Love must now compete with fear in real time."),
                ("restraint_under_fire", 9, "replace pride with gentleness", f"{main} chooses contact, patience, and listening over being right.", "unsteady but reaching", "soft and brave", "Trust begins to move through behavior."),
                ("deepened_self_awareness", 10, "understand what repair must cost", f"{main} sees that reunion requires yielding a cherished self-protection.", "soft and brave", "ready to risk honesty", "The ending must now be earned through sacrifice."),
                ("repair_choice", 11, "act on vulnerability", f"{main} repairs the evening with an act of care that includes {second} and the children.", "ready to risk honesty", "emotionally reunited", "Love becomes visible through action."),
                ("closing_image", 12, "land intimacy with cost absorbed", f"{second} receives the repair and {stakes} remains safe inside renewed tenderness.", "emotionally reunited", "hopeful and intimate", "Distance resolves through chosen closeness."),
            ]
        else:
            beats = [
                ("opening_image", 1, "establish warmth before pressure", f"{main} enters {setting} gently and reads the room before speaking.", "worn down but contained", "present and attentive", f"{stakes} is visible but not yet endangered by anger."),
                ("setup", 2, "define family stakes and responsibility", f"{main} keeps the room soft while exhaustion and history sit just beneath the surface.", "present and attentive", "quietly responsible", "The home understands he is a caregiver first."),
                ("pressure_trigger", 3, "introduce the testing event", f"{pressure.capitalize()} pushes the family toward a breaking point.", "quietly responsible", "pressure rising fast", "The toddlers become active emotional witnesses."),
                ("internal_anger", 4, "identify the inner rupture", f"{main} feels anger arrive before it reaches his voice or hands.", "pressure rising fast", "self-aware and tense", "The danger shifts from the event to the possible reaction."),
                ("visible_restraint", 5, "interrupt the pattern physically", f"{main} steps away, lowers the temperature of the room, and keeps his voice low.", "self-aware and tense", "contained and deliberately quiet", "The room is protected by visible restraint."),
                ("self_awareness", 6, "understand what the children are learning", f"{main} realizes the toddlers are inheriting whatever he models next.", "contained and deliberately quiet", "clear enough to repair", "The stakes become emotional inheritance."),
                ("midpoint_reversal", 7, "change what the conflict means", f"{main} sees the problem is no longer the mess itself but the kind of memory it could become.", "clear enough to repair", "burdened but lucid", "The story pivots from household stress to legacy."),
                ("secondary_pressure", 8, "renew practical pressure after the insight", f"The practical consequences of {pressure} intensify before the room can reset.", "burdened but lucid", "strained but deliberate", "Insight is tested by fresh pressure."),
                ("restraint_under_fire", 9, "hold the new behavior in motion", f"{main} chooses slow action over inherited speed and sharpness.", "strained but deliberate", "steady under load", "Care now becomes an intentional practice."),
                ("deepened_self_awareness", 10, "translate restraint into readiness to repair", f"{main} knows apology alone is not enough; the room needs a changed action.", "steady under load", "emotionally available", "Repair is defined behaviorally, not verbally."),
                ("repair_choice", 11, "return with action instead of explanation", f"{main} comes back to {second} and the toddlers with care rather than speech.", "emotionally available", "connected and softened", "The family receives repair, not a lecture."),
                ("closing_image", 12, "land earned hope", f"The night closes quietly with {stakes} protected and the home reset through tenderness.", "connected and softened", "hopeful and settled", "Restraint becomes a visible family memory."),
            ]
        return [_beat(*beat) for beat in beats]

    if scale == "expanded":
        if parsed["genre"] == "thriller":
            beats = [
                ("opening_image", 1, "seed instability before the reveal", f"{main} notices something off in {setting}.", "guarded", "watchful", f"{stakes} is vulnerable before anyone admits why."),
                ("setup", 2, "anchor motive and vulnerability", f"{second} keeps the emotional stakes near the surface.", "watchful", "coiled", "The relationship now carries the threat."),
                ("pressure_trigger", 3, "introduce direct threat pressure", f"{pressure.capitalize()} locks the room into a threat response.", "coiled", "frightened but controlled", "What felt private now feels dangerous."),
                ("internal_anger", 4, "show fear mutating into control struggle", f"{main} feels fear harden into anger.", "frightened but controlled", "split between force and care", "The wrong response could widen the threat."),
                ("midpoint_reversal", 5, "reveal the real emotional cost", f"{main} realizes the real danger is what panic will teach the children.", "split between force and care", "strategically calm", "The story pivots from threat reaction to moral choice."),
                ("visible_restraint", 6, "restraint becomes tactical action", f"{main} lowers the energy in the room instead of escalating it.", "strategically calm", "contained and deliberate", "Restraint now becomes the only workable strategy."),
                ("repair_choice", 7, "act on the insight", f"{main} re-enters the room with a precise repair move that includes {second}.", "contained and deliberate", "connected and resolving", "Trust begins to outrun fear."),
                ("closing_image", 8, "land quiet aftermath", f"The room settles with {stakes} protected and the threat converted into caution.", "connected and resolving", "relieved and vigilant", "The final image proves care, not panic, kept the world intact."),
            ]
        elif parsed["genre"] == "romance":
            beats = [
                ("opening_image", 1, "establish emotional closeness under strain", f"{main} and {second} move around each other with practiced affection.", "tired but connected", "tentatively open", f"{stakes} sits between them like shared responsibility."),
                ("setup", 2, "show shared history and pressure", f"{main} tries to protect the moment without naming the deeper fear.", "tentatively open", "fragile", "The relationship already carries unsaid pressure."),
                ("pressure_trigger", 3, "trigger intimacy under stress", f"{pressure.capitalize()} makes avoidance impossible.", "fragile", "defensive", "Distance now threatens more than the practical problem."),
                ("internal_anger", 4, "translate anger into vulnerability risk", f"{main} realizes the anger is covering shame and fear.", "defensive", "self-aware and exposed", "The real risk becomes emotional withdrawal."),
                ("midpoint_reversal", 5, "change what the silence means", f"{main} recognizes how the distance feels from {second}'s side.", "self-aware and exposed", "willing to be seen", "The conflict turns from pride to vulnerability."),
                ("visible_restraint", 6, "use gentleness instead of pride", f"{main} speaks softly and chooses contact over distance.", "willing to be seen", "soft and brave", "The room shifts from argument logic to relational trust."),
                ("repair_choice", 7, "confess and reconnect", f"{main} repairs the moment with an act of care that includes {second} and the children.", "soft and brave", "emotionally reunited", "Love becomes an action, not a line."),
                ("closing_image", 8, "land earned intimacy", f"{second} receives the repair and {stakes} stays safe inside the new tenderness.", "emotionally reunited", "hopeful and intimate", "The ending image resolves distance through care."),
            ]
        else:
            beats = [
                ("opening_image", 1, "establish warmth before pressure", f"{main} enters {setting} softly and notices the children before the problem.", "worn down but contained", "present and attentive", f"{stakes} is visible but not yet threatened by anger."),
                ("setup", 2, "define family stakes and the protagonist's warmth", f"{main} responds with care and keeps the room gentle.", "present and attentive", "quietly responsible", "The room understands that the protagonist is a caregiver first."),
                ("pressure_trigger", 3, "introduce the conflict that tests restraint", f"{pressure.capitalize()} pushes the room toward a breaking point while {second} watches.", "quietly responsible", "pressure rising fast", "The toddlers become active emotional stakes."),
                ("internal_anger", 4, "identify the inner rupture", f"{main} notices anger before it reaches his voice or hands.", "pressure rising fast", "self-aware and tense", "The danger shifts from the event to the protagonist's possible reaction."),
                ("midpoint_reversal", 5, "change what the conflict means", f"{main} realizes the real stakes are what the toddlers will learn from him tonight.", "self-aware and tense", "contained and deliberately quiet", "The story pivots from household problem to emotional inheritance."),
                ("visible_restraint", 6, "show restraint as action", f"{main} steps away, breathes, and keeps his voice low.", "contained and deliberately quiet", "clear enough to repair", "The room is protected because the protagonist interrupts the pattern."),
                ("repair_choice", 7, "turn awareness into repair", f"{main} returns to {second} and the toddlers with care instead of explanation.", "clear enough to repair", "connected and softened", "The family receives action, not a lecture."),
                ("closing_image", 8, "land earned hope", f"The night closes softly with {stakes} protected.", "connected and softened", "hopeful and settled", "The final image proves restraint can become tenderness."),
            ]
        return [_beat(*beat) for beat in beats]

    if parsed["genre"] == "thriller":
        beats = [
            ("opening_image", 1, "seed instability before the reveal", f"{main} notices something off in {setting}.", "guarded", "watchful", f"{stakes} is vulnerable before anyone admits why."),
            ("setup", 1, "anchor motive and vulnerability", f"{second} keeps the emotional stakes near the surface.", "watchful", "coiled", "The relationship now carries the threat."),
            ("pressure_trigger", 2, "introduce direct threat pressure", f"{pressure.capitalize()} locks the room into a threat response.", "coiled", "frightened but controlled", "What felt private now feels dangerous."),
            ("internal_anger", 3, "show fear mutating into control struggle", f"{main} feels fear harden into anger.", "frightened but controlled", "split between force and care", "The wrong response could widen the threat."),
            ("midpoint_reversal", 4, "reveal the real emotional cost", f"{main} realizes the real danger is what panic will teach the children.", "split between force and care", "strategically calm", "The story pivots from threat reaction to moral choice."),
            ("visible_restraint", 4, "restraint becomes tactical action", f"{main} lowers the energy in the room instead of escalating it.", "strategically calm", "contained and deliberate", "Restraint now becomes the only workable strategy."),
            ("repair_choice", 5, "act on the insight", f"{main} re-enters the room with a precise repair move that includes {second}.", "contained and deliberate", "connected and resolving", "Trust begins to outrun fear."),
            ("closing_image", 6, "land quiet aftermath", f"The room settles with {stakes} protected and the threat converted into caution.", "connected and resolving", "relieved and vigilant", "The final image proves care, not panic, kept the world intact."),
        ]
    elif parsed["genre"] == "romance":
        beats = [
            ("opening_image", 1, "establish emotional closeness under strain", f"{main} and {second} move around each other with practiced affection.", "tired but connected", "tentatively open", f"{stakes} sits between them like shared responsibility."),
            ("setup", 1, "show shared history and pressure", f"{main} tries to protect the moment without naming the deeper fear.", "tentatively open", "fragile", "The relationship already carries unsaid pressure."),
            ("pressure_trigger", 2, "trigger intimacy under stress", f"{pressure.capitalize()} makes avoidance impossible.", "fragile", "defensive", "Distance now threatens more than the practical problem."),
            ("internal_anger", 3, "translate anger into vulnerability risk", f"{main} realizes the anger is covering shame and fear.", "defensive", "self-aware and exposed", "The real risk becomes emotional withdrawal."),
            ("self_awareness", 4, "recognize the wound beneath reaction", f"{main} understands what tenderness costs here.", "self-aware and exposed", "willing to be seen", "The relationship can now move toward confession."),
            ("visible_restraint", 5, "use gentleness instead of pride", f"{main} speaks softly and chooses contact over distance.", "willing to be seen", "soft and brave", "The room shifts from argument logic to relational trust."),
            ("repair_choice", 6, "confess and reconnect", f"{main} repairs the moment with an act of care that includes {second} and the children.", "soft and brave", "emotionally reunited", "Love becomes an action, not a line."),
            ("closing_image", 6, "land earned intimacy", f"{second} receives the repair and {stakes} stays safe inside the new tenderness.", "emotionally reunited", "hopeful and intimate", "The ending image resolves distance through care."),
        ]
    else:
        beats = [
            ("opening_image", 1, "establish warmth before pressure", f"{main} enters {setting} softly and notices the children before the problem.", "worn down but contained", "present and attentive", f"{stakes} is visible but not yet threatened by anger."),
            ("setup", 1, "define family stakes and the protagonist's warmth", f"{main} responds with care and keeps the room gentle.", "present and attentive", "quietly responsible", "The room understands that the protagonist is a caregiver first."),
            ("pressure_trigger", 2, "introduce the conflict that tests restraint", f"{pressure.capitalize()} pushes the room toward a breaking point while {second} watches.", "quietly responsible", "pressure rising fast", "The toddlers become active emotional stakes."),
            ("internal_anger", 3, "identify the inner rupture", f"{main} notices anger before it reaches his voice or hands.", "pressure rising fast", "self-aware and tense", "The danger shifts from the event to the protagonist's possible reaction."),
            ("visible_restraint", 4, "show restraint as action", f"{main} steps away, breathes, and keeps his voice low.", "self-aware and tense", "contained and deliberately quiet", "The room is protected because the protagonist interrupts the pattern."),
            ("self_awareness", 5, "convert restraint into understanding", f"{main} names the anger and understands what the toddlers are learning from him.", "contained and deliberately quiet", "clear enough to repair", "The stakes become emotional inheritance, not just a household problem."),
            ("repair_choice", 6, "turn awareness into repair", f"{main} returns to {second} and the toddlers with care instead of explanation.", "clear enough to repair", "connected and softened", "The family receives action, not a lecture."),
            ("closing_image", 6, "land earned hope", f"The night closes softly with {stakes} protected.", "connected and softened", "hopeful and settled", "The final image proves restraint can become tenderness."),
        ]
    return [_beat(*beat) for beat in beats]

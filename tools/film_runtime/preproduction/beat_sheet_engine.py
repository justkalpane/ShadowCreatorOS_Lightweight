"""Structured beat sheet generator for cinema preproduction."""

from __future__ import annotations

from typing import Any


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

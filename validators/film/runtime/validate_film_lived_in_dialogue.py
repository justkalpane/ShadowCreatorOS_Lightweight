from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, result


GENERIC_DIALOGUE = {
    "believe in yourself",
    "never give up",
    "we will be better tomorrow",
    "i feel bad and things are hard",
}


def validate(payload: dict) -> dict:
    data = packet(payload)
    screenplay = data.get("screenplay", "").lower()
    errors = []
    for phrase in GENERIC_DIALOGUE:
        if phrase in screenplay:
            errors.append(f"generic dialogue phrase present: {phrase}")
    if "i feel" in screenplay and "?" not in screenplay and "..." not in screenplay:
        errors.append("dialogue remains too explanatory")
    if not any(term in screenplay for term in ["—", "...", "not polished. just here.", "don't fix", "you smelled it too", "late on purpose", "keep the better piece"]):
        errors.append("dialogue lacks interruption or compression")
    if "therapy" in screenplay or "process my feelings" in screenplay:
        errors.append("therapy-speak present")
    if data.get("genre") == "romance":
        if "first one-room rental" not in screenplay and "blue sugar bowl" not in screenplay and "spare key" not in screenplay:
            errors.append("romance dialogue lacks specific shared history")
        if "i'm sorry" in screenplay and "but" not in screenplay and "instead" not in screenplay:
            errors.append("romance dialogue too clean")
        if "start there. not polished. just here." in screenplay and "keep the better piece" not in screenplay:
            errors.append("romance reconciliation still too composed")
    return result("validate_film_lived_in_dialogue", not errors, errors)

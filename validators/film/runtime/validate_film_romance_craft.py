from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    screenplay = data.get("screenplay", "").lower()
    scenes = data.get("scene_cards") or []
    errors = []

    if data.get("genre") != "romance":
        return result("validate_film_romance_craft", True, [])

    shared_history_terms = ["first one-room rental", "blue sugar bowl", "chipped tea glass", "spare key"]
    if "shame" not in screenplay and "distance" not in screenplay and "late on purpose" not in screenplay:
        errors.append("relational wound exists insufficiently")
    if not any(term in screenplay for term in shared_history_terms):
        errors.append("no specific shared history exists")
    if not any("misread" in str(scene).lower() or "mistaken" in str(scene).lower() or "translate" in str(scene).lower() or "decided for me" in str(scene).lower() for scene in scenes):
        errors.append("misread intention affects no scene")
    confession_index = screenplay.find("distance was easier")
    if confession_index == -1:
        confession_index = screenplay.find("i wasn't hiding")
    if confession_index == -1:
        confession_index = screenplay.find("i kept arriving late")
    if confession_index == -1:
        confession_index = screenplay.find("i was late on purpose")
    if confession_index != -1:
        pre_confession = screenplay[:confession_index]
        if "don't fix the pan" not in pre_confession and "don't rescue the pan" not in pre_confession and "anniversary table" not in pre_confession:
            errors.append("subtext does not appear before confession")
    if "sets the stems in a water glass" not in screenplay and "spare key" not in screenplay:
        errors.append("vulnerability is not shown through action")
    if "spare key" not in screenplay and "keep the better piece" not in screenplay:
        errors.append("reconciliation does not require a cost or choice")
    if "share the glass" not in screenplay and "joined reflection" not in screenplay and "same reflection" not in screenplay:
        errors.append("final image is not specific to the relationship")
    if "you never miss the apology" not in screenplay and "you remembered flowers" not in screenplay:
        errors.append("both characters speak in the same voice")
    if "panic" in screenplay or "toddlers memorize the wrong lesson" in screenplay:
        errors.append("dialogue sounds interchangeable with another lane")
    if "speech to rescue the moment" in screenplay:
        errors.append("final image still too generic")
    return result("validate_film_romance_craft", not errors, errors)

from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    scenes = data.get("scene_cards") or []
    errors = []
    if len(scenes) < 3:
        errors.append("scene embodiment requires at least 3 scenes")
    for idx, scene in enumerate(scenes, start=1):
        actions = scene.get("action_lines") or []
        if not scene.get("location") or len(str(scene.get("location")).split()) < 2:
            errors.append(f"scene {idx} lacks concrete location detail")
        if not actions or len(actions) < 2:
            errors.append(f"scene {idx} lacks specific physical action")
        if not scene.get("conflict"):
            errors.append(f"scene {idx} lacks scene opposition")
        if not scene.get("turning_point"):
            errors.append(f"scene {idx} lacks behavior turn")
        action_text = " ".join(actions).lower()
        if not any(term in action_text for term in ["pause", "wait", "still", "stops", "silence", "quiet", "listen", "holds", "held", "count"]):
            errors.append(f"scene {idx} lacks silence/pause/interruption")
        if not scene.get("dialogue_subtext_goal"):
            errors.append(f"scene {idx} lacks subtextual dialogue goal")
        if not scene.get("visual_motif"):
            errors.append(f"scene {idx} lacks visual beat")
    if data.get("genre") == "romance":
        joined = " ".join(
            " ".join(scene.get("action_lines") or []) + " " + str(scene.get("visual_motif") or "")
            for scene in scenes
        ).lower()
        if not any(term in joined for term in ["reflection", "window fog", "glass", "key", "sugar bowl", "tea glass"]):
            errors.append("romance visual intimacy is generic")
        if "spare key" not in joined:
            errors.append("romance reconciliation has no embodied cost")
    return result("validate_film_scene_embodiment", not errors, errors)

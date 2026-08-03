import sys
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests._f16_helpers import ARTIFACT_ROOT, generate_f16_romance_outputs
from validators.film.runtime import validate_film_lived_in_dialogue, validate_film_romance_craft, validate_film_scene_embodiment


def test_f16_romance_depth_validator():
    output = generate_f16_romance_outputs()
    packet = output["packet"]

    romance_validation = validate_film_romance_craft.validate({"preproduction_packet": packet})
    dialogue_validation = validate_film_lived_in_dialogue.validate({"preproduction_packet": packet})
    embodiment_validation = validate_film_scene_embodiment.validate({"preproduction_packet": packet})

    assert romance_validation["passed"] is True, romance_validation["errors"]
    assert dialogue_validation["passed"] is True, dialogue_validation["errors"]
    assert embodiment_validation["passed"] is True, embodiment_validation["errors"]

    broken = deepcopy(packet)
    broken["screenplay"] = broken["screenplay"].replace("blue sugar bowl", "small bowl")
    broken["screenplay"] = broken["screenplay"].replace("spare key", "folded note")
    broken["final_image_line"] = "FINAL IMAGE: they stand together and feel better."
    broken["scene_cards"][0]["action_lines"][1] = "Ansa moves the pan."
    broken["scene_cards"][2]["dialogue_lines"][1]["line"] = "I understand your feelings."
    broken["scene_cards"][4]["action_lines"][0] = "Mirel stands by the window."
    broken["scene_cards"][4]["visual_motif"] = "night light"
    for scene in broken["scene_cards"]:
        scene["visual_motif"] = "plain room"
        scene["action_lines"] = [line.replace("spare key", "folded note").replace("reflection", "shadow").replace("sugar bowl", "bowl").replace("tea glass", "cup") for line in scene.get("action_lines", [])]

    broken_screenplay = broken["screenplay"].lower()
    broken_screenplay = broken_screenplay.replace("you remembered flowers. you forgot the hour that made them matter.", "i'm sorry i hurt you.")
    broken_screenplay = broken_screenplay.replace(
        "take the spare key back. if i leave again, i want it to be because i said goodbye, not because i vanished neatly.",
        "i'm sorry. let's just try again.",
    )
    broken["screenplay"] = broken_screenplay
    broken["screenplay"] += "\nI feel bad and things are hard.\nWe will be better tomorrow.\n"

    failed_romance = validate_film_romance_craft.validate({"preproduction_packet": broken})
    failed_dialogue = validate_film_lived_in_dialogue.validate({"preproduction_packet": broken})
    failed_embodiment = validate_film_scene_embodiment.validate({"preproduction_packet": broken})

    assert failed_romance["passed"] is False, "generic_romance_dialogue/no_shared_history/no_visual_intimacy/clean_reconciliation_without_cost/same_voice_both_characters/final_image_not_romance_specific should fail"
    assert failed_dialogue["passed"] is False, "generic romance lived-in dialogue failure expected"
    assert failed_embodiment["passed"] is False, "generic romance embodiment failure expected"

    assert (ARTIFACT_ROOT / "romance_revised_screenplay.md").exists()
    assert output["human_score"]["overall_human_readable_quality"] >= 6.5, output["human_score"]


if __name__ == "__main__":
    test_f16_romance_depth_validator()
    print("phase_13d_f16_romance_depth_validator_ok")

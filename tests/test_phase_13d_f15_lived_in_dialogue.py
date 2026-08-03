import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests._f15_helpers import generate_f15_outputs, write_report
from validators.film.runtime import validate_film_lived_in_dialogue, validate_film_romance_craft


def test_f15_lived_in_dialogue():
    outputs = generate_f15_outputs()
    report = {}
    for label, output in outputs.items():
        packet = output["packet"]
        validation = validate_film_lived_in_dialogue.validate({"preproduction_packet": packet})
        assert validation["passed"] is True, f"{label}: {validation['errors']}"
        report[label] = {"dialogue_validation": validation}
    romance_validation = validate_film_romance_craft.validate({"preproduction_packet": outputs["romance"]["packet"]})
    assert romance_validation["passed"] is True, romance_validation["errors"]
    report["romance"]["romance_craft_validation"] = romance_validation
    write_report("f15_dialogue_quality_report", report)


if __name__ == "__main__":
    test_f15_lived_in_dialogue()
    print("phase_13d_f15_lived_in_dialogue_ok")

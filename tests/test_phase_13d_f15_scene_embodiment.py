import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests._f15_helpers import generate_f15_outputs, write_report
from validators.film.runtime import validate_film_scene_embodiment


def test_f15_scene_embodiment():
    outputs = generate_f15_outputs()
    report = {}
    for label, output in outputs.items():
        validation = validate_film_scene_embodiment.validate({"preproduction_packet": output["packet"]})
        assert validation["passed"] is True, f"{label}: {validation['errors']}"
        report[label] = validation
    write_report("f15_scene_embodiment_report", report)


if __name__ == "__main__":
    test_f15_scene_embodiment()
    print("phase_13d_f15_scene_embodiment_ok")

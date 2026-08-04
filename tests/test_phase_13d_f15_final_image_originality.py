import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests._f15_helpers import generate_f15_outputs, write_report
from validators.film.runtime import validate_film_final_image_originality


def test_f15_final_image_originality():
    outputs = generate_f15_outputs()
    packets = [output["packet"] for output in outputs.values()]
    validation = validate_film_final_image_originality.validate({"packets": packets})
    assert validation["passed"] is True, validation["errors"]
    write_report(
        "f15_final_image_originality_report",
        {
            "motivational_final_image": outputs["motivational"]["packet"]["final_image_line"],
            "thriller_final_image": outputs["thriller"]["packet"]["final_image_line"],
            "romance_final_image": outputs["romance"]["packet"]["final_image_line"],
            "validation": validation,
        },
    )


if __name__ == "__main__":
    test_f15_final_image_originality()
    print("phase_13d_f15_final_image_originality_ok")

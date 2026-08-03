import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests._f15_helpers import generate_f15_outputs, write_report
from validators.film.runtime import validate_film_lane_voice_differentiation


def test_f15_lane_voice_differentiation():
    outputs = generate_f15_outputs()
    packets = [output["packet"] for output in outputs.values()]
    validation = validate_film_lane_voice_differentiation.validate({"packets": packets})
    assert validation["passed"] is True, validation["errors"]
    write_report(
        "f15_cross_lane_voice_report",
        {
            "motivational_voice": outputs["motivational"]["packet"]["quality_revision_metadata"]["rewrite_strategy"],
            "thriller_voice": outputs["thriller"]["packet"]["quality_revision_metadata"]["rewrite_strategy"],
            "romance_voice": outputs["romance"]["packet"]["quality_revision_metadata"]["rewrite_strategy"],
            "validation": validation,
        },
    )


if __name__ == "__main__":
    test_f15_lane_voice_differentiation()
    print("phase_13d_f15_lane_voice_differentiation_ok")

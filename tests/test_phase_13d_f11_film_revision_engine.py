import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.quality.film_quality_benchmark_utils import build_weak_packet_from_fixture, run_existing_validator_suite
from tools.film_runtime.quality.film_quality_score_engine import score_packet
from tools.film_runtime.quality.film_revision_engine import revise_packet
from validators.film.runtime import validate_film_revision_delta
from validators.film.runtime import validate_film_revised_packet_improvement


FIXTURES = [
    ROOT / "tests/fixtures/film/f11_weak_motivational_drama.json",
    ROOT / "tests/fixtures/film/f11_weak_thriller_short.json",
    ROOT / "tests/fixtures/film/f11_weak_romance_drama.json",
]


def test_revision_engine():
    for fixture_path in FIXTURES:
        weak_packet, _ = build_weak_packet_from_fixture(fixture_path)
        original_score = score_packet(weak_packet)
        revision = revise_packet(weak_packet, original_score)
        revised_packet = revision["revised_preproduction_packet"]
        revised_score = score_packet(revised_packet)
        delta_validation = validate_film_revision_delta.validate({"revision_delta_report": revision["revision_delta_report"]})
        assert delta_validation["passed"] is True, delta_validation["errors"]
        improvement_validation = validate_film_revised_packet_improvement.validate(
            {
                "original_quality_score": original_score,
                "revised_quality_score": revised_score,
                "validator_results": run_existing_validator_suite(revised_packet),
                "revision_delta_report": revision["revision_delta_report"],
                "revised_preproduction_packet": revised_packet,
            }
        )
        assert improvement_validation["passed"] is True, improvement_validation["errors"]


if __name__ == "__main__":
    test_revision_engine()
    print("phase_13d_f11_film_revision_engine_ok")


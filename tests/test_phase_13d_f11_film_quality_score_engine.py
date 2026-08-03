import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.quality.film_quality_benchmark_utils import build_weak_packet_from_fixture
from tools.film_runtime.quality.film_quality_score_engine import score_packet
from validators.film.runtime import validate_film_quality_score


FIXTURES = [
    ROOT / "tests/fixtures/film/f11_weak_motivational_drama.json",
    ROOT / "tests/fixtures/film/f11_weak_thriller_short.json",
    ROOT / "tests/fixtures/film/f11_weak_romance_drama.json",
]


def test_quality_score_engine():
    for fixture_path in FIXTURES:
        weak_packet, _ = build_weak_packet_from_fixture(fixture_path)
        report = score_packet(weak_packet)
        assert report["overall_score"] <= 5.0, fixture_path.name
        validation = validate_film_quality_score.validate({"quality_score_report": report, "expect_weak": True})
        assert validation["passed"] is True, validation["errors"]


if __name__ == "__main__":
    test_quality_score_engine()
    print("phase_13d_f11_film_quality_score_engine_ok")


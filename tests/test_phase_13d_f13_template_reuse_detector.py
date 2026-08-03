import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.quality.film_quality_benchmark_utils import build_weak_packet_from_fixture
from tools.film_runtime.quality.film_quality_score_engine import score_packet
from tools.film_runtime.quality.film_revision_engine import revise_packet
from validators.film.runtime import validate_film_template_reuse


FIXTURES = {
    "motivational": ROOT / "tests/fixtures/film/f11_weak_motivational_drama.json",
    "thriller": ROOT / "tests/fixtures/film/f11_weak_thriller_short.json",
    "romance": ROOT / "tests/fixtures/film/f11_weak_romance_drama.json",
}


def test_f13_template_reuse_detector():
    packets = []
    for fixture_path in FIXTURES.values():
        weak_packet, _ = build_weak_packet_from_fixture(fixture_path)
        packets.append(revise_packet(weak_packet, score_packet(weak_packet))["revised_preproduction_packet"])

    pass_validation = validate_film_template_reuse.validate({"packets": packets})
    assert pass_validation["passed"] is True, pass_validation["errors"]

    copied_packets = [dict(packet) for packet in packets[:2]]
    copied_packets.append(dict(packets[0]))
    copied_packets[2]["genre"] = "romance"
    fail_validation = validate_film_template_reuse.validate({"packets": copied_packets})
    assert fail_validation["passed"] is False


if __name__ == "__main__":
    test_f13_template_reuse_detector()
    print("phase_13d_f13_template_reuse_detector_ok")

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.quality.film_quality_benchmark_utils import (
    QUALITY_ARTIFACT_ROOT,
    build_weak_packet_from_fixture,
    markdown_from_mapping,
    write_json,
    write_text,
)
from tools.film_runtime.quality.film_quality_score_engine import score_packet
from tools.film_runtime.quality.film_revision_engine import revise_packet
from validators.film.runtime import validate_film_template_reuse


FIXTURES = {
    "motivational": ROOT / "tests/fixtures/film/f11_weak_motivational_drama.json",
    "thriller": ROOT / "tests/fixtures/film/f11_weak_thriller_short.json",
    "romance": ROOT / "tests/fixtures/film/f11_weak_romance_drama.json",
}

RUN_DIR = QUALITY_ARTIFACT_ROOT / "f13_quality_calibration_latest"


def test_f13_non_template_revision():
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    packets = []
    summary = {}
    for label, fixture_path in FIXTURES.items():
        weak_packet, _ = build_weak_packet_from_fixture(fixture_path)
        revision = revise_packet(weak_packet, score_packet(weak_packet))
        packet = revision["revised_preproduction_packet"]
        packets.append(packet)
        summary[label] = {
            "scene_count": len(packet.get("scene_cards", [])),
            "midpoint": packet.get("act_structure", {}).get("midpoint_shift_or_reversal"),
            "rewrite_strategy": packet.get("quality_revision_metadata", {}).get("rewrite_strategy"),
            "first_objective": (packet.get("scene_cards") or [{}])[0].get("scene_objective"),
        }

    validation = validate_film_template_reuse.validate({"packets": packets})
    assert validation["passed"] is True, validation["errors"]

    counts = [summary[label]["scene_count"] for label in summary]
    assert len(set(counts)) > 1
    assert "domestic micro-action" in summary["motivational"]["rewrite_strategy"]
    assert "threat escalation" in summary["thriller"]["rewrite_strategy"]
    assert "relational wound" in summary["romance"]["rewrite_strategy"]

    write_json(RUN_DIR / "f13_template_reuse_report.json", {"summary": summary, "validation": validation})
    write_text(
        RUN_DIR / "f13_template_reuse_report.md",
        markdown_from_mapping("F13 Template Reuse Report", {"summary": summary, "validation": validation}),
    )


if __name__ == "__main__":
    test_f13_non_template_revision()
    print("phase_13d_f13_non_template_revision_ok")

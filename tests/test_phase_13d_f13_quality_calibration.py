import json
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
from validators.film.runtime import validate_film_human_score_alignment


FIXTURES = {
    "motivational": ROOT / "tests/fixtures/film/f11_weak_motivational_drama.json",
    "thriller": ROOT / "tests/fixtures/film/f11_weak_thriller_short.json",
    "romance": ROOT / "tests/fixtures/film/f11_weak_romance_drama.json",
}

F12_BASELINE_ROOTS = {
    "motivational": ROOT / "artifacts/film_quality_proof/20260803_182805_motivational/revised_quality_score.json",
    "thriller": ROOT / "artifacts/film_quality_proof/20260803_182805_thriller/revised_quality_score.json",
    "romance": ROOT / "artifacts/film_quality_proof/20260803_182805_romance/revised_quality_score.json",
}

RUN_DIR = QUALITY_ARTIFACT_ROOT / "f13_quality_calibration_latest"


def test_f13_quality_calibration():
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    report = {}
    for label, fixture_path in FIXTURES.items():
        weak_packet, _ = build_weak_packet_from_fixture(fixture_path)
        weak_score = score_packet(weak_packet)
        revision = revise_packet(weak_packet, weak_score)
        revised_packet = revision["revised_preproduction_packet"]
        revised_score = score_packet(revised_packet)
        validation = validate_film_human_score_alignment.validate(
            {
                "quality_score_report": revised_score,
                "preproduction_packet": revised_packet,
                "estimated_human_score": revised_score["estimated_human_score"],
            }
        )
        assert validation["passed"] is True, validation["errors"]
        assert revised_score["overall_score"] > weak_score["overall_score"], label
        baseline = json.loads(F12_BASELINE_ROOTS[label].read_text())
        assert revised_score["overall_score"] <= revised_score["estimated_human_score"] + 1.5, label
        baseline_template_hits = len((baseline.get("template_signals") or {}).get("template_phrase_hits", {}))
        revised_template_hits = len((revised_score.get("template_signals") or {}).get("template_phrase_hits", {}))
        if baseline_template_hits:
            assert revised_template_hits <= baseline_template_hits, label
        report[label] = {
            "engine_score_before": baseline["overall_score"],
            "engine_score_after_calibration": revised_score["overall_score"],
            "estimated_human_score": revised_score["estimated_human_score"],
            "template_reuse_before": "shared six-scene cadence",
            "template_reuse_after": revised_score["template_signals"],
            "scene_vividness_before": baseline["score_dimensions"].get("visual_motivation"),
            "scene_vividness_after": revised_score["score_dimensions"]["scene_vividness"],
            "dialogue_subtext_before": baseline["score_dimensions"].get("dialogue_subtext"),
            "dialogue_subtext_after": revised_score["score_dimensions"]["dialogue_subtext_depth"],
            "visual_embodiment_before": baseline["score_dimensions"].get("visual_motivation"),
            "visual_embodiment_after": revised_score["score_dimensions"]["visual_embodiment"],
        }

    write_json(RUN_DIR / "f13_quality_calibration_report.json", report)
    write_text(RUN_DIR / "f13_quality_calibration_report.md", markdown_from_mapping("F13 Quality Calibration Report", report))


if __name__ == "__main__":
    test_f13_quality_calibration()
    print("phase_13d_f13_quality_calibration_ok")

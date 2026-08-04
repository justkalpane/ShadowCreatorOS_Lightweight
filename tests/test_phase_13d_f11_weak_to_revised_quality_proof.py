import json
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.quality.film_quality_benchmark_utils import (
    QUALITY_ARTIFACT_ROOT,
    build_weak_packet_from_fixture,
    markdown_from_mapping,
    run_existing_validator_suite,
    write_json,
    write_text,
)
from tools.film_runtime.quality.film_quality_score_engine import render_quality_score_markdown, score_packet
from tools.film_runtime.quality.film_revision_engine import render_revision_delta_markdown, revise_packet
from validators.film.runtime import validate_film_quality_score
from validators.film.runtime import validate_film_revision_delta
from validators.film.runtime import validate_film_revised_packet_improvement


FIXTURES = {
    "motivational": ROOT / "tests/fixtures/film/f11_weak_motivational_drama.json",
    "thriller": ROOT / "tests/fixtures/film/f11_weak_thriller_short.json",
    "romance": ROOT / "tests/fixtures/film/f11_weak_romance_drama.json",
}


def _artifact_dir(label: str) -> Path:
    return QUALITY_ARTIFACT_ROOT / f"{time.strftime('%Y%m%d_%H%M%S')}_{label}"


def _write_fixture_artifacts(run_dir: Path, original_packet: dict, original_score: dict, revision: dict, revised_score: dict, improvement_report: dict) -> None:
    run_dir.mkdir(parents=True, exist_ok=True)
    write_json(run_dir / "original_preproduction_packet.json", original_packet)
    write_text(run_dir / "original_screenplay.md", original_packet["screenplay"])
    write_json(run_dir / "original_quality_score.json", original_score)
    write_text(run_dir / "original_quality_score.md", render_quality_score_markdown("Original Quality Score", original_score))
    write_json(run_dir / "revision_strategy.json", revision["revision_strategy"])
    write_text(run_dir / "revision_strategy.md", markdown_from_mapping("Revision Strategy", revision["revision_strategy"]))
    write_json(run_dir / "revised_preproduction_packet.json", revision["revised_preproduction_packet"])
    write_text(run_dir / "revised_screenplay.md", revision["revised_preproduction_packet"]["screenplay"])
    write_json(run_dir / "revised_quality_score.json", revised_score)
    write_text(run_dir / "revised_quality_score.md", render_quality_score_markdown("Revised Quality Score", revised_score))
    write_json(run_dir / "revision_delta_report.json", revision["revision_delta_report"])
    write_text(run_dir / "revision_delta_report.md", render_revision_delta_markdown("Revision Delta Report", revision["revision_delta_report"]))
    write_json(run_dir / "improvement_validation_report.json", improvement_report)
    write_text(run_dir / "execution.log", "F11 weak-to-revised proof executed locally.\n")


def test_weak_to_revised_quality_proof():
    summary = {}
    artifact_roots = {}
    for label, fixture_path in FIXTURES.items():
        original_packet, _ = build_weak_packet_from_fixture(fixture_path)
        original_score = score_packet(original_packet)
        quality_validation = validate_film_quality_score.validate({"quality_score_report": original_score, "expect_weak": True})
        assert quality_validation["passed"] is True, quality_validation["errors"]

        revision = revise_packet(original_packet, original_score)
        revised_packet = revision["revised_preproduction_packet"]
        revised_score = score_packet(revised_packet)
        validator_results = run_existing_validator_suite(revised_packet)

        delta_validation = validate_film_revision_delta.validate({"revision_delta_report": revision["revision_delta_report"]})
        assert delta_validation["passed"] is True, delta_validation["errors"]

        improvement_validation = validate_film_revised_packet_improvement.validate(
            {
                "original_quality_score": original_score,
                "revised_quality_score": revised_score,
                "validator_results": validator_results,
                "revision_delta_report": revision["revision_delta_report"],
                "revised_preproduction_packet": revised_packet,
            }
        )
        assert improvement_validation["passed"] is True, improvement_validation["errors"]
        run_dir = _artifact_dir(label)
        artifact_roots[label] = str(run_dir)
        _write_fixture_artifacts(run_dir, original_packet, original_score, revision, revised_score, improvement_validation)
        summary[label] = {
            "artifact_root": str(run_dir),
            "original_score": original_score["overall_score"],
            "revised_score": revised_score["overall_score"],
            "original_band": original_score["quality_band"],
            "revised_band": revised_score["quality_band"],
            "defects_before": original_score["defect_list"],
            "defects_after": revised_score["defect_list"],
        }
        assert revised_score["overall_score"] > original_score["overall_score"], label

    combined = {
        "artifact_roots": artifact_roots,
        "summary": summary,
        "all_revisions_improved": all(item["revised_score"] > item["original_score"] for item in summary.values()),
        "top_defects_reduced": all(len(item["defects_after"]) < len(item["defects_before"]) for item in summary.values()),
    }
    latest_dir = max((Path(path) for path in artifact_roots.values()), key=lambda p: p.name)
    write_json(latest_dir / "f11_quality_benchmark_summary.json", combined)
    write_text(latest_dir / "f11_quality_benchmark_summary.md", markdown_from_mapping("F11 Quality Benchmark Summary", combined))


if __name__ == "__main__":
    test_weak_to_revised_quality_proof()
    print("phase_13d_f11_weak_to_revised_quality_proof_ok")

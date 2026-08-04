import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"
ARTIFACT_ROOT = ROOT / "artifacts/film_runtime_proof"
PAYLOADS = {
    "motivational_drama": ROOT / "tests/fixtures/film/f9_payload_motivational_drama.json",
    "thriller": ROOT / "tests/fixtures/film/f9_payload_thriller_short.json",
    "romance": ROOT / "tests/fixtures/film/f9_payload_romance_drama.json",
}


def run_runner(payload_path: Path, output_root: Path) -> dict:
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--payload", str(payload_path), "--output-root", str(output_root)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_comparison_report(output_dir: Path, comparison: dict) -> None:
    (output_dir / "f9_multi_payload_comparison.json").write_text(json.dumps(comparison, indent=2) + "\n", encoding="utf-8")
    lines = ["# F9 Multi Payload Comparison", ""]
    for name, details in comparison["payloads"].items():
        lines.append(f"## {name}")
        for key, value in details.items():
            lines.append(f"- {key}: {value}")
        lines.append("")
    (output_dir / "f9_multi_payload_comparison.md").write_text("\n".join(lines), encoding="utf-8")


def test_multi_payload_cinema_depth(output_root: Path = ARTIFACT_ROOT):
    runs = {}
    packets = {}
    for genre, payload_path in PAYLOADS.items():
        summary = run_runner(payload_path, output_root)
        assert summary["status"] == "PASS_RUNTIME_ARTIFACT_PROVEN"
        artifact_root = Path(summary["artifact_root"])
        runs[genre] = artifact_root
        packets[genre] = load_json(artifact_root / "preproduction_packet.json")

    assert len({packets[name]["genre_grammar_report"]["genre"] for name in packets}) == 3
    assert len({packets[name]["character_arc"]["transformation_end"] for name in packets}) == 3
    assert len({json.dumps(packets[name]["world_bible"], sort_keys=True) for name in packets}) == 3
    assert len({json.dumps(packets[name]["visual_language"], sort_keys=True) for name in packets}) == 3
    assert len({json.dumps(packets[name]["cinematography_plan"], sort_keys=True) for name in packets}) == 3
    assert all(packets[name]["mode"] == "script_only" for name in packets)
    assert all(packets[name]["route"] == "FILM_SCREENPLAY_GENERATION" for name in packets)
    assert all((packets[name]["downstream_adapter_boundary"]["media_provider_triggered"] is False) for name in packets)

    comparison = {
        "payloads": {
            name: {
                "artifact_root": str(runs[name]),
                "genre": packets[name]["genre_grammar_report"]["genre"],
                "character_arc_end": packets[name]["character_arc"]["transformation_end"],
                "world_type": packets[name]["world_bible"]["world_type"],
                "visual_grammar": packets[name]["visual_language"]["visual_grammar"],
                "lens_intent": packets[name]["cinematography_plan"]["lens_intent"],
            }
            for name in packets
        }
    }
    latest_output = max(runs.values(), key=lambda p: p.name)
    write_comparison_report(latest_output, comparison)


if __name__ == "__main__":
    test_multi_payload_cinema_depth()
    print("phase_13d_f9_multi_payload_cinema_depth_ok")

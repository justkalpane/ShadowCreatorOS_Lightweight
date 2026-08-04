import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"
PAYLOADS = {
    "motivational_drama": ROOT / "tests/fixtures/film/f23_positive_feature_motivational_drama_depth.json",
    "thriller": ROOT / "tests/fixtures/film/f23_positive_thriller_escalating_threat_depth.json",
    "romance": ROOT / "tests/fixtures/film/f23_positive_romance_relationship_change_depth.json",
}

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.quality.film_quality_score_engine import score_packet


def _run_runner(payload: Path, output_root: Path) -> dict:
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--payload", str(payload), "--output-root", str(output_root)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    summary = json.loads(result.stdout)
    return json.loads(Path(summary["screenplay_packet_path"]).read_text(encoding="utf-8"))


def test_f23_quality_score_depth(tmp_path):
    packets = {
        genre: _run_runner(path, tmp_path / genre)
        for genre, path in PAYLOADS.items()
    }

    scores = {genre: score_packet(packet) for genre, packet in packets.items()}
    assert scores["motivational_drama"]["overall_score"] >= 6.8
    assert scores["thriller"]["overall_score"] >= 6.8
    assert scores["romance"]["overall_score"] >= 6.8

    weak_packet = deepcopy(packets["motivational_drama"])
    weak_packet["screenplay"] = "Someone has a hard day. They want to be better. Everything is probably fine now."
    weak_packet["scene_cards"] = weak_packet["scene_cards"][:3]
    weak_packet["beat_sheet"] = weak_packet["beat_sheet"][:3]
    weak_packet["cinema_depth_packet"]["emotional_depth"]["flatline_risk_flags"] = ["flat emotional repetition"]
    weak_packet["cinema_depth_packet"]["character_depth"]["arc_completion_status"] = False
    weak_packet["cinema_depth_packet"]["dialogue_depth"]["same_voice_risk_flags"] = ["voices match"]
    weak_packet["cinema_depth_packet"]["feature_density"]["feature_thinness_flags"] = ["feature too thin"]
    weak_packet["genre_grammar_report"]["passed"] = False
    weak_score = score_packet(weak_packet)
    assert weak_score["overall_score"] <= 5.5

    thin_packet = deepcopy(packets["motivational_drama"])
    thin_packet["cinema_depth_packet"]["feature_density"]["feature_thinness_flags"] = ["feature too thin"]
    thin_packet["cinema_depth_packet"]["feature_density"]["actual_sub_scene_count"] = 12
    thin_packet["cinema_depth_packet"]["feature_density"]["minimum_scene_count_required"] = 36
    thin_score = score_packet(thin_packet)
    assert thin_score["overall_score"] <= 5.2


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp:
        test_f23_quality_score_depth(Path(tmp))
    print("phase_13d_f23_quality_score_depth_ok")

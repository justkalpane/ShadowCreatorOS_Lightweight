import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.film_runtime.quality.film_quality_benchmark_utils import (
    QUALITY_ARTIFACT_ROOT,
    generate_runtime_packet_from_payload,
    markdown_from_mapping,
    write_json,
    write_text,
)
from tools.film_runtime.quality.scene_rewrite_engine import rewrite_packet


FIXTURE = ROOT / "tests/fixtures/film/f11_weak_thriller_short.json"
RUN_DIR = QUALITY_ARTIFACT_ROOT / "f13_quality_calibration_latest"


def test_f13_scene_rewrite_engine():
    payload = __import__("json").loads(FIXTURE.read_text())["payload"]
    packet = generate_runtime_packet_from_payload(payload)
    rewritten = rewrite_packet(packet)

    assert rewritten["screenplay"] != packet["screenplay"]
    assert len(rewritten.get("scene_cards", [])) >= 5
    for card in rewritten["scene_cards"]:
        assert card["scene_objective"]
        assert card["conflict"]
        assert card["turning_point"]
        assert card["dialogue_subtext_goal"]
        assert card["visual_plan"]["visual_strategy"]
        assert card["action_lines"]
        assert card["dialogue_lines"]

    comparison = {
        "before_scene_count": len(packet.get("scene_cards", [])),
        "after_scene_count": len(rewritten.get("scene_cards", [])),
        "before_midpoint": packet.get("act_structure", {}).get("midpoint_shift_or_reversal"),
        "after_midpoint": rewritten.get("act_structure", {}).get("midpoint_shift_or_reversal"),
        "before_screenplay_tail": packet["screenplay"].splitlines()[-2:],
        "after_screenplay_tail": rewritten["screenplay"].splitlines()[-2:],
    }
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    write_json(RUN_DIR / "f13_scene_rewrite_comparison.json", comparison)
    write_text(RUN_DIR / "f13_scene_rewrite_comparison.md", markdown_from_mapping("F13 Scene Rewrite Comparison", comparison))


if __name__ == "__main__":
    test_f13_scene_rewrite_engine()
    print("phase_13d_f13_scene_rewrite_engine_ok")

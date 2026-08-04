import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.cinema_depth.validate_scene_logic_depth import validate


packet = {
    "cinema_depth_packet": {
        "scene_logic_depth": {
            "scene_logic_map": [
                {"scene_number": 1, "objective": "x", "conflict": "same conflict repeated", "turning_point": "t1", "consequence": "c1"},
                {"scene_number": 2, "objective": "x2", "conflict": "same conflict repeated", "turning_point": "t2", "consequence": "c2"},
                {"scene_number": 3, "objective": "x3", "conflict": "same conflict repeated", "turning_point": "t3", "consequence": "c3"},
            ],
            "duplicate_conflict_flags": ["scene 3 repeats conflict pattern too often: same conflict repeated"],
            "summary_scene_flags": [],
            "cause_effect_links": [{"a": 1}, {"a": 2}],
        }
    }
}
result = validate({"screenplay_packet": packet})
assert result["passed"] is False
print("phase_13d_f23_same_conflict_reused_across_scenes_should_fail_ok")

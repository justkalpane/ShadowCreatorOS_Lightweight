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
                {"scene_number": 1, "objective": "x", "conflict": "y", "turning_point": "", "consequence": "z"},
                {"scene_number": 2, "objective": "x2", "conflict": "y2", "turning_point": "t2", "consequence": "z2"},
                {"scene_number": 3, "objective": "x3", "conflict": "y3", "turning_point": "t3", "consequence": "z3"},
            ],
            "duplicate_conflict_flags": [],
            "summary_scene_flags": [],
            "cause_effect_links": [{"a": 1}, {"a": 2}],
        }
    }
}
result = validate({"screenplay_packet": packet})
assert result["passed"] is False
print("phase_13d_f23_scene_card_without_turning_point_should_fail_ok")

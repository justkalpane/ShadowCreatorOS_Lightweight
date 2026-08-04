import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.cinema_depth.validate_emotional_escalation import validate


packet = {
    "cinema_depth_packet": {
        "emotional_depth": {
            "scene_emotional_state": [{"scene_number": 1}, {"scene_number": 2}, {"scene_number": 3}],
            "emotional_turning_points": [{"scene_number": 1}],
            "flatline_risk_flags": [],
            "act_emotional_progression": {
                "act_one": {"flatline": False},
                "act_two": {"flatline": True},
                "act_three": {"flatline": False},
            },
        }
    }
}
result = validate({"screenplay_packet": packet})
assert result["passed"] is False
print("phase_13d_f23_act_two_without_midpoint_should_fail_ok")

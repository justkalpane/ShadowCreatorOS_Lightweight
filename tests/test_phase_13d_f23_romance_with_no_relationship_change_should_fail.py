import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.cinema_depth.validate_character_arc_progression import validate


packet = {
    "cinema_depth_packet": {
        "character_depth": {
            "character_arc_map": {
                "transformation_start": "guarded",
                "transformation_end": "guarded",
            },
            "want_need_gap": True,
            "flaw_pressure_points": [1],
            "decision_progression": [
                {"scene_number": 1, "behavior_shift": False},
                {"scene_number": 2, "behavior_shift": False},
                {"scene_number": 3, "behavior_shift": False},
            ],
        }
    }
}
result = validate({"screenplay_packet": packet})
assert result["passed"] is False
print("phase_13d_f23_romance_with_no_relationship_change_should_fail_ok")

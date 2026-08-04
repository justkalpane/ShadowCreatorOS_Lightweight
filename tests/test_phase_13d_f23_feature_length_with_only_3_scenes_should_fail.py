import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.cinema_depth.validate_feature_length_density import validate


packet = {
    "format_family": "feature_film",
    "cinema_depth_packet": {
        "feature_density": {
            "actual_scene_count": 3,
            "actual_sub_scene_count": 0,
            "sequence_density_score": 0.4,
            "feature_thinness_flags": [],
        }
    },
}
result = validate({"screenplay_packet": packet})
assert result["passed"] is False
print("phase_13d_f23_feature_length_with_only_3_scenes_should_fail_ok")

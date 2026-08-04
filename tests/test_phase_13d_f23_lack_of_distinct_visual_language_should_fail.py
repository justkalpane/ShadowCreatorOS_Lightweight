import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.cinema_depth.validate_genre_differentiation import validate


packet = {
    "cinema_depth_packet": {
        "genre_depth": {
            "genre_required_turns": ["belief tested", "midpoint self-recognition", "repair through action"],
            "genre_pacing_profile": {"turn_density": 0.3},
            "genre_failure_flags": [],
        }
    }
}
result = validate({"screenplay_packet": packet})
assert result["passed"] is False
print("phase_13d_f23_lack_of_distinct_visual_language_should_fail_ok")

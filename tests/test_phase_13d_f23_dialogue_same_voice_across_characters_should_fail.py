import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.cinema_depth.validate_dialogue_voice_subtext import validate


packet = {
    "cinema_depth_packet": {
        "dialogue_depth": {
            "character_voice_fingerprints": {"A": {}, "B": {}},
            "subtext_map": [{"scene_number": 1}, {"scene_number": 2}],
            "same_voice_risk_flags": ["A and B sound interchangeable"],
            "generic_dialogue_flags": [],
            "exposition_dump_flags": [],
        }
    }
}
result = validate({"screenplay_packet": packet})
assert result["passed"] is False
print("phase_13d_f23_dialogue_same_voice_across_characters_should_fail_ok")

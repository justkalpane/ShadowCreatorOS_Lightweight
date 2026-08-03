import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests._f15_helpers import ARTIFACT_ROOT, generate_f15_outputs


def test_f15_character_identity_preservation():
    outputs = generate_f15_outputs()
    for label, output in outputs.items():
        packet = output["packet"]
        payload = packet["quality_benchmark_source_payload"]
        screenplay = packet["screenplay"]
        assert payload["main_character_name"] in screenplay
        assert payload["second_character_name"] in screenplay
        if payload["main_character_name"] != "Ari":
            assert "Ari " not in screenplay
        if payload["second_character_name"] != "Mina":
            assert "Mina " not in screenplay
        assert packet["title"] and "domestic interior" not in packet["title"].lower()
        first_slugline = packet["scene_cards"][0]["slugline"].lower()
        assert payload["setting"].split()[0].lower() in first_slugline or payload["setting"].split()[0].lower() in packet["scene_cards"][0]["location"].lower()
    assert ARTIFACT_ROOT.exists()


if __name__ == "__main__":
    test_f15_character_identity_preservation()
    print("phase_13d_f15_character_identity_preservation_ok")

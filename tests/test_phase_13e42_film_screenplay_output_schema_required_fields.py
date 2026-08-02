import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/film/output_packet/film_screenplay_output_packet.schema.json"

EXPECTED_REQUIRED_FIELDS = {
    "route_state_capsule",
    "film_intent_lock",
    "logline",
    "theme",
    "premise",
    "genre",
    "tone",
    "protagonist_want",
    "protagonist_need",
    "protagonist_flaw",
    "protagonist_arc",
    "opposing_force",
    "beat_sheet",
    "scene_dramaturgy_map",
    "dialogue_subtext_pass",
    "visual_motif_system",
    "style_bible",
    "screenplay_body",
    "film_validation_scorecard",
    "no_fake_pass_gate",
}

FIXTURE_TRANSLATION_COVERAGE = {
    "film_packet_shape": {"film_intent_lock", "logline", "premise", "screenplay_body"},
    "beat_sheet": {"beat_sheet"},
    "character_arc": {"protagonist_want", "protagonist_need", "protagonist_flaw", "protagonist_arc"},
    "scene_dramaturgy": {"scene_dramaturgy_map"},
    "dialogue_subtext": {"dialogue_subtext_pass"},
    "visual_motif_system": {"visual_motif_system"},
    "validation_scorecard": {"film_validation_scorecard"},
}


def load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def test_schema_required_fields_are_non_empty_and_expected():
    schema = load_schema()
    required = set(schema["required"])

    assert required == EXPECTED_REQUIRED_FIELDS
    assert len(required) == 20


def test_required_fields_all_exist_in_schema_properties():
    schema = load_schema()
    properties = set(schema["properties"])

    for field in schema["required"]:
        assert field in properties


def test_fixture_derived_core_filmcraft_is_represented():
    required = set(load_schema()["required"])

    for fixture_concept, schema_fields in FIXTURE_TRANSLATION_COVERAGE.items():
        assert schema_fields.issubset(required), fixture_concept


def test_schema_boundaries_remain_unbound_and_non_runtime_proof():
    schema = load_schema()

    assert schema["x_runtime_behavior_changed"] is False
    assert schema["x_route_selector_modified"] is False
    assert schema["x_schema_enforcement_bound"] is False
    assert schema["x_validator_bound"] is False
    assert schema["x_governed_runtime_proof_claimed"] is False


def test_source_and_downstream_fields_remain_available_but_not_required_yet():
    schema = load_schema()
    required = set(schema["required"])
    properties = set(schema["properties"])

    future_specialized_fields = {
        "source_research_status",
        "source_ledger",
        "fact_vs_anecdote_map",
        "downstream_handoff_recommendations",
    }
    assert future_specialized_fields.issubset(properties)
    assert required.isdisjoint(future_specialized_fields)


if __name__ == "__main__":
    test_schema_required_fields_are_non_empty_and_expected()
    test_required_fields_all_exist_in_schema_properties()
    test_fixture_derived_core_filmcraft_is_represented()
    test_schema_boundaries_remain_unbound_and_non_runtime_proof()
    test_source_and_downstream_fields_remain_available_but_not_required_yet()
    print("phase_13e42_film_screenplay_output_schema_required_fields_ok")

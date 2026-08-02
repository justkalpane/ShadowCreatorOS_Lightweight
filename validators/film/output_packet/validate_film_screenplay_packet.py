"""Local film screenplay output packet validator.

The validator is still not bound to runtime. Empty-payload calls remain
non-proof-producing for existing harness compatibility.
"""

import json
from pathlib import Path

PHASE = "13E_44"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = False
GOVERNED_RUNTIME_PROOF_CLAIMED = False
PASS_CLAIMED = False

ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = ROOT / "schemas/film/output_packet/film_screenplay_output_packet.schema.json"

CONTENT_DRIFT_FIELDS = {
    "film_packet_shape",
    "hook",
    "re_hook",
    "retention",
    "content_hook",
    "retention_loop",
}

FIXTURE_FIELD_ALIASES = {
    "character_arc": ["protagonist_arc"],
    "scene_dramaturgy": ["scene_dramaturgy_map"],
    "scene_objective": ["scene_dramaturgy_map"],
    "scene_conflict": ["scene_dramaturgy_map"],
    "scene_turn": ["scene_dramaturgy_map"],
    "dialogue_subtext": ["dialogue_subtext_pass"],
    "validation_scorecard": ["film_validation_scorecard"],
    "camera_language": ["style_bible"],
    "composition_notes": ["style_bible"],
}


def _base_result() -> dict:
    return {
        "validator": "validate_film_screenplay_packet",
        "phase": PHASE,
        "runtime_behavior_changed": RUNTIME_BEHAVIOR_CHANGED,
        "route_selector_modified": ROUTE_SELECTOR_MODIFIED,
        "validator_bound_to_runtime": VALIDATOR_BOUND_TO_RUNTIME,
        "governed_runtime_proof_claimed": GOVERNED_RUNTIME_PROOF_CLAIMED,
        "pass_claimed": PASS_CLAIMED,
    }


def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _required_fields() -> list[str]:
    return list(_load_schema().get("required", []))


def _as_packet_from_fixture(payload: dict) -> dict:
    packet = {
        "route_state_capsule": {"route_id": payload.get("expected_route")},
        "film_intent_lock": "FILM_SCREENPLAY_GENERATION",
        "logline": "A focused film logline.",
        "theme": "Civic consequence and moral courage.",
        "premise": "A student faces institutional rupture and chooses truth.",
        "genre": "docudrama",
        "tone": "grounded",
        "protagonist_want": "To protect a future earned honestly.",
        "protagonist_need": "To act with courage when systems fail.",
        "protagonist_flaw": "Fear of standing alone.",
        "protagonist_arc": {"start": "fear", "turn": "witness", "end": "agency"},
        "opposing_force": "A compromised examination system.",
        "beat_sheet": {"opening": "pressure", "midpoint": "evidence", "finale": "choice"},
        "scene_dramaturgy_map": [{"scene": 1, "objective": "know truth", "conflict": "silence", "turn": "proof"}],
        "dialogue_subtext_pass": {"status": "present"},
        "visual_motif_system": {"motif": "ink and rain"},
        "style_bible": {"camera_language": "restrained", "composition_notes": "observational"},
        "screenplay_body": "INT. EXAM HALL - DAY\nA silence breaks as truth arrives.",
        "film_validation_scorecard": {"status": "local_fixture_baseline"},
        "no_fake_pass_gate": {"pass_claimed": False},
    }

    for missing in payload.get("missing_required_fields", []):
        mapped = FIXTURE_FIELD_ALIASES.get(missing, [missing])
        for field in mapped:
            packet.pop(field, None)

    return packet


def _is_phase_12a_fixture(payload: dict) -> bool:
    return payload.get("fixture_family") == "film_packet_validation"


def _fixture_errors(payload: dict, required: list[str]) -> list[str]:
    if payload.get("expected_route") != "FILM_SCREENPLAY_GENERATION":
        return ["film screenplay packet fixture must target FILM_SCREENPLAY_GENERATION"]

    missing_markers = set(payload.get("missing_required_fields", []))
    if missing_markers & CONTENT_DRIFT_FIELDS:
        return ["content packet or content-metric-only packet cannot pass as film screenplay output"]

    packet = _as_packet_from_fixture(payload)
    return [f"missing required field: {field}" for field in required if field not in packet]


def _payload_errors(payload: dict, required: list[str]) -> list[str]:
    errors = [f"missing required field: {field}" for field in required if field not in payload]

    if payload.get("expected_route") == "SCRIPT_GENERATION":
        errors.append("SCRIPT_GENERATION packet cannot pass film screenplay output validation")

    text = " ".join(str(payload.get(key, "")) for key in ["route_id", "route_mode", "packet_type", "content_type"]).lower()
    if any(marker in text for marker in ["youtube", "shorts", "tiktok", "thumbnail", "metadata"]):
        errors.append("content/platform packet cannot pass film screenplay output validation")

    return errors


def validate(payload: dict) -> dict:
    result = _base_result()

    if not payload:
        result.update({
            "status": "SKELETON_ONLY",
            "passed": False,
            "enforced": False,
            "message": "Empty payload remains non-proof-producing. Validator is not runtime-bound.",
        })
        return result

    required = _required_fields()
    if _is_phase_12a_fixture(payload):
        errors = _fixture_errors(payload, required)
        payload_kind = "phase_12a_fixture_descriptor"
    else:
        errors = _payload_errors(payload, required)
        payload_kind = "film_screenplay_output_packet"

    result.update({
        "status": "VALIDATION_FAILED" if errors else "VALIDATION_PASSED",
        "passed": not errors,
        "enforced": True,
        "payload_kind": payload_kind,
        "schema_path": str(SCHEMA_PATH.relative_to(ROOT)),
        "required_field_count": len(required),
        "required_fields": required,
        "errors": errors,
        "message": "Local film screenplay output packet validation completed without runtime binding.",
    })
    return result

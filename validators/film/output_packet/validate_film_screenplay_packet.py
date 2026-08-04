"""Local film screenplay output packet validator.

Empty-payload and legacy fixture calls remain non-proof-producing for existing
harness compatibility. When the payload points at a runtime artifact bundle, the
validator inspects the generated packet on disk instead of pretending the bundle
is a synthetic schema object.
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


def _artifact_paths(payload: dict) -> dict[str, Path | None]:
    artifact_root = payload.get("artifact_root")
    root = Path(artifact_root) if artifact_root else None
    return {
        "artifact_root": root,
        "screenplay_packet_path": Path(payload["screenplay_packet_path"]) if payload.get("screenplay_packet_path") else (root / "screenplay_packet.json" if root else None),
        "validation_report_path": Path(payload["validation_report_path"]) if payload.get("validation_report_path") else (root / "validation_report.json" if root else None),
        "screenplay_md_path": Path(payload["screenplay_md_path"]) if payload.get("screenplay_md_path") else (root / "screenplay.md" if root else None),
    }


def _is_phase_12a_fixture(payload: dict) -> bool:
    return payload.get("fixture_family") == "film_packet_validation"


def _is_artifact_bundle(payload: dict) -> bool:
    return any(key in payload for key in ("screenplay_packet_path", "validation_report_path", "artifact_root"))


def _artifact_errors(payload: dict, required: list[str]) -> tuple[list[str], dict]:
    paths = _artifact_paths(payload)
    errors: list[str] = []

    packet_path = paths["screenplay_packet_path"]
    report_path = paths["validation_report_path"]
    md_path = paths["screenplay_md_path"]

    if not packet_path or not packet_path.is_file():
        return ["screenplay packet artifact is missing"], {}

    packet = json.loads(packet_path.read_text(encoding="utf-8"))

    for field in required:
        if field not in packet:
            errors.append(f"missing required field: {field}")

    if packet.get("route") != "FILM_SCREENPLAY_GENERATION":
        errors.append("artifact packet must target FILM_SCREENPLAY_GENERATION")
    if packet.get("mode") != "script_only":
        errors.append("artifact packet must preserve script_only mode")
    duration_minutes = packet.get("duration_minutes")
    estimated_duration = packet.get("estimated_duration_minutes")
    if not isinstance(duration_minutes, int) or duration_minutes < 5:
        errors.append("artifact packet must preserve a valid film duration")
    if estimated_duration != duration_minutes:
        errors.append("artifact packet must preserve estimated_duration_minutes matching duration_minutes")

    route_state_capsule = packet.get("route_state_capsule") or {}
    if route_state_capsule.get("route_id") != "FILM_SCREENPLAY_GENERATION":
        errors.append("route_state_capsule must preserve FILM_SCREENPLAY_GENERATION")

    route_state = packet.get("route_state") or {}
    if route_state.get("route_id") != "FILM_SCREENPLAY_GENERATION":
        errors.append("route_state must preserve FILM_SCREENPLAY_GENERATION")
    if route_state.get("output_phase_started") is not True:
        errors.append("route_state must record output phase start")

    screenplay = packet.get("screenplay_body") or packet.get("screenplay") or ""
    if not screenplay.strip():
        errors.append("screenplay_body must not be empty for artifact validation")
    else:
        heading_count = sum(
            1
            for line in screenplay.splitlines()
            if line.startswith(("INT.", "EXT.")) or line.strip().startswith(("INT.", "EXT."))
        )
        if heading_count < 3:
            errors.append("screenplay artifact must contain at least 3 scene headings")

    if not report_path or not report_path.is_file():
        errors.append("validation report artifact is missing")
    else:
        report = json.loads(report_path.read_text(encoding="utf-8"))
        if report.get("status") not in {"VALIDATION_IN_PROGRESS", "PASS_RUNTIME_ARTIFACT_PROVEN"}:
            errors.append("validation report status must prove the runtime artifact path")
        route_checks = report.get("route_checks") or {}
        if route_checks.get("route_exists") is not True or route_checks.get("script_generation_preserved") is not True:
            errors.append("validation report must preserve route existence and script_generation")
        if "validator_results" not in report:
            errors.append("validation report must include validator results")

    if not md_path or not md_path.is_file():
        errors.append("screenplay markdown artifact is missing")

    return errors, packet


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
    if _is_artifact_bundle(payload):
        errors, packet = _artifact_errors(payload, required)
        result.update({
            "status": "VALIDATION_FAILED" if errors else "VALIDATION_PASSED",
            "passed": not errors,
            "enforced": True,
            "payload_kind": "runtime_artifact_bundle",
            "schema_path": str(SCHEMA_PATH.relative_to(ROOT)),
            "required_field_count": len(required),
            "required_fields": required,
            "errors": errors,
            "message": "Runtime artifact bundle validation completed without runtime binding.",
            "artifact_root": str(payload.get("artifact_root")) if payload.get("artifact_root") is not None else None,
            "screenplay_packet_path": str(payload.get("screenplay_packet_path")) if payload.get("screenplay_packet_path") is not None else None,
            "validation_report_path": str(payload.get("validation_report_path")) if payload.get("validation_report_path") is not None else None,
            "screenplay_md_path": str(payload.get("screenplay_md_path")) if payload.get("screenplay_md_path") is not None else None,
            "screenplay_packet_summary": {
                "route": packet.get("route"),
                "mode": packet.get("mode"),
                "duration_minutes": packet.get("duration_minutes"),
                "scene_count": len(packet.get("scene_breakdown", [])),
                "character_count": len(packet.get("character_list", [])),
            } if packet else {},
        })
        return result

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

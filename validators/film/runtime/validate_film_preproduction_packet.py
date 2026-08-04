from __future__ import annotations

import json
from pathlib import Path

from tools.film_runtime.preproduction.department_handoff_engine import DEPARTMENTS
from validators.film.runtime.preproduction_validator_utils import (
    contains_forbidden_media_terms,
    packet,
    read_json_file,
    require_fields,
    result,
    validate_schema_file,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA = REPO_ROOT / "schemas/film/preproduction_packet.schema.json"
REQUIRED = json.loads(SCHEMA.read_text(encoding="utf-8"))["required"]
PACKET_SCHEMAS = {
    "concept_note": "schemas/film/preproduction/concept_note.schema.json",
    "premise_test": "schemas/film/preproduction/premise_test.schema.json",
    "treatment": "schemas/film/preproduction/treatment.schema.json",
    "synopsis": "schemas/film/preproduction/synopsis.schema.json",
    "beat_sheet": "schemas/film/preproduction/beat_sheet.schema.json",
    "act_structure": "schemas/film/preproduction/act_structure.schema.json",
    "sequence_structure": "schemas/film/preproduction/sequence_structure.schema.json",
    "scene_cards": "schemas/film/preproduction/scene_cards.schema.json",
    "character_bible": "schemas/film/preproduction/character_bible.schema.json",
    "character_arc": "schemas/film/preproduction/character_arc.schema.json",
    "opposing_force": "schemas/film/preproduction/opposing_force.schema.json",
    "relationship_map": "schemas/film/preproduction/relationship_map.schema.json",
    "moral_dilemma": "schemas/film/preproduction/moral_dilemma.schema.json",
    "world_bible": "schemas/film/preproduction/world_bible.schema.json",
    "director_vision": "schemas/film/preproduction/director_vision.schema.json",
    "visual_language": "schemas/film/preproduction/visual_language.schema.json",
    "cinematography_plan": "schemas/film/preproduction/cinematography_plan.schema.json",
    "department_handoffs": "schemas/film/preproduction/department_handoffs.schema.json",
    "production_risk_sheet": "schemas/film/preproduction/production_risk_sheet.schema.json",
    "revision_report": "schemas/film/preproduction/revision_report.schema.json",
    "source_evidence_ledger": "schemas/film/preproduction/source_evidence_ledger.schema.json",
}
NEGATIVE_TARGETS = {
    "missing_beat_sheet_fails",
    "missing_act_structure_fails",
    "missing_sequence_structure_fails",
    "missing_character_arc_fails",
    "missing_world_bible_fails",
    "missing_director_vision_fails",
    "missing_visual_language_fails",
    "missing_cinematography_plan_fails",
    "missing_department_handoffs_fails",
    "missing_production_risk_fails",
    "missing_revision_report_fails",
    "wrong_route_state_mode_fails",
    "SCRIPT_GENERATION_leak_into_FILM_route_fails",
    "media_provider_flag_true_fails",
    "content_route_terms_inside_film_core_fail",
}
REQUIRED_GENRES = {
    "motivational_drama",
    "social_drama",
    "thriller",
    "horror",
    "romance",
    "comedy",
    "crime",
    "action",
    "mythology_fantasy",
    "mass_commercial",
    "short_film",
    "feature_film",
    "web_series",
}


def validate(payload: dict) -> dict:
    data = packet(payload)
    errors = require_fields(data, REQUIRED)
    errors.extend(validate_schema_file(data, "schemas/film/preproduction_packet.schema.json"))
    for field, schema_rel_path in PACKET_SCHEMAS.items():
        if field in data:
            errors.extend(validate_schema_file(data[field], schema_rel_path))

    route_state = data.get("route_state") or {}
    if data.get("route") != "FILM_SCREENPLAY_GENERATION":
        errors.append("route must be FILM_SCREENPLAY_GENERATION")
    if data.get("mode") != "script_only":
        errors.append("mode must remain script_only")
    if route_state.get("mode") != "script_only":
        errors.append("route_state.mode must remain script_only")
    if route_state.get("route") != "FILM_SCREENPLAY_GENERATION":
        errors.append("route_state.route must be FILM_SCREENPLAY_GENERATION")

    if not (data.get("genre_grammar_report") or {}).get("passed"):
        errors.append("genre grammar report must pass")
    if "repair" not in str(data.get("character_arc", "")).lower():
        errors.append("character arc must resolve repair")
    if "consequence_chain" not in (data.get("world_bible") or {}):
        errors.append("world bible missing consequence chain")
    if "transformation_midpoint" not in (data.get("character_arc") or {}):
        errors.append("character transformation midpoint missing")
    if len(data.get("scene_cards") or []) < 3:
        errors.append("scene card integrity failed")
    for field in ["visual_language", "cinematography_plan", "production_risk_sheet", "revision_report"]:
        if not data.get(field):
            errors.append(f"{field} missing")
    handoffs = data.get("department_handoffs") or {}
    for department in DEPARTMENTS:
        if department not in handoffs:
            errors.append(f"department handoff missing: {department}")

    if contains_forbidden_media_terms(data):
        errors.append("media/provider call markers are forbidden")
    source = data.get("source_evidence_ledger") or {}
    if source.get("source_policy") != "fictional_local_payload_no_external_sources_required":
        errors.append("source evidence ledger policy is missing or invalid")

    available_genres = set((data.get("genre_grammar_report") or {}).get("available_genres") or [])
    if not REQUIRED_GENRES.issubset(available_genres):
        errors.append("multi-genre rule map is incomplete")

    gap_matrix_meta = data.get("openworker_gap_reconciliation_matrix") or {}
    if not gap_matrix_meta.get("json_path") or not Path(gap_matrix_meta["json_path"]).is_file():
        errors.append("OpenWorker gap reconciliation matrix missing")
    else:
        matrix = read_json_file(Path(gap_matrix_meta["json_path"]))
        categories = matrix.get("categories", {})
        if any(value in {"NOT_CLOSED", "SCAFFOLD_ONLY"} for value in categories.values()):
            errors.append("OpenWorker gap reconciliation still contains scaffold-only or not-closed categories")

    audit_meta = data.get("validator_depth_audit") or {}
    if not audit_meta.get("json_path") or not Path(audit_meta["json_path"]).is_file():
        errors.append("validator depth audit missing")
    else:
        audit = read_json_file(Path(audit_meta["json_path"]))
        for entry in audit.get("validators", []):
            if entry.get("validator_type") == "PRESENCE_ONLY":
                errors.append(f"presence-only validator remains: {entry.get('validator_name')}")
            if not entry.get("has_negative_test"):
                errors.append(f"negative test missing for validator: {entry.get('validator_name')}")

    negative_targets = set(data.get("negative_validation_targets") or [])
    if not NEGATIVE_TARGETS.issubset(negative_targets):
        errors.append("negative validation proof targets are incomplete")

    downstream = data.get("downstream_adapter_boundary") or {}
    if not downstream.get("preproduction_only"):
        errors.append("downstream boundary missing preproduction_only lock")
    if downstream.get("downstream_execution_triggered") is not False:
        errors.append("downstream execution must remain false")
    if len(downstream.get("allowed_future_targets") or []) < 4:
        errors.append("downstream boundary allowed future targets incomplete")

    return result("validate_film_preproduction_packet", not errors, errors)

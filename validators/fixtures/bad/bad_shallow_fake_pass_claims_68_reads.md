fixture_id=FX-BAD-001
fixture_type=bad
stage=script_generation
expected_validator=validate_route_claim_evidence_consistency.py
expected_result=FAIL

SHALLOW_FAKE_PASS_CLAIM
route_id=SCRIPT_GENERATION
final_status=PASS
mandatory_files_read=68
actual_files_read=3
route_manifest_read=false
selected_route_slice_read=false
component_consumption_unproven=true
semantic_influence_map_present=false
output_phase_started=false
final_script_generated=false
validators_run=false

CLAIM_EVIDENCE_STATUS
claim=SCRIPT_GENERATION route consumed complete scope and reached PASS.
evidence=Only startup files were listed. Route manifest, source ledger, semantic influence, and output proof are absent.
evidence_scope=memory_only
evidence_path=
command_output_or_file_reference=
status=PASS

failure_reason=Claimed route consumption outruns concrete read evidence and converts an unsupported shallow run into PASS.

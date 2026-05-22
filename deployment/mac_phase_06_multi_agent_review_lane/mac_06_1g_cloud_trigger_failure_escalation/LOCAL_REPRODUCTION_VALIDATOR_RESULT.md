# Local Reproduction Validator Result

validator_run=true
validator_classification=PASS
missing_sections=none
invalid_statuses=none
false_execution_claims=none
content_engineering_present=true
boot_signature_present=true

## Command

```text
python3 validators/validate_mac06_1a_output.py deployment/mac_phase_06_multi_agent_review_lane/mac_06_1g_cloud_trigger_failure_escalation/LOCAL_REPO_CONTROLLED_REPRODUCTION.md
```

## Result Summary

```text
VALIDATION_STATUS=PASS
missing_required_sections_count=0
invalid_gate_status_count=0
invalid_research_mode_count=0
false_execution_claim_count=0
internet_first_marker_count=0
sources_before_repo_route=false
generic_output_detected=false
shadow_boot_confirmation_present=true
content_before_shadow_boot_confirmation=false
required_true_field_failure_count=0
shadow_mode_chat_only=true
capability_matrix_cited=true
agent_runtime_selection_index_cited=true
files_created_in_chat_only=false
dossier_artifacts_created_in_chat_only=false
source_claim_without_source_list=false
final_proof_classification=PASS
final_status_matches_weakest_evidence_layer=true
```

## Fixture Regression Summary

- `mac06_1a_fail_internet_first_before_repo.txt` -> `VALIDATION_STATUS=FAIL`
- `mac06_1a_fail_no_shadow_boot_confirmation.txt` -> `VALIDATION_STATUS=FAIL`
- `mac06_1a_fail_generic_output.txt` -> `VALIDATION_STATUS=FAIL`
- `mac06_1a_partial_missing_content_engineering.txt` -> `VALIDATION_STATUS=PARTIAL`
- `mac06_1a_partial_missing_agent_index.txt` -> `VALIDATION_STATUS=PARTIAL`
- `mac06_1a_pass_minimal_complete.txt` -> `VALIDATION_STATUS=PASS`

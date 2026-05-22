# Validator Fixture Test Result

audit_date=2026-05-22
operator_mode=OLD_LOCAL_MAC_CODEX_CHAT

fixtures_created=true
fixture_tests_run=true
fixture_tests_passed=true

## Fixture Results

### FAIL Generic Output

```text
command=python3 validators/validate_mac06_1a_output.py validators/fixtures/mac06_1a_fail_generic_output.txt
VALIDATION_STATUS=FAIL
generic_output_detected=true
final_proof_classification=PASS
final_status_matches_weakest_evidence_layer=false
expected=FAIL
result=PASS
```

### PARTIAL Missing Content Engineering

```text
command=python3 validators/validate_mac06_1a_output.py validators/fixtures/mac06_1a_partial_missing_content_engineering.txt
VALIDATION_STATUS=PARTIAL
missing_required_sections_count=10
missing=CONTENT_MISSION_BRIEF
missing=RESEARCH_AND_SOURCE_STATUS
missing=SCRIPT_STRUCTURE
missing=TIMED_BEAT_MAP
missing=VOICE_GENERATION_CONTEXT
missing=IMAGE_GENERATION_CONTEXT
missing=VIDEO_GENERATION_CONTEXT
missing=MUSIC_AND_SFX_CONTEXT
missing=EDITING_CONTEXT
missing=PLATFORM_PACKAGING
expected=PARTIAL
result=PASS
```

### PARTIAL Missing Agent Index

```text
command=python3 validators/validate_mac06_1a_output.py validators/fixtures/mac06_1a_partial_missing_agent_index.txt
VALIDATION_STATUS=PARTIAL
missing_required_sections_count=1
missing=registries/agent_runtime_selection_index.yaml
agent_runtime_selection_index_cited=false
expected=PARTIAL
result=PASS
```

### PASS Minimal Complete

```text
command=python3 validators/validate_mac06_1a_output.py validators/fixtures/mac06_1a_pass_minimal_complete.txt
VALIDATION_STATUS=PASS
missing_required_sections_count=0
capability_matrix_cited=true
agent_runtime_selection_index_cited=true
final_status_matches_weakest_evidence_layer=true
expected=PASS
result=PASS
```

validator_fixtures_created=true
validator_fixture_tests_passed=true

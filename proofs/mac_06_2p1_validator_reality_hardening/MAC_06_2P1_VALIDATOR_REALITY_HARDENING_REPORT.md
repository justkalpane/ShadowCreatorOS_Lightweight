# MAC-06.2P1 Validator Reality Hardening Report

## PATCH_SUMMARY

MAC-06.2P1 closes the known fake-depth escape paths in the local
script-generation validator. It also aligns the declared `M-039` recurring
re-hook requirement with the executable script-generation DAG.

This is a local enforcement patch only. It does not declare creative
excellence, provider execution, n8n readiness, or Lightweight OS onboarding.

## FILES_CHANGED

Primary 2P1 files:

- `validators/validate_script_generation_output.py`
- `registries/route_dag_registry.yaml`
- `registries/component_lifecycle_registry.yaml`
- `registries/communication_pointer_registry.yaml`
- `schemas/packets/rehook_plan_packet.schema.json`
- `tools/shadow_runtime/packet_flow_runner.py`
- `tools/shadow_runtime/schema_rationalizer.py`
- `tools/shadow_runtime/script_behavior_propagation_scanner.py`
- `skills/script_intelligence_army/M-039-re-hook-system.py`
- `skills/script_intelligence/S-202-first-draft-generation.py`
- `tests/shadow_runtime/fixtures/route_dags/pass_script_generation_ordered_nodes.yaml`
- `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
- `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md`
- `deployment/proofs/MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS.md`

## VALIDATOR_REALITY_HARDENING

```text
script_body_language_check=PASS
rehook_reality_check=PASS
source_ledger_reality_check=PASS
fact_vs_anecdote_reality_check=PASS
scene_sync_reality_check=PASS
weakest_gate_reality_check=PASS
propagation_reality_check=PASS
```

The validator now:

- detects Hindi/Hinglish body drift instead of trusting the declared language;
- parses scoped `source_row_json=`, `fact_map_row_json=`, `rehook_row_json=`,
  and `scene_row_json=` rows;
- ignores URLs outside `SOURCE_LEDGER` for source sufficiency;
- calculates re-hook gaps from timestamps;
- binds re-hooks to final script, beat-map scenes, and influence references;
- validates Media Factory scene rows against the scene-sync schema;
- reads `final_status=` during weakest-gate enforcement;
- rejects marker-only propagation when responsibility-specific enforcement
  text is absent.

## M039_DAG_ALIGNMENT

```text
m039_manifest_required=true
m039_workflow_registry_present=false
m039_skill_registry_present=true
m039_dag_present=true
s202_executes_directly=true
chosen_fix=A
dag_alignment_status=PASS
```

`workflow_registry.yaml` registers workflow packs rather than skill nodes.
`M-039` is registered in the skill registry and route manifest. The executable
DAG now places `M-039-re-hook-system` before `S-202-first-draft-generation`.
`M-039` emits `rehook_plan_packet`; strict `S-202` consumes it and rejects a
missing packet.

## PROPAGATION_COVERAGE_EXPANSION

```text
keyword_candidates_total=3951
allowlisted_runtime_files=63
reviewed_not_applicable_count=2532
reference_only_count=635
historical_or_test_count=216
generated_artifact_count=505
needs_patch_count=0
unclassified_relevant_candidates=0
coverage_expansion_status=PASS
review_method=automated_keyword_bucket_review
```

The expanded ledger is:

- `PROPAGATION_COVERAGE_EXPANSION.csv`
- `propagation_coverage_expansion.json`

## NEGATIVE_TESTS_ADDED

```text
NEG-LANG-001
NEG-REHOOK-001
NEG-REHOOK-002
NEG-REHOOK-003
NEG-SOURCE-001
NEG-SOURCE-002
NEG-FACT-001
NEG-FACT-002
NEG-SCENE-001
NEG-SCENE-002
NEG-STATUS-001
NEG-PROP-001
NEG-DAG-001
```

## SELF_TEST_RESULT

```text
positive_or_alignment_tests=3
negative_escape_tests=17
validator_self_tests=20/20
overall_status=PASS
shadow_runtime_regression=PASS
shadow_runtime_tests=20/20
validator_integrity_scanner=PASS
always_pass_logic_remaining=0
hardcoded_success_remaining=0
ignored_exceptions_remaining=0
text_only_critical_checks_remaining=0
git_diff_check=PASS
```

## REMAINING_LIMITATIONS

- English body detection is a deterministic local heuristic, not a full
  multilingual classifier. It intentionally blocks obvious Hindi/Hinglish and
  Indic-script drift while allowing proper nouns and cultural references.
- Propagation coverage expansion is an automated bucket review. A later human
  audit may still inspect suspicious `NOT_APPLICABLE_WITH_REASON` rows.
- The validator proves structural production depth. It does not yet prove that
  every fresh naturally generated script is creatively excellent.
- A fresh saved diagnostic script and a saved Media Factory final-draft packet
  should be validated next before acceptance or commit review.
- n8n, providers, and media execution remain disabled.

## DO_NOT_COMMIT_STATUS

```text
commit_performed=false
push_performed=false
n8n_started=false
providers_called=false
media_generated=false
```

## NEXT_STEP_RECOMMENDATION

Run one fresh natural Yash self-investment diagnostic in local chat, save the
generated output, validate that saved output with
`validators/validate_script_generation_output.py`, then run the Media Factory
final-draft diagnostic against the same script.

## FINAL_CLASSIFICATION

```text
MAC_06_2P1_VALIDATOR_REALITY_HARDENING_STATUS=PASS
fresh_diagnostic_test_allowed=true
fresh_acceptance_test_ready=false
safe_to_commit=false
safe_to_push=false
safe_to_start_n8n=false
safe_to_declare_lightweight_os_onboarded=false
```

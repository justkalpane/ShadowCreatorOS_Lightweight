# Task Execution State Machine Contract

Bootstrap loaded is not enough.
`task_intent_routing_matrix` loaded during bootstrap is not enough.

## Mandatory Order

1. `SHADOW_BOOT_CONFIRMATION`
2. `TASK_ROUTE_LOCK`
3. `ROUTE_DEPENDENCY_EXPANSION_LOCK`
4. `CONSUMPTION_LOCK`
5. `SOURCE_RESEARCH_LOCK`
6. `QUALITY_LOCK`
7. `GOVERNANCE_LOCK`
8. `FINAL_OUTPUT`
9. `FINAL_PROOF_CLASSIFICATION`

## Hard Laws

- Every task must read the selected route manifest before output.
- Every task must read all mandatory route files before output.
- Final content is forbidden before all required locks pass.
- Current/latest claims are forbidden before `SOURCE_RESEARCH_LOCK`.
- Final acceptance is forbidden before `GOVERNANCE_LOCK`.
- If manual rerun improves structure but lacks ledgers, classify `PARTIAL`, not `PASS`.

## TASK_ROUTE_LOCK

```text
TASK_ROUTE_LOCK
task_intent_classified=
route_id=
route_name=
task_intent_routing_matrix_read=
route_manifest_path=
route_selected_before_output=
route_lock_status=
```

## ROUTE_DEPENDENCY_EXPANSION_LOCK

```text
ROUTE_DEPENDENCY_EXPANSION_LOCK
route_manifest_read=
mandatory_files_identified=
mandatory_files_read=
missing_mandatory_files=
transitive_dependencies_checked=
governance_files_included=
route_scope_complete=
route_dependency_expansion_lock_status=
```

## CONSUMPTION_LOCK

```text
CONSUMPTION_LOCK
director_consumption_complete=
agent_consumption_complete=
subagent_consumption_complete=
skill_consumption_complete=
subskill_consumption_complete=
exact_rules_extracted=
output_decisions_changed_by_rules=
missed_repo_rules_listed=
consumption_lock_status=
```

## SOURCE_RESEARCH_LOCK

```text
SOURCE_RESEARCH_LOCK
freshness_class=
research_mode=
web_required=
web_used=
sources_used_before_output=
source_list_present=
latest_claims_allowed=
current_fact_confidence=
unsupported_claims=
source_research_lock_status=
```

## QUALITY_LOCK

```text
QUALITY_LOCK
topic_quality_gate_complete=
hook_generation_gate_complete=
hook_variants_count=
hook_scores_present=
selected_hook_reason_present=
script_quality_gate_complete=
script_overall_score=
script_pass_threshold=
rewrite_required=
rewrite_done_if_required=
quality_lock_status=
```

## GOVERNANCE_LOCK

```text
GOVERNANCE_LOCK
governance_directors_selected=
quality_governance_applied=
risk_policy_governance_applied=
rejection_or_approval_recorded=
repair_route_defined_if_failed=
governance_lock_status=
```

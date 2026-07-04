# Task Execution State Machine Contract

Bootstrap loaded is not enough.
`task_intent_routing_matrix` loaded during bootstrap is not enough.

## Mandatory Order

1. `SHADOW_BOOT_CONFIRMATION`
2. `TASK_ROUTE_LOCK`
3. `ROUTE_DEPENDENCY_EXPANSION_LOCK`
4. `CONSUMPTION_LOCK`
5. `SOURCE_RESEARCH_LOCK`
6. `SCRIPT_LANGUAGE_LOCK` for script/content routes
7. `QUALITY_LOCK`
8. `VALIDATION_SCORECARD`
9. `RECURRING_HOOK_DENSITY_LOCK` for 3-10 minute YouTube scripts
10. `MEDIA_FACTORY_SYNC_LOCK` when final media draft is requested
11. `GOVERNANCE_LOCK`
12. `FINAL_OUTPUT`
13. `FINAL_PROOF_CLASSIFICATION`

## Hard Laws

- Every task must read the selected route manifest before output.
- Every task must read all mandatory route files before output.
- Final content is forbidden before all required locks pass.
- Current/latest claims are forbidden before `SOURCE_RESEARCH_LOCK`.
- Final acceptance is forbidden before `GOVERNANCE_LOCK`.
- Final acceptance is forbidden before execution visibility is shown in a
  visible gate log and trace bundle.
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
current_data_required=
research_mode=
web_access_available=
web_access_used=
web_required=
web_used=
sources_used_before_output=
source_list_present=
source_list=
video_reference_list=
real_time_sources_used=
latest_claims_allowed=
current_fact_confidence=
unsupported_claims=
research_sufficiency_gate_status=
source_research_lock_status=
```

`SOURCE_RESEARCH_LOCK` is mandatory for current/latest prompts and for
real-person, real-incident, brand, company, factual case-study, biographical,
career, article-reference, or video-reference claims used as proof.

If `unsupported_claims` is non-empty, the lock cannot pass. If web evidence is
required but unused, the final proof cannot pass unless the user explicitly
approved repo-only limited continuation.

## SCRIPT_LANGUAGE_LOCK

```text
SCRIPT_LANGUAGE_LOCK
master_script_language=
explicit_language_requested=
translation_stage_required=
language_inference_blocked=
script_language_lock_status=
```

The default master language is English unless the user explicitly requests
another language or translation/localization.

## CINEMATIC_STORY_GATE

```text
CINEMATIC_STORY_GATE
cinematic_story_required=
story_duration_target_seconds=
story_basis=
character_present=
conflict_present=
turning_point_present=
cinematic_visuals_present=
emotional_peak_present=
lesson_bridge_present=
source_dependency_satisfied=
cinematic_story_gate_status=
```

This gate is mandatory for every 3-10 minute YouTube script.

## MEDIA_FACTORY_SYNC_LOCK

```text
MEDIA_FACTORY_SYNC_LOCK
media_factory_final_draft_requested=
dynamic_beat_map_present=
scene_sync_matrix_complete=
media_contexts_synchronized=
local_cloud_hybrid_execution_plan_present=
provider_execution_allowed=false
media_factory_sync_lock_status=
```

This lock is mandatory when a final Media Factory draft is requested.

## RECURRING_HOOK_DENSITY_LOCK

```text
RECURRING_HOOK_DENSITY_LOCK
opening_hook_present=
recurring_rehook_required=
recurring_rehook_count=
max_gap_without_rehook_seconds=
rehook_interval_reason_present=
rehooks_mapped_to_final_script=
rehooks_mapped_to_dynamic_beat_map=
rehooks_mapped_to_editing_context=
rehooks_mapped_to_line_influence_map=
rehooks_mapped_to_scene_sync_matrix=
rehook_density_lock_status=
```

For a 5-minute script, at least three internal re-hooks plus a CTA hook are
required. `HOOK_VARIANTS` is only the opening-hook selection gate.

## QUALITY_LOCK

```text
QUALITY_LOCK
topic_quality_gate_complete=
hook_generation_gate_complete=
hook_variants_count=
hook_scores_present=
selected_hook_reason_present=
script_quality_gate_complete=
cadence_and_retention_gate_complete=
source_integrity_gate_complete=
script_overall_score=
script_pass_threshold=
rewrite_required=
rewrite_done_if_required=
quality_lock_status=
```

## VALIDATION_SCORECARD

```text
VALIDATION_SCORECARD
topic_quality_gate_status=
hook_generation_gate_status=
script_quality_gate_status=
cadence_and_retention_gate_status=
source_integrity_gate_status=
script_body_depth_lock_status=
recurring_hook_density_lock_status=
governance_lock_status=
line_by_line_influence_map_status=
final_proof_classification=
validation_scorecard_status=
```

`VALIDATION_SCORECARD` is mandatory before final proof. It must reflect the
weakest gate and cannot be replaced by prose-only threshold claims.

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

## ROUTE_STATE_CAPSULE_LOCK

Every production task must progress through:

```text
BOOT_CONFIRMED
TASK_CLASSIFIED
ROUTE_LOCKED
DEPENDENCIES_CONSUMED
OUTPUT_PHASE_STARTED
OUTPUT_GENERATED
VALIDATED
```

Required proof fields:

```text
route_state_capsule_present=true
route_state_capsule_schema_path=
evidence_bundle_present=true/false
evidence_bundle_schema_path=
gate_visibility_log_present=true/false
gate_visibility_log_schema_path=
proof_trace_bundle_present=true/false
proof_trace_bundle_schema_path=
chitragupta_audit_event_present=true/false
chitragupta_audit_event_schema_path=
bridge_job_packet_present=true/false
bridge_job_packet_schema_path=
validator_surface_bound=true/false
validator_surface_status=
route_manifest_hash=
task_mode=
route_phase=
selected_route_slice_read=true/false
mandatory_route_slice_paths_consumed=true/false
dependencies_complete=true/false
output_phase_started=true/false
last_completed_step=
next_required_step=
compaction_recovery_ready=true/false
semantic_influence_map_present=true/false
gate_to_script_trace_present=true/false
line_to_gate_trace_present=true/false
validation_scorecard_present=true/false
validation_scorecard_status=
final_deliverable_generated=true/false
pilot_prep_allowed=false
pilot_execution_allowed=false
full_render_allowed=false
audio_allowed=false
provider_allowed=false
davinci_allowed=false
```

If `dependencies_complete=true` and `output_phase_started=false`, the route is
stuck in analysis and cannot pass.

If `route_state_capsule_present=true` but `validator_surface_bound=false`, the
route may be documented, but the Batch 4 runtime surface is still not active
enough to declare the new governance layer consumed.

If a media-factory route claims route advancement without an evidence bundle or
without a Chitragupta audit event, the claim is blocked even when the route
manifest and validator list are loaded.

MEDIA_FACTORY_HANDOFF must remain blocked.

It may only advance once the bound route runtime contract, evidence scope
contract, and audit-event contract are all present and referenced by the route
state capsule.

If `compaction_detected=true`, resume from `route_state` and do not restart
boot unless `boot_state_invalid=true`.

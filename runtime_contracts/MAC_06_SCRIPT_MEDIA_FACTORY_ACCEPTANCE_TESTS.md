# MAC-06 Script Media Factory Acceptance Tests

## Purpose

This contract defines the acceptance gates for the `SCRIPT_GENERATION` route
when a script output also carries content-engineering, visual planning, visual
generation draft, or Media Factory handoff requirements.

It exists to keep the route honest:

- A script-only request may stop after the approved script package.
- A script plus visual/media request must prove the requested downstream depth.
- Planning output must not claim provider execution, local rendering, DaVinci
  assembly, FFmpeg export, or created media artifacts unless those artifacts
  exist and the user approved execution.
- File-count telemetry cannot substitute for route-slice completion, semantic
  influence, output phase, and validator proof.

## Activation Scope

```text
route_id=SCRIPT_GENERATION
contract_id=MAC_06_SCRIPT_MEDIA_FACTORY_ACCEPTANCE_TESTS
applies_when_any=
  - script_generation_output
  - content_engineering_output
  - visual_media_plan_requested
  - visual_media_generation_draft_requested
  - media_factory_final_draft_requested
  - media_factory_handoff_requested
  - local_cloud_hybrid_execution_plan_present
  - provider_or_artifact_readiness_claim_present
```

This contract does not authorize media generation. It is an acceptance and
proof contract only.

## Required Upstream Locks

Before the route can pass, the output must prove:

```text
SHADOW_BOOT_CONFIRMATION_present=true
TASK_ROUTE_LOCK_present=true
ROUTE_DEPENDENCY_EXPANSION_LOCK_present=true
selected_route_manifest_read=true
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
CONSUMPTION_LOCK_present=true
dependencies_complete=true
output_phase_started=true
semantic_influence_map_present=true
final_deliverable_generated=true
```

If any required lock is missing, final status is:

```text
FINAL_PROOF_STATUS=BLOCKED
```

## Script Acceptance Gates

For 3-10 minute YouTube scripts, the script package must include:

```text
SCRIPT_LANGUAGE_DECLARATION
SHADOW_MISSION_PACKET
CONTENT_MISSION_BRIEF
RESEARCH_AND_SOURCE_STATUS
SOURCE_LEDGER
FACT_VS_ANECDOTE_MAP
CLAIM_EVIDENCE_STATUS
HOOK_VARIANTS
CINEMATIC_SHORT_STORY_BLOCK
FINAL_SCRIPT
DYNAMIC_TIMED_BEAT_MAP
RECURRING_REHOOK_MAP
VOICE_GENERATION_CONTEXT
IMAGE_GENERATION_CONTEXT
VIDEO_GENERATION_CONTEXT
MUSIC_AND_SFX_CONTEXT
LINE_BY_LINE_INFLUENCE_MAP
VALIDATION_SCORECARD
FINAL_PROOF_CLASSIFICATION
```

The cinematic story block must be 45-75 seconds unless a route-level exception
is documented with evidence.

The recurring re-hook map must keep the default gap under 30 seconds for
3-10 minute YouTube scripts unless a route-level pacing reason is documented.

## Source And Claim Gates

Real-person, real-incident, celebrity, brand, company, or current-world proof
claims require source honesty:

```text
web_used=true -> exact_source_url_or_tool_evidence_required=true
freshness_class=CURRENT -> exact_url_ledger_required=true
real_time_sources_used=false + freshness_class=CURRENT + PASS -> BLOCKED
memory_only_evidence_scope + PASS -> BLOCKED
```

Every production-sensitive claim must use:

```text
claim=
evidence=
evidence_scope=
evidence_path=
command_output_or_file_reference=
status=PASS | BLOCKED | NEEDS_USER_APPROVAL | NEEDS_CONFIRMATION
```

If the evidence is missing, the status must be `NEEDS_CONFIRMATION`, not
`PASS`.

## Visual Media Plan Acceptance Gates

When `visual_media_plan_requested=true`, the output must remain planning-only
and include:

```text
planning_only_mode=true
locked_script_reference_present=true
scene_sync_matrix_present=true
readable_per_scene_breakout_blocks=true
visual_method_distribution_present=true
a_roll_broll_motion_graphics_summary_present=true
cost_distribution_present=true
provider_honesty_gate_present=true
local_cloud_hybrid_boundary_present=true
asset_execution_claimed=false
repo_file_creation_claimed=false_unless_user_approved
```

A flat visual summary cannot pass if scene-level reasoning, visual method,
audio/SFX, editing, provider boundary, and proof fields are absent.

## Visual Generation Draft Acceptance Gates

When `visual_media_generation_draft_requested=true`, the output must include:

```text
script_integrity_lock=PASS
visual_plan_integrity_lock=PASS
asset_generation_order_present=true
scene_level_reasoning_present=true
scene_prompt_packets_present=true
video_motion_prompt_packets_present=true
sfx_timestamp_injection_map_present=true
voice_image_video_music_sfx_lanes_present=true
local_cloud_hybrid_boundary_present=true
provider_honesty_gate_present=true
davinci_ffmpeg_assembly_plan_present=true
qc_proof_registry_present=true
```

The preferred scene format is a readable transposed scene block:

```text
SCENE_ID=
SCENE_METADATA=
SCRIPT_LINE=
| Layer | Detail |
| Visual | ... |
| Audio / SFX | ... |
| Editing / Motion | ... |
| Provider / Local Lane | ... |
| Proof / Dependency | ... |
| Reasoning | ... |
```

The draft cannot pass with only generic SFX prose, generic DaVinci prose, or a
single shallow horizontal table.

## Media Factory Final Draft Acceptance Gates

When `media_factory_final_draft_requested=true`, the output must satisfy:

```text
MEDIA_FACTORY_FINAL_DRAFT_CONTRACT_consumed=true
LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT_consumed=true
LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT_consumed=true
scene_sync_matrix_present=true
production_order_lock_present=true
asset_dependency_graph_present=true
control_panel_execution_plan_present=true
davinci_timeline_packet_present=true
production_proof_gate_present=true
```

The production order must keep planning separate from execution:

```text
provider_execution_allowed=false_unless_user_approved
local_engine_execution_allowed=false_unless_user_approved
media_artifacts_claimed=false_unless_artifact_paths_exist
```

## B-Roll Ratio Gate

For Media Factory final draft or visual generation draft outputs:

```text
cinematic_broll_seconds >= ceil(total_runtime_seconds * 0.12)
```

If the ratio is below 12%, final proof is `BLOCKED` unless the route explicitly
documents that cinematic B-roll is not part of the requested deliverable.

## Packet Ready And Artifact Honesty Gate

`PACKET_READY` is allowed only when the output includes concrete artifact or
payload evidence:

```text
DaVinci_Resolve=PACKET_READY -> davinci_project_or_timeline_packet_path_required=true
FFmpeg=PACKET_READY -> ffmpeg_command_or_script_path_required=true
tool_specific_translation_readiness=PACKET_READY -> json_or_yaml_payload_path_required=true
proof_json_claimed=true -> proof_json_path_required=true
export_claimed=true -> export_artifact_path_required=true
```

Without artifact paths or explicit execution proof, the correct classification
is:

```text
TEXT_PLAN_ONLY
```

## Compaction And Route-State Gate

After compaction or continuation, a production-sensitive `PASS` requires:

```text
route_state_capsule_present=true
route_manifest_hash_present=true
files_consumed_present=true
file_hashes_present=true
last_completed_lock_present=true
next_required_lock_present=true
evidence_scope=persisted_route_state_with_hash
```

If the output relies on memory-only continuation, final proof is `BLOCKED` or
`NEEDS_CONFIRMATION`.

## Validator Acceptance

The local validator suite must be runnable without provider execution:

```text
node validators/run_all_validators.cjs --strict
```

Required validator families include:

```text
route_claim_evidence_consistency
source_freshness_url_ledger
packet_ready_artifacts
visual_generation_depth
visual_template_lock
broll_ratio
evidence_scope_claims
route_state_capsule
duplicate_read_guard
output_phase_lock
dominant_failure_classifier
route_scope_telemetry_law
active_skill_contamination
```

If any required validator reports a blocking failure, final proof is
`BLOCKED`.

## Final Acceptance Status

Allowed final classifications:

```text
FINAL_PROOF_STATUS=PASS
FINAL_PROOF_STATUS=BLOCKED
FINAL_PROOF_STATUS=NEEDS_USER_APPROVAL
FINAL_PROOF_STATUS=NEEDS_CONFIRMATION
```

`PASS` is allowed only when the requested depth has been produced, route scope
is complete, semantic influence is proven, and validators do not report
blocking failures.

`NEEDS_CONFIRMATION` must not be upgraded to `PASS` without new evidence.

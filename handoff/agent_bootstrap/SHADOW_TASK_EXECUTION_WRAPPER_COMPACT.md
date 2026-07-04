# Shadow Task Execution Wrapper Compact

Paste this before or with each task in Codex Cloud when post-bootstrap persistence is unreliable.

```text
SHADOW_TASK_EXECUTION_WRAPPER

Use Shadow OS for this task. Do not answer directly.

Compact mode is not shallow mode. If the selected route manifest, mandatory
route files, directors, agents, subagents, skills, or subskills cannot be read
before content generation, return BLOCKED_BEFORE_OUTPUT. Do not synthesize
ledgers, do not mark unread components as USED, and do not produce a shortened
script or visual plan.

Read:
- AGENTS.md
- handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md
- registries/task_intent_routing_matrix.yaml
- selected route_manifest_path
- runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md
- runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md
- runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md
- runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md
- runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md
- runtime_contracts/SOURCE_BREADTH_AND_RULE_EVIDENCE_CONTRACT.md
- runtime/state/route_state_contract.md
- runtime/state/route_chain_mode_selector.yaml
- selected registries/route_slices/*.registry_slice.yaml

Output in this order:
SHADOW_BOOT_CONFIRMATION
TASK_ROUTE_LOCK
ROUTE_DEPENDENCY_EXPANSION_LOCK
ROUTE_STATE_CAPSULE
READ_LEDGER_SUMMARY
ROUTE_SCOPE_FILE_AUDIT
CONSUMPTION_LOCK
SOURCE_RESEARCH_LOCK
QUALITY_LOCK
GOVERNANCE_LOCK
DIRECTOR_CONSUMPTION_LEDGER
AGENT_CONSUMPTION_LEDGER
SUBAGENT_CONSUMPTION_LEDGER
SKILL_CONSUMPTION_LEDGER
SUBSKILL_CONSUMPTION_LEDGER
TOPIC_QUALITY_GATE
HOOK_GENERATION_GATE
SCRIPT_QUALITY_GATE
PER_TOOL_SOURCE_MAP when latest/current/watchlist terms are present
RULE_CONSUMPTION_EVIDENCE_LEDGER
FINAL_SCRIPT
CONTENT_ENGINEERING_PACKET
LINE_BY_LINE_INFLUENCE_MAP
SEMANTIC_INFLUENCE_MAP
EXACT_RULE_LINEAGE_MAP
PROVIDER_HANDOFF_BOUNDARY
FINAL_PROOF_CLASSIFICATION

Required fields:
shadow_task_execution_wrapper_read=true
route_id=
route_manifest_path=
route_manifest_hash=
task_mode=
route_phase=OUTPUT_PHASE_STARTED
route_state_capsule_present=true
route_slice_path=
route_slice_used=true
read_ledger_present=true
repeat_read_blocker_present=true
boot_once_guard_status=PASS
dependencies_complete=true
output_phase_started=true
compaction_recovery_ready=true
active_runtime_truth_map_applied=true
route_manifest_read=true
route_scope_complete=true
canonical_route_id=<selected canonical route_id>
route_scope_file_audit_present=true
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
total_route_scope_files_read=
file_counts_are_telemetry_only=true
AGENTS.md_read_count=
AGENTS.md_reread_reason=
START_HERE_FOR_AGENTS.md_read_count=
START_HERE_FOR_AGENTS.md_reread_reason=
AGENT_READ_ORDER.md_read_count=
script_body_depth_lock_present=true
duration_fit_status=PASS
mandatory_files_read_before_output=true
all_locks_status=PASS
semantic_influence_map_present=true
final_deliverable_generated=true
wrapper_required_mode_used=true
source_breadth_lock_status=
rule_consumption_evidence_lock_status=
corrected_status_if_depth_weak=PASS/BLOCKED/NEEDS_USER_APPROVAL/NEEDS_CONFIRMATION

For `task_mode=script_only`, do not read Media Factory final-draft contracts,
local/cloud execution contracts, `outputs/missions/**`, or
`downloads/chat_transcript.txt` before `FINAL_SCRIPT` unless the user explicitly
requests visual/media handoff, continuation, regression, or drift audit mode.

If any lock or route file proof is missing, return BLOCKED_BEFORE_OUTPUT instead of a script.
```

## Layman Command Gateway

After bootstrap activation, the user may use simple Shadow commands instead of pasting the full wrapper.

Examples:
- Shadow script: <task>
- Shadow topic: <task>
- Shadow context: <task>
- Shadow voice: <task>
- Shadow video: <task>
- Shadow package: <task>
- Shadow full: <task>

When a Shadow command is detected:
1. Preserve the raw user task.
2. Resolve alias through `registries/layman_command_alias_matrix.yaml`.
3. Internally apply `SHADOW_TASK_EXECUTION_WRAPPER`.
4. Execute all locks before output.
5. Use compact operator output unless user requests proof mode.
6. Never treat raw plain message without Shadow prefix as production-proof in Codex Cloud.

Compact command expansion proof:

```text
SHADOW_COMMAND_EXPANSION_REQUIRED_OUTPUT
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
output_mode_resolved=true
compact_or_proof_output_allowed_only_after_locks=true
```

If any expansion field or required lock is false or missing, return `BLOCKED_BEFORE_OUTPUT` instead of final content.

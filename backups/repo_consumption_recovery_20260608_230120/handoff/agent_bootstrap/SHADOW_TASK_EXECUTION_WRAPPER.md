# Shadow Task Execution Wrapper

Use this wrapper before or with each user task in Codex Cloud when persistent bootstrap behavior is not reliable.

`SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md` remains the session activator. This wrapper is the per-task execution guard for `WRAPPER_REQUIRED_COMPATIBLE` environments.

For short manual runs, use `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER_COMPACT.md`. The compact wrapper is valid only when it preserves the same lock order and proof fields.

## Pre-Output Hard Block

The wrapper exists to prevent shallow production output.

If the selected route manifest, mandatory route files, directors, agents,
subagents, skills, or subskills cannot be read before artifact generation, do
not synthesize consumption ledgers and do not produce the requested content.

Return exactly:

```text
BLOCKED_BEFORE_OUTPUT
route_manifest_read=false
route_scope_complete=false
shallow_repo_routing_detected=true
synthetic_consumption_attempted=true/false
missing_required_repo_scope=<comma-separated repo-relative paths>
next_stage=Read missing route scope before generating content
```

"I cannot read all files within the time limit" is a block condition, not
permission to shorten the repo scope.

## Required Output Order

For every wrapped task, output in this exact order:

1. `SHADOW_BOOT_CONFIRMATION`
2. `TASK_ROUTE_LOCK`
3. `ROUTE_DEPENDENCY_EXPANSION_LOCK`
4. `ROUTE_SCOPE_FILE_AUDIT`
5. `CONSUMPTION_LOCK`
6. `SOURCE_RESEARCH_LOCK`
7. `QUALITY_LOCK`
8. `GOVERNANCE_LOCK`
9. `DIRECTOR_CONSUMPTION_LEDGER`
10. `AGENT_CONSUMPTION_LEDGER`
11. `SUBAGENT_CONSUMPTION_LEDGER`
12. `SKILL_CONSUMPTION_LEDGER`
13. `SUBSKILL_CONSUMPTION_LEDGER`
14. `TOPIC_QUALITY_GATE`
15. `HOOK_GENERATION_GATE`
16. `SCRIPT_QUALITY_GATE`
17. `FINAL_SCRIPT`
18. `CONTENT_ENGINEERING_PACKET`
19. `LINE_BY_LINE_INFLUENCE_MAP`
20. `PROVIDER_HANDOFF_BOUNDARY`
21. `FINAL_PROOF_CLASSIFICATION`

For latest/current/watchlist tasks, include `PER_TOOL_SOURCE_MAP` before final output.
For every consumed component, include exact rule evidence, not only role summaries.

## Required Execution Proof

Before `FINAL_SCRIPT`, prove:

```text
route_id=
route_manifest_path=
route_manifest_read=true
route_scope_complete=true
canonical_route_id=SCRIPT_GENERATION
route_scope_file_audit_present=true
startup_docs_read_count=
runtime_contracts_read_count=
registries_read_count=
directors_read_count=
agents_read_count=
subagents_read_count=
skills_read_count=
subskills_read_count=
total_route_scope_files_read=
route_scope_file_paths_listed=true
route_scope_listed_paths_exist=true
script_body_depth_lock_present=true
duration_fit_status=PASS
mandatory_files_read_before_output=true
task_route_lock_status=PASS
route_dependency_expansion_lock_status=PASS
consumption_lock_status=PASS
source_research_lock_status=PASS
quality_lock_status=PASS
governance_lock_status=PASS
source_breadth_lock_status=PASS/BLOCKED/NEEDS_USER_APPROVAL/NEEDS_CONFIRMATION
rule_consumption_evidence_lock_status=PASS/BLOCKED/NEEDS_USER_APPROVAL/NEEDS_CONFIRMATION
per_tool_source_map_present=true/false
source_ledger_structured_rows_present=true/false
fact_vs_anecdote_structured_rows_present=true/false
exact_rule_evidence_present=true/false
exact_rule_lineage_map_present=true/false
corrected_status_if_depth_weak=PASS/BLOCKED/NEEDS_USER_APPROVAL/NEEDS_CONFIRMATION
```

If any lock cannot pass, do not generate the final script. Return:

```text
BLOCKED_BEFORE_OUTPUT
failed_lock=
reason=
missing_files=
next_required_action=
```

## Final Classification Block

Every wrapper-required recovery run must end with:

```text
MAC_06_1J_K_TEST_B_RECOVERY_RUN_STATUS=PASS/BLOCKED/NEEDS_USER_APPROVAL/NEEDS_CONFIRMATION
default_task_execution_previously_failed=true
recovery_prompt_required=true
wrapper_required_mode_used=true
source_breadth_lock_status=
rule_consumption_evidence_lock_status=
corrected_status_if_depth_weak=PASS/BLOCKED/NEEDS_USER_APPROVAL/NEEDS_CONFIRMATION
safe_to_declare_default_bootstrap_mode_onboarded=false
```

## Compatibility Meaning

Native auto-trigger failed.
Bootstrap activation works.
Default post-bootstrap task persistence failed.
Recovery route-scope-lock run passed.

Therefore Codex Cloud reliable mode is:

```text
codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE
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

## Shadow Command Expansion Lock

When this wrapper is applied by the Layman Command Gateway, prove this block before final content:

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

If any field is false or missing, do not produce normal final content. Return:

```text
BLOCKED_BEFORE_OUTPUT
failed_lock=SHADOW_COMMAND_EXPANSION
reason=
missing_fields=
next_required_action=
```

`OPERATOR_MODE` and `PROOF_MODE` are allowed only after route, dependency expansion, consumption, source/research where required, source breadth where required, rule evidence, quality, governance, and provider-boundary locks have been executed.

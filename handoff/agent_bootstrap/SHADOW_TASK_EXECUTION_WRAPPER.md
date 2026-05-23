# Shadow Task Execution Wrapper

Use this wrapper before or with each user task in Codex Cloud when persistent bootstrap behavior is not reliable.

`SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md` remains the session activator. This wrapper is the per-task execution guard for `WRAPPER_REQUIRED_COMPATIBLE` environments.

For short manual runs, use `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER_COMPACT.md`. The compact wrapper is valid only when it preserves the same lock order and proof fields.

## Required Output Order

For every wrapped task, output in this exact order:

1. `SHADOW_BOOT_CONFIRMATION`
2. `TASK_ROUTE_LOCK`
3. `ROUTE_DEPENDENCY_EXPANSION_LOCK`
4. `CONSUMPTION_LOCK`
5. `SOURCE_RESEARCH_LOCK`
6. `QUALITY_LOCK`
7. `GOVERNANCE_LOCK`
8. `DIRECTOR_CONSUMPTION_LEDGER`
9. `AGENT_CONSUMPTION_LEDGER`
10. `SUBAGENT_CONSUMPTION_LEDGER`
11. `SKILL_CONSUMPTION_LEDGER`
12. `SUBSKILL_CONSUMPTION_LEDGER`
13. `TOPIC_QUALITY_GATE`
14. `HOOK_GENERATION_GATE`
15. `SCRIPT_QUALITY_GATE`
16. `FINAL_SCRIPT`
17. `CONTENT_ENGINEERING_PACKET`
18. `LINE_BY_LINE_INFLUENCE_MAP`
19. `PROVIDER_HANDOFF_BOUNDARY`
20. `FINAL_PROOF_CLASSIFICATION`

## Required Execution Proof

Before `FINAL_SCRIPT`, prove:

```text
route_id=
route_manifest_path=
route_manifest_read=true
route_scope_complete=true
mandatory_files_read_before_output=true
task_route_lock_status=PASS
route_dependency_expansion_lock_status=PASS
consumption_lock_status=PASS
source_research_lock_status=PASS
quality_lock_status=PASS
governance_lock_status=PASS
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
MAC_06_1J_K_TEST_B_RECOVERY_RUN_STATUS=PASS/PARTIAL/FAIL
default_task_execution_previously_failed=true
recovery_prompt_required=true
wrapper_required_mode_used=true
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

# MAC-06.1O Layman Command Gateway Report

```text
MAC_06_1O_LAYMAN_COMMAND_GATEWAY_STATUS=PASS

mac06_1n_live_test_recorded=true
layman_command_gateway_contract_created=true
layman_command_alias_matrix_created=true
shadow_output_mode_contract_created=true
quick_commands_guide_created=true
bootstrap_docs_patched=true
wrapper_docs_patched=true
startup_docs_patched=true
mac06_1a_docs_patched=true
validator_patched=true
validator_fixtures_created=true
validator_fixtures_passed=true

shadow_aliases_supported=true
operator_mode_supported=true
proof_mode_supported=true
debug_mode_supported=true
raw_plain_task_still_not_production_proof=true

commit_performed=false
push_performed=false

safe_to_commit_after_user_review=true
safe_to_test_shadow_command_after_commit_push=true
safe_to_declare_default_bootstrap_mode_onboarded=false
safe_to_declare_lightweight_os_onboarded=false
safe_to_start_n8n_execution_bus=false

NEXT_ACTION=User must review MAC-06.1O layman command gateway patch before commit.
```

## Summary

MAC-06.1O converts the long wrapper-required execution prompt into a user-facing command gateway.

The reliable Codex Cloud path is now:

```text
Bootstrap once
→ Shadow <command>: <normal task>
→ internal wrapper route locks
→ operator/proof/debug output mode
```

## Created

- `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md`
- `registries/layman_command_alias_matrix.yaml`
- `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md`
- `handoff/agent_bootstrap/SHADOW_QUICK_COMMANDS.md`
- `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1n_source_breadth_rule_evidence_hardening/MAC_06_1N_WRAPPER_REQUIRED_MODE_LIVE_TEST_RESULT.md`

## Patched

- `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md`
- `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md`
- `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER_COMPACT.md`
- `AGENTS.md`
- `START_HERE_FOR_AGENTS.md`
- `AGENT_STARTUP_PROMPT.md`
- `AGENT_READ_ORDER.md`
- `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
- `AGENT_ANTI_DRIFT_RULES.md`
- MAC-06.1A proof docs
- `validators/validate_mac06_1a_output.py`

## Validator Result

```text
validator_fixture_result=26/26 passed
```

New fixtures:

- `validators/fixtures/mac06_1a_pass_shadow_script_operator_mode.txt`
- `validators/fixtures/expected_pass_shadow_script_operator_mode.json`
- `validators/fixtures/mac06_1a_fail_shadow_alias_without_locks.txt`
- `validators/fixtures/expected_fail_shadow_alias_without_locks.json`
- `validators/fixtures/mac06_1a_partial_operator_mode_missing_source_summary.txt`
- `validators/fixtures/expected_partial_operator_mode_missing_source_summary.json`
- `validators/fixtures/mac06_1a_fail_raw_plain_task_claimed_onboarded.txt`
- `validators/fixtures/expected_fail_raw_plain_task_claimed_onboarded.json`


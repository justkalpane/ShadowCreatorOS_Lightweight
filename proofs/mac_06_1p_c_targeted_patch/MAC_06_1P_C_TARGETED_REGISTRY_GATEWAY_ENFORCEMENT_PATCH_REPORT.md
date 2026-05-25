# MAC-06.1P-C Targeted Registry + Gateway Enforcement Patch Report

MAC_06_1P_C_TARGETED_PATCH_STATUS=PASS

prepatch_truth_status=PASS
safety_snapshot_status=PASS
active_runtime_precedence_patch_status=PASS
registry_pointer_repair_status=PASS
bootstrap_load_order_patch_status=PASS
layman_gateway_enforcement_patch_status=PASS
route_manifest_binding_patch_status=PASS
validator_hardening_patch_status=PASS

## Prepatch Truth

repo_root=/Users/apple/Documents/ShadowCreatorOS_Lightweight
branch=main
head=92ded7e6605e363c687ece5466b9b4f7d8831af0
remote_origin_main=92ded7e6605e363c687ece5466b9b4f7d8831af0
local_matches_remote=true
git_diff_check_pass=true
p_a_evidence_present=true
p_b_plan_present=true
safe_to_patch=true

## Safety Snapshot

tag_created=true
tag_name=mac-06-1p-c-prepatch-92ded7e
commit_tagged=92ded7e6605e363c687ece5466b9b4f7d8831af0
tag_pushed=false

## Patch Summary

files_patched=32
fixtures_created=16
fixtures_passed=34/34
registry_references_repaired=141
registry_references_disabled_missing_file=14
unresolved_registry_references=0
routes_patched=8

## Active Runtime Precedence

`runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md` now defines:

- `ACTIVE_RUNTIME_TRUTH`
- `HISTORICAL_REFERENCE_ONLY`
- `FUTURE_EXECUTION_ONLY`
- `PROOF_ONLY`
- active-language quarantine rules

Old Windows, n8n, provider, archive, proof, and historical rows are not active runtime law unless explicitly connected by active runtime truth.

## Registry Repair

Proof table:

`proofs/mac_06_1p_c_targeted_patch/registry_pointer_repair_table.csv`

Results:

- `sub_agents/` normalized to `subagents/` where replacement files exist.
- stale `agents/*.md` paths in `registries/agent_runtime_selection_index.yaml` repaired to existing Python agent files when a direct slug/class match exists.
- missing/non-obvious agent references marked `DISABLED_MISSING_FILE`.
- missing `agents/maya/maya_agent.py` remains disabled in `agents/AGENT_RUNTIME_REGISTRY.yaml` and `registries/agent_class_matrix.json`; no fake file was created.

## Bootstrap And Gateway Enforcement

Patched startup and wrapper files now require gateway/output/wrapper loading before Shadow command output:

- `AGENTS.md`
- `START_HERE_FOR_AGENTS.md`
- `AGENT_READ_ORDER.md`
- `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md`
- `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md`
- `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md`
- `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md`
- `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER_COMPACT.md`
- `registries/layman_command_alias_matrix.yaml`

Required expansion proof:

```text
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
output_mode_resolved=true
compact_or_proof_output_allowed_only_after_locks=true
```

If any field is false or missing, output must return `BLOCKED_BEFORE_OUTPUT`.

## Route Manifest Binding

All active route manifests under `registries/route_manifests/` now include:

- `trigger_aliases`
- `mandatory_contracts`
- `output_blocks`
- `validator_binding`
- `provider_boundary`
- `status_limits`
- `onboarding_limits`

`SCRIPT_GENERATION` validator binding includes the requested source-map, exact-lineage, provider-boundary, no-execution, and weakest-layer checks.

## Validator Hardening

Patched:

`validators/validate_mac06_1a_output.py`

New checks include:

- `shadow_alias_detected`
- `raw_task_preserved`
- `internal_wrapper_applied`
- `route_manifest_loaded`
- `gateway_contract_loaded_before_alias`
- `output_mode_contract_loaded`
- `registry_paths_exist`
- `route_components_exist`
- `selected_components_are_registered`
- role-summary-only full PASS rejection
- raw plain task onboarding claim rejection
- operator mode without compact proof rejection
- missing provider boundary rejection
- false n8n/provider/media claim rejection

Fixture result:

```text
fixture_count=34
fixtures_passed=34
failed_fixtures=0
```

## Remaining Partial Items

unresolved_blockers=0 in MAC-06.1P-C patch scope
remaining_partial_items=
- Fresh Codex Cloud hostile `Shadow script proof mode:` behavior test is not run in this patch.
- Lightweight OS onboarding remains false until fresh cloud behavior proof passes.
- Codex Cloud primary operator safety remains false until live behavior proof passes.
- n8n/provider/media remain disabled.

safe_to_run_shadow_command_proof_after_commit_push=true
safe_to_commit_after_user_review=true
safe_to_start_n8n=false
safe_to_declare_lightweight_os_onboarded=false

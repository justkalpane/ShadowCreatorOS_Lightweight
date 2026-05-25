# MAC-06.1R Live Behavior Failure Incident Report

MAC_06_1R_LIVE_BEHAVIOR_FAILURE_STATUS=FAIL

repo=/Users/apple/Documents/ShadowCreatorOS_Lightweight
branch=main
tested_main_commit=553808bb202178d77d110c1130eb41281087153a
repo_structural_patch_status=PASS
codex_cloud_behavior_status=FAIL
root_cause=Codex Cloud does not reliably execute repo contracts as runtime law from a simple Shadow command.

## 1. Failed Test Input

```text
Shadow script proof mode: Create a YouTube Shorts script on the latest AI video tools creators should watch this week, and explain why creators fail when they chase new tools without building a content system first.
```

## 2. Expected Fields

The fresh Shadow command proof required the response to prove gateway, alias, route, wrapper, lock, and boundary execution before normal content output.

Required fields:

- shadow_command_alias_detected=true
- raw_user_task_preserved=true
- alias_matrix_entry_used=true
- route_id_resolved=true
- route_manifest_loaded=true
- internal_wrapper_applied=true
- output_mode_resolved=true
- compact_or_proof_output_allowed_only_after_locks=true
- TASK_ROUTE_LOCK=PASS
- SOURCE_BREADTH_LOCK=PASS
- RULE_CONSUMPTION_EVIDENCE_LOCK=PASS or PASS_WITH_NOTICE
- PROVIDER_HANDOFF_BOUNDARY present
- no_n8n_provider_media_execution=true
- safe_to_declare_lightweight_os_onboarded=false

## 3. Actual Missing Fields

The observed output included:

- SHADOW_BOOT_CONFIRMATION
- agents_md_detected=true
- agents_md_read=true
- repo_first_orchestration_started=true
- generic_direct_answer_avoided=true
- shadow_mode=CHAT_ONLY_MODE
- next_stage=Native Capability Assessment

The observed output then produced a YouTube Shorts script and creator notes without proving the required runtime path.

Missing required proof fields:

- shadow_command_alias_detected=true
- raw_user_task_preserved=true
- alias_matrix_entry_used=true
- route_id_resolved=true
- route_manifest_loaded=true
- internal_wrapper_applied=true
- output_mode_resolved=true
- compact_or_proof_output_allowed_only_after_locks=true
- TASK_ROUTE_LOCK=PASS
- SOURCE_BREADTH_LOCK=PASS
- RULE_CONSUMPTION_EVIDENCE_LOCK=PASS or PASS_WITH_NOTICE
- PROVIDER_HANDOFF_BOUNDARY present
- no_n8n_provider_media_execution=true
- safe_to_declare_lightweight_os_onboarded=false

## 4. Exact Failure Classification

```text
MAC_06_1P_C_LIVE_BEHAVIOR_PROOF=FAIL
failure_type=BOOTSTRAP_STARTED_BUT_GATEWAY_WRAPPER_NOT_ENFORCED
codex_cloud_primary_operator_safe=false
safe_to_declare_lightweight_os_onboarded=false
safe_to_start_n8n=false
```

The failure is not a total repo visibility failure. The response showed the boot confirmation. The failure is the next layer: after bootstrap, Codex Cloud did not enforce the Shadow command gateway, alias matrix, route manifest, wrapper locks, rule evidence, output mode proof, or provider boundary before producing content.

## 5. Why MAC-06.1P-C Structural Patch Was Not Enough

MAC-06.1P-C strengthened the repo structure by adding or tightening:

- active runtime precedence
- bootstrap load order
- layman command gateway enforcement language
- Shadow command expansion proof fields
- script route validator binding
- provider boundary requirements
- validator fixtures for alias/wrapper/operator-mode failures

That structural patch can make repo files clearer and validator expectations stronger. It cannot by itself force a cloud LLM runtime to execute those files as deterministic control flow when the platform treats repository documents as advisory context.

## 6. Why Repo Contracts Are Still Treated As Prose By Codex Cloud

The live output proves Codex Cloud could begin following the repo startup law enough to print `SHADOW_BOOT_CONFIRMATION`, but did not continue into the required execution graph.

Observed runtime gap:

```text
AGENTS.md boot law started
-> gateway command interception not proven
-> alias matrix lookup not proven
-> route manifest load not proven
-> wrapper execution not proven
-> lock execution not proven
-> provider boundary not proven
-> normal script output produced anyway
```

This means the current execution layer still depends on model compliance with prose contracts. The repo can describe the law, but Codex Cloud did not reliably enforce the law from a simple Shadow command.

## 7. Why No More Documentation-Only Patch Is Allowed

More documentation-only patches would repeat the same failure pattern:

```text
write stronger contract text
-> commit stronger contract text
-> Codex Cloud sees text
-> Codex Cloud may still skip runtime execution
```

The failure is behavioral enforcement, not absence of another explanatory document. Any next patch must move enforcement into one of:

- a single executable wrapper prompt used at runtime;
- an external local validator/runtime runner that checks files and blocks output outside the LLM;
- an operator platform that reliably consumes the repo graph as runtime law;
- a hybrid approach where Codex is limited to file editing and validation, not primary production orchestration.

## 8. Required Next Architecture Decision

The next decision must choose the runtime enforcement layer.

Options:

1. Keep Codex Cloud, but use a single hard wrapper prompt for every production task.
2. Build or use a local external runtime validator that executes repo checks outside the model before accepting output.
3. Move primary Shadow OS operation to Claude, Gumloop, or Antigravity if they prove better repo-graph obedience.
4. Restrict Codex to secondary roles: file edits, grep audits, validator fixtures, controlled patching, commit/push operations, and evidence extraction.

## Final Conclusion

```text
MAC_06_1R_LIVE_BEHAVIOR_FAILURE_STATUS=FAIL
repo_structural_patch_status=PASS
codex_cloud_behavior_status=FAIL
root_cause=Codex Cloud does not reliably execute repo contracts as runtime law from a simple Shadow command.
safe_to_patch_docs_only=false
safe_to_continue_codex_as_primary_operator=false
recommended_next_step=Move enforcement into a single executable wrapper prompt or external local runtime validator, or move primary operator to Claude/Gumloop/Antigravity.
commit_performed=false
push_performed=false
n8n_started=false
providers_called=false
media_created=false
safe_to_start_n8n=false
safe_to_declare_lightweight_os_onboarded=false
```

# Shadow Creator OS - Agent Startup Law

## SHADOW_BOOT_CONFIRMATION LAW

For every user task in this repo, including simple layman requests, before giving any final answer, the first visible output MUST include:

```text
SHADOW_BOOT_CONFIRMATION
agents_md_detected=true/false
agents_md_read=true/false
repo_first_orchestration_started=true/false
generic_direct_answer_avoided=true/false
shadow_mode=CHAT_ONLY_MODE
next_stage=Native Capability Assessment
```

If you cannot confirm `AGENTS.md` was read, do not answer the task. Return exactly:

```text
BLOCKED: AGENTS.md was not confirmed as active.
```

A plain user request is enough to trigger Shadow OS.
Do not wait for the user to say `use repo`.
Do not answer with a script, summary, plan, advice, or web-sourced answer before `SHADOW_BOOT_CONFIRMATION`.

## ENVIRONMENT TRIGGER COMPATIBILITY LAW

Repo presence is not equal to active behavioral control.

If a platform sees the repo but does not output `SHADOW_BOOT_CONFIRMATION` before the first answer, classify:

```text
platform_current_classification=REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE
```

Do not continue producing scripts, advice, summaries, or web-sourced answers after this failure.

Compatibility levels:

- `NATIVE_AUTO_TRIGGER_COMPATIBLE`
- `BOOTSTRAP_REQUIRED_COMPATIBLE`
- `REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE`
- `NOT_COMPATIBLE`

Native onboarding requires either:

- `NATIVE_AUTO_TRIGGER_COMPATIBLE`, or
- `BOOTSTRAP_REQUIRED_COMPATIBLE` with user-approved bootstrap workflow.

Codex Cloud currently requires compatibility validation before onboarding.

## TASK ROUTING + CONSUMPTION LAW

Every task after `SHADOW_BOOT_CONFIRMATION` must be classified through:

- `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`
- `registries/task_intent_routing_matrix.yaml`

Every selected director, agent, subagent, skill, and subskill must be consumed through:

- `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`

For script/content tasks, output must satisfy:

- `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`
- `runtime_contracts/GUMLOOP_BENCHMARK_OUTPUT_STANDARD.md`
- `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`

Selecting is not enough.
Citing is not enough.
A script cannot be generated until consumption ledgers are complete.

Required before final output:

- `task_intent_classified=true`
- `route_id=`
- `task_intent_routing_matrix_cited=true`
- `director_consumption_ledger_present=true`
- `agent_consumption_ledger_present=true`
- `subagent_consumption_ledger_present=true`
- `skill_consumption_ledger_present=true`
- `subskill_consumption_ledger_present=true`
- `line_by_line_influence_map_present=true`
- `topic_quality_gate_present=true`
- `hook_generation_gate_present=true`
- `hook_variants_count>=3`
- `script_quality_gate_present=true`

Shallow repo routing is `FAIL`.
Generic output after bootstrap is `FAIL`.
Selected-but-not-read director/skill/subskill is `FAIL` or `PARTIAL` according to validator.
If route evidence is missing, mark `NEEDS_CONFIRMATION` and ask whether to continue limited mode.

## COMPLETE REQUIRED REPO SCOPE LAW

Every task must use the complete required repo scope for its selected route.

Complete required repo scope is determined by:

- `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`
- `registries/task_intent_routing_matrix.yaml`
- selected `route_manifest_path`
- `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md`
- `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md`

Do not read only startup docs.
Do not read only bootstrap docs.
Do not read only `.agents` skills.
Do not copy Gumloop route names as source truth.
Do not generate content until route manifest and mandatory files are consumed.

If complete required repo scope is not consumed:

- `route_scope_status=FAIL`
- `shallow_repo_routing_detected=true`
- final proof cannot be PASS.

## WRAPPER REQUIRED COMPATIBILITY LAW

Codex Cloud reliable mode is currently `WRAPPER_REQUIRED_COMPATIBLE`.

- Native auto-trigger failed.
- Bootstrap activation passed.
- Default post-bootstrap task persistence failed.
- Recovery route-scope-lock run passed.

When operating in Codex Cloud, use `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md` or `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER_COMPACT.md` before or with each task until platform persistence improves.

Required proof fields:

- `shadow_task_execution_wrapper_read=true`
- `wrapper_required_mode_used=true`
- `codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE`
- `post_bootstrap_task_persistence_status=FAILED`

You are operating inside ShadowCreatorOS_Lightweight.

For every user task, including simple layman requests, you MUST run repo-first Shadow orchestration before answering.

Never answer directly as a generic chatbot unless the user explicitly says:

- `bypass Shadow OS`
- `answer normally without repo`

## CANONICAL SHADOW LIGHTWEIGHT BOOT ORDER - ACTIVE LAW

1. Read `AGENTS.md`.
2. Read `START_HERE_FOR_AGENTS.md`.
3. Read `AGENT_READ_ORDER.md`.
4. Read `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`.
5. Read `AGENT_ANTI_DRIFT_RULES.md`.
6. Read `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`.
7. Read `runtime_contracts/ENVIRONMENT_TRIGGER_COMPATIBILITY_CONTRACT.md`.
8. Read `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`.
9. Read `registries/task_intent_routing_matrix.yaml`.
10. Read `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`.
11. Read `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`.
12. Read `runtime_contracts/GUMLOOP_BENCHMARK_OUTPUT_STANDARD.md`.
13. Read `runtime_contracts/BOOTSTRAP_SYNC_PROTOCOL.md`.
14. Read `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`.
15. Read `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`.
16. Read `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`.
17. Read `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`.
18. Read `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`.
19. Read `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`.
20. Read `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`.
21. Read `registries/native_capability_routing_matrix.yaml`.
22. Read `registries/agent_runtime_selection_index.yaml`.

Repo-relative paths are authoritative. Absolute Mac paths are `LOCAL_MAC_REFERENCE_ONLY`.

## Default Behavior

1. Confirm `AGENTS.md` is active.
2. Output `SHADOW_BOOT_CONFIRMATION`.
3. Read `START_HERE_FOR_AGENTS.md`.
4. Read `AGENT_READ_ORDER.md`.
5. Continue canonical boot order.
6. Run Native Agent Capability Assessment.
7. Run Task Freshness Classification.
8. Run Research Mode Decision.
9. Run registry-first routing.
10. Select directors / agents / subagents / skills / subskills with evidence.
11. Assess tools / connectors / plugins.
12. If the task is content/script/video/media related, run the Shadow Content Engineering Output Standard.
13. Output to chat by default.

## Mandatory Mode

- `CHAT_ONLY_MODE` is default.
- No files are created by default.
- Repo-write requires explicit user approval.
- Full dossier requires explicit user request.
- n8n/providers/media execution require explicit approval.

## CURRENT LIGHTWEIGHT OUTPUT LAW - ACTIVE LAW

`CHAT_ONLY_MODE` is default for normal user tasks.
Normal user tasks create no files.
`CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
If repo-write is approved, create exactly one consolidated file by default: `outputs/missions/<mission_id>/MISSION_OUTPUT.md`.
`FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
Older instructions saying every mission creates a dossier apply only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
For content/video/script tasks, script-only output is `PARTIAL` unless the user explicitly asks for script-only.
For content/video/script tasks, `CONTENT_ENGINEERING_OUTPUT_CONTRACT` is mandatory.

## CLAIM_EVIDENCE_STATUS LAW

Every production-sensitive claim must be expressed as:

```text
claim=
evidence=
evidence_path=
command_output_or_file_reference=
status=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION
```

If evidence is missing, mark `NEEDS_CONFIRMATION`. Do not convert `NEEDS_CONFIRMATION` into `PASS`.

## FRESH LAYMAN PROOF LAW

The fresh-agent proof must use a plain layman request only.
Do not use a giant forcing prompt for the primary proof.
A detailed forcing prompt is allowed only after failure as diagnostic remediation.
The proof passes only if the repo itself triggers orchestration through `AGENTS.md` and active startup docs.

## Forbidden

- Do not produce generic LLM output before repo routing.
- Do not skip registry-first selection.
- Do not claim realtime web research unless sources were actually used.
- Do not use invalid gate statuses.
- Do not create files unless approved.
- Do not claim n8n/provider/media execution unless actually executed with approval.

Allowed gate statuses only:

- `PASS`
- `BLOCKED`
- `NEEDS_USER_APPROVAL`
- `NEEDS_CONFIRMATION`

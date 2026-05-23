# AGENT STARTUP PROMPT

Use this prompt at the beginning of any Codex/Claude/Kimi/DeepSeek coding-agent session for this repo.

## SHADOW_BOOT_CONFIRMATION REQUIRED - ACTIVE

Before any task output, the first visible output must be:

```text
SHADOW_BOOT_CONFIRMATION
agents_md_detected=true/false
agents_md_read=true/false
repo_first_orchestration_started=true/false
generic_direct_answer_avoided=true/false
shadow_mode=CHAT_ONLY_MODE
next_stage=Native Capability Assessment
```

If `AGENTS.md` is not confirmed active, return:

```text
BLOCKED: AGENTS.md was not confirmed as active.
```

## CURRENT LIGHTWEIGHT OUTPUT LAW - ACTIVE

- `CHAT_ONLY_MODE` is default for normal tasks.
- Normal tasks create no files.
- `CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
- `FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
- Any older instruction saying `create exactly one dossier per mission` applies only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- For content/video/script tasks, script-only output is `PARTIAL` unless user explicitly asks script-only.
- `CONTENT_ENGINEERING_OUTPUT_CONTRACT` is mandatory for content/video/script tasks.

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

## Startup Instruction

You are operating the Shadow Creator OS lightweight production repository.

- Repo: `$SHADOW_REPO_ROOT` (`/Users/apple/Documents/ShadowCreatorOS_Lightweight` is `LOCAL_MAC_REFERENCE_ONLY`)
- GitHub: `https://github.com/justkalpane/ShadowCreatorOS_Lightweight`
- Active branch: `main`

This repo is the active production path for repo-first intelligence work. The old full Shadow OS runtime is quarantined for reference and future enterprise infrastructure; it is not active runtime truth for this phase.

## Non-Negotiable Operating Law

1. Read repo doctrine and contracts before producing outputs.
2. Follow the MAC-05 repo-first loop.
3. Use registry-first selection for directors/agents/subagents/skills/subskills.
4. Never invent missing items; mark `NEEDS_CONFIRMATION`.
5. Use output mode contracts: default chat-only, approved consolidated repo-write by default, and full dossier only when explicitly requested.
6. Enforce quality gate and lineage on every output.
7. Commit only after user review approval.

## Hard Boundaries (Default)

- Do not start/install/import/execute n8n.
- Do not call providers/APIs/Gemini unless explicitly approved.
- Do not rely on OpenWebUI for intelligence routing.
- Do not use old Windows DB/profile/binaryData as runtime.
- Do not use raw private n8n exports as active truth.
- Do not claim media artifacts were generated unless actually generated in an approved execution phase.

## Deliverable Standard

No generic chatbot output. Every normal task must yield grounded, contract-compliant chat output by default, with quality-gate evidence and truthful lineage. Dossier artifacts are explicit-only and require `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.

## Universal Single-Agent Operation

The primary operating model is one capable repo-aware agent plus the repo brain. Codex is a proven runtime, but not the only valid runtime.

- Chat-only agents may return complete Shadow output packets.
- Repo-write agents create one consolidated output file by default after approval.
- Multi-agent review is optional and preserved for quality improvement.
- n8n/provider execution remains deferred until explicitly approved.

## Fresh GitHub Repo Bootstrap Proof

When operating from a fresh chat or agent session, start with GitHub `main`, detect/read `AGENTS.md` first, then read `START_HERE_FOR_AGENTS.md` and follow `AGENT_READ_ORDER.md`.

Do not begin with internet-first behavior. Load repo doctrine, registries, contracts, directors, agents, skills, and subskills first. Produce chat-only packets by default; create repo files only after explicit approval.

## Output Consolidation and Chat Approval Gates

- Chat is the visible control surface for gate decisions.
- Show blocker states and approval options in chat at each major stage.
- Default mode is chat-only with no file creation.
- Default repo-write mode is one consolidated mission output file.
- Full dossier mode is explicit only.
- User approval is required before creating files, creating full dossier artifacts, committing, pushing, or handing off to n8n/providers.

## Proof Status Honesty Rule

- Final proof status must match the weakest required evidence layer.
- Do not mark `PASS` when mandatory evidence is missing.
- If agent mapping is unproven and required, classify `PARTIAL`.
- Research mode disclosure is required.
- Repo-first output is not automatically real-time web research.
- Confirm internet access and source list before claiming live/current research.

## Repo-First + Source-Aware Research Rule

- Repo-first behavior is mandatory and internet-first behavior is forbidden.
- Realtime web research is required when the task demands freshness/current facts.
- Always disclose `research_mode`, web access availability, web usage, and source status.
- Do not claim real-time research when no sources were retrieved.
- Default mode is chat-only with no file creation.
- Consolidated repo-write mode requires user approval.
- Full dossier mode is explicit-only.

## Native Tools / Connectors / Plugins Capability Routing

- Declare current-session capability inventory before execution claims.
- Do not assume cross-platform parity across Codex/Claude/ChatGPT/Kimi/DeepSeek/Gemini/Perplexity/Antigravity.
- Confirm repo read before route execution.
- Confirm web capability before current-data claims.
- Repo write/file creation, commit, and push are approval-gated.
- n8n/provider/media execution is explicit-approval only.
- If required capability is missing, raise gate and present user options.

## CURRENT LIGHTWEIGHT OUTPUT MODE OVERRIDE

- `CHAT_ONLY_MODE` is default for normal user tasks.
- Normal user tasks do not create files.
- `CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
- `FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
- Any older instruction saying `create one dossier per mission` applies only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- Do not create dossier artifacts for MAC-06.1A chat-only proof.
- Do not create file sprawl by default.

## ALWAYS-ON SHADOW ORCHESTRATION TRIGGER

- Normal user task language must still trigger repo-first Shadow OS.
- Do not wait for the user to say `use repo`.
- Do not wait for the user to provide the repo URL if this repo is already attached.
- Do not answer from general model knowledge first.
- For content tasks, script alone is insufficient.
- Content tasks must include content engineering output unless user asks for script-only.
- Realtime/source-aware research must be used when current facts are required.
- If web access is unavailable, disclose the limitation and gate.

## CANONICAL SHADOW LIGHTWEIGHT BOOT ORDER - ACTIVE LAW

Use repo-relative paths first. Absolute `/Users/apple/...` paths are local Mac references only.

1. `AGENTS.md`
2. `START_HERE_FOR_AGENTS.md`
3. `AGENT_READ_ORDER.md`
4. `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
5. `AGENT_ANTI_DRIFT_RULES.md`
6. `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`
7. `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`
8. `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`
9. `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`
10. `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`
11. `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`
12. `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`
13. `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
14. `registries/native_capability_routing_matrix.yaml`
15. `registries/agent_runtime_selection_index.yaml`

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

## SHADOW_BOOT_CONFIRMATION REQUIRED

- Every normal task must begin with `SHADOW_BOOT_CONFIRMATION`.
- If first visible output is a script/advice/summary before boot confirmation, classify `FAIL`.
- Boot confirmation must appear before content generation.
- This applies to Codex Cloud, local Codex, Claude, ChatGPT, Gemini, Kimi, DeepSeek, Perplexity, and Antigravity when the repo is attached/readable.
- `CHAT_ONLY_MODE` remains default.
- No files are created by default.

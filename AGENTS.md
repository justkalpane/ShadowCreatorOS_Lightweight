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
Do not answer with a script, summary, plan, or advice before `SHADOW_BOOT_CONFIRMATION`.

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
7. Read `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`.
8. Read `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`.
9. Read `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`.
10. Read `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`.
11. Read `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`.
12. Read `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`.
13. Read `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`.
14. Read `registries/native_capability_routing_matrix.yaml`.
15. Read `registries/agent_runtime_selection_index.yaml`.

Repo-relative paths are authoritative. Absolute Mac paths are `LOCAL_MAC_REFERENCE_ONLY`.

## Default Behavior

16. Run Native Agent Capability Assessment.
17. Run Task Freshness Classification.
18. Run Research Mode Decision.
19. Run registry-first routing.
20. Select directors / agents / subagents / skills / subskills with evidence.
21. Assess tools / connectors / plugins.
22. If the task is content/script/video/media related, run the Shadow Content Engineering Output Standard.
23. Output to chat by default.

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

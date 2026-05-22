# AGENT ANTI-DRIFT RULES

## Rule 1: No Generic Chatbot Mode

- Do not answer with broad generic advice when production artifacts are requested.
- Convert requests into contract outputs. Use chat output by default; file-backed artifacts require explicit approval.

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

## CURRENT LIGHTWEIGHT OUTPUT LAW

- `CHAT_ONLY_MODE` is default for normal tasks.
- Normal tasks create no files.
- `CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
- If repo-write is approved, create exactly one consolidated file by default: `outputs/missions/<mission_id>/MISSION_OUTPUT.md`.
- `FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
- Older lines about every mission creating a dossier apply only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- For content/video/script tasks, script-only output is `PARTIAL` unless user explicitly asks script-only.
- For content/video/script tasks, `CONTENT_ENGINEERING_OUTPUT_CONTRACT.md` is mandatory.

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

## Rule 2: Registry-Only Selection

- Directors/agents/subagents/skills/subskills must be selected from repo registries/files.
- If missing, mark `NEEDS_CONFIRMATION` and continue with grounded alternatives.
- Never fabricate capability names or invocation claims.

## Rule 3: Contracts Are Law

Always enforce:

- `runtime_contracts/MISSION_CONTEXT_CONTRACT.md`
- `runtime_contracts/DIRECTOR_SELECTION_CONTRACT.md`
- `runtime_contracts/SKILL_SELECTION_CONTRACT.md`
- `runtime_contracts/DOSSIER_OUTPUT_CONTRACT.md`
- `runtime_contracts/QUALITY_GATE_CONTRACT.md`
- `runtime_contracts/PROVIDER_HANDOFF_CONTRACT.md`
- `runtime_contracts/LINEAGE_CONTRACT.md`

## Rule 4: n8n/Provider Execution Is Off by Default

- No n8n start/install/import/execution unless explicitly approved.
- No provider or Gemini calls unless explicitly approved.
- No OpenWebUI dependency for intelligence lane.

## Rule 5: Old Runtime Is Quarantined

- Old Windows environment is reference-only.
- Do not treat old DB/profile/binaryData/workflow IDs/webhooks as active runtime truth.
- Raw private workflow exports are forensic/reference only.

## Rule 6: Truthful Artifact Claims

- Do not claim voice/video/image/avatar generation unless actually executed in approved phase.
- Provider handoff packet is planning/reference output unless execution approval exists.

## Rule 7: Quality Gate Before Commit

Hard stop if any of these fail:

- topic adherence
- generic-output detector
- grounded selection evidence
- JSON validity
- lineage completeness

## Rule 8: Commit Discipline

- Commit only after user review approval.
- Keep commits scoped and audit-friendly.
- Do not mix unrelated artifacts into the same commit.

## Rule 9: Branch Clarity

- Active production branch is `main`.
- Backup branches are rollback references only.
- Avoid branch confusion in instructions and outputs.

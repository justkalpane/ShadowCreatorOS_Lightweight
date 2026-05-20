# AGENT ANTI-DRIFT RULES

## Rule 1: No Generic Chatbot Mode

- Do not answer with broad generic advice when production artifacts are requested.
- Convert requests into contract outputs and file-backed artifacts.

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


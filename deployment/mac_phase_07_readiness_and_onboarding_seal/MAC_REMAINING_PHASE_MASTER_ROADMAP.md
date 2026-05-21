# MAC Remaining Phase Master Roadmap

This roadmap locks the remaining phase order and prevents shortcut drift.

## MAC-06: Multi-agent review lane planning

- Status: Planning created, commit pending.
- Purpose: Define review lane structure only.
- Execution: Not allowed in this phase.

## MAC-06.1: First controlled multi-agent review proof

- Purpose: Run one reviewer-lane test against an existing dossier.
- Gate: Allowed only after MAC-06 planning commit.
- Boundary: No n8n/providers/media execution.

## MAC-06.2: Codex reviewer-finalization proof

- Purpose: Codex applies only user-approved review changes.
- Required checks: JSON validity, quality gate, lineage truth.
- Boundary: No unapproved edits.

## MAC-07: Repo-first production readiness seal

- Purpose: Final readiness proof for repo-first production onboarding.
- Must verify:
  - GitHub `main` active for lightweight repo
  - Agent doctrine present and committed
  - Historical docs indexed and reconciled
  - Production Dossier #2 and #3 pushed
  - MAC-06.1 and MAC-06.2 proven
  - Clean git state
  - No n8n/provider drift

## MAC-08: Agent onboarding package

- Purpose: Final onboarding pack for Codex/Claude/Kimi/DeepSeek.
- Must include:
  - repo URL
  - branch `main`
  - required read order
  - review packet contract
  - MAC-05 production rules
  - MAC-06 review rules
  - execution boundaries

## MAC-09: Future n8n execution bus planning

- Purpose: Plan fresh Mac n8n execution bus.
- Boundary: No install/import/execution in this phase.

## MAC-10: Fresh Mac n8n installation gate

- Purpose: Install and verify n8n after explicit approval.
- Note: Not required for repo-first production onboarding.

## MAC-11: Selected workflow import proof

- Purpose: Review/import only selected sanitized workflows after manual classification.
- Boundary: No raw private export import.

## MAC-12: Provider/media execution pilot

- Purpose: Voice/image/video/provider execution after cost gates, credentials, and approval.

## Classification

- Required before lightweight onboarding declaration:
  - MAC-06 (commit)
  - MAC-06.1
  - MAC-06.2
  - MAC-07
  - MAC-08
- Future execution-bus phases (not required for repo-first onboarding):
  - MAC-09
  - MAC-10
  - MAC-11
  - MAC-12


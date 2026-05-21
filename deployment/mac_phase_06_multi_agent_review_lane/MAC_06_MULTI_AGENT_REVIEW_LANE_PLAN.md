# MAC-06 Multi-Agent Review Lane Plan

## Objective

Define a controlled review lane where Codex remains the primary production operator and optional reviewer agents (Claude/Kimi/DeepSeek/others) improve dossier quality without violating repo-first doctrine.

## Scope

Planning only. No review execution, no dossier creation, no n8n/provider/runtime actions.

## Workflow

1. Codex creates dossier under MAC-05 contract.
2. User performs first review.
3. User optionally requests reviewer lanes.
4. Reviewer agent receives:
   - repo path
   - branch
   - dossier path
   - review packet contract
   - scorecard standard
5. Reviewer checks:
   - topic adherence
   - generic output risk
   - director grounding
   - skill grounding
   - script quality
   - context packet quality
   - provider handoff quality
   - lineage truth
6. Reviewer returns a structured review packet.
7. User approves accepted changes.
8. Codex applies only approved changes.
9. Codex re-validates JSON + quality gates.
10. Commit after user approval.

## Inputs

- Dossier path
- Topic + platform + audience constraints
- Runtime contracts
- Active doctrine files
- Reviewer prompt template

## Outputs

- Reviewer packet(s)
- Updated dossier (if approved changes applied)
- Final quality gate delta
- Commit-ready state

## Hard Boundaries

- No n8n execution/install/import.
- No provider or Gemini calls.
- No OpenWebUI dependency.
- No old Windows runtime activation.
- No raw private export usage.
- No false media generation claims.

## Review and Commit Gates

- Overall score >= 8.0
- No critical grounding failures
- No JSON validation failures
- No false execution/media claims
- User approval before commit


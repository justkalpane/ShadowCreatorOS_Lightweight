# Repo-Write Operation Contract

Coding agents with filesystem access can operate in repo-write mode.

## Required Actions

- Create one dossier folder.
- Create required dossier files.
- Validate JSON packets.
- Create/update quality gate report.
- Create/update lineage.
- Wait for user approval before commit/push.

## Required Boundaries

- Never push without user approval.
- Never execute n8n/providers unless explicitly approved.
- Never use old Windows runtime as active truth.
- Never claim media artifacts unless actually generated in an approved execution phase.

## Commit Gate

Commit only after:

- user review approval
- JSON validation pass
- quality gate pass
- forbidden file scan pass

## MAC-06.1B Governance Addendum

- Future repo-write proof defaults to one consolidated output file, not multi-file dossier.
- Full dossier mode requires explicit user approval.
- Chat output must include approval gate blocks before file creation.
- User approval is required before file creation, commit, push, or provider handoff.

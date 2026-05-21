# MAC Do Not Skip Phases Rule

This repository follows strict sequential phase discipline.

## Rule

- Do not skip defined gates.
- Do not declare onboarding complete before MAC-08 is complete.
- Do not start execution-bus phases before explicit transition approval.

## Why

- Prevents drift back into heavy-runtime instability.
- Preserves clean audit lineage and trustable readiness claims.
- Keeps repo-first production stable while execution layers remain deferred.

## Enforcement

- Every phase must produce a result report.
- Every report must be committed and pushed before the next phase.
- Any deviation must be explicitly approved by user and documented.


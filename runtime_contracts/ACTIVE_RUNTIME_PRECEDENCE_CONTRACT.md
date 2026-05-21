# Active Runtime Precedence Contract

Current runtime precedence order:

1. User explicit instruction
2. Runtime safety boundaries
3. Output consolidation and chat approval gates
4. Source-aware research gate
5. Proof status honesty
6. MAC-06.1A proof contract
7. MAC-05 full dossier contract only when full dossier mode is explicitly approved
8. Historical handoff/migration/build docs are reference only

## Mode Clarification

- Old handoff rules that say one dossier per mission are historical unless `FULL_DOSSIER_ARCHIVE_MODE` is explicitly requested.
- `CHAT_ONLY_MODE` creates no files by default.
- `CONSOLIDATED_REPO_WRITE_MODE` creates one consolidated output file only after user approval.
- `FULL_DOSSIER_ARCHIVE_MODE` is explicit-only.

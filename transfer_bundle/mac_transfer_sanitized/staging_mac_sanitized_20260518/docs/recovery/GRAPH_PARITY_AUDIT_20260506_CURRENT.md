# GRAPH PARITY AUDIT 2026-05-06 CURRENT

## Scope
- Repo: `C:\ShadowEmpire-Git_Restore_01`
- Active profile: `C:\ShadowEmpire\n8n_user_restore_01`
- Active DB: `C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite`
- Mode: Repo-only graph mirror synchronization (no runtime DB edits/imports)

## Architecture verdict
- WF-010 direct 7-pack chain is correct: WF-100, WF-200, WF-300, WF-400, WF-500, WF-600, WF-020.
- CWF chains remain nested under pack workflows.

## Commit-6 sync scope
- n8n/workflows/WF-010.json
- n8n/workflows/WF-020.json
- n8n/workflows/WF-300.json
- n8n/workflows/WF-400.json
- n8n/workflows/WF-500.json
- n8n/workflows/WF-600.json

## Backup
- Backup path: C:\ShadowEmpire\workflow_graph_ref_sync_backup\20260507_074458

## Notes
- WF-100/WF-200 were already in parity and were intentionally not patched.
- This is a repo mirror repair to align restore source with live working graph.

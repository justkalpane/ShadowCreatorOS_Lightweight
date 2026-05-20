# FINAL RECOVERY BRANCH STATUS (2026-05-07)

## 1) Pushed Branch
- Remote branch: `origin/recovery/runtime-lock-20260506`
- Latest pushed commit: `3160292afaac68a4bca936fb55a2b66530d3e1c1`
- Main branch push/merge status: `main untouched`

## 2) Clean Recovery Commit Stack
1. `85dec0a` - fix: lock n8n runtime profile and add recovery hardening evidence
2. `fc0f0fa` - fix: repair workflow child references for WF-010 WF-100 and WF-200
3. `e57ff64` - chore: normalize workflow repoRoot paths to Restore_01
4. `37274cc` - fix: repair proven operator surfaces and canonical API wiring
5. `7a02a9a` - docs: add operator runbooks and recovery evidence
6. `9be3149` - docs: add production reference manuals and roadmap
7. `3160292` - fix: sync workflow graph refs with live Restore_01 runtime

## 3) Production Runtime Paths (Canonical)
- Production repo: `C:\ShadowEmpire-Git_Restore_01`
- n8n profile: `C:\ShadowEmpire\n8n_user_restore_01`
- n8n DB: `C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite`
- n8n WAL: `C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite-wal`
- Old wrong profile (must remain absent): `C:\ShadowEmpire\n8n_user`

## 4) Canonical Local Endpoints
- n8n UI: `http://127.0.0.1:5678/home/workflows`
- n8n base: `http://127.0.0.1:5678`
- Operator API (canonical): `http://localhost:5002`
- Operator health: `http://localhost:5002/operator/health`
- Open WebUI: `http://localhost:3000`
- Ollama: `http://localhost:11434`

## 5) Recovered State (What Is Confirmed)
- Runtime/profile recovery completed and locked to Restore_01 profile.
- Canonical workflow set active in runtime.
- WF-010/WF-100/WF-200 repairs completed.
- Repo workflow graph parity synced to live runtime (Commit 6).
- Operator surface hardening committed (non-Command-Center scope).
- Recovery and production documentation stack committed.

## 6) Quarantined State (Intentionally Not Merged)
- Command Center/chat-layer remains quarantined and intentionally excluded from recovery commits:
  - `ui/src/screens/Chat.jsx`
  - `engine/api/chat.js`
  - `engine/chat/chat_orchestration_service.js`
  - `engine/chat/n8n_workflow_client.js`
  - `server.js`

## 7) Do-Not-Touch Rules
- Do not push `main` directly.
- Do not run `git pull`, `git reset --hard`, or `git clean -fd` on this dirty working tree.
- Do not import repo workflows into n8n without explicit controlled plan.
- Do not recreate/use old profile `C:\ShadowEmpire\n8n_user`.

## 8) Merge Recommendation
- Current recommendation: **Do not merge to main yet**.
- Keep `recovery/runtime-lock-20260506` as restore checkpoint branch.
- Open PR/compare review first; merge only after explicit acceptance.

## 9) Remaining Dirty Local Files (Category View)
Local working tree remains intentionally dirty/untracked and local-only.
- Runtime/data/artifact-like: `96`
- Command-center/chat-layer-like: `6`
- Secret-like (`.webui_secret_key`): `1`
- Other local/untracked helpers/exports: `75`

## 10) Next Production Usage Path
Use proven operator surfaces (not Command Center):
1. PowerShell operator scripts (`scripts/operator/*`)
2. Operator API on port `5002`
3. n8n direct UI (`127.0.0.1:5678/home/workflows`)
4. Open WebUI + Ollama for local model workflows

## 11) Current Operational Verdict
- Active runtime: **usable**
- Repo restore safety: **strengthened (post Commit 6)**
- Recovery branch safety checkpoint: **present on GitHub**
- Main branch: **unchanged**

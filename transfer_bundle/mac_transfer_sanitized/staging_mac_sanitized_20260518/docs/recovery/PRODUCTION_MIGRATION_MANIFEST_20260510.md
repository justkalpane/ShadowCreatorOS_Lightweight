# PRODUCTION_MIGRATION_MANIFEST_20260510

## Canonical Production Targets
- Repo: `C:\ShadowEmpire-Git_Restore_01`
- n8n profile: `C:\ShadowEmpire\n8n_user_restore_01`
- Operator API: `http://localhost:5002`
- n8n: `http://127.0.0.1:5678`
- Ollama: `http://localhost:11434`
- Open WebUI: `http://localhost:3000`

## Required Services
1. Ollama runtime
2. n8n runtime (profile locked to `n8n_user_restore_01`)
3. Operator API (`server.js`)
4. Optional Open WebUI runtime

## Required Ports
- `5002` Operator API
- `5678` n8n
- `11434` Ollama
- `3000` Open WebUI (optional surface)

## Startup Order (Canonical)
1. `powershell -ExecutionPolicy Bypass -File .\scripts\windows\start_n8n_shadow_phase1.ps1`
2. `powershell -ExecutionPolicy Bypass -File .\scripts\windows\start_shadow_operator_api.ps1`
3. `powershell -ExecutionPolicy Bypass -File .\scripts\windows\start_openwebui_local_runtime.ps1` (optional)

## Path-Lock Guard
- Guard script: `scripts/windows/assert_restore01_path.ps1`
- Startup scripts call guard before launch.
- Guard enforces git root: `C:/ShadowEmpire-Git_Restore_01`.

## Required Environment/Runtime Settings
- `N8N_USER_FOLDER=C:\ShadowEmpire\n8n_user_restore_01`
- `N8N_STORAGE_PATH=C:\ShadowEmpire\n8n_user_restore_01\.n8n\binaryData`
- `N8N_DEFAULT_BINARY_DATA_MODE=filesystem`
- `N8N_HOST=127.0.0.1`
- `N8N_PORT=5678`
- `N8N_RUNNERS_ENABLED=false`
- `NODE_FUNCTION_ALLOW_BUILTIN=fs,path`
- `NODE_FUNCTION_ALLOW_EXTERNAL=axios`
- Execution persistence enabled (`EXECUTIONS_DATA_SAVE_*`, prune disabled)

## n8n Workflow Activation Requirement
- 22/22 CWF workflows must be active with non-null `activeVersionId`.
- Active CWF code must use `/operator/skill-runtime` and `axios`.
- Active CWF code must not include `fetch(` or direct `skill_loader` imports.

## Validation Commands
1. Path lock:
   - `Set-Location C:\ShadowEmpire-Git_Restore_01`
   - `.\scripts\windows\assert_restore01_path.ps1`
2. Health:
   - `.\scripts\operator\check-shadow-health.ps1`
3. Skill runtime direct:
   - `POST http://localhost:5002/operator/skill-runtime`
4. Creative-chain proof:
   - `powershell -ExecutionPolicy Bypass -File .\scripts\operator\new-content-job.ps1 "<topic>"`
   - `powershell -ExecutionPolicy Bypass -File .\scripts\operator\list-outputs.ps1 <DOSSIER_ID>`

## Proof Dossiers (Examples)
- `DOSSIER-1778409695497-HSA9L9GDY`
- `DOSSIER-1778413615265-NQ6GTQ5WQ`
- `DOSSIER-1778414996783-0NSODRPXU`

## Critical Folders to Copy for New PC
- `C:\ShadowEmpire-Git_Restore_01\` (repo)
- `C:\ShadowEmpire\n8n_user_restore_01\` (profile and DB)

## Folders/Artifacts Not to Copy as Runtime Source-of-Truth
- `C:\ShadowEmpire-Git\` old repo runtime path
- runtime temp/cache/log folders
- old profile paths
- transient dossier output cache if not needed
- secrets must be provisioned separately

## Rollback / Backup Notes
- Reconciliation backup folder used during this pass:
  - `C:\ShadowEmpire\repo_reconciliation_backup\20260510_173412`
- Keep startup script backups before any launcher edits.

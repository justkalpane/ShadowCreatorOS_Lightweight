# Runtime Profile Recovery Correction Report - 2026-05-06

## Verdict
PARTIALLY RECOVERED - n8n runtime profile/path is corrected and active. Full WF-001 -> WF-010 content-chain smoke is still the next proof step.

## Root Cause
The running n8n instance was pointed at `C:\ShadowEmpire\n8n_user`, not the documented May 4 recovery runtime `C:\ShadowEmpire\n8n_user_restore_01`.

Evidence:
- Stale runtime listener before correction: PID 3808, started 2026-05-06 13:00:00.
- Active WAL before correction: `C:\ShadowEmpire\n8n_user\.n8n\database.sqlite-wal`, modified 2026-05-06 13:02:49.
- Plain `n8n_user` DB has canonical workflow IDs like `IG8PekK_Cn4qM6ve` and `5eWEDik6TqWnsMSH`, which do not match May 4 R9 proof IDs.

## Correct Runtime Restored
Launcher corrected to:
- `N8N_USER_FOLDER=C:\ShadowEmpire\n8n_user_restore_01`
- `N8N_STORAGE_PATH=C:\ShadowEmpire\n8n_user_restore_01\.n8n\binaryData`

Active runtime after correction:
- n8n listener PID: 15408
- ports: 5678 and 5679 listening
- active WAL: `C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite-wal`, modified 2026-05-06 13:17:07

## Workflow Proof
Startup log: `C:\ShadowEmpire-Git\runtime_logs\n8n_restore01_start_20260506_131329.log`

The log shows 37 canonical workflows activated, including:
- WF-000 `OhbVrpoiVgRV5IfL`
- WF-001 `BcbfnoGMbJmTPSIA`
- WF-010 `oCLrZ3aWZkSBvrjn`
- WF-020 `9Wvgfygw2wMqZcUD`
- WF-021 `Ih7yfJs1ON43xKmT`
- WF-500 `nPFz46PDjqipVJIq`

Read-only DB count:
- canonical_total: 37
- canonical_active: 37

## Registry Correction
`registries/n8n_webhook_registry.yaml` corrected to Restore_01 IDs and n8n 2.18 production URL form:
`/webhook/{workflowId}/trigger%2520node/{webhookPath}`

Resolver proof:
- `node scripts/validate_webhook_resolution.js` PASS for WF-000, WF-001, WF-010, WF-020, WF-021, WF-500.
- All six resolved from `registry_full_url`, not JSON fallback.

Safe webhook proof:
- WF-000 POST returned HTTP 200 with `{"message":"Workflow was started"}`.

## Backups
Before correcting launcher/registry, backups were created at:
`C:\ShadowEmpire-Git_Restore_01\docs\recovery\RUNTIME_PROFILE_CORRECTION_BACKUP_20260506_131135`

Earlier full forensic backup remains:
`C:\ShadowEmpire\forensic_recovery_backups\20260506_122700`

## Remaining Proof Needed
1. Refresh n8n browser at `http://127.0.0.1:5678/home/workflows` and confirm canonical workflows are visible.
2. Run WF-001 direct or Operator API job to create a fresh dossier.
3. Run WF-010 with that dossier ID to prove full dossier -> orchestration chain after profile correction.
4. Then restart Operator API so it reloads the corrected webhook registry.

## Do Not Do
- Do not start n8n using `C:\ShadowEmpire\n8n_user`.
- Do not use stale workflow editor/bookmark URLs that trigger permission 404s.
- Do not import workflows unless DB/profile visibility proves missing workflows after this correction.

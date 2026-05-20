# OLD_REPO_REQUIREMENT_RECONCILIATION_20260510

## Executive Verdict
- Production repo remains: `C:\ShadowEmpire-Git_Restore_01`.
- Old repo remains quarantined: `C:\ShadowEmpire-Git`.
- No old-repo files were required to restore runtime-critical execution.
- One old-only evidence bundle was migrated as reference docs only:
  - `docs/recovery/GRAPH_PARITY_AUDIT_20260506_CURRENT/*`.

## Production Root Confirmation
- Git root lock: `C:/ShadowEmpire-Git_Restore_01` (PASS)
- Branch: `recovery/runtime-lock-20260506`
- HEAD: `aca5c63 docs: add final recovery branch status handoff`

## Inventory Summary (scoped to production source directories)
| Category | Old Count | Restore_01 Count | Old-only | Restore-only | Different |
|---|---:|---:|---:|---:|---:|
| Overall scoped inventory | 2061 | 2156 | 21 | 116 | 66 |
| `n8n` | 148 | 148 | 0 | 0 | 31 |
| `operator` | 19 | 24 | 0 | 5 | 6 |
| `engine` | 80 | 80 | 0 | 0 | 5 |
| `scripts` | 80 | 98 | 7 | 25 | 14 |
| `docs` | 66 | 133 | 13 | 80 | 6 |
| `config` | 1 | 7 | 0 | 6 | 1 |

## Old-only Required Files Ledger

### REQUIRED_PRODUCTION
- None.

### REQUIRED_DOCUMENTATION
- None mandatory for runtime.

### REQUIRED_MIGRATION_REFERENCE
- Migrated:
  - `C:\ShadowEmpire-Git\docs\recovery\GRAPH_PARITY_AUDIT_20260506_CURRENT\*`
  - Destination: `C:\ShadowEmpire-Git_Restore_01\docs\recovery\GRAPH_PARITY_AUDIT_20260506_CURRENT\*`
  - Reason: preserve parity evidence package for future migration/forensics.

### UNKNOWN_REVIEW_REQUIRED
- None.

### IGNORE / QUARANTINE / DO_NOT_MIGRATE
- `registries\n8n_webhook_registry.yaml.bak` -> duplicate legacy backup.
- `scripts\cli\reimport_workflows.cjs` -> old recovery utility, stale risk.
- `scripts\import_n8n_workflows.js` -> old import path utility, stale risk.
- `scripts\patch_n8n_wf010_database.js` -> direct DB patch utility, unsafe for steady-state.
- `scripts\patch_wf010_dossier_load.js` -> old repair utility, stale risk.
- `scripts\recovery\publish_all_cli.cjs` -> old recovery utility, superseded.
- `scripts\recovery\publish_all_workflows.cjs` -> old recovery utility, superseded.
- `scripts\windows\run_openwebui_local.cmd` -> non-canonical launcher, drift risk.

## Divergent Critical File Review
| File/Group | Restore_01 Status | Old Repo Status | Difference | Production Required? | Action |
|---|---|---|---|---|---|
| `engine/api/operator.js` | Contains `/operator/skill-runtime` path | Missing reconciled endpoint behavior | major divergence | Yes | KEEP_RESTORE_01 |
| `operator/skill_runtime.js` | Present | Missing | restore-only critical | Yes | KEEP_RESTORE_01 |
| `operator/n8n_execution_reconciler.js` | Present | Missing | restore-only critical | Yes | KEEP_RESTORE_01 |
| `operator/output_reader.js` | Reconciled packet visibility | Narrower old behavior | divergence | Yes | KEEP_RESTORE_01 |
| `n8n/workflows/CWF-*.json` | `axios` + `/operator/skill-runtime`; no `skill_loader` import | Direct `skill_loader` import pattern | unsafe old runtime boundary | Yes | KEEP_RESTORE_01 |
| `scripts/windows/start_n8n_shadow_phase1.ps1` | `n8n_user_restore_01` + `NODE_FUNCTION_ALLOW_EXTERNAL=axios` | old `n8n_user` profile | critical drift | Yes | KEEP_RESTORE_01 |
| `operator/ollama_tool_runner.js` | canonical runtime bridge wiring | stale implementation | divergence | Yes | KEEP_RESTORE_01 |
| `config/open_webui_tools.json` | `5002` canonical tool endpoints | drifted variant | divergence | Yes | KEEP_RESTORE_01 |

## Files Migrated in This Reconciliation
- `docs/recovery/GRAPH_PARITY_AUDIT_20260506_CURRENT/*` (reference evidence only)

## Files Not Migrated Intentionally
- All old runtime repair scripts, DB patch scripts, and non-canonical launchers were not migrated due stale/unsafe risk.

## Future Migration Implications
- Source-of-truth for production replication is now Restore_01 + `n8n_user_restore_01` profile.
- Old repo may be archived for forensic reference only; not for runtime operations.

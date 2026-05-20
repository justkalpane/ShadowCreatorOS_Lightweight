# QUARANTINE STATUS (Wave 1)

Current environment is now FROZEN and REFERENCE-ONLY.

- Do not modify this environment for the new lightweight build.
- Preserve as future enterprise infrastructure.
- Allowed: read-only inspection, controlled copy of approved intelligence assets.
- Forbidden: runtime patching, workflow mutation, service restarts, provider recovery work, production test execution.

## Preservation Classification
| asset_category | path | exists | quarantine_action | future_use | safe_to_copy_for_wave2 | active_runtime_dependency | notes |
|---|---|---:|---|---|---:|---:|---|
| current_repo | C:\ShadowEmpire-Git_Restore_01 | true | freeze_read_only | enterprise_reference | false | true | Do not mutate; reference/copy-only. |
| n8n_profile | C:\ShadowEmpire\n8n_user_restore_01 | true | freeze_read_only | enterprise_automation_runtime | false | true | Stateful runtime profile. |
| n8n_sqlite_db | C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite | true | freeze_read_only | forensic/runtime continuity | false | true | Do not use as active truth in lightweight path. |
| n8n_binary_data | C:\ShadowEmpire\n8n_user_restore_01\.n8n\binaryData | true | freeze_read_only | enterprise workflow artifacts | false | true | Do not activate in lightweight path. |
| repo_workflow_jsons | C:\ShadowEmpire-Git_Restore_01\n8n\workflows | true | preserve_reference | reference contracts | true | true | Reference-only, not active runtime truth. |
| live_workflow_registry | C:\ShadowEmpire-Git_Restore_01\registries\workflow_registry.yaml | true | preserve_reference | workflow mapping reference | true | true | Do not treat IDs as active truth. |
| webhook_registry | C:\ShadowEmpire-Git_Restore_01\registries\n8n_webhook_registry.yaml | true | preserve_reference | route reference | true | true | Webhook IDs are historical reference only. |
| operator_api_files | C:\ShadowEmpire-Git_Restore_01\engine\api\operator.js | true | freeze_read_only | enterprise runtime | true | true | Reference only for lightweight design. |
| openwebui_files | C:\ShadowEmpire-Git_Restore_01\config\openwebui_shadow_creator_os_direct_pipe.py | true | freeze_read_only | enterprise UI bridge reference | true | true | Do not make mandatory in lightweight path. |
| provider_router_files | C:\ShadowEmpire-Git_Restore_01\operator\provider_router.js | true | freeze_read_only | provider orchestration reference | true | true | Keep as optional future execution layer. |
| gemini_provider_patch_state | C:\ShadowEmpire-Git_Restore_01\operator\providers\gemini_provider.js | true | preserve_as_forensic | quota/failure handling reference | false | true | Current blocker GEMINI_HTTP_429. |
| directors | C:\ShadowEmpire-Git_Restore_01\directors | true | preserve_copyable | repo-first intelligence | true | false | Primary copy target. |
| agents | C:\ShadowEmpire-Git_Restore_01\agents | true | preserve_copyable | repo-first intelligence | true | false | Primary copy target. |
| subagents | C:\ShadowEmpire-Git_Restore_01\sub_agents | true | preserve_copyable | repo-first intelligence | true | false | Directory uses underscore naming. |
| skills | C:\ShadowEmpire-Git_Restore_01\skills | true | preserve_copyable | repo-first intelligence | true | false | Primary copy target. |
| subskills | C:\ShadowEmpire-Git_Restore_01\sub-skills | false | preserve_if_present | repo-first intelligence | true | false | Not found as top-level folder currently. |
| registries | C:\ShadowEmpire-Git_Restore_01\registries | true | preserve_copyable | runtime constitution | true | false | Primary copy target. |
| schemas | C:\ShadowEmpire-Git_Restore_01\schemas | true | preserve_copyable | contracts | true | false | Primary copy target. |
| validators | C:\ShadowEmpire-Git_Restore_01\validators | true | preserve_copyable | quality gates | true | false | Primary copy target. |
| docs | C:\ShadowEmpire-Git_Restore_01\docs | true | preserve_copyable | reference/PRDs | true | false | Primary copy target. |
| dossiers | C:\ShadowEmpire-Git_Restore_01\dossiers | true | preserve_reference | forensic history/templates | true | true | Copy templates/selected examples only. |
| logs | C:\ShadowEmpire-Git_Restore_01\logs | false | preserve_reference | forensic diagnostics | false | true | Do not adopt as active state. |
| backups | C:\ShadowEmpire-Git_Restore_01\backups | true | preserve_reference | rollback history | true | true | Reference-only. |
| .env_files | C:\ShadowEmpire-Git_Restore_01\.env* | true | redact_keep_local | local runtime only | false | true | Never copy secrets. |
| node_modules | C:\ShadowEmpire-Git_Restore_01\node_modules | true | exclude_from_copy | none | false | true | Regenerate per repo when needed. |
| runtime_caches | C:\ShadowEmpire-Git_Restore_01\temp|tmp_audit|data | true | preserve_reference | forensics only | false | true | Do not treat as clean runtime truth. |
| package_lock_files | C:\ShadowEmpire-Git_Restore_01\package-lock.json | true | optional_reference | dependency pin reference | false | true | Not required for lightweight repo-brain start. |

## Current Strategic State Snapshot
- mission-context/director routing patched partially in current track
- blocker remains GEMINI_HTTP_429
- production_wave_1_sealed=false
- production_ready_for_wave_2=false
- environment frozen for future enterprise infrastructure
- Wave 2 will create a separate lightweight repo-first path

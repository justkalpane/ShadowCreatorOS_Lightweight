# Copy Manifest

- source_repo: C:\ShadowEmpire-Git_Restore_01
- destination_repo: C:\ShadowCreatorOS_Lightweight
- quarantine_reference: C:\ShadowEmpire_Quarantine\quarantine_20260515_112944
- copy_timestamp: 2026-05-15T19:01:32.0914908+05:30
- active_assets_copied_count: 9
- reference_assets_copied_count: 4
- n8n_workflow_jsons_reference_count: 38
- operator_reference_files_count: 31
- openwebui_reference_files_count: 1

## Exclusions enforced
- node_modules
- .git
- .env
- .env.*
- n8n profile/sqlite/binaryData
- secrets/tokens/cookies/session files
- runtime caches as active state
- old workflow/webhook IDs as active truth

## Safety Flags
- secrets_copied: false
- source_repo_modified: false
- n8n_db_copied: false
- n8n_profile_copied: false
- old_workflow_ids_active: false
- old_webhook_ids_active: false
- openwebui_required: false
- n8n_required_for_intelligence: false
- safe_for_new_codex_chat: true


## Audit Clarifications
- old workflow IDs are reference only (not active runtime truth).
- old webhook IDs are reference only (not active runtime truth).
- OpenWebUI is optional for lightweight repo-first flow.
- n8n is not required for intelligence in lightweight mode.
- Gemini is not default in lightweight mode.

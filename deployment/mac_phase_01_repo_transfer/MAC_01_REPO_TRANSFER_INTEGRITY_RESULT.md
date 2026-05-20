# MAC-01 Repo Transfer Integrity Result

Status: PASS
Generated: 2026-05-20
Repo path: /Users/apple/Documents/ShadowCreatorOS_Lightweight

## Repo Discovery

repo_found=true
repo_path=/Users/apple/Documents/ShadowCreatorOS_Lightweight
duplicate_repo_candidates=
- /Users/apple/Documents/ShadowCreatorOS_Lightweight
selected_repo_path=/Users/apple/Documents/ShadowCreatorOS_Lightweight
selection_reason=Only discovered ShadowCreatorOS_Lightweight candidate in the requested Mac search locations; it is also the active working directory.

## Read-First Files

read_first_files_found=
- /Users/apple/Downloads/FRESH_MAC_CODEX_STARTUP_PROMPT.md
- /Users/apple/Downloads/MAC_CODEX_READ_ORDER_ON_FIRST_OPEN.md
- /Users/apple/Documents/Shadow Docs/Detailed_PRD_MASTERPIECE_v34_ZERO_LOSS_HARNESS_RESTRUCTURED.txt
- /Users/apple/Documents/Shadow Docs/latest Claude entire Build status.txt
- /Users/apple/Documents/Shadow Docs/latest Codex entire Build status.txt
- START_HERE_FOR_MAC_CODEX.md
- 00_READ_ME_FIRST_FOR_MAC_MIGRATION.md
- MAC_CODEX_READ_ORDER_ON_FIRST_OPEN.md
- handoff/MAC_MIGRATION_MASTER_INDEX.md
- handoff/final_self_explaining_technical_handout/00_FINAL_HANDOUT_README.md
- handoff/final_self_explaining_technical_handout/01_COMPLETE_BUILD_STATUS_END_TO_END.md
- handoff/final_self_explaining_technical_handout/07_MAC_DEPLOYMENT_NEXT_PHASE_RUNBOOK.md
- deployment/mac_phase_00_baseline/MAC_00_BASELINE_AUDIT.md
- deployment/mac_phase_01_repo_transfer/MAC_01_REPO_TRANSFER_AND_INTEGRITY.md
- deployment/mac_phase_02_dependency_install/MAC_02_DEPENDENCY_INSTALL_PLAN.md
- deployment/mac_phase_03_agent_setup/MAC_03_CODEX_CLAUDE_KIMI_AGENT_SETUP.md
- deployment/mac_phase_04_first_repo_proof/FIRST_MAC_REPO_FIRST_PROOF_PROMPT.md
- handoff/n8n_export_summary/N8N_FULL_EXPORT_SUMMARY.md
- archive_reference/n8n_full_environment_reference_20260518_v8/EXPORT_MANIFEST.json

read_first_files_missing=
- None

migration_doctrine_understood=true

## Required Folder Integrity

required_folders_present=
- handoff/
- deployment/
- audits/
- runtime_contracts/
- directors/
- agents/
- subagents/
- skills/
- registries/
- schemas/
- validators/
- docs/
- archive_reference/n8n_full_environment_reference_20260518_v8/
- archive_reference/n8n_full_environment_reference_20260518_v8/workflow_export_sanitized/

required_folders_missing=
- None

## n8n Archive Boundary

sanitized_workflow_exports_count=71
sanitized_workflow_exports_expected=71
sanitized_workflow_exports_status=PASS

secret_scan_report_exists=true
secret_scan_report_path=archive_reference/n8n_full_environment_reference_20260518_v8/SANITIZED_EXPORT_SECRET_SCAN_REPORT.md
secret_scan_pass=true
secret_scan_findings_total=0

checksum_manifest_exists=true
checksum_manifest_paths=
- COPY_MANIFEST.json
- COPY_MANIFEST.md
- transfer_bundle/MAC_SANITIZED_TRANSFER_MANIFEST.json
- transfer_bundle/MAC_SANITIZED_TRANSFER_MANIFEST.md
- transfer_bundle/checksums/ShadowCreatorOS_Lightweight_MAC_SANITIZED_TRANSFER_20260518.sha256.txt

raw_private_exports_used=false
raw_private_exports_note=Raw private exports are present only under archive_reference/n8n_full_environment_reference_20260518_v8/workflow_export_raw_private_DO_NOT_COMMIT and were not opened, imported, activated, or used as runtime truth.

old_db_profile_binaryData_active_runtime=false
old_db_profile_binaryData_note=The old DB snapshot is present only under PRIVATE_DB_SNAPSHOT_DO_NOT_USE_AS_RUNTIME. EXPORT_MANIFEST.json records credentials_exported=false, executions_exported=false, binaryData_exported=false, old_db_copied_as_active_runtime=false, old_workflow_ids_active_truth=false, and old_webhook_ids_active_truth=false.

## Runtime Guard Confirmation

n8n_started=false
workflow_imported=false
workflow_executed=false
provider_called=false
gemini_called=false
openwebui_used=false
first_proof_started=false

## Result

repo_integrity_status=PASS
next_gate=MAC-02 dependency install planning after MAC-00 baseline audit review and user approval.

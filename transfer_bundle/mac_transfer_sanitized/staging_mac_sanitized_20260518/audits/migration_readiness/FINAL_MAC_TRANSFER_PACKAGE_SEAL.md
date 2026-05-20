FINAL_MAC_TRANSFER_PACKAGE_SEAL_STATUS=PASS

root_path=C:\ShadowCreatorOS_Lightweight

required_structure_verified=true
mac_read_order_created=true
sanitized_transfer_manifest_created=true
transfer_checksum_plan_created=true
forbidden_file_scan_created=true

n8n_full_export_present=true
sanitized_workflow_exports_count=71
secret_scan_pass=true
checksum_manifest_present=true
raw_private_exports_excluded_from_default_transfer=true

old_db_excluded_from_active_transfer=true
old_profile_excluded_from_active_transfer=true
binaryData_excluded_from_active_transfer=true
env_files_excluded_from_active_transfer=true
node_modules_excluded_from_active_transfer=true
credentials_excluded_from_active_transfer=true

safe_to_transfer_sanitized_repo_package_to_mac=true
safe_to_transfer_raw_private_exports_to_mac=false
safe_to_begin_mac_installation=false
safe_to_start_first_mac_proof=false

old_windows_repo_modified=false
old_n8n_profile_modified=false
old_sqlite_modified=false
old_openwebui_modified=false
old_operator_api_modified=false
n8n_started=false
workflow_imported=false
workflow_activated=false
workflow_executed=false
gemini_called=false
providers_called=false
secrets_exposed=false

files_created=
- C:\ShadowCreatorOS_Lightweight\transfer_bundle\MAC_SANITIZED_TRANSFER_MANIFEST.md
- C:\ShadowCreatorOS_Lightweight\transfer_bundle\MAC_SANITIZED_TRANSFER_MANIFEST.json
- C:\ShadowCreatorOS_Lightweight\transfer_bundle\checksums\TRANSFER_CHECKSUM_PLAN.md
- C:\ShadowCreatorOS_Lightweight\MAC_CODEX_READ_ORDER_ON_FIRST_OPEN.md
- C:\ShadowCreatorOS_Lightweight\audits\transfer_safety\FINAL_FORBIDDEN_FILE_SCAN.md
- C:\ShadowCreatorOS_Lightweight\audits\migration_readiness\FINAL_MAC_TRANSFER_PACKAGE_SEAL.md

blockers_found=
- none
high_risks_found=
- none
medium_risks_found=
- none
low_risks_found=
- none
needs_confirmation=
- 2 DB-only workflows still UNKNOWN_NEEDS_MANUAL_REVIEW before import/reuse planning.

NEXT_ACTION=Create a sanitized transfer artifact only when explicitly approved, then run MAC-0 baseline audit on Mac and stop before installation/runtime activation.

# MAC Bootstrap Start Report

MAC_BOOTSTRAP_START_STATUS=PARTIAL

repo_found=true
repo_path=/Users/apple/Documents/ShadowCreatorOS_Lightweight
duplicate_repo_candidates=/Users/apple/Documents/ShadowCreatorOS_Lightweight
selected_repo_path=/Users/apple/Documents/ShadowCreatorOS_Lightweight
selection_reason=Only discovered repo candidate in requested Mac search locations; active working directory matches.

read_first_files_ok=true
read_first_files_found=19
read_first_files_missing=0
migration_doctrine_understood=true

repo_integrity_status=PASS
sanitized_workflow_exports_count=71
secret_scan_report_exists=true
checksum_manifest_exists=true
raw_private_exports_used=false
old_db_profile_binaryData_active_runtime=false

MAC_00_BASELINE_AUDIT_STATUS=PARTIAL
macos_version=macOS 26.5 build 25F71
architecture=arm64
memory=64 GB
disk_available=827Gi

xcode_clt_present=true
homebrew_present=false
git_present=true
gh_present=false
node_present=true
npm_present=false
python3_present=true
sqlite3_present=true
jq_present=true
yq_present=false
codex_present=true
claude_present=false
kimi_present=false
deepseek_present=false

install_plan_created=true
install_now_missing=Homebrew; GitHub CLI; npm; yq; Claude Code/app or CLI route; Kimi Code/app if chosen; DeepSeek local/CLI/app if chosen; VS Code or Cursor if chosen
install_later_items=Docker Desktop or Colima; n8n fresh Mac runtime; OpenWebUI optional; Ollama/LM Studio optional; FFmpeg; PostgreSQL; Redis; Qdrant; provider SDKs; media generation tools; publishing/analytics tooling; YouTube analyzer workflows; ElevenLabs / HeyGen / Higgsfield / Sora / Seedance integrations
forbidden_first_proof_items=n8n execution; n8n workflow import; old workflow IDs/webhooks as active truth; old DB/profile active runtime; Gemini/API provider calls; provider credentials; OpenWebUI as required dependency; raw private workflow exports; workflow activation; workflow execution

n8n_started=false
workflow_imported=false
workflow_executed=false
provider_called=false
gemini_called=false
openwebui_used=false
first_proof_started=false

safe_to_continue_to_install_after_user_approval=true
safe_to_start_first_mac_proof=false

NEXT_ACTION=Review the bootstrap reports, then approve the MAC-02 install-now stack decisions before any install commands are run.

## Supporting Reports

- deployment/mac_phase_00_baseline/MAC_00_BASELINE_AUDIT_RESULT.md
- deployment/mac_phase_01_repo_transfer/MAC_01_REPO_TRANSFER_INTEGRITY_RESULT.md
- deployment/mac_phase_02_dependency_install/MAC_02_PREREQUISITE_INSTALL_PLAN_RESULT.md

## Notes

- `sysctl hw.memsize` was blocked by sandbox permissions, so memory was captured with `system_profiler SPHardwareDataType`.
- The folder is not currently a Git repository. Before this becomes the permanent production Git source of truth, initialize or connect the repo deliberately after user approval.
- No installs, runtimes, n8n actions, workflow imports, workflow executions, provider calls, Gemini calls, OpenWebUI usage, secret creation, or first proof work were performed.

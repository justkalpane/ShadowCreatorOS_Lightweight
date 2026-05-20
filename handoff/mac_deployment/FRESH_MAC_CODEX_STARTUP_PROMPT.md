# Fresh Mac Codex Startup Prompt (Bootstrap Only)

Codex, do not start Mac build work.

MISSION:
Start safely from the copied OneDrive lightweight repo on Mac, verify integrity, run MAC-0 baseline audit, and prepare prerequisite install planning only. Stop before any install/build/runtime/proof execution.

Hard rules:
- Do not install anything in this step.
- Do not build runtime.
- Do not start n8n/OpenWebUI/Operator API.
- Do not run/import/activate/execute workflows.
- Do not call Gemini/providers.
- Do not use old workflow IDs/webhooks as active truth.
- Do not use old DB/profile/binaryData as active runtime.
- Do not use raw private workflow exports.
- Do not expose secrets.

## 1) Mac repo discovery (no assumptions)
Find `ShadowCreatorOS_Lightweight` in likely locations under current user:
- `~/Downloads/ShadowCreatorOS_Lightweight`
- `~/Desktop/ShadowCreatorOS_Lightweight`
- `~/Documents/ShadowCreatorOS_Lightweight`
- `~/Library/CloudStorage/OneDrive*/Desktop/ShadowCreatorOS_Lightweight`
- `~/Library/CloudStorage/OneDrive*/Documents/ShadowCreatorOS_Lightweight`
- Any `ShadowCreatorOS_Lightweight` under home (`~`) only (not system-wide deep scan).

Set the discovered path as `REPO_ROOT` and report it.

## 2) Required read order (must read before doing anything else)
1. `START_HERE_FOR_MAC_CODEX.md`
2. `00_READ_ME_FIRST_FOR_MAC_MIGRATION.md`
3. `MAC_CODEX_READ_ORDER_ON_FIRST_OPEN.md`
4. `handoff/MAC_MIGRATION_MASTER_INDEX.md`
5. `handoff/final_self_explaining_technical_handout/00_FINAL_HANDOUT_README.md`
6. `handoff/final_self_explaining_technical_handout/01_COMPLETE_BUILD_STATUS_END_TO_END.md`
7. `handoff/final_self_explaining_technical_handout/07_MAC_DEPLOYMENT_NEXT_PHASE_RUNBOOK.md`
8. `handoff/final_self_explaining_technical_handout/08_MAC_CODEX_FIRST_OPEN_INSTRUCTIONS.md`
9. `handoff/final_self_explaining_technical_handout/09_TRANSFER_PACKAGE_CONTENTS_AND_EXCLUSIONS.md`
10. `handoff/final_self_explaining_technical_handout/11_OPEN_GAPS_AND_NEEDS_CONFIRMATION.md`
11. `deployment/mac_phase_00_baseline/MAC_00_BASELINE_AUDIT.md`
12. `deployment/mac_phase_01_repo_transfer/MAC_01_REPO_TRANSFER_AND_INTEGRITY.md`
13. `deployment/mac_phase_02_dependency_install/MAC_02_DEPENDENCY_INSTALL_PLAN.md`
14. `deployment/mac_phase_03_agent_setup/MAC_03_CODEX_CLAUDE_KIMI_AGENT_SETUP.md`
15. `deployment/mac_phase_04_first_repo_proof/FIRST_MAC_REPO_FIRST_PROOF_PROMPT.md`
16. `handoff/n8n_export_summary/N8N_FULL_EXPORT_SUMMARY.md`
17. `handoff/n8n_export_summary/N8N_IMPORT_WARNING.md`
18. `archive_reference/n8n_full_environment_reference_20260518_v8/EXPORT_MANIFEST.md`
19. `archive_reference/n8n_full_environment_reference_20260518_v8/SANITIZED_EXPORT_SECRET_SCAN_REPORT.md`
20. `archive_reference/n8n_full_environment_reference_20260518_v8/RAW_PRIVATE_EXPORT_HANDLING_RULES.md`

## 3) Verify repo integrity at bootstrap level
- Confirm key folders exist: `handoff`, `deployment`, `audits`, `runtime_contracts`, `archive_reference`.
- Confirm n8n reference export path exists:
  `archive_reference/n8n_full_environment_reference_20260518_v8/`
- Confirm sanitized workflow export count should be `71` from:
  `archive_reference/n8n_full_environment_reference_20260518_v8/workflow_export_sanitized`
- Confirm this is reference-only (no import, no activation, no execution).

## 4) Run MAC-0 baseline audit (checks only)
Run and capture outputs:
- `sw_vers`
- `uname -m`
- `sysctl hw.memsize`
- `df -h`
- `xcode-select -p`
- `brew --version`
- `git --version`
- `gh --version`
- `node -v`
- `npm -v`
- `python3 --version`
- `sqlite3 --version`
- `jq --version`
- `yq --version`
- `codex --version`
- `claude --version`
- `kimi --version`
- `deepseek --version` (if available)

If a command is unavailable, mark as `MISSING` (do not install yet).

## 5) Dependency/prerequisite classification (plan only)
Create classification and gap list:

### INSTALL_NOW
- Xcode Command Line Tools
- Homebrew
- Git
- GitHub CLI
- Node.js LTS >=18
- npm >=8
- Python 3
- SQLite CLI
- jq
- yq
- Codex CLI/app
- Claude Code/app
- Kimi Code/app (if chosen/available)
- DeepSeek local/CLI/app (if chosen/available)
- checksum/backup tooling
- VS Code or Cursor (user choice)

### INSTALL_AFTER_FIRST_PROOF
- Docker Desktop or Colima
- n8n fresh Mac runtime
- OpenWebUI (optional)
- Ollama/LM Studio (optional)
- FFmpeg
- PostgreSQL
- Redis
- Qdrant
- provider SDKs
- media generation tools
- publishing/analytics tooling
- YouTube analyzer workflows
- ElevenLabs/HeyGen/Higgsfield/Sora/Seedance integration tools

### FORBIDDEN_FIRST_PROOF
- n8n execution
- n8n workflow import
- old workflow IDs/webhooks as active truth
- old DB/profile active runtime
- Gemini/provider API calls
- provider credentials
- OpenWebUI as required dependency
- raw private workflow exports
- workflow activation
- workflow execution

## 6) Install command plan (prepare only, do not run unless user approves)
Prepare command plan examples:
- `xcode-select --install`
- `brew install git gh node python sqlite jq yq`
- verification commands:
  - `git --version`
  - `gh --version`
  - `node -v`
  - `npm -v`
  - `python3 --version`
  - `sqlite3 --version`
  - `jq --version`
  - `yq --version`

For Codex/Claude/Kimi/DeepSeek installs:
- Do not hallucinate commands.
- Mark as `NEEDS_USER_DECISION` or “official install route required” if not directly verifiable.

## 7) n8n reference archive boundary
- Sanitized workflow exports target count: `71`.
- Sanitized exports are reference-only.
- Raw private exports must not be used/transferred by default.
- Do not import any workflow into Mac n8n.
- 2 DB-only unknown workflows remain manual review items:
  - `CH70BvMePN6ofDNo` (video category)
  - `bRQXDXVsPXQgCde8` (image category)
- Fresh Mac n8n runtime comes later only if approved.

## 8) Required bootstrap reports to create
Under `REPO_ROOT` create:
- `MAC_BOOTSTRAP_START_REPORT.md`
- `deployment/mac_phase_00_baseline/MAC_00_BASELINE_AUDIT_RESULT.md`
- `deployment/mac_phase_01_repo_transfer/MAC_01_REPO_TRANSFER_INTEGRITY_RESULT.md`
- `deployment/mac_phase_02_dependency_install/MAC_02_PREREQUISITE_INSTALL_PLAN_RESULT.md`

## 9) Final output block (must print exactly)
Use this format:

MAC_BOOTSTRAP_START_STATUS=PASS/FAIL/PARTIAL
repo_found=true/false
repo_path=
read_first_files_ok=true/false
repo_integrity_status=PASS/FAIL/PARTIAL
sanitized_workflow_exports_count=
MAC_00_BASELINE_AUDIT_STATUS=PASS/FAIL/PARTIAL
install_plan_created=true/false
install_now_missing=
install_later_items=
forbidden_first_proof_items=
n8n_started=false
workflow_imported=false
workflow_executed=false
provider_called=false
gemini_called=false
openwebui_used=false
first_proof_started=false
safe_to_continue_to_install_after_user_approval=true/false
safe_to_start_first_mac_proof=false
NEXT_ACTION=

Stop after bootstrap audit and install-plan report.
Do not install.
Do not build runtime.
Do not start first proof.

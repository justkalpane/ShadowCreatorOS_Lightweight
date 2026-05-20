# MAC-00 Baseline Audit Result

Status: PARTIAL
Generated: 2026-05-20
Repo path: /Users/apple/Documents/ShadowCreatorOS_Lightweight

## System Baseline

macos_version=macOS 26.5 build 25F71
architecture=arm64
chip=Apple M1 Max
memory=64 GB
memory_source=system_profiler SPHardwareDataType fallback; sysctl hw.memsize was blocked by sandbox permissions.
disk_available=827Gi available on root and Data volumes

## Command Results

| Check | Status | Output |
| --- | --- | --- |
| sw_vers | PRESENT | ProductVersion 26.5, BuildVersion 25F71 |
| uname -m | PRESENT | arm64 |
| sysctl hw.memsize | BLOCKED | Operation not permitted in sandbox |
| system_profiler SPHardwareDataType | PRESENT | Apple M1 Max, 10 cores, 64 GB memory |
| df -h | PRESENT | 827Gi available on / and /System/Volumes/Data |
| xcode-select -p | PRESENT | /Library/Developer/CommandLineTools |
| brew --version | MISSING | command not found: brew |
| git --version | PRESENT | git version 2.50.1 (Apple Git-155) |
| gh --version | MISSING | command not found: gh |
| node -v | PRESENT | v24.14.0 |
| npm -v | MISSING | command not found: npm |
| python3 --version | PRESENT | Python 3.9.6 |
| sqlite3 --version | PRESENT | 3.51.0 |
| jq --version | PRESENT | jq-1.7.1-apple |
| yq --version | MISSING | command not found: yq |
| codex --version | PRESENT | codex-cli 0.131.0-alpha.9 |
| claude --version | MISSING | command not found: claude |
| kimi --version | MISSING | command not found: kimi |
| deepseek --version | MISSING | command not found: deepseek |
| shasum --version | PRESENT | 6.02 |
| rsync --version | PRESENT | openrsync protocol 29 / rsync 2.6.9 compatible |
| code --version | MISSING | command not found: code |
| cursor --version | MISSING | command not found: cursor |

## Presence Flags

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

## Notes

- Node is present, but npm is missing from PATH, so the Node/npm toolchain is incomplete.
- Git is present as Apple Git through Command Line Tools. A Homebrew Git install can be considered during dependency standardization, but Git is not currently absent.
- Python 3 is present as the macOS system Python. A Homebrew Python install can be considered later if the project standardizes on Homebrew-managed runtimes.
- The current folder is not a Git repository at audit time (`git status --short` returned "not a git repository"). This does not block the requested bootstrap audit, but it should be resolved before treating this folder as the permanent production Git remote source of truth.

## Runtime Guard Confirmation

n8n_started=false
workflow_imported=false
workflow_executed=false
provider_called=false
gemini_called=false
openwebui_used=false
first_proof_started=false

## Result

MAC_00_BASELINE_AUDIT_STATUS=PARTIAL
stop_reason=Required install-now tools are missing or incomplete: Homebrew, GitHub CLI, npm, yq, Claude CLI, and optional/choice agent tools Kimi and DeepSeek.
safe_to_continue_to_install_after_user_approval=true
safe_to_start_first_mac_proof=false

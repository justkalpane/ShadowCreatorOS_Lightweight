# MAC-02 Foundation Install Result

MAC_02_FOUNDATION_INSTALL_STATUS=PASS

Generated: 2026-05-20
Repo path: /Users/apple/Documents/ShadowCreatorOS_Lightweight

## Scope Guard

Foundation install scope only:
- Homebrew
- GitHub CLI
- Node/npm standardization
- yq

No n8n, Docker, OpenWebUI, provider SDKs, workflow import, workflow execution, Gemini calls, provider calls, or first proof work were performed.

## Baseline Reconfirmation

| Tool | Status Before Install | Output |
| --- | --- | --- |
| brew | MISSING | command not found: brew |
| git | PRESENT | git version 2.50.1 (Apple Git-155) |
| gh | MISSING | command not found: gh |
| node | PRESENT | v24.14.0 |
| npm | MISSING | command not found: npm |
| python3 | PRESENT | Python 3.9.6 |
| sqlite3 | PRESENT | 3.51.0 |
| jq | PRESENT | jq-1.7.1-apple |
| yq | MISSING | command not found: yq |
| codex | PRESENT | codex-cli 0.131.0-alpha.9 |

## Install Execution

homebrew_installed=true
homebrew_install_route=manual_terminal_then_codex_resume
homebrew_version=5.1.12

approved_install_command_run=true
approved_install_command=
`brew install git gh node python sqlite jq yq`

notes=
- Homebrew successfully installed by user in normal macOS Terminal using the official installer.
- Codex resumed and installed only the approved foundation formula set.
- `brew shellenv zsh` was applied for verification commands in this session.

## Verification Results

brew --version: Homebrew 5.1.12
git --version: git version 2.54.0
gh --version: gh version 2.92.0
node -v: v26.0.0
npm -v: 11.12.1
python3 --version: Python 3.14.5
sqlite3 --version: 3.51.0
jq --version: jq-1.8.1
yq --version: yq version v4.53.2
codex --version: codex-cli 0.131.0-alpha.9

homebrew_path=/opt/homebrew/bin/brew
node_path=/opt/homebrew/bin/node
npm_path=/opt/homebrew/bin/npm
python3_path=/opt/homebrew/bin/python3

homebrew_installed=true
gh_installed=true
node_present=true
npm_present=true
python3_present=true
sqlite3_present=true
jq_present=true
yq_present=true
codex_present=true

tools_installed=
- git
- gh
- node
- python
- sqlite
- jq
- yq

tools_verified=
- brew
- git
- gh
- node
- npm
- python3
- sqlite3
- jq
- yq
- codex

tools_failed=
- None

## Path Notes

- Before `brew shellenv`, macOS system binaries (`/usr/bin/*`) could shadow some Homebrew tools.
- During MAC-02 verification, `eval "$(/opt/homebrew/bin/brew shellenv zsh)"` placed Homebrew first in PATH and activated the expected toolchain versions.

## Forbidden Actions Confirmation

n8n_installed=false
docker_installed=false
openwebui_installed=false
provider_tools_installed=false
workflow_imported=false
workflow_executed=false
gemini_called=false
providers_called=false
first_proof_started=false

repo_modified_only_by_report=true
safe_to_continue_to_MAC_03_agent_setup=true
safe_to_start_first_mac_proof=false

NEXT_ACTION=Proceed to MAC-03 agent setup readiness checks (Codex/Claude/Kimi decisions) while keeping first proof locked.

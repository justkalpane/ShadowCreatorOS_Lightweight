# MAC-02 Prerequisite Install Plan Result

Status: CREATED
Generated: 2026-05-20
Repo path: /Users/apple/Documents/ShadowCreatorOS_Lightweight
Architecture: arm64

No commands in this plan were run.

## INSTALL_NOW

| Dependency | Current Status | Action |
| --- | --- | --- |
| Xcode Command Line Tools | PRESENT | No install needed. Verify with `xcode-select -p`. |
| Homebrew | MISSING | Install after user approval from the official Homebrew route. |
| Git | PRESENT | Apple Git present. Optional Homebrew Git standardization after Homebrew is installed. |
| GitHub CLI | MISSING | Install with Homebrew after Homebrew is installed. |
| Node.js LTS >=18 | PRESENT | Node v24.14.0 present, but npm missing. Reinstall/standardize Node with Homebrew if approved. |
| npm >=8 | MISSING | Fix through approved Node/npm install route. |
| Python 3 | PRESENT | Python 3.9.6 present. Optional Homebrew Python standardization if approved. |
| SQLite CLI | PRESENT | sqlite3 3.51.0 present. |
| jq | PRESENT | jq-1.7.1-apple present. |
| yq | MISSING | Install with Homebrew after Homebrew is installed. |
| Codex CLI/app | PRESENT | codex-cli 0.131.0-alpha.9 present. |
| Claude Code/app | MISSING_FROM_PATH | NEEDS_USER_DECISION: use official Anthropic Claude Code install/auth route; do not infer command in this bootstrap. |
| Kimi Code/app if chosen | MISSING_FROM_PATH | NEEDS_USER_DECISION: only install if chosen, using official route. |
| DeepSeek local/CLI/app if chosen | MISSING_FROM_PATH | NEEDS_USER_DECISION: only install if chosen, using official route. |
| checksum/backup tooling | PRESENT | shasum and rsync present. |
| VS Code or Cursor if chosen | MISSING_FROM_PATH | NEEDS_USER_DECISION: choose VS Code, Cursor, both, or neither for this phase. |

install_now_missing=
- Homebrew
- GitHub CLI
- npm
- yq
- Claude Code/app or CLI route
- Kimi Code/app if chosen
- DeepSeek local/CLI/app if chosen
- VS Code or Cursor if chosen

## INSTALL_AFTER_FIRST_PROOF

- Docker Desktop or Colima
- n8n fresh Mac runtime
- OpenWebUI optional
- Ollama/LM Studio optional
- FFmpeg
- PostgreSQL
- Redis
- Qdrant
- provider SDKs
- media generation tools
- publishing/analytics tooling
- YouTube analyzer workflows
- ElevenLabs / HeyGen / Higgsfield / Sora / Seedance integrations

## FORBIDDEN_FIRST_PROOF

- n8n execution
- n8n workflow import
- old workflow IDs/webhooks as active truth
- old DB/profile active runtime
- Gemini/API provider calls
- provider credentials
- OpenWebUI as required dependency
- raw private workflow exports
- workflow activation
- workflow execution

## Command Plan Only

### Verify Existing Xcode CLT

```sh
xcode-select -p
```

If Xcode Command Line Tools are ever missing, approved install command:

```sh
xcode-select --install
```

### Install Homebrew

Use the official Homebrew install route after user approval:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After install on Apple Silicon, follow Homebrew's printed shell environment instructions for `/opt/homebrew`.

### Install Core CLI Stack With Homebrew

Run only after Homebrew is installed and user approves:

```sh
brew install git gh node python sqlite jq yq
```

### Verify Core CLI Stack

```sh
brew --version
git --version
gh --version
node -v
npm -v
python3 --version
sqlite3 --version
jq --version
yq --version
codex --version
```

### Agent/App Decisions

Claude Code/app:
- NEEDS_USER_DECISION
- Use official Anthropic install/auth route.
- Do not run first proof until Claude readiness is documented or explicitly deferred.

Kimi Code/app:
- NEEDS_USER_DECISION
- Install only if chosen for MAC-03.

DeepSeek local/CLI/app:
- NEEDS_USER_DECISION
- Install only if chosen for MAC-03.

VS Code or Cursor:
- NEEDS_USER_DECISION
- Install only after editor choice is confirmed.

## Runtime Guard Confirmation

n8n_started=false
workflow_imported=false
workflow_executed=false
provider_called=false
gemini_called=false
openwebui_used=false
first_proof_started=false

## Result

install_plan_created=true
safe_to_continue_to_install_after_user_approval=true
safe_to_start_first_mac_proof=false

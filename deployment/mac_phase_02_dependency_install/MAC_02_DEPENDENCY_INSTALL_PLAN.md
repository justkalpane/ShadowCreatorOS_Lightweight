# MAC-02 Dependency Install Plan

## Objective
Install required tools in controlled order.

## INSTALL_NOW
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
- Codex
- Claude Code
- Kimi Code (if chosen)
- checksum/backup tooling

## INSTALL_LATER
- Docker Desktop or Colima
- fresh Mac n8n runtime
- OpenWebUI (optional)
- Ollama/LM Studio (optional)
- FFmpeg
- PostgreSQL/Redis/Qdrant (if needed)
- provider SDKs (after approval)

## FORBIDDEN_FIRST_PROOF
- n8n execution
- Gemini/provider calls
- old DB/profile as active runtime
- old workflow IDs/webhooks as active truth
- OpenWebUI as required dependency

## Pass criteria
- Install-now stack verified and documented.

## Next gate
- MAC-03 agent setup.

# Mac Transfer Include/Exclude Rules

## SAFE TO TRANSFER
- lightweight repo docs and contracts
- deployment phase docs
- handoff docs
- sanitized n8n workflow exports
- n8n inventories and manifests
- checksum files

## DO NOT TRANSFER BY DEFAULT
- raw private workflow exports
- old n8n DB/profile/binaryData
- .env, secrets, tokens, cookies
- old Codex sessions
- node_modules, logs, execution payloads
- OpenWebUI runtime state
- provider credentials

## Rule
- Do not copy raw private exports into 	ransfer_bundle\\mac_transfer_sanitized.

# N8N Full Export Status And Reuse Boundary

- workflows preserved: 71
- shadow guessed: 38
- DB-only: 33
- unknown remaining: 2

## Transfer and safety
- sanitized exports: transfer-safe for reference
- raw private exports: not transfer-safe by default
- credentials exported: false
- executions exported: false
- binaryData exported: false

## Reuse boundary
- Imported templates and non-shadow workflows are reference-only now.
- Future Mac n8n must be fresh runtime.
- Do not auto-import workflows.
- Manual review required before reuse/import.
- Future media execution bus may reuse reviewed templates only after gating.

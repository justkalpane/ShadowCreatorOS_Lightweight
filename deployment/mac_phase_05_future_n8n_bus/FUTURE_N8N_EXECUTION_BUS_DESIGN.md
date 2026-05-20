# Future N8N Execution Bus Design

This design document defines the future execution-only n8n lane.

- Repo-first stage outputs `provider_handoff_packet.json`.
- n8n consumes only approved provider handoff packets.
- Imports from archived workflows require manual review before reuse.
- No automatic workflow import from historical export sets.
- Execution categories: voice, image, thumbnail, avatar, video, publish, analytics, callback/polling, retry/DLQ, cost gate, artifact lineage.

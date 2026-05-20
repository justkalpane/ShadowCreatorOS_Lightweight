# Wave History And Decision Log

## Why old Windows was frozen
To preserve enterprise runtime evidence while stopping drift and accidental mutation during migration.

## Wave timeline
- Wave 1 (Quarantine): PASS. Environment frozen with guard rails.
- Wave 2 (Lightweight copy): PASS. Lightweight repo copied; old DB/profile/secrets excluded.
- Wave 3 (Handoff): PASS. Migration doctrine and phase docs established.
- n8n full export: PASS. Full workflow universe preserved (71 workflows).
- n8n final verification: PASS. Secret-scan/checksum/classification lock produced.
- migration organization: PASS. Command-center structure established.
- final transfer package seal: PASS. Sanitized transfer readiness verified.

## Strategic decisions
- Mac starts repo-first, not n8n-first.
- Preserve full n8n workflow universe as reference/template pool.
- Do not auto-import workflows into Mac n8n.

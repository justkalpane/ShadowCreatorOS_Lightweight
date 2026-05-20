# Raw Private Export Handling Rules

- Raw private exports are FORENSIC ONLY.
- Do not commit raw private exports to Git.
- Do not transfer raw private exports to Mac by default.
- Do not import raw private exports into n8n runtime.
- Use sanitized exports for Mac reference and diff workflows.
- Raw private exports may be backed up only in encrypted private storage.
- Credentials and secret payloads must never be extracted from these files for runtime use.

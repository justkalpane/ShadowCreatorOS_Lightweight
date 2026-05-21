# Output Retention and Cleanup Policy

## Retention Defaults

- Default chat-only tasks create no files.
- Default repo-write mode creates one consolidated mission output folder/file under `outputs/missions/`.
- Full dossier mode is explicit only and uses `dossiers/`.

## Cleanup and Archive

- Temporary scratch files must not be committed.
- Old failed attempts can be placed under `outputs/archive/` only with user approval.
- Users can safely delete `outputs/missions/*` when not committed or needed.

## Security and Data Restrictions

- Never store secrets, credentials, API keys, cookies, or tokens.
- Never store raw provider outputs containing sensitive data unless explicitly approved and sanitized.
- Never store old DB/runtime state as active outputs.


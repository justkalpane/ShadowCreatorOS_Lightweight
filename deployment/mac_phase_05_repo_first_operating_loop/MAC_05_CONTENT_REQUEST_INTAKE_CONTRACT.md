# MAC-05 Content Request Intake Contract

## Required User Input Fields

- `topic`
- `platform`
- `language`
- `format`
- `target_duration`
- `tone`
- `audience`
- `objective`
- `constraints`
- `approval_mode`
- `provider_handoff_needed` (yes/no)
- `n8n_execution_needed` (yes/no)

## Intake Normalization Rules

- Normalize topic into concise canonical phrase.
- Convert user constraints into explicit no-go list.
- If `n8n_execution_needed=yes`, keep planning-only unless separate execution approval exists.
- If fields are missing, mark `NEEDS_CONFIRMATION`.

## Intake Output

- `mission_context.json` containing contract-required fields:
  - `original_user_message`
  - `normalized_topic`
  - `intent_id`
  - `intent_family`
  - `mission_hash`
  - `created_at`


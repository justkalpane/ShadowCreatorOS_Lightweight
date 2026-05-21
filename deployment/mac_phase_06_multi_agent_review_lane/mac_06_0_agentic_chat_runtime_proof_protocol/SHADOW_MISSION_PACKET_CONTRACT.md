# Shadow Mission Packet Contract

The Shadow Mission Packet normalizes a user request before repo-context loading and reasoning.

## Required Fields

- `user_request`
- `normalized_topic`
- `platform`
- `target_format`
- `audience`
- `tone`
- `objective`
- `constraints`
- `requested_output_mode`
- `allowed_execution_layer`
- `repo_branch`
- `active_doctrine_files`
- `historical_context_required`
- `n8n_allowed`
- `provider_execution_allowed`
- `expected_outputs`

## Defaults

- `repo_branch`: `main`
- `historical_context_required`: `false`
- `n8n_allowed`: `false`
- `provider_execution_allowed`: `false`
- `allowed_execution_layer`: `repo_first_agentic_reasoning`

## Expected Output Modes

- `chat_packet_only`
- `repo_dossier_files`
- `review_packet`
- `provider_handoff_reference_only`

## Safety Rule

If the user asks for external execution, the agent must stop at provider handoff unless execution approval, cost gate, and credential boundary are explicitly cleared.


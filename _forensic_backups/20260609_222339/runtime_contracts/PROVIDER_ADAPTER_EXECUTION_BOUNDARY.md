# Provider Adapter Execution Boundary

status: ACTIVE_BOUNDARY_CONTRACT
provider_execution_enabled: false
default_policy: provider_handoff_packet_may_be_prepared_but_not_executed_without_approval_packet
required_packets_before_execution:
- provider_handoff_packet
- approval_packet
- lineage_packet
validator_bindings:
- provider_handoff_packet_present
- provider_boundary_present
- no_n8n_provider_media_execution
forbidden_without_approval:
- n8n execution
- Gemini call
- OpenWebUI call
- media creation
- provider API call

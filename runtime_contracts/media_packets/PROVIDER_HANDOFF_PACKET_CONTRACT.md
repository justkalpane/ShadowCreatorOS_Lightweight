# PROVIDER_HANDOFF_PACKET Contract

packet_id: PROVIDER_HANDOFF_PACKET
producer_component: media_context_agents
consumer_component: provider_adapter_or_user_approval_gate
required_fields:
- provider_type
- typed_input
- typed_output
- provider_boundary
- execution_approval
- no_false_claims
- provider_execution_allowed
optional_fields:
- provider_notes
- user_review_notes
- version
validation_rules:
- all required_fields must be present before downstream stage runs
- packet must include lineage_fields and quality_metrics
- provider_execution_allowed=false unless explicitly approved
quality_metrics:
- completeness_score
- sync_score
- consistency_score
- risk_score
fallback_behavior: BLOCKED_BEFORE_OUTPUT or NEEDS_HUMAN_REVIEW when required fields are missing
lineage_fields:
- upstream_packet_id
- downstream_packet_id
- source_component_id
- evidence_path
approval_required: true when provider execution, media creation, repo write, or segment regeneration is requested
provider_execution_allowed: false

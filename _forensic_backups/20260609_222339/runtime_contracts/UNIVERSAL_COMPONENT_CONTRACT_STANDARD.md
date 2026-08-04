# MAC-06.2B Universal Component Contract Standard

status=ACTIVE_SUPPORTING_CONTRACT
applies_to=directors, agents, subagents, skills, subskills
purpose=Prevent shallow component labels by requiring typed inputs, outputs, communication pointers, validation, fallback, lineage, and provider boundaries for every runtime component.

## Mandatory Fields For Every Component

component_id:
component_layer:
component_name:
route_families:
activation_triggers:
upstream_inputs:
downstream_outputs:
required_input_packets:
emitted_output_packets:
communication_pointers:
quality_gates:
validator_bindings:
fallback_behavior:
lineage_fields:
provider_boundary:
status_limits:
human_approval_points:
failure_modes:
handoff_targets:
production_score_fields:

## Layer-Specific Requirements

### DIRECTOR

- decision_authority: Owns route decision boundary and cannot be a role label only.
- route_ownership: Declares route families it can govern.
- downstream_agent_selection: Selects only registered agents with matching route and packet capability.
- quality_authority: Can block output when required packets, scores, or lineage are missing.
- escalation_authority: Escalates to user or governance gate when route, evidence, or provider boundary is unclear.

### AGENT

- workflow_ownership: Owns one production stage from input packet to output packet.
- input_packet_consumption: Must consume required upstream packets before execution.
- output_packet_emission: Must emit a typed downstream packet with lineage and score.
- cross_agent_handoff: Handoff must use registries/communication_pointer_registry.yaml.
- fallback_route: Defines blocked, retry, degrade, or human review behavior.

### SUB_AGENT

- execution_lane: Owns a bounded lane such as hook, retention, claim validation, visual continuity, sync, or quality scoring.
- route_binding: Activated by route manifest or parent agent.
- skill_activation: Activates only skills with matching input schema and validator binding.
- validation_checkpoint: Records lane_output_validated=true/false and fallback.

### SKILL

- atomic_capability_group: Defines a callable capability group, not a generic description.
- activation_trigger: Declares trigger and route condition.
- input_output_schema: Defines required input and emitted output packet.
- downstream_subskill_hook: Calls subskills only through atomic_task_packet.
- quality_metric: Emits skill_quality_score and threshold.
- provider_boundary: Provider/tool execution disabled unless explicit approval and provider adapter contract exist.

### SUB_SKILL

- atomic_reusable_operation: Smallest reusable operation.
- micro_input: Explicit typed input.
- micro_output: Explicit typed output.
- validation_behavior: PASS/FAIL/NEEDS_HUMAN_REVIEW with reason.
- evidence_path: Points to upstream packet, source, or rule evidence.

## Runtime Rule

No downstream component may run from a selected component label alone. Every stage must have a required input packet, emitted output packet, communication pointer, validation rule, fallback behavior, and lineage field. If any required field is missing, return BLOCKED_BEFORE_OUTPUT or NEEDS_HUMAN_REVIEW instead of producing a normal final answer.

## Provider Boundary

VOICE_PROVIDER, IMAGE_PROVIDER, VIDEO_PROVIDER, MUSIC_SFX_PROVIDER, EDITING_PROVIDER, and PUBLISH_PROVIDER are typed handoff abstractions only by default. No provider, n8n, Gemini, OpenWebUI, or media execution is allowed unless explicitly approved and validated by a provider adapter contract.

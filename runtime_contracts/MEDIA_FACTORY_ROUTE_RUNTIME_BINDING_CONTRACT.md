# Media Factory Route Runtime Binding Contract

```text
contract_id=C-SO-ROUTE-8K
file_path=runtime_contracts/MEDIA_FACTORY_ROUTE_RUNTIME_BINDING_CONTRACT.md
owner=ShadowCreatorOS_Lightweight
route_id=MEDIA_FACTORY_HANDOFF
scope=bind_route_runtime_state_evidence_and_audit_flow
status=ACTIVE_BOUNDING_CONTRACT
unlocks_nothing=true
```

## Purpose

This contract binds the proven Batch 8H schemas, Batch 8I fixture oracle, and
Batch 8J validator layer into the `MEDIA_FACTORY_HANDOFF` control flow.

Route-state truth, evidence claims, and audit events must move together. A
route-state advance without a validator pass, evidence bundle, or Chitragupta
audit event is not a valid production claim.

## Required Inputs

```text
route_state_capsule
evidence_bundle
chitragupta_audit_event
validator_surface
human_review_packet
approval_token
pilot_cut_validation_packet
source_vs_render_artifact
visual_qa_artifact
contact_sheet
vayu_preflight
kubera_gate
yama_policy_gate
full_render_unlock_packet
tool_provider_boundary
tools_connectors_plugins_assessment
cut_level_visual_ledger
c18_comfyui_failure_state
```

## Required Outputs

```text
route_state_transition_record
route_gate_block_matrix
route_unlock_block_matrix
route_pass_evidence_matrix
no_fake_pass_regression_matrix
tools_connectors_plugins_assessment_record
```

## Bound Validator Surface

```text
validators/validate_pilot_cut_manifest.py
validators/validate_source_vs_render_artifact.py
validators/validate_visual_qa_artifact.py
validators/validate_contact_sheet.py
validators/validate_human_review_packet.py
validators/validate_approval_token.py
validators/validate_c04a_asset_manifest.py
validators/validate_approval_gate_matrix.py
validators/validate_route_state_capsule.py
validators/validate_evidence_bundle.py
validators/validate_chitragupta_audit_event.py
validators/validate_vayu_preflight.py
validators/validate_kubera_gate.py
validators/validate_yama_policy_gate.py
validators/validate_creative_intent_packet.py
validators/validate_packet_handoff_chain.py
validators/validate_cut_level_visual_ledger.py
validators/validate_full_render_unlock_packet.py
validators/validate_c18_comfyui_failure_state.py
validators/validate_tool_provider_boundary.py
validators/validate_ffmpeg_filtergraph_governance.py
validators/validate_depth_true_parallax.py
validators/validate_hyperframes_composition.py
```

## Route Gate Model

The route may only advance when all of these are true:

```text
pilot_prep_allowed=false until validator surface passes
pilot_execution_allowed=false until Vayu, Kubera, and Yama gates pass
full_render_allowed=false until pilot acceptance and full render unlock pass
audio_allowed=false until visual acceptance and timing lock are explicit
provider_allowed=false until approval and lineage are explicit
davinci_allowed=false until visual and audio acceptance are explicit
```

## Required Transition Constraints

Every route-state transition must include:

```text
required_validators
required_artifacts
required_evidence_bundle
required_audit_event
required_human_action
required_token
blocked_actions
forbidden_next_states
error_code_if_blocked
```

## Route Bindings

```text
MEDIA_FACTORY_HANDOFF
```

## Evidence Rules

- Every gate claim must cite an evidence bundle.
- Every route-state truth claim must cite a route-state capsule hash.
- Every unlock claim must be traceable to a validator pass and an audit event.
- No fake PASS may upgrade route state.

## Audit Rules

- Every route-state transition must emit a Chitragupta audit event.
- The audit event must reference the same route-state capsule and evidence
  bundle.
- A transition without an audit event is blocked, even if the validator pass
  exists.

## Forbidden Claims

- `full_render_allowed=true` before pilot acceptance.
- `pilot_prep_allowed=true` without the full validation surface.
- `audio_allowed=true`, `provider_allowed=true`, or `davinci_allowed=true`
  from route truth alone.
- `PASS` from file-exists-only, ffprobe-only, hash-only, or memory-only proof.
- HyperFrames lane claims without `TOOLS_CONNECTORS_PLUGINS_ASSESSMENT` and
  `HYPERFRAMES_SKILL_MD_PROOF` are blocked even if a render artifact exists.

## Route State Defaults

```text
pilot_prep_allowed=false
pilot_execution_allowed=false
full_render_allowed=false
audio_allowed=false
provider_allowed=false
davinci_allowed=false
```

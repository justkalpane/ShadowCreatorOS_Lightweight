# Antigravity HyperFrames Method Test Checklist

mission_id=yash_self_investment
route_id=MEDIA_FACTORY_HANDOFF
mode=TEST_ONLY_NO_REPO_WRITE

## Objective

Test every active HyperFrames non-cinematic B-roll family one by one and verify exact capability behavior instead of relying on one bundled 30-second proof.

## Hard Rules

- Do not modify anything under `/Users/apple/Documents/ShadowCreatorOS_Lightweight`
- Do not modify control contracts, schemas, or packets
- Do not call cloud providers
- Do not use `n8n`
- Do not generate new images
- Do not use Depth Anything V2 for this suite
- Do not require DaVinci Resolve
- Return all findings in chat or external notes unless explicit write-back approval is later granted

## Required Inputs

- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/packets/hyperframes_method_validation_packet.json`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/packets/hyperframes_30s_proof_packet.json`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/packets/media_factory_packet.json`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/support/antigravity_hyperframes_method_test_checklist.md`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/support/antigravity_result_deep_analysis_checklist.md`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/outputs/missions/yash_self_investment/support/antigravity_repo_deep_audit_checklist.md`
- `/Users/apple/ShadowMediaFactory/control_panel/templates/hyperframes_template_registry.json`
- `/Users/apple/ShadowMediaFactory/control_panel/templates/hyperframes_effect_pack_registry.json`

## Required Preflight

1. Run local status
2. Run local doctor
3. Confirm `hyperframes_callable=true`
4. Confirm `ffmpeg_callable=true`
5. Confirm `ffprobe_callable=true`
6. Confirm `providers_called=false`
7. Confirm `n8n_used=false`
8. Confirm alpha overlay production truth on this machine is `.mov`

## Family Coverage

Every family below must be tested independently:

1. `playstation_dashboard_panel`
2. `notebooklm_dual_panel`
3. `image_evidence_wall`
4. `kinetic_principle_card`
5. `webm_alpha_overlay`

## Capability Coverage Per Family

For each test case, verify all relevant items below:

- raw family render succeeds
- source background path is honored where required
- scene-reactive payload text is honored
- `effect_pack_ids` are either visibly applied or honestly marked unproven
- `border_pack_id` is visibly applied or honestly marked unproven
- output container matches expectation
- duration matches expectation
- proof JSON exists
- registry event exists
- fallback is explicit if a requested behavior cannot be executed

## Required Test Sequence

### Stage 1 — Raw Family Render

For each family:

- render a raw family output
- verify container, codec, duration, proof JSON, registry event
- extract one verification frame

### Stage 2 — Payload Injection

For dashboard, notebook, evidence wall, and principle card:

- inject cut-specific fields from the validation packet
- verify that rendered text is not generic template placeholder text
- compare expected headline/support/metric values against the frame

### Stage 3 — Background Integration

For non-overlay families:

- composite family output against the specified `source_background`
- verify the background image is the real local image, not a template-native filler background
- extract one verification frame

### Stage 4 — V3 Effect Validation

Test visible application of:

- `dust_motes_01`
- `glowing_node_01`
- `sparks_01`

Rules:

- if the asset is present and composited, mark `VISIBLE_PROVEN`
- if present on disk but not visibly composited, mark `PRESENT_NOT_PROVEN_IN_OUTPUT`
- do not claim smoke unless it is truly rendered and visible

### Stage 5 — Border / HUD Validation

Validate:

- `hud_corner_brackets`
- `gold_border_sweep`
- any family-embedded rails, lines, traces, nodes, or corner brackets

### Stage 6 — Alpha Overlay Validation

For `webm_alpha_overlay`:

- render to `.mov` only
- verify alpha-capable pixel format
- composite over a real local background
- confirm no white-card or black-plate failure

### Stage 7 — Timing / Assembly Validation

For each micro test:

- verify raw duration
- verify composite duration
- verify no accidental clip truncation
- if concat or final assembly is attempted, verify `ffprobe` truth instead of trusting summary JSON

### Stage 8 — Audio Truth Check

Do not force a full audio build if the test does not require it.

Instead verify honestly:

- audio assets declared
- audio assembly path exists or does not exist
- audio actually present or absent in produced artifact

## Required Outputs Per Test

Each test must return:

- `test_id`
- `template_family`
- `expected_capabilities`
- `actual_capabilities`
- `output_path`
- `proof_json_path`
- `registry_evidence_path`
- `ffprobe_summary`
- `verification_frame_path`
- `drift_found=true/false`
- `drift_reason=`
- `status=PASS/PARTIAL/BLOCKED`

## Fail Conditions

- generic template text shown instead of packet text
- background image ignored
- requested effect claimed but not visible
- overlay rendered in non-approved alpha container
- proof JSON disagrees with `ffprobe`
- duration mismatch
- fallback occurred but was not reported

## Final Summary Required

Antigravity must finish with:

- proved families
- proved capabilities
- capabilities present on disk but not proven in output
- capabilities requested but missed
- root cause guesses for each drift
- exact list of files/artifacts inspected

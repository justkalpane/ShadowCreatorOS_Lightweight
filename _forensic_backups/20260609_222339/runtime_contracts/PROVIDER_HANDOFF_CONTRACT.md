# Provider Handoff Contract

## Purpose

Media Factory handoff packets must be generated with strict honesty about what
was executed, what was planned, and what requires approval. This contract governs
provider and local engine execution claims, artifact evidence requirements, and
the honesty status vocabulary for all media lanes.

## Provider Honesty Law

Every Media Factory output must declare its execution state for each lane.

```text
PROVIDER_HONESTY_GATE
providers_called=true/false
n8n_used=true/false
local_media_generation_engine_used=true/false
media_artifacts_claimed=true/false
provider_execution_allowed=false
```

Rules:

- If no provider was called, set `providers_called=false`. Do not imply otherwise.
- If no n8n workflow was executed, set `n8n_used=false`. Do not imply otherwise.
- If a local media engine (ComfyUI, FFmpeg, AnimateDiff, etc.) produced output,
  set `local_media_generation_engine_used=true` and include artifact evidence.
- If only prompt packets were generated and no media was produced, set
  `media_artifacts_claimed=false`.
- If actual images, videos, or audio were generated, set
  `media_artifacts_claimed=true` and include evidence for every artifact.

No fake PASS. No fake execution claim. No implied execution without evidence.

## Execution Evidence Schema

For every claimed media artifact, the following evidence block is mandatory:

```text
media_artifact_evidence:
  artifact_id=
  file_path=
  artifact_name=
  artifact_type=image/video/audio/storyboard/pacing_metadata
  generation_method=local_engine/cloud_provider/ai_image_generation/manual
  engine_or_provider_used=
  source_prompt_packet_ref=
  render_metadata_path=
  validation_result=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION
  human_review_status=reviewed/pending/not_required
```

Missing any field on a claimed artifact downgrades status from `PASS` to
`PARTIAL` or `BLOCKED`.

## Local Engine Honesty

When a local engine produces output:

```text
local_engine_evidence:
  engine_id=
  engine_readiness_at_execution=LOCAL_ENGINE_READY/EXECUTABLE
  render_metadata_path=
  output_path=
  output_format=
  validation_result=
  human_review_status=
```

Claiming `local_media_generation_engine_used=true` without a valid
`local_engine_evidence` block is `FAIL`.

## Handoff Packet Requirement

By default, generate a handoff packet only. No external execution unless
explicitly approved by the user. The handoff packet must be structured and
provider-ready without being executed.

A valid handoff packet includes:

- voice context (ElevenLabs-ready prompt boundary)
- image prompt packets (tool-translated, schema-valid)
- video prompt packets (camera, motion, ControlNet guidance)
- music/SFX direction brief
- editing timeline
- storyboard export plan (if applicable)
- local engine bridge status per lane
- execution boundary declaration

## Status Vocabulary

Allowed values for any execution-related status field:

```text
DESIGNED          — architecture planned, no execution performed
STUB              — placeholder, fields incomplete
PACKET_READY      — packet validated, execution not performed
LOCAL_ENGINE_READY — local engine confirmed, execution not yet triggered
PROVIDER_READY    — formatted for provider, execution not yet triggered
EXECUTABLE        — execution explicitly approved
BLOCKED           — dependency missing or approval not granted
NEEDS_CONFIRMATION — requires user decision
```

## Safety Boundary

```text
n8n_used=false
providers_called=false
media_artifacts_claimed=false
provider_execution_allowed=false
local_media_generation_engine_used=false
```

No field above may be set to `true` in a planning-only handoff. Override only
when execution is explicitly approved and evidence is present.

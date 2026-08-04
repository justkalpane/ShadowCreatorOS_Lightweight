# MAC-06.2M MindStudio Benchmark Deep Repo Hardening Audit

Status: PASS_AS_AUDIT

## Sources Read

1. https://www.mindstudio.ai/blog/generate-ai-videos-claude-code-hyperframes-elevenlabs-workflow
2. https://www.mindstudio.ai/blog/claude-code-skills-social-media-content-repurposing
3. https://www.mindstudio.ai/blog/generate-ai-videos-claude-code-hyperframes-elevenlabs

The benchmark shows a segment-based production pipeline: structured JSON scripts, per-segment narration and visuals, voice/audio synthesis, timing metadata, sync/assembly, review, partial regeneration, typed tool calls, and platform repurposing.

## Current Baseline

- Head: 94fd0acf9f9b729c904640e4778ec1851c7ab3ca
- Local enforcement baseline exists.
- Provider execution remains disabled.
- n8n remains disabled.
- Lightweight OS onboarding remains false.

## Alignment Summary

Shadow now has roads/gates/locks: route DAGs, packet schemas, validators, provider boundary, quality runtime, lineage/approval, and dry-run flow. It does not yet have benchmark-grade production intelligence inside every content/media route.

Coverage counts:

- concepts_extracted=57
- fully_covered=20
- partial_contract_only=7
- partial_runtime_only=21
- missing=0
- future_provider_only=9
- not_applicable=0

## Already Covered by MAC-06.2B-2I

- Route DAG validation and packet continuity.
- Packet schema validator and canonical schema index.
- Provider boundary blocking and false execution claim detection.
- Lineage and approval state store.
- Segment regeneration action at approval-store level.
- Quality scorecard runtime.
- Operator packet/handoff wrapper.

## Still Shallow

- Script segment schema is not a rich object model.
- Voice context lacks benchmark-grade fields like voice_id, tone, pause map, pronunciation notes, word timestamps, and per-segment emotion.
- Visual context lacks active seed/style-prefix/palette/composition/lighting/negative-prompt enforcement.
- Editing timeline lacks FFmpeg-safe command planning, concat, transitions, and timestamp drift correction.
- Social repurposing is not an active first-class route DAG.
- Quality validators do not yet reject generic content, vague visual prompts, weak hooks, or boring lines at the semantic level.

## Required Next Patch

Patch the intelligence layer, not more scaffolding. Priority order:

1. Upgrade segment/object packet schemas.
2. Add script quality semantic validators and negative fixtures.
3. Upgrade voice/visual/video/editing packet depth.
4. Add social repurposing route DAG in planning-only mode.
5. Add typed provider handoff call profiles while keeping provider_execution_allowed=false.

## Deferred

- n8n/webhook/cron automation.
- Provider execution and media generation.
- Real FFmpeg merge execution.
- Production-ready/onboarding claims.

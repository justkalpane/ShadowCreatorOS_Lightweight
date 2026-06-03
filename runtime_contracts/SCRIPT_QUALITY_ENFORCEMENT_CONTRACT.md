# Script Quality Enforcement Contract

Every script/content task must include these gates before final verdict.

For every 3-10 minute YouTube script, the quality gate must consume
`runtime_contracts/SCRIPT_STORY_ENGINE_CONTRACT.md`.

It must also consume:

- `runtime_contracts/SCRIPT_LANGUAGE_CONTROL_CONTRACT.md`
- `runtime_contracts/REAL_TIME_RESEARCH_ENFORCEMENT_CONTRACT.md`
- `runtime_contracts/SOURCE_QUALITY_CLASSIFICATION_CONTRACT.md`
- `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md`
- `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md`
- `runtime_contracts/LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT.md`

## TOPIC_QUALITY_GATE

```text
relevance_score=
trend_source_score=
audience_fit_score=
novelty_score=
production_feasibility_score=
approved=true/false
reason=
```

## HOOK_GENERATION_GATE

```text
hook_variant_1=
hook_variant_2=
hook_variant_3=
score_each=
selected_hook=
selection_reason=
```

## SCRIPT_QUALITY_GATE

```text
emotional_strength_score=
clarity_score=
novelty_score=
retention_score=
creator_specificity_score=
visualizability_score=
CTA_strength_score=
overall_score=
pass_threshold=
passed=true/false
```

## CINEMATIC_STORY_GATE

```text
cinematic_story_required=true/false
story_duration_target_seconds=
story_basis=
character_present=true/false
conflict_present=true/false
turning_point_present=true/false
cinematic_visuals_present=true/false
emotional_peak_present=true/false
lesson_bridge_present=true/false
source_dependency_satisfied=true/false
cinematic_story_gate_status=
```

## Production Gates

```text
LANGUAGE_GATE
default_master_script_language_english=
explicit_language_request_respected=
translation_stage_separate=
language_gate_status=

SOURCE_QUALITY_GATE
source_count=
non_encyclopedia_source_count=
source_category_count=
fact_vs_anecdote_map_present=
source_quality_gate_status=

DYNAMIC_BEAT_MAP_GATE
beat_duration_dynamic=
uniform_15_second_grid=
uniform_grid_justification_present=
dynamic_beat_fields_complete=
dynamic_beat_map_gate_status=

MEDIA_SYNC_GATE
media_factory_final_draft_requested=
scene_sync_matrix_complete=
media_contexts_synchronized=
influence_map_creative_depth_complete=
media_sync_gate_status=

LOCAL_CLOUD_HYBRID_GATE
local_cloud_hybrid_execution_plan_present=
provider_execution_allowed=false
local_cloud_hybrid_gate_status=
```

## RECURRING_HOOK_DENSITY_GATE

`HOOK_GENERATION_GATE` chooses the opening hook only. It does not satisfy
recurring retention-hook requirements.

```text
opening_hook_present=
recurring_rehook_required=
recurring_rehook_count=
rehook_interval_seconds=
max_gap_without_rehook_seconds=
rehook_interval_dynamic=
rehook_interval_reason_present=
rehooks_mapped_to_final_script=
rehooks_mapped_to_beat_map=
rehooks_mapped_to_editing_context=
rehooks_mapped_to_line_influence_map=
rehooks_mapped_to_scene_sync_matrix=
rehook_density_gate_status=
```

For every 3-10 minute YouTube script:

- opening hook is mandatory
- recurring re-hooks default to a dynamic 70-90 second interval
- no unexplained gap without a re-hook may exceed 90 seconds
- every major section needs a topic-relevant retention reset
- a 5-minute script needs at least three internal re-hooks plus a CTA hook
- factual re-hooks must be source-safe and present in `FACT_VS_ANECDOTE_MAP`
- Media Factory final drafts must synchronize re-hook moments across voice,
  image, video, music/SFX, editing, platform, influence, and execution rows

## Rewrite Law

- If `overall_score < pass_threshold`, rewrite before final.
- If hook score is weak, generate new hooks.
- If visualizability is weak, route to visual/context skill.
- If emotional strength is weak, route to emotion rewrite.
- If creator specificity is weak, route to audience/persona skill.
- Do not label script output final until the gate passes or the user explicitly approves limited mode.
- Hook variants require scores and rejection reasons.
- Quality gate requires scores plus `pass_threshold`.
- Rewrite is required if `overall_score < pass_threshold`.
- Governance lock must approve the final script.
- Final output cannot classify as `PASS` if `SCRIPT_QUALITY_GATE` is missing.
- Manual structured output without a quality scorecard is `PARTIAL`, not `PASS`.
- A required cinematic story that is missing or structurally incomplete cannot
  pass.
- A real-person or real-incident story without source evidence cannot pass.
- A non-English master draft without explicit user request cannot pass.
- Source presence without source sufficiency cannot pass.
- A rigid unexplained 15-second timeline cannot pass.
- A final Media Factory draft without a scene sync matrix cannot pass.
- Final proof must match the weakest production gate.
- Three opening-hook variants do not excuse a missing recurring re-hook map.
- One-hook-only 3-10 minute YouTube scripts cannot pass.

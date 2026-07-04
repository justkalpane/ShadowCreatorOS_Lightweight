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
spoken_cadence_score=
sentence_length_variety_score=
contrast_shift_score=
attention_reset_score=
article_like_risk_score=
overall_score=
pass_threshold=
passed=true/false
```

## CADENCE_AND_RETENTION_GATE

```text
spoken_cadence_score=
sentence_length_variety_score=
contrast_shift_score=
attention_reset_score=
article_like_risk_score=
cadence_gate_status=
```

This gate measures whether the script actually sounds spoken. It must fail if
the draft is smooth but flat, article-like, or missing a visible rhythm shift
across the body.

## LIVE_HOST_REALTIME_BEHAVIOR_GATE

```text
second_person_address_present=
direct_host_turns_present=
spoken_interruptions_present=
emotional_pivots_present=
live_host_realtime_behavior_gate_status=
```

For every 3-10 minute YouTube script, the spoken body must sound like a real
host talking to a viewer in motion, not like an article, essay, or theory
summary. A clean motivational article surface cannot pass this gate.

## ARTICLE_LIKE_RISK_GATE

```text
article_like_risk_score=
host_presence_score=
article_like_risk_gate_status=
```

If article-like surface risk is high and host presence is weak, final proof
cannot be `PASS` even when numeric quality scores are otherwise high.

## VALIDATION_SCORECARD

```text
topic_quality_gate_status=
hook_generation_gate_status=
script_quality_gate_status=
cadence_and_retention_gate_status=
source_integrity_gate_status=
script_body_depth_lock_status=
recurring_hook_density_lock_status=
governance_lock_status=
line_by_line_influence_map_status=
final_proof_classification=
```

Numeric scores, `overall_score`, and `passed=true` are advisory only until all
hard gates pass. No score surface may override a failed source, cadence,
host-behavior, route-scope, or governance gate.

## EXECUTION_VISIBILITY_GATE

```text
gate_visibility_log_present=
proof_trace_bundle_present=
route_state_capsule_present=
trace_back_to_gates_present=
line_to_gate_trace_present=
execution_visibility_gate_status=
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

SOURCE_INTEGRITY_GATE
source_specificity_score=
source_url_specificity_score=
claim_classification_completeness_score=
fact_vs_anecdote_map_completeness_score=
unsupported_claims_count=
source_integrity_gate_status=

SOURCE_TO_SCRIPT_ALIGNMENT_GATE
fact_like_script_lines_checked=
aligned_fact_like_lines=
unaligned_fact_like_lines=
source_to_script_alignment_gate_status=

ABSOLUTE_CLAIM_DOWNGRADE_GATE
absolute_claim_lines_checked=
unsupported_absolute_claims=
absolute_claim_downgrade_gate_status=

DYNAMIC_BEAT_MAP_GATE
beat_duration_dynamic=
uniform_15_second_grid=
uniform_grid_justification_present=
dynamic_beat_fields_complete=
dynamic_beat_map_gate_status=

SCRIPT_BODY_DEPTH_GATE
target_runtime_seconds=
estimated_spoken_word_count=
narration_pacing_wpm=
pause_buffer_seconds=
estimated_spoken_runtime_seconds=
duration_fit_status=PASS/BLOCKED/NEEDS_CONFIRMATION
script_body_depth_gate_status=

MEDIA_SYNC_GATE
media_factory_final_draft_requested=
scene_sync_matrix_complete=
media_contexts_synchronized=
influence_map_creative_depth_complete=
media_sync_gate_status=

PRODUCTION_CHAIN_GATE
production_order_lock_present=
production_phase_rows_exact_order=
control_panel_phase_rows_present=
mandatory_route_actors_individually_opened=
rule_consumption_evidence_ledger_present=
exact_rule_lineage_map_present=
production_chain_gate_status=

LOCAL_CLOUD_HYBRID_GATE
local_cloud_hybrid_execution_plan_present=
provider_execution_allowed=false
local_cloud_hybrid_gate_status=

CHAT_OUTPUT_CLEANNESS_GATE
chat_output_primary_asset=
final_script_before_media_context_sections=
chat_output_cleanness_gate_status=

BIOPIC_RECONSTRUCTION_DISCLOSURE_GATE
cinematic_reconstruction=
biopic_reconstruction_disclosure_present=
verified_scene_details_disclosed=
biopic_reconstruction_disclosure_gate_status=

SCRIPT_HONESTY_CONTRADICTION_GATE
verified_scene_details_false_with_pass=false
weak_inference_presented_as_fact=false
root_domain_source_ledger_urls=false
evergreen_current_or_realtime_inflation=false
script_honesty_contradiction_gate_status=
```

If any hard gate is `FAIL`, `BLOCKED`, or `NEEDS_CONFIRMATION`, the script must
not self-report `PASS`. Validator-visible contradiction is an automatic fail.

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
- recurring re-hooks default to a dynamic 25-30 second interval
- no unexplained gap without a re-hook may exceed 30 seconds
- every major section needs a topic-relevant retention reset
- a 5-minute script needs recurring re-hooks throughout the body, typically
  eight to ten internal re-hooks plus a CTA hook
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
- Do not produce a shortened or "best effort" script when route scope is
  incomplete. Missing route manifest, mandatory files, or unread mandatory
  actors requires `BLOCKED_BEFORE_OUTPUT`.
- Synthetic consumption ledgers, "evaluated internally" statements, and
  unread components marked as `USED` invalidate the script quality gate.
- Hook variants require scores and rejection reasons.
- Quality gate requires scores plus `pass_threshold`.
- Rewrite is required if `overall_score < pass_threshold`.
- Governance lock must approve the final script.
- Final output cannot classify as `PASS` if `SCRIPT_QUALITY_GATE` is missing.
- Final output cannot classify as `PASS` if `VALIDATION_SCORECARD` is missing.
- Final output cannot classify as `PASS` if `EXECUTION_VISIBILITY_GATE` is missing.
- Manual structured output without a quality scorecard is `PARTIAL`, not `PASS`.
- A required cinematic story that is missing or structurally incomplete cannot
  pass.
- A real-person or real-incident story without source evidence cannot pass.
- A non-English master draft without explicit user request cannot pass.
- Source presence without source sufficiency cannot pass.
- Root-domain-only source ledgers cannot pass. Source rows must cite specific
  pages/articles/interviews/records, not only domains.
- Evergreen or stable biographical topics cannot inflate themselves into
  `current_data_required=true`, `real_time_sources_used=true`, or realtime
  research unless the user asked for current/latest context or the claim truly
  depends on recency.
- `verified_scene_details=false` cannot coexist with `status=PASS` for a real
  person cinematic story block. It must remain disclosed/limited.
- Inferences cannot be phrased as hard facts. Phrases such as "every single
  rupee," "all the money," "entirely," or "all earnings" require direct
  evidence; otherwise they must be downgraded or removed.
- A real-person script whose spoken lines outrun the mapped facts cannot pass.
- Unsupported absolute claims about a real person cannot pass.
- A rigid unexplained 15-second timeline cannot pass.
- A script with weak spoken cadence or high article-like risk cannot pass.
- A script that does not vary sentence shape, contrast, and attention resets
  cannot pass even if the factual content is otherwise correct.
- A final Media Factory draft without a scene sync matrix cannot pass.
- Off-topic current-film or teaser promotion inside the spoken script cannot
  pass unless the user explicitly requested the tie-in.
- Final proof must match the weakest production gate.
- Three opening-hook variants do not excuse a missing recurring re-hook map.
- One-hook-only 3-10 minute YouTube scripts cannot pass.

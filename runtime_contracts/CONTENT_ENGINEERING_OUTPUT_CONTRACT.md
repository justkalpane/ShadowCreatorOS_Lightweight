# Content Engineering Output Contract

Every script/content/video task must output more than a script unless the user explicitly asks for script-only.

For every 3-10 minute YouTube script, a 45-75 second
`CINEMATIC_SHORT_STORY_BLOCK` is mandatory. The story appears after the hook and
before the main teaching section unless the route records a justified override.

## Default Assumptions

- YouTube Shorts default duration is 45-60 seconds when the user does not specify duration.
- Instagram Reel default duration is 30-45 seconds when the user does not specify duration.
- YouTube long-form uses the user-provided duration; if the user says 5 minutes,
  produce a long-form English master script plus a dynamic timed beat map.
- Beat durations must be justified and vary with narrative and Media Factory
  needs. Do not hard-lock long-form output to a uniform 15-second grid.
- If platform is unknown, infer the likely platform and disclose the assumption.
- If the user explicitly asks for script-only, provide script-only and mark full content engineering as not requested.
- Default the first master script to English. Translation/localization is a
  separate downstream stage unless the user explicitly requests another
  language.

## 0. SCRIPT_LANGUAGE_DECLARATION

- master script language
- explicit user language request check
- translation stage status
- language inference blocked

## 1. SHADOW_MISSION_PACKET

- task intent
- selected route
- script-only explicitly requested: true/false
- platform
- duration
- provider execution boundary

## 2. CONTENT_MISSION_BRIEF

- topic
- platform
- duration
- audience
- objective
- emotional promise
- transformation promise

## 3. RESEARCH_AND_SOURCE_STATUS

- freshness_class
- research_mode
- web_access_available
- web_access_used
- real_time_sources_used
- source_list
- confidence
- current_data_required
- source_list with URL, title, date, and access status
- video_reference_list when available
- unsupported_claims
- current_fact_confidence
- research_sufficiency_gate_status
- source count, non-encyclopedia source count, and source category count

## 3A. SOURCE_LEDGER + FACT_VS_ANECDOTE_MAP

- classify every source by type
- separate verified fact, anecdotal support, background context, inference,
  needs-confirmation, and unsupported claims
- require at least three sources, two non-encyclopedia sources, and three
  source categories for real-person proof scripts when suitable sources exist

## 4. CLAIM_EVIDENCE_STATUS

For every production-sensitive real-world claim:

- claim
- evidence
- evidence path
- command output or source reference
- status

## 5. HOOK_VARIANTS

- at least three scored variants
- selected hook
- selected hook reason

`HOOK_VARIANTS` chooses the opening hook only. It does not satisfy recurring
retention-hook requirements.

## 6. CINEMATIC_SHORT_STORY_BLOCK

```yaml
cinematic_short_story:
  required: true
  duration_target_seconds: 45-75
  story_basis: verified_real_incident | real_person_public_arc | realistic_composite | mythological_parallel | hybrid_modern_mythological_reference
  cinematic_reconstruction:
  verified_scene_details:
  source_dependency:
    required_when_real_person_or_real_incident: true
  character:
  setting:
  conflict:
  stakes:
  turning_point:
  cinematic_visuals:
  emotional_peak:
  lesson_bridge:
  topic_connection:
  source_references:
  unsupported_claims:
  status: PASS | PARTIAL | FAIL
```

The story must resemble the topic and bridge naturally into the teaching
section. A real-person or real-incident story cannot pass without source
references.

## 7. SCRIPT_STRUCTURE

- hook
- setup
- tension
- payoff
- CTA

## 7A. RECURRING_REHOOK_MAP

For every 3-10 minute YouTube script:

- `rehook_id`
- `timestamp_range`
- `hook_type`
- `hook_line`
- `retention_function`
- `emotional_trigger`
- `topic_connection`
- `beat_map_scene_id`
- `media_factory_dependency`

Recurring re-hooks default to a dynamic 70-90 second interval. A 5-minute
script needs at least three internal re-hooks plus a CTA hook. Re-hooks must
appear inside the final script, not only in a planning list.

Canonical machine-check output must emit one JSON object per row:

```text
rehook_row_json={"rehook_id":"...","timestamp_seconds":75,"hook_type":"...","hook_line":"...","retention_function":"...","emotional_trigger":"...","topic_connection":"...","beat_map_scene_id":"...","line_influence_reference":"..."}
```

Headings, booleans, and placeholder rows do not satisfy the re-hook gate.
For real-person proof scripts, `SOURCE_LEDGER` and `FACT_VS_ANECDOTE_MAP`
must also emit structured `source_row_json=` and `fact_map_row_json=` rows.

## 8. FINAL_SCRIPT

Provide the final spoken script.

## 9. DYNAMIC_TIMED_BEAT_MAP

Use dynamic 3-20 second blocks. Every block needs a duration reason.

- scene ID, start time, end time, duration, and duration reason
- spoken line or summary and scene purpose
- emotion and voice cue
- avatar, B-roll, image, and video cues
- music/SFX and transition cues
- platform dependency
- local/cloud/hybrid dependency
- hook marker, re-hook type, and retention reset goal

## 10. VOICE_GENERATION_CONTEXT

- voice style
- gender/age vibe if user allows
- tone
- pacing
- pauses
- emphasis
- emotion per segment
- pronunciation notes
- ElevenLabs-ready prompt boundary without calling ElevenLabs

## 11. IMAGE_GENERATION_CONTEXT

- thumbnail concept
- scene image prompts
- style
- lighting
- composition
- negative prompts if applicable
- provider boundary

## 12. VIDEO_GENERATION_CONTEXT

- scene prompts
- camera motion
- character action
- transitions
- visual continuity
- provider boundary for Sora / Seedance / Higgsfield / HeyGen

## 13. MUSIC_AND_SFX_CONTEXT

- music mood
- tempo
- intensity changes
- SFX moments
- silence moments

## 14. EDITING_CONTEXT

- retention cuts
- zooms
- captions
- transitions
- pattern interrupts
- re-hooks

## 15. PLATFORM_PACKAGING

- title ideas
- thumbnail text
- description
- hashtags
- pinned comment
- CTA

## 16. PROVIDER_HANDOFF_BOUNDARY

- `n8n_used=false`
- `providers_called=false`
- `media_artifacts_claimed=false`
- execution requires approval

## 17. QUALITY_GATE

- topic adherence
- emotional strength
- retention strength
- originality
- platform fit
- source confidence
- provider boundary compliance

## 18. LINEAGE_SUMMARY

- upstream research packet IDs
- claim evidence references
- story source references
- script segment IDs
- quality-gate decision
- approval state

## 19. SCENE_SYNC_MATRIX

Required when a Media Factory final draft is requested. Every scene must align
script, voice, image, video, music/SFX, editing, platform packaging, creative
influence, and local/cloud/hybrid execution.

## 20. LOCAL_CLOUD_HYBRID_EXECUTION_PLAN

When media context is present, define local, cloud, and hybrid options plus a
fallback for voice, image, video, music/SFX, editing, and packaging.

## 21. MEDIA_FACTORY_EVIDENCE_GATE

Required when any media artifact is claimed or local engine execution is referenced.

```text
MEDIA_FACTORY_EVIDENCE_GATE
providers_called=true/false
n8n_used=true/false
local_media_generation_engine_used=true/false
media_artifacts_claimed=true/false
provider_execution_allowed=false
storyboard_export_status=DESIGNED/STUB/PACKET_READY/LOCAL_ENGINE_READY/EXECUTABLE
```

For each claimed artifact:

```text
media_artifact_evidence:
  artifact_id=
  file_path=
  artifact_name=
  artifact_type=image/video/audio/storyboard/pacing_metadata
  generation_method=
  engine_or_provider_used=
  source_prompt_packet_ref=
  render_metadata_path=
  validation_result=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION
  human_review_status=reviewed/pending/not_required
```

This gate must be present in every Media Factory final draft output. Missing gate
when artifacts are claimed downgrades status from `PASS` to `BLOCKED`.

## PASS Honesty Law

- Missing `CINEMATIC_SHORT_STORY_BLOCK` is `PARTIAL` or `FAIL`.
- A real-person or real-incident story without source references is `PARTIAL`
  or `FAIL`.
- Non-empty `unsupported_claims` prevents `SOURCE_RESEARCH_LOCK=PASS`.
- Script-only output is `PARTIAL` unless the user explicitly requested
  script-only.
- Final proof status must match the weakest evidence layer.
- A 3-10 minute YouTube script with only an opening hook cannot pass.
- Missing `RECURRING_REHOOK_MAP` or an unexplained re-hook gap above 90 seconds
  prevents `PASS`.
- A non-English master script without explicit user request cannot pass.
- A real-person script with insufficient source breadth cannot pass.
- A rigid unexplained 15-second beat grid cannot pass.
- A Media Factory final draft with disconnected context sections cannot pass.
- Missing `MEDIA_FACTORY_EVIDENCE_GATE` when media artifacts are claimed prevents `PASS`.
- A claimed artifact without `file_path` and `generation_method` evidence prevents `PASS`.

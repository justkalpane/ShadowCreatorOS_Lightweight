# Content Engineering Output Contract

Every script/content/video task must output more than a script unless the user explicitly asks for script-only.

## 1. CONTENT_MISSION_BRIEF

- topic
- platform
- duration
- audience
- objective
- emotional promise
- transformation promise

## 2. RESEARCH_AND_SOURCE_STATUS

- freshness_class
- research_mode
- web_access_available
- web_access_used
- real_time_sources_used
- source_list
- confidence

## 3. SCRIPT_STRUCTURE

- hook
- setup
- tension
- payoff
- CTA

## 4. FINAL_SCRIPT

Provide the final spoken script.

## 5. TIMED_BEAT_MAP

For every 5-10 seconds:

- timestamp
- spoken line
- emotion
- pacing
- facial expression
- gesture/body movement
- visual direction
- on-screen text
- B-roll/image/video idea
- edit cue
- music/SFX cue

## 6. VOICE_GENERATION_CONTEXT

- voice style
- gender/age vibe if user allows
- tone
- pacing
- pauses
- emphasis
- emotion per segment
- pronunciation notes
- ElevenLabs-ready prompt boundary without calling ElevenLabs

## 7. IMAGE_GENERATION_CONTEXT

- thumbnail concept
- scene image prompts
- style
- lighting
- composition
- negative prompts if applicable
- provider boundary

## 8. VIDEO_GENERATION_CONTEXT

- scene prompts
- camera motion
- character action
- transitions
- visual continuity
- provider boundary for Sora / Seedance / Higgsfield / HeyGen

## 9. MUSIC_AND_SFX_CONTEXT

- music mood
- tempo
- intensity changes
- SFX moments
- silence moments

## 10. EDITING_CONTEXT

- retention cuts
- zooms
- captions
- transitions
- pattern interrupts
- re-hooks

## 11. PLATFORM_PACKAGING

- title ideas
- thumbnail text
- description
- hashtags
- pinned comment
- CTA

## 12. PROVIDER_HANDOFF_BOUNDARY

- `n8n_used=false`
- `providers_called=false`
- `media_artifacts_claimed=false`
- execution requires approval

## 13. QUALITY_GATE

- topic adherence
- emotional strength
- retention strength
- originality
- platform fit
- source confidence
- provider boundary compliance

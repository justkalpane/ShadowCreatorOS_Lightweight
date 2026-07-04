# Dynamic Timed Beat Map Contract

## Purpose

Timed beats must follow narrative and Media Factory dependencies. A rigid
15-second grid is not a production timeline.

## Dynamic Timing Law

```text
beat_duration_dynamic=true
allowed_block_duration_seconds=3-20
block_duration_reason_required=true
uniform_15_second_grid_allowed_only_with_justification=true
```

Beat duration must respond to:

- topic type
- total duration
- voice pacing
- avatar delivery
- image generation needs
- video generation complexity
- B-roll availability
- music and SFX timing
- platform format
- local, cloud, or hybrid Media Factory dependencies

## Required Beat Fields

```text
scene_id=
start_time=
end_time=
duration_seconds=
duration_reason=
spoken_line_or_summary=
scene_purpose=
emotional_cue=
voice_cue=
visual_cue=
avatar_cue=
broll_or_image_cue=
music_sfx_cue=
transition_cue=
platform_dependency=
local_cloud_hybrid_dependency=
hook_marker=true/false
rehook_type=
retention_reset_goal=
```

Every 3-10 minute YouTube script must mark opening-hook and recurring re-hook
beats. Re-hook intervals default to 70-90 seconds and remain dynamic. Every
re-hook scene requires a topic-relevant retention reset goal.

## Guidance

- Hook beats commonly use 3-7 seconds.
- Cinematic story beats commonly use 8-12 seconds.
- Teaching beats commonly use 10-18 seconds.
- Action steps commonly use 8-15 seconds.
- CTA beats commonly use 5-10 seconds.

These are ranges, not hard locks.

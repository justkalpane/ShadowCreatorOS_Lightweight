# Script Story Engine Contract

## Purpose

Every 3-10 minute YouTube script must contain a relevant cinematic short story
that earns attention before the main teaching section.

## Mandatory Trigger

```text
platform=YouTube
script_duration_minutes>=3
script_duration_minutes<=10
cinematic_story_required=true
story_duration_target=45_to_75_seconds
story_position=after_hook_before_main_teaching
story_must_resemble_topic=true
```

## Story Shape

The `CINEMATIC_SHORT_STORY_BLOCK` must include:

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

## Source Dependency

- `verified_real_incident` and `real_person_public_arc` stories require source
  references.
- Biographical or career claims require web-assisted research when web access
  is available.
- A named public figure, celebrity, actor, founder, brand owner, or other
  known real-world identity defaults to `real_person_public_arc`.
- A known real-world identity cannot be downgraded to `realistic_composite`
  unless the user explicitly asks for a fictionalized, inspired-by, or
  composite retelling.
- If unsupported claims remain, story status and source-research status cannot
  be `PASS`.
- A `realistic_composite` or `mythological_parallel` story must be labeled
  honestly. Do not present it as a verified real event.
- If cinematic details are reconstructed, set `cinematic_reconstruction=true`
  and `verified_scene_details=false`.
- Mythological parallels must directly reinforce the topic. Decorative or
  unrelated mythology fails.

## Quality Gate

The story gate fails or downgrades when:

- the story block is missing
- duration is outside 45-75 seconds
- character, conflict, stakes, turning point, cinematic visuals, emotional
  peak, lesson bridge, or topic connection is missing
- the story does not resemble the topic
- real-person or real-incident proof lacks source references
- unsupported claims remain while status is `PASS`
- generic motivation filler is used instead of a story
- reconstructed scene details are presented as verified facts

## Provider Boundary

This contract produces story context only.

```text
n8n_used=false
providers_called=false
media_artifacts_claimed=false
```

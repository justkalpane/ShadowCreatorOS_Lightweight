# Phase 4 Skill Film Mode Proposal

This proposal defines the target skill architecture for a cinema-first Shadow OS skill lane while preserving the existing content and distribution stack.

## 1. Proposed film-mode skill families

Recommended new skill families:

- `skills/film_screenplay/`
- `skills/film_character/`
- `skills/film_scene_dramaturgy/`
- `skills/film_dialogue/`
- `skills/film_visual_language/`
- `skills/film_directorial_style/`
- `skills/film_production/`
- `skills/film_validation/`
- `skills/film_release_adaptation/`

These should sit beside, not inside, the existing content-growth skill families.

## 2. Proposed film-mode skills

Recommended new skill set:

- `F-301-logline-theme-engine.skill.md`
- `F-302-premise-and-genre-engine.skill.md`
- `F-303-save-the-cat-beat-mapper.skill.md`
- `F-304-three-act-eight-sequence-builder.skill.md`
- `F-305-character-want-need-arc-builder.skill.md`
- `F-306-character-web-and-opposing-force-builder.skill.md`
- `F-307-scene-objective-conflict-turn-engine.skill.md`
- `F-308-subtext-dialogue-engine.skill.md`
- `F-309-visual-motif-image-system-designer.skill.md`
- `F-310-mise-en-scene-blocking-composition-engine.skill.md`
- `F-311-director-camera-language-engine.skill.md`
- `F-312-sound-motif-and-silence-engine.skill.md`
- `F-313-performance-direction-engine.skill.md`
- `F-314-screenplay-format-packager.skill.md`
- `F-315-film-continuity-guard.skill.md`
- `F-316-film-validation-scorecard.skill.md`
- `F-317-director-notes-production-notes-packager.skill.md`
- `F-318-release-adaptation-bridge.skill.md`

## 3. Reuse map

| Existing skill/family | Current bias | Film-mode use | Downstream retained? | Recommendation |
|---|---|---|---|---|
| `S-201-hook-optimizer` | Content hook and approval-gate logic | Use only as a content-route helper | Yes | Duplicate a film-mode opening tension skill instead of reusing it directly. |
| `S-202-first-draft-generation` | Content-first drafting | Keep content mode only | Yes | Replace the core draft lane with a film-first writing skill. |
| `S-203-retention-engineer` | Retention cadence | Keep downstream only | Yes | Do not use in film core. |
| `M-039-re-hook-system` | Recurring re-hook cadence | Keep downstream only | Yes | Not suitable for screenplay core. |
| `M-040-story-momentum-engine` | Story energy and beats | Reuse with film mode | Yes | Strong candidate for a film pacing mirror. |
| `M-041-scene-energy-analyzer` | Scene energy | Reuse with film mode | Yes | Refactor toward cinematic tension. |
| `M-046-cinematic-enhancement-engine` | Cinematic uplift | Reuse with film mode | Yes | Good bridge skill. |
| `M-086-cinematic-shot-planner` | Cinematic support | Reuse as-is | Yes | Keep. |
| `M-088-scene-composition-engine` | Cinematic support | Reuse as-is | Yes | Keep. |
| `M-089-motion-director` | Motion and camera support | Reuse with film mode | Yes | Keep but tighten the language. |
| `M-231-voiceover-direction-script` | Narration and performance direction | Duplicate for film mode | Yes | Add a film narration/dialogue direction mirror. |
| `A-403-audio-script-optimizer` | Audio pacing | Move downstream | Yes | Use for trailer and post-production only. |
| `D-501-platform-metadata-generator` | Release metadata | Move downstream | Yes | Not part of film core. |
| `D-502-seo-optimization-specialist` | SEO/discovery | Move downstream | Yes | Release layer only. |
| `D-503-publish-readiness-checker` | Publish gate | Keep downstream | Yes | Useful at release time. |
| `M-001-global-trend-scanner` | Trend and audience scoring | Move to research/adaptation | Yes | Not screenplay core. |
| `M-002-topic-opportunity-miner` | Opportunity mining | Move to research/adaptation | Yes | Not screenplay core. |

## 4. Old-to-new responsibility map

| Existing skill responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| Opening hooks and curiosity gaps | Click/retention | Cinematic opening tension and inciting-image design | Yes | Opening energy should become film-native. |
| Retention cadence and re-hooks | Platform retention | Scene momentum and act-turn pacing | Yes | Film pacing should not inherit content cadence law. |
| Topic opportunity scoring | Platform trend fit | Story premise and theme fit | Yes | Film mode should evaluate dramatic potential, not trend velocity. |
| Audience alignment scoring | Creator fit | Viewer emotional access and genre expectation fit | Yes | Film-mode equivalent should be cinematic, not creator-growth oriented. |
| Channel strategy | Platform growth | Release strategy and distribution planning | Yes | Downstream only. |
| Voiceover scripting | Content narration | Film narration, trailer narration, and performance notes | Yes | Useful in film mode if renamed clearly. |
| Thumbnail and metadata work | Click packaging | Poster, key art, trailer packaging, release metadata | Yes | Distribution only. |
| Editing optimization | Content pacing | Cinematic rhythm and editorial intent | Yes | Needs a film-first mirror. |

## 5. Interface to Phase 5 Subskills

Phase 5 should inspect subskill families that support:

- content angle
- UVP
- hook variation
- open loop
- pacing
- cliffhanger
- retention loop
- story tension
- cinematic scene turns
- character arc
- dialogue subtext
- visual motif
- composition and blocking
- sound motif
- camera language
- screenplay validation

The current skill findings suggest those subskills will need a cinema-first mirror even if some content-route versions remain intact.

## 6. Future patch plan

Phase 5 should inspect whether subskills are:

- content-route only
- reusable as film support
- currently missing
- duplicated into multiple route families
- wrongly steering screenplay generation toward retention and platform logic

The likely outcome is a parallel cinema-subskill family that mirrors the most useful content-subskill behavior without inheriting the platform-first defaults.

## 7. Non-goals

This phase does not create or patch any skills yet.

It does not alter routes, contracts, validators, schemas, or runtime behavior.


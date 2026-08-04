# Phase 4 Skill Route Split Plan

## 1. Objective

Phase 4 audits the skill layer so we can separate cinema-first filmmaking behavior from the existing YouTube/content-engine skill lane without deleting the useful downstream stack.

The goal is to preserve:

- content route skills that remain valid for scripts, hooks, retention, publishing, and platform packaging
- production and media support skills that help with voice, composition, shot planning, color, and editing
- governance and research skills that are reusable across both modes

And to identify where a parallel filmcraft skill family is required for:

- screenplay structure
- character and arc design
- scene dramaturgy
- dialogue subtext
- visual language
- directorial style
- film validation

## 2. Relationship to Phases 1 to 3

- Phase 1 found that the director layer still contains platform/content drift in some route-facing behavior and recommended route separation before broad rewrite.
- Phase 2 found the agent layer still carries content-engine and platform bias, especially where routing, trend logic, and content growth logic are encoded.
- Phase 3 found the subagent layer still carries hook, retention, trend, and distribution bias, but also some reusable film-support primitives.
- Phase 4 now checks the skill layer, which is where most of the actual content logic and production logic is concentrated.

## 3. Skill inventory

This phase inspected the following skill files directly and used repo-wide term scans to widen coverage:

| Skill | File path | Current role | Cinema-core ready? | Platform/content drift? | Recommended mode split | Patch priority | Notes |
|---|---|---|---|---|---|---|---|
| Hook Optimizer | `skills/script_intelligence/S-201-hook-optimizer.skill.md` | Opening-hook and lineage gate skill for script generation | No | Yes | Duplicate film-mode plus keep content-mode | High | Strong route bias toward `script_generation` and approval-gate flow. |
| First Draft Generation | `skills/script_intelligence/S-202-first-draft-generation.skill.md` | First-draft script generator with opening hook, story block, and recurring re-hooks | No | Yes | Replace core writing lane with film-mode equivalent | High | Keeps YouTube/content cadence law in the core draft path. |
| Retention Engineer | `skills/script_intelligence/S-203-retention-engineer.skill.md` | Cadence, retention, and re-hook timing skill | No | Yes | Move content retention to downstream; duplicate a film pace variant | High | Explicit 25-second re-hook law is content-specific. |
| Conflict Intensity Booster | `skills/script_intelligence/S-207-conflict-intensity-booster.skill.md` | Content conflict/energy shaping | Partial | Some | Refactor toward cinematic tension language | Medium | Useful tension control, but currently still a script-engine style support skill. |
| Final Script Packager | `skills/script_intelligence/S-210-final-script-packager.skill.md` | Final script packaging and validation handoff | Partial | Some | Refactor for film packager mirror | Medium | Good packaging support, but core route still content-first. |
| Re-Hook System | `skills/script_intelligence_army/M-039-re-hook-system.py` and `.skill.md` | Re-hook timing, retention resets, and CTA hook logic | No | Yes | Replace in film core; keep in content route | High | One of the clearest content-retention anchors in the repo. |
| Story Momentum Engine | `skills/script_intelligence_army/M-040-story-momentum-engine.skill.md` | Momentum, twist, and lesson bridge support | Partial | Some | Duplicate film-mode version | Medium | More reusable than the hook system, but still script-growth oriented. |
| Scene Energy Analyzer | `skills/script_intelligence_army/M-041-scene-energy-analyzer.skill.md` | Scene-level intensity and energy shaping | Partial | Some | Refactor toward cinematic scene energy | Medium | Good bridge candidate into film mode. |
| Cinematic Enhancement Engine | `skills/script_intelligence_army/M-046-cinematic-enhancement-engine.skill.md` | Cinematic uplift pass for script content | Partial | Some | Refactor into film-style enhancer | Medium | Strong candidate for a film mirror without removing current behavior. |
| Global Trend Scanner | `skills/topic_intelligence/M-001-global-trend-scanner.skill.md` | Trend discovery and audience/platform filtering | No | Yes | Move to topic/research lane only | High | Strong audience/platform bias; not film-core. |
| Topic Opportunity Miner | `skills/topic_intelligence/M-002-topic-opportunity-miner.skill.md` | Opportunity mining from trends and competitor analysis | No | Yes | Move to research/growth lane | High | Clearly built for creator-style platform opportunity selection. |
| Cinematic Shot Planner | `skills/system_intelligence/M-086-cinematic-shot-planner.skill.md` | Shot planning and cinematic framing support | Yes | Low | Keep as reusable film-support | Low | One of the strongest existing film-support assets. |
| Scene Composition Engine | `skills/system_intelligence/M-088-scene-composition-engine.skill.md` | Scene composition and visual arrangement support | Yes | Low | Keep as reusable film-support | Low | Valuable for cinematic scene planning. |
| Motion Director | `skills/system_intelligence/M-089-motion-director.skill.md` | Motion, scene, and camera support | Partial | Low | Keep or refactor into film motion lane | Low | Good film-adjacent support, not a screenplay core skill. |
| Voiceover Direction Script | `skills/media_audio/M-231-voiceover-direction-script.skill.md` | Voiceover direction and performance notes | Partial | Some | Duplicate film-mode voice direction | Medium | Reusable for film narration and trailer work. |
| Audio/Voiceover Script Optimizer | `skills/media_production/A-403-audio-script-optimizer.skill.md` | Audio and pacing optimization | Partial | Some | Refactor into film audio support | Medium | More useful downstream than in screenplay core. |
| Platform Metadata Generator | `skills/publishing/D-501-platform-metadata-generator.skill.md` | Publishing metadata and platform packaging | No | Yes | Move downstream only | High | Should not influence film-core screenplay decisions. |
| SEO Optimization Specialist | `skills/publishing/D-502-seo-optimization-specialist.py` | SEO and discoverability support | No | Yes | Move downstream only | High | Release/distribution support, not screenplay core. |
| Publish Readiness Checker | `skills/publishing/D-503-publish-readiness-checker.skill.md` | Release readiness and publication gates | Partial | Some | Keep downstream only | Medium | Useful, but after the film product is built. |

## 4. Skill family classification

### Script intelligence

- `S-201-hook-optimizer` - content-route only with a film mirror needed
- `S-202-first-draft-generation` - content-route only; core writing lane should become cinema-first
- `S-203-retention-engineer` - downstream content lane only
- `S-207-conflict-intensity-booster` - refactor toward cinematic tension
- `S-210-final-script-packager` - keep packaging behavior, add film packaging mirror

### Script intelligence army

- `M-039-re-hook-system` - content-route only
- `M-040-story-momentum-engine` - reusable, but needs film-mode equivalent
- `M-041-scene-energy-analyzer` - reusable with film-mode wording
- `M-046-cinematic-enhancement-engine` - reusable with a stronger film mirror

### Topic intelligence and growth

- `M-001-global-trend-scanner` - content-route only
- `M-002-topic-opportunity-miner` - content-route only

### System intelligence and cinematic support

- `M-086-cinematic-shot-planner` - core film compatible
- `M-088-scene-composition-engine` - core film compatible
- `M-089-motion-director` - reusable film-support

### Media audio and production

- `M-231-voiceover-direction-script` - reusable, but should gain a film mode
- `A-403-audio-script-optimizer` - downstream production support

### Publishing and release

- `D-501-platform-metadata-generator` - downstream only
- `D-502-seo-optimization-specialist` - downstream only
- `D-503-publish-readiness-checker` - downstream only

## 5. Film-core skill requirements

A cinema-first skill layer needs dedicated skills for:

- logline and theme
- premise and genre
- beat-sheet structure
- three-act and eight-sequence structure
- character want, need, flaw, and arc
- character web and opposing force
- scene objective, conflict, and turn
- subtext dialogue
- visual motif and image system
- mise-en-scene and blocking
- camera and lens language
- sound motif and silence
- performance direction
- screenplay formatting
- continuity control
- film validation
- director notes and production notes

## 6. Non-goals

Phase 4 does not patch skills yet.

It does not:

- delete the existing content engine
- create film routes
- create contracts
- create validators
- change runtime behavior
- claim any PASS state


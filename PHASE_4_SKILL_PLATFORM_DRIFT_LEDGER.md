# Phase 4 Skill Platform Drift Ledger

This ledger focuses on the highest-signal skill files and repository scans that showed content-platform bias, hook/retention bias, or reusable film-support behavior.

Repo-wide scan scope for the skills layer:

- real skill files scanned: 565
- direct line-read evidence files: a focused subset chosen for highest authority and drift

| Skill/File | Line or evidence reference | Term/finding | Current context | Classification | Reason | Proposed film-mode equivalent | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| `skills/script_intelligence_army/M-039-re-hook-system.py` | lines 58-66, 96-97 | 25-second default re-hook interval, CTA hook, fixed retention resets | Content retention and YouTube script cadence law | REPLACE | Hard-coded retention cadence belongs to content route, not cinema core | `film_pacing_engine` or `film_scene_momentum_engine` | Yes, downstream | Film prompts will inherit creator retention logic instead of screenplay structure. |
| `skills/script_intelligence/S-201-hook-optimizer.skill.md` | lines 141-149, 189-194 | `script_generation`, hook variants, recurring re-hooks, immediate attention arrestor | Script generation and content hook lane | REPLACE | Core draft path still encodes content hook law | `screenplay_opening_tension_engine` | Yes, downstream | Film openings may be optimized for clicks instead of cinematic setup. |
| `skills/script_intelligence/S-202-first-draft-generation.skill.md` | lines 191-195 | cinematic story plus recurring re-hooks, CTA hook | First-draft content script path | REPLACE | It mixes film-story language with content cadence law in the same route | `film_first_draft_engine` | Some downstream use only | Screenplays may remain structurally content-first. |
| `skills/script_intelligence/S-203-retention-engineer.skill.md` | lines 120, 193-200 | cadence as retention variable, fixed 25-second interval | Retention-focused content optimization | REPLACE | Strong platform retention bias, not filmcraft | `film_pacing_and_tension_engine` | Yes, downstream | Retention law can contaminate film rhythm decisions. |
| `skills/topic_intelligence/M-001-global-trend-scanner.skill.md` | lines 44-70, 166-206, 302-305 | social feeds, TikTok, Instagram, YouTube, audience alignment, viral potential | Creator trend discovery and platform filtering | REPLACE | Trend discovery is useful, but not film-core writing logic | `film_audience_insight_brief` or `research_intelligence` mirror | Yes, downstream | Trend signals can hijack the core film route. |
| `skills/topic_intelligence/M-002-topic-opportunity-miner.skill.md` | search hits and lines around competitor analysis, winning_format, shorts/reels | competitor coverage, creator fit, winning format | Content opportunity mining | REPLACE | Built to choose platform opportunities, not screenplay ideas | `film_market_opportunity_brief` | Yes, downstream | Story development may be reduced to format competition. |
| `skills/script_intelligence_army/M-049-viral-distribution-planner.skill.md` | repo-wide search hits for viral/distribution | viral distribution and release optimization | Content distribution planning | MOVE | Valuable only after the core film exists | `film_release_adaptation_planner` | Yes, downstream | Distribution concerns will leak into story development. |
| `skills/script_intelligence_army/M-050-platform-algorithm-adapter.py` | repo-wide search hits for platform, hook, voice, visual | platform algorithm adaptation | Creator platform tailoring | MOVE | Downstream platform adaptation, not cinema craft | `platform_release_adapter` | Yes, downstream | Core writing may be forced to satisfy algorithms. |
| `skills/script_intelligence_army/M-060-channel-strategy-director.skill.md` | repo-wide search hits for channel and hook | channel strategy | Channel-growth logic | MOVE | Useful for release/distribution, not screenplay generation | `film_distribution_strategy_director` | Yes, downstream | Channel fit can override narrative integrity. |
| `skills/script_intelligence_army/M-080-shorts-generator.py` | repo-wide search hits for Shorts and retention | Shorts generation | Social short-form creation | MOVE | It belongs in downstream adaptation, not film core | `short_form_cutdown_generator` | Yes, downstream | Short-form logic may dominate long-form cinema planning. |
| `skills/system_intelligence/M-086-cinematic-shot-planner.skill.md` | direct read lines 1-16, 42-57, 142-188 | cinematic shot planning, append-only dossier target | Cinematic support skill | KEEP | Useful as a reusable film-support layer | None required | Yes | Low risk; this is a film-support asset worth preserving. |
| `skills/system_intelligence/M-088-scene-composition-engine.skill.md` | direct read lines 1-16, 42-57, 142-188 | scene composition engine | Cinematic support skill | KEEP | Useful for film composition and blocking support | None required | Yes | Low risk; supports cinema-first output. |
| `skills/system_intelligence/M-089-motion-director.skill.md` | direct read lines 1-16, 42-57, 142-188 | motion director | Motion and camera support | REFACTOR | Useful, but scope should become cinema-first language | `film_motion_direction_engine` | Yes | If left unchanged, its wording remains generic and less film-native. |
| `skills/media_audio/M-231-voiceover-direction-script.skill.md` | direct read lines 1-17, 51-69, 191-237 | voiceover direction, performance direction, media vein | Voice support for narration | DUPLICATE | Keep voiceover mode, add film narration/performance mode | `film_dialogue_and_narration_direction` | Yes | Film narration may remain secondary to content voiceover. |
| `skills/media_production/A-403-audio-script-optimizer.skill.md` | direct read lines 1-17, 142-184 | audio/voiceover script optimizer | Audio/pacing support | REFACTOR | Useful downstream and for trailer work | `film_audio_notes_optimizer` | Yes | Could remain generic if not labeled clearly. |
| `skills/publishing/D-501-platform-metadata-generator.skill.md` | direct read lines 1-17, 138-184 | publishing metadata generator | Release/distribution | MOVE | Strictly downstream release support | `film_release_metadata_generator` | Yes | Must not be read as a screenplay skill. |
| `skills/publishing/D-502-seo-optimization-specialist.py` | repo-wide search hits for SEO/platform/publishing | SEO and discoverability | Release/distribution | MOVE | Important for launch, not for core film writing | `film_release_discovery_optimizer` | Yes | Can distort writing if pulled into core. |
| `skills/publishing/D-503-publish-readiness-checker.skill.md` | repo-wide search hits for publish readiness | publish readiness checker | Release gate | KEEP | Valid downstream quality gate | None required | Yes | Low if kept downstream only. |
| `skills/script_intelligence_army/M-041-scene-energy-analyzer.skill.md` | direct reads and search hits for scene/energy | scene energy analyzer | Film-support adjacent | REFACTOR | Good bridge into cinematic tension and pacing | `film_scene_energy_analyzer` | Yes | Without film wording, it stays generic. |
| `skills/script_intelligence_army/M-046-cinematic-enhancement-engine.skill.md` | repo-wide search hits for cinematic/scene/camera/visual | cinematic enhancement | Film-support adjacent | REFACTOR | Good content-to-film bridge, but needs stronger film semantics | `film_enhancement_pass` | Yes | Otherwise it reads as cosmetic uplift rather than cinema craft. |
| `skills/media_graphics/M-204-layout-composition-strategist.skill.md` | repo-wide search hits for composition/layout | layout composition | Production support | KEEP | Useful for presentation and visual planning | None required | Yes | Keep as downstream production support. |
| `skills/autonomous_loop/M-094-color-grading-engine.skill.md` | repo-wide search hits for color grading | color grading support | Post-production support | KEEP | Valuable downstream production asset | None required | Yes | Low risk when kept in post-production lane. |
| `skills/operations/M-165-dialogue-style-generator.skill.md` | repo-wide search hits for dialogue | dialogue style generation | Style support, but not subtext craft | REPLACE | Too generic for screenplay dialogue craft | `dialogue_subtext_and_distinctness_engine` | Maybe | Dialogue style alone is not enough for cinema writing. |
| `skills/operations/M-164-character-behavior-engine.skill.md` | repo-wide search hits for character | character behavior engine | Character support, but generic | REFACTOR | Needs want/need/flaw/arc language | `character_arc_and_desire_engine` | Maybe | Without film craft language it stays too broad. |

## Classification summary

Counts based on the focused ledger above:

- KEEP: 5
- REFACTOR: 5
- MOVE: 6
- REPLACE: 7
- DUPLICATE: 1
- DELETE: 0
- NEEDS_DESIGN_DECISION: 0
- MISSING_FILMCRAFT_CAPABILITY: 16
- REGISTRY_FILE_MISMATCH: 0
- READ_BLOCKED: 0

## Top 10 highest-risk skill drifts

1. `M-039-re-hook-system` - hard-coded 25-second retention cadence
2. `S-201-hook-optimizer` - opening-hook logic dominates the core route
3. `S-202-first-draft-generation` - content cadence is embedded in the first draft lane
4. `S-203-retention-engineer` - retention language drives pacing decisions
5. `M-001-global-trend-scanner` - audience/platform/viral logic can steer story selection
6. `M-002-topic-opportunity-miner` - opportunity mining can override narrative intent
7. `D-501-platform-metadata-generator` - release packaging can leak into core writing
8. `D-502-seo-optimization-specialist` - discoverability pressure can distort film development
9. `M-060-channel-strategy-director` - channel strategy can wrongly influence screenplay decisions
10. `M-080-shorts-generator` - short-form logic can become the default shape of the work

## Top 10 most reusable cinema-compatible skill capabilities

1. `M-086-cinematic-shot-planner`
2. `M-088-scene-composition-engine`
3. `M-089-motion-director`
4. `M-094-color-grading-engine`
5. `M-231-voiceover-direction-script`
6. `A-403-audio-script-optimizer`
7. `M-041-scene-energy-analyzer`
8. `M-046-cinematic-enhancement-engine`
9. `M-204-layout-composition-strategist`
10. `D-503-publish-readiness-checker` as a downstream gate only

## Missing filmcraft capabilities

The repo does not show dedicated skills for the following filmcraft capabilities:

- Save the Cat
- Blake Snyder beats
- three-act structure
- eight-sequence structure
- Hero's Journey
- Dan Harmon Story Circle
- Robert McKee scene value turns
- Syd Field plot points
- character want vs need
- character flaw and transformation
- character web
- antagonistic force
- scene objective / obstacle / tactic
- scene turn
- dialogue subtext
- dialogue distinctness
- mise-en-scene
- blocking
- lens grammar
- camera movement
- visual motif
- sound motif
- performance direction
- screenplay format
- director's notes
- production notes
- film validation

## Non-goals

Phase 4 does not patch skills yet.

It only documents the current state and the next required filmcraft split.

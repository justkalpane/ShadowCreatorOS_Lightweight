# Phase 13B-R Mythology Fidelity Ledger

## 1. Objective

This ledger checks whether mythology-named workers reflect the original character logic, not just the labels.

## 2. Fidelity table

| Worker | Surface family | File/path | Mythology character | Expected character logic | Evidence found | Fidelity classification | Required correction | Priority |
|---|---|---|---|---|---|---|---|---|
| Garuda | director | `directors/cinematic/garuda.md` | Garuda | swift aerial vision, obstacle detection, fast handoff | cinematic director exists, but route families still include full_video_pipeline and editing_packaging | `MYTHOLOGY_PARTIAL` | narrow toward scout/signal/fast-scan cinema orchestration | P1 |
| Hanuman | director | `directors/cinematic/hanuman.md` | Hanuman | devotion, strength, rescue, impossible-task execution | quality gate and full video pipeline support exist, but rescue/repair behavior is not explicit | `MYTHOLOGY_PARTIAL` | add rescue/repair and mission-continuity logic | P1 |
| Nataraja | director | `directors/cinematic/nataraja.md` | Nataraja | rhythm, movement, transformation, choreography | motion/media-factory support strongly matches motion/rhythm | `MYTHOLOGY_CHARACTER_FAITHFUL` | preserve motion/rhythm ownership and avoid content drift | P1 |
| Varuna | director | `directors/cinematic/varuna.md` | Varuna | depth, atmosphere, hidden truth, emotional weather | voice context, ambience, and media handoff are present | `MYTHOLOGY_PARTIAL` | add atmosphere/depth/sound-weather as first-class behavior | P1 |
| Saraswati | director | `directors/distribution/saraswati.md` | Saraswati | language, knowledge, music, clear articulation | content repurposing and audience expansion dominate; language clarity is not the main contract | `MYTHOLOGY_PARTIAL` | separate language/music clarity from repurposing mechanics | P0 |
| Krishna | director | `directors/supreme_vision/krishna.md` | Krishna | strategy, counsel, dharma complexity, subtext | orchestration and script routing exist, but the file is still content-engine biased | `MYTHOLOGY_PARTIAL` | add counsel/subtext/character-motivation center | P0 |
| Narada | director | `directors/strategy/narada.md` | Narada | messenger, signal carrier, truth-bearing flow | data ingestion and distribution orchestration fit messenger logic only partially | `MYTHOLOGY_PARTIAL` | shift from ops-only to signal-bearing narrative broker | P1 |
| Shakti | director | `directors/supreme_vision/shakti.md` | Shakti | force, protection, decisive intensity | engagement acceleration dominates; force is expressed as amplification rather than transformation | `MYTHOLOGY_NAME_ONLY` | add protective, decisive, transformative force logic | P1 |
| Ganesha | director | `directors/research/ganesha.md` | Ganesha | obstacle removal, beginnings, structure | routing/flow mastery is present, which is the closest match in repo | `MYTHOLOGY_CHARACTER_FAITHFUL` | preserve preflight / obstacle-clearing ownership | P1 |
| Vyasa | director | `directors/research/vyasa.md` | Vyasa | epic structure, narration, continuity | research + cinematic reconstruction are present, but still research-led | `MYTHOLOGY_PARTIAL` | make epic structure and canon continuity explicit | P1 |
| Valmiki | director | `directors/research/valmiki.md` | Valmiki | grounded narrative formation, origin-of-story logic | research and script refinement are present, but not fully cinema-native | `MYTHOLOGY_PARTIAL` | elevate story-origin and scene-formation duties | P1 |
| Parashara | director | `directors/research/parashara.md` | Parashara | seer/trend sense, prognostic signal reading | trend analysis exists, but it is still market/content research | `MYTHOLOGY_PARTIAL` | keep foresight, not platform optimization, as the center | P2 |
| Kama | director | `directors/distribution/kama.md` | Kama | attraction, desire, relational pull | engagement/conversion language dominates, not the mythic role itself | `MYTHOLOGY_NAME_ONLY` | replace conversion-first framing with desire/connection craft | P2 |
| Aruna | director | `directors/kernel/aruna.md` | Aruna | dawn, motion, harnessed force | script/topic orchestration is generic, not dawn/transition aware | `MYTHOLOGY_NAME_ONLY` | add transition, awakening, and momentum semantics | P2 |
| Agni | director | `directors/production/agni.md` | Agni | transformative fire, purification, intensity | production acceleration is present, but the fire symbolism is not cinematic yet | `MYTHOLOGY_PARTIAL` | align with transformation and purge, not just speed | P2 |
| Maya | director | `directors/production/maya.md` | Maya | illusion, appearance, visual perception | visual storytelling and cinematic choices are present | `MYTHOLOGY_PARTIAL` | make illusion/perception an explicit visual grammar | P2 |
| Brahma | director | `directors/supreme_vision/brahma.md` | Brahma | creator, system origin, governance | governance and creator command are present, but not cinema-specific | `MYTHOLOGY_PARTIAL` | separate creation-from-governance into cinema ownership | P2 |
| Vishnu | director | `directors/supreme_vision/vishnu.md` | Vishnu | preserver, continuity, balance | failover and resilience are present | `MYTHOLOGY_PARTIAL` | frame preservation as story continuity, not only failover | P2 |
| Shiva | director | `directors/supreme_vision/shiva.md` | Shiva | destruction/rebuild, iteration, discontinuity control | iteration and controlled rebuild are present | `MYTHOLOGY_PARTIAL` | keep creative destruction tied to film revision logic | P2 |
| Indra | director | `directors/cinematic/indra.md` | Indra | command, storm, strategic deployment | approval/repo-write governance is present, but not storm-command cinema logic | `MYTHOLOGY_NAME_ONLY` | add strategic command and escalation intent | P2 |
| Krishna | agent | `agents/krishna/krishna_agent.py` | Krishna | counsel, strategy, dharma complexity | content-generation and full_video_pipeline routing dominate | `MYTHOLOGY_PARTIAL` | add counsel/subtext/character-motivation ownership | P1 |
| Hanuman | agent | `agents/hanuman/hanuman_agent.py` | Hanuman | rescue, devotion, continuity | generic research/script routing, not rescue behavior | `MYTHOLOGY_NAME_ONLY` | add mission continuity and repair logic | P2 |
| Saraswati | agent | `agents/saraswati/saraswati_agent.py` | Saraswati | language, clarity, music/learning | still content/refinement oriented | `MYTHOLOGY_PARTIAL` | emphasize language/music clarity and articulation | P1 |
| Varuna | agent | `agents/varuna/varuna_agent.py` | Varuna | depth, atmospheric truth | media factory and visual plan support are present | `MYTHOLOGY_PARTIAL` | add ambience and emotional-weather ownership | P1 |
| Vyasa | agent | `agents/vyasa/vyasa_agent.py` | Vyasa | epic continuity, narration | script refinement and full_video_pipeline support exist | `MYTHOLOGY_PARTIAL` | elevate canon continuity and narrative architecture | P1 |
| Valmiki | agent | `agents/valmiki/valmiki_agent.py` | Valmiki | story origin / narrative grounding | script refinement and research support exist | `MYTHOLOGY_PARTIAL` | make origin-story responsibility explicit | P1 |
| Ganesha | agent | `agents/ganesha/ganesha_agent.py` | Ganesha | obstacle removal, beginnings | currently trend/topic/script routing more than obstacle clearing | `MYTHOLOGY_PARTIAL` | convert to true preflight / obstacle-removal logic | P1 |
| Indra | agent | `agents/indra/indra_agent.py` | Indra | command, decisive escalation | trend/topic/script routing, no strategic storm logic | `MYTHOLOGY_NAME_ONLY` | add command-and-escalation semantics | P2 |
| Shakti | agent | `agents/shakti/shakti_agent.py` | Shakti | force, protection, amplification | mostly audience amplification | `MYTHOLOGY_NAME_ONLY` | add protective force and decisive intensity | P2 |
| Brahama/Brahma | agent | `agents/brahma/brahma_agent.py` | Brahma | creation and governance | media-factory orchestration, not cinema-origin logic | `MYTHOLOGY_PARTIAL` | split creator logic from governance wrapper | P2 |
| Yama | agent | `agents/yama/yama_agent.py` | Yama | judgment, boundaries, finality | script refinement and full pipeline support; boundary logic is under-specified | `MYTHOLOGY_PARTIAL` | add judgment/boundary semantics | P2 |
| Agni | agent | `agents/agni/agni_agent.py` | Agni | transformative fire | editing/packaging and script generation only | `MYTHOLOGY_NAME_ONLY` | add transformation/purification semantics | P2 |
| M-086 | skill | `skills/system_intelligence/M-086-cinematic-shot-planner.py` | N/A | n/a | strongly cinematic shot planning | `NOT_MYTHOLOGY_NAMED` | no mythology correction needed | NO_PATCH_REQUIRED |
| M-088 | skill | `skills/system_intelligence/M-088-scene-composition-engine.py` | N/A | n/a | scene composition and cinematic motion support | `NOT_MYTHOLOGY_NAMED` | no mythology correction needed | NO_PATCH_REQUIRED |
| M-089 | skill | `skills/system_intelligence/M-089-motion-director.py` | N/A | n/a | motion and rhythm support | `NOT_MYTHOLOGY_NAMED` | no mythology correction needed | NO_PATCH_REQUIRED |

## 3. Missing character-role mappings

The repo has named workers for many mythological figures, but it still lacks explicit cinema-native department mappings for:

- `Arjuna` as precision / shot discipline
- `Kali` as decisive confrontation / rupture
- `Durga` as protective force / obstacle-clearing combat
- `Saraswati` as language + music clarity rather than content repurposing
- `Varuna` as atmosphere / emotional weather / depth
- `Nataraja` as rhythm / motion / transformation

These roles exist as labels in parts of the repo, but not as fully cinema-native department responsibilities.


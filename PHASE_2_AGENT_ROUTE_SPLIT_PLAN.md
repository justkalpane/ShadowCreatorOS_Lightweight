# Phase 2 Agent Route Split Plan

## Objective

Phase 2 audits the agent layer so the repo can evolve toward cinema-first route separation without breaking the existing script/content stack.

This phase does **not** patch agents yet. It only determines which agents can support future film routes and which ones still embody content-engine behavior that should stay downstream or be split later.

## Relationship to Phase 1

Phase 1 found that the director layer still anchors the top route in `SCRIPT_GENERATION` and creator/content terms. Phase 2 checks whether the agent layer can support the next cinema-first route family:

- `FILM_SCREENPLAY_GENERATION`
- `FILM_STORY_DEVELOPMENT`
- `CINEMATIC_DIRECTOR_PLAN`
- `FEATURE_FILM_PRODUCTION_PIPELINE`
- `FILM_RELEASE_DISTRIBUTION`

The question here is not whether agents are useful. They are.
The question is whether the current agent bindings still point too hard at script-generation, trend, retention, platform, and distribution language for the core film layer.

## Agent Inventory

### Agent files inspected in this phase

| File path | Short role |
|---|---|
| `agents/krishna/krishna_agent.py` | top-level script/arbitration agent |
| `agents/narada/narada_agent.py` | trend and distribution optimizer |
| `agents/saraswati/saraswati_agent.py` | refinement / multiplication / distribution agent |
| `agents/garuda/garuda_agent.py` | release and packaging dispatcher |
| `agents/chanakya/chanakya_agent.py` | strategic filtering / opportunity selection |
| `agents/shakti/shakti_agent.py` | force amplification / engagement acceleration |
| `agents/kama/kama_agent.py` | hook density / retention gate |
| `agents/durga/durga_agent.py` | safety / veto / boundary enforcement |
| `agents/ganesha/ganesha_agent.py` | routing intelligence / index router |
| `agents/yama/yama_agent.py` | policy and boundary gate |
| `agents/arjuna/arjuna_agent.py` | production execution / scoring |
| `agents/maya/maya_agent.py` | visual production / storyboard support |
| `agents/nataraja/nataraja_agent.py` | pacing / editing / flow control |
| `agents/tumburu/tumburu_agent.py` | voice and audio direction |
| `agents/vishwakarma/vishwakarma_agent.py` | technical production / build support |
| `agents/vishnu/vishnu_agent.py` | cross-route synchronization / resilience |
| `agents/indra/indra_agent.py` | premium production / high-value release support |
| `agents/hanuman/hanuman_agent.py` | approval and source-breadth support |
| `agents/agastya/agastya_agent.py` | source-safe research brief agent |
| `agents/chandra/chandra_agent.py` | audience intelligence / analytics agent |
| `agents/brahma/brahma_agent.py` | governance / council coordination agent |
| `agents/kubera/kubera_agent.py` | budget / cost gate agent |
| `agents/chitragupta/chitragupta_agent.py` | audit trail / lineage tracking agent |
| `agents/parashara/parashara_agent.py` | trend analysis / pattern discovery agent |

### Shared agent infrastructure inspected

- `agents/AGENT_RUNTIME_REGISTRY.yaml`
- `registries/agent_runtime_selection_index.yaml`
- `registries/agent_class_matrix.json`
- `agents/common/director_authority_profiles.py`
- `agents/common/production_agent_base.py`
- `agents/common/sub_agent_matrix.py`
- `agents/common/workflow_binding_contracts.py`
- `runtime_contracts/ROUTE_STATE_PERSISTENCE_CONTRACT.md`

## Agent Classification Table

| Agent | File path | Current role | Cinema-core ready? | Platform/content drift? | Recommended mode split | Patch priority | Notes |
|---|---|---|---|---|---|---|---|
| Krishna | `agents/krishna/krishna_agent.py` | top-level orchestrator and final script arbiter | No | High | Replace top-level film-core use with a cinema-first route arbiter, keep content route support downstream | High | Still resolves to `full_video_pipeline`, `trend_research`, `topic_discovery`, and `script_generation`; it also consumes `RECURRING_HOOK_DENSITY_LAW` and blocks on missing recurring-hook proof. |
| Narada | `agents/narada/narada_agent.py` | trend and distribution optimizer | No | High | Move trend/distribution logic downstream; add a film-research sibling later if needed | High | Directly tied to Google Trends, `distribution`, `platform_score`, and `script_generation` routing. |
| Saraswati | `agents/saraswati/saraswati_agent.py` | script refinement and distribution multiplication | Partial | Medium | Keep downstream; later add film refinement sibling if film mode needs it | Medium | Strong for packaging, channel adaptation, and recurring-hook alignment, but it still speaks in platform packaging terms. |
| Garuda | `agents/garuda/garuda_agent.py` | release and packaging dispatcher | Yes, downstream only | Low | Keep as downstream release layer | Low | Good fit for film release/distribution, not for screenplay core. |
| Chanakya | `agents/chanakya/chanakya_agent.py` | strategic filtering / opportunity selection | Partial | High | Refactor into film opportunity fit / story-market fit | High | Current scoring language is creator/platform-oriented. |
| Shakti | `agents/shakti/shakti_agent.py` | force amplification / engagement acceleration | Partial | High | Refactor into dramatic force / emotional pressure support | High | Valuable in cinema, but its present language is engagement and viral velocity heavy. |
| Kama | `agents/kama/kama_agent.py` | hook density / retention gate | No for film core | High | Move downstream into content/marketing lane; later duplicate if film tension support is needed | High | This is useful for platform hooks, but not a screenplay-core authority. |
| Durga | `agents/durga/durga_agent.py` | safety / veto / boundary enforcement | Yes | Low | Keep as governance and safety gate | Low | Strong reusable control-plane agent. |
| Ganesha | `agents/ganesha/ganesha_agent.py` | routing intelligence / index router | Partial | Medium | Needs design decision before any film-core reuse | Medium | It is a router, but the film-mode boundary is not yet clearly separated. |
| Yama | `agents/yama/yama_agent.py` | policy and boundary gate | Yes | Low | Keep as governance downstream and release gate | Low | Good for legality/policy protection. |
| Arjuna | `agents/arjuna/arjuna_agent.py` | production execution / scoring | Partial | Medium | Refactor into film production feasibility / scene-readiness scoring | Medium | Current production score fields still include hook/retention/platform language. |
| Maya | `agents/maya/maya_agent.py` | visual production / storyboard support | Yes | Low | Keep and later extend for film visual language | Low | Strong cinema-compatible support already visible in the file. |
| Nataraja | `agents/nataraja/nataraja_agent.py` | pacing / editing / flow control | Partial | Medium | Refactor into film rhythm / scene cadence / cut rhythm | Medium | Good candidate for film-mode reuse with a wording and scope retarget. |
| Tumburu | `agents/tumburu/tumburu_agent.py` | voice and audio direction | Yes | Low | Keep and later extend to cinematic sound motif direction | Low | Reusable in both content and film lanes. |
| Vishwakarma | `agents/vishwakarma/vishwakarma_agent.py` | technical production / build support | Yes | Low | Keep as production backbone | Low | Mostly technical support with minimal platform drift evidence. |
| Vishnu | `agents/vishnu/vishnu_agent.py` | cross-route synchronization / resilience | Partial | Medium | Duplicate for film continuity sync while preserving current cross-route sync | Medium | Useful enough to keep, but it needs a film-mode sibling. |
| Indra | `agents/indra/indra_agent.py` | premium production / high-value release support | Yes | Low | Keep as premium finish / release readiness support | Low | Strong downstream production support. |
| Hanuman | `agents/hanuman/hanuman_agent.py` | approval and source-breadth support | Partial | Low | Keep as gated support, not film-core authority | Medium | Useful for approval-gated motion, but not a screenplay engine. |
| Agastya | `agents/agastya/agastya_agent.py` | source-safe research brief agent | Yes | Low | Keep as research support | Low | Useful for honest research and fact-lineage handling. |
| Chandra | `agents/chandra/chandra_agent.py` | audience intelligence / analytics agent | Partial | Medium | Move toward downstream audience intelligence; do not let it steer screenplay core | Medium | Useful, but its current purpose is still audience/analytics-oriented. |
| Brahma | `agents/brahma/brahma_agent.py` | governance / council coordination agent | Yes | Low | Keep as orchestration/governance support | Low | Good structural backbone. |
| Kubera | `agents/kubera/kubera_agent.py` | budget / cost gate agent | Yes | Low | Keep as finance/cost gate support | Low | No film drift issue; still needed. |
| Chitragupta | `agents/chitragupta/chitragupta_agent.py` | audit trail / lineage tracking agent | Yes | Low | Keep as lineage/audit support | Low | Highly reusable for film provenance and traceability. |
| Parashara | `agents/parashara/parashara_agent.py` | trend analysis / pattern discovery agent | Partial | Medium | Refactor into film research signal and thematic pattern analysis | Medium | Useful, but not the screenplay core. |

## Film-Core Agent Requirements

A cinema-first agent layer needs dedicated support for:

- screenplay structure
- character design
- scene dramaturgy
- dialogue and subtext
- visual motif design
- composition and blocking
- director style
- production feasibility
- continuity control
- performance direction
- film validation

The current agent layer does support pieces of this, but not as a clean film-mode stack yet.

## Non-goals

Phase 2 does **not**:

- patch agent files
- patch subagents
- patch skills
- patch contracts
- patch route manifests
- add `FILM_SCREENPLAY_GENERATION`
- claim runtime proof
- claim PASS states
- remove the existing YouTube/content behavior

## Phase 2 Outcome

The agent estate is usable, but it is still shaped around script-generation, trend analysis, distribution, retention, and platform logic at the highest layers. That means the film conversion must be designed, not assumed.


# Phase 2 Agent Platform Drift Ledger

## Scope

This ledger records the most meaningful agent-level drift found in the inspected agent files and registries.

### Files and registries examined

- `agents/AGENT_RUNTIME_REGISTRY.yaml`
- `registries/agent_runtime_selection_index.yaml`
- `registries/agent_class_matrix.json`
- `agents/common/director_authority_profiles.py`
- `agents/common/production_agent_base.py`
- `agents/common/sub_agent_matrix.py`
- `agents/common/workflow_binding_contracts.py`
- `runtime_contracts/ROUTE_STATE_PERSISTENCE_CONTRACT.md`
- `agents/krishna/krishna_agent.py`
- `agents/narada/narada_agent.py`
- `agents/saraswati/saraswati_agent.py`
- `agents/garuda/garuda_agent.py`
- `agents/chanakya/chanakya_agent.py`
- `agents/shakti/shakti_agent.py`
- `agents/kama/kama_agent.py`
- `agents/durga/durga_agent.py`
- `agents/ganesha/ganesha_agent.py`
- `agents/yama/yama_agent.py`
- `agents/arjuna/arjuna_agent.py`
- `agents/maya/maya_agent.py`
- `agents/nataraja/nataraja_agent.py`
- `agents/tumburu/tumburu_agent.py`
- `agents/vishwakarma/vishwakarma_agent.py`
- `agents/vishnu/vishnu_agent.py`
- `agents/indra/indra_agent.py`
- `agents/hanuman/hanuman_agent.py`
- `agents/agastya/agastya_agent.py`
- `agents/chandra/chandra_agent.py`
- `agents/brahma/brahma_agent.py`
- `agents/kubera/kubera_agent.py`
- `agents/chitragupta/chitragupta_agent.py`
- `agents/parashara/parashara_agent.py`

## Classification Legend

- `KEEP` = valid where it is, usually downstream distribution, analytics, release, or platform adaptation
- `REFACTOR` = good capability, wrong wording or wrong scope
- `MOVE` = useful logic, but belongs downstream, not inside core film screenplay generation
- `REPLACE` = platform/content logic is unsafe inside film-core agent behavior
- `DUPLICATE` = keep existing behavior and add a film-mode equivalent
- `DELETE` = obsolete or harmful; used rarely
- `NEEDS_DESIGN_DECISION` = not enough certainty yet

## Ledger

| Agent/File | Line or evidence reference | Term/finding | Current context | Classification | Reason | Proposed film-mode equivalent | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| Krishna / `agents/krishna/krishna_agent.py` | `route_families` and `behavior_laws_consumed` lines 38, 81-83 | `full_video_pipeline`, `trend_research`, `topic_discovery`, `script_generation`, recurring-hook law, final script arbitration | Top-level agent still binds film requests to creator/video logic and to recurring-hook proof | `REPLACE` | This is the highest-authority script arbiter, so the core route must be retargeted first | `film_screenplay_arbiter_agent` | Yes, for downstream content routes | Very high |
| Narada / `agents/narada/narada_agent.py` | lines 33-38, 199-243 | Google Trends, distribution, platform_score, script_generation | Trend/distribution intelligence is central to this agent | `MOVE` | Great downstream intelligence, but not a film-core authority | `film_research_signal_agent` | Yes | High |
| Saraswati / `agents/saraswati/saraswati_agent.py` | lines 38-83 | `script_refinement`, `editing_packaging`, `full_video_pipeline`, platform packaging | Strong refinement and multiplication agent, but still content/distribution shaped | `KEEP` | This is useful downstream behavior and should stay intact | `film_release_adaptation_agent` later if needed | Yes | Medium |
| Garuda / `agents/garuda/garuda_agent.py` | lines 38-74 | `full_video_pipeline`, `editing_packaging`, release/dispatch logic | Release dispatcher for packaging and distribution | `KEEP` | Correct downstream function | `film_release_dispatch_agent` | Yes | Low |
| Chanakya / `agents/chanakya/chanakya_agent.py` | lines 38-74 | `trend_research`, `topic_discovery`, `script_generation` | Strategic filtering still frames opportunities through creator/content success | `REFACTOR` | Needs film-market / story-market fit wording | `film_opportunity_fit_agent` | Yes, as support | High |
| Shakti / `agents/shakti/shakti_agent.py` | lines 38-74 and authority profile lines 248-257 | `distribution`, `engagement`, `viral`, audience force, distribution velocity | Strong amplifier, but the current frame is still growth/engagement-heavy | `REFACTOR` | Cinema can use force, but not a growth-first vocabulary | `dramatic_force_amplifier_agent` | Yes, for downstream tension support | High |
| Kama / `agents/kama/kama_agent.py` | lines 38-83 | recurring re-hook density, topic relevance, CTA hook, max retention gap | This is a content-retention gate, not a film-core craft layer | `MOVE` | Valuable for platform packaging and trailers, not screenplay core | `attention_and_retention_agent` downstream | Yes | High |
| Durga / `agents/durga/durga_agent.py` | lines 38-74 | safety, veto, creator safety, content safety | Governance and boundary protection | `KEEP` | This is a valid control layer regardless of route family | `film_safety_gate_agent` | Yes | Low |
| Ganesha / `agents/ganesha/ganesha_agent.py` | lines 38-83 | route intelligence, hook subskills, recurring-hook routing | Routing intelligence is useful, but the film-mode boundary is not yet explicit | `NEEDS_DESIGN_DECISION` | Decide whether this becomes a pure router, film router, or stays shared | `film_route_router_agent` or shared router | Yes, if clarified | Medium |
| Yama / `agents/yama/yama_agent.py` | lines 38-83 | policy, boundary, unsupported proof, disconnected Media Factory context | Strong governance gate | `KEEP` | Good release/policy control, not a creative route owner | `film_policy_gate_agent` | Yes | Low |
| Arjuna / `agents/arjuna/arjuna_agent.py` | lines 38-74 and production fields 505-528 | `hook_score`, `retention_score`, `platform_score`, production scoring | Production scoring is useful, but still content-platform flavored | `REFACTOR` | Should become shoot-readiness / scene-readiness scoring | `film_production_feasibility_agent` | Yes | Medium |
| Maya / `agents/maya/maya_agent.py` | lines 81-123 | scene prompts, storyboard export, visual DNA, cinematic/storyboard support | Already strongly compatible with film visual planning | `KEEP` | Reusable as a core film visual support agent | `film_visual_language_agent` | Yes | Low |
| Nataraja / `agents/nataraja/nataraja_agent.py` | route/production references around lines 60-74 | pacing, editing, flow control, ready for distribution | Rhythm engine is useful but still oriented to release readiness | `REFACTOR` | Film needs scene rhythm and cut rhythm language | `cinematic_rhythm_agent` | Yes | Medium |
| Tumburu / `agents/tumburu/tumburu_agent.py` | lines 38-74 | voice, audio direction, sonic branding, voiceover support | Audio and voice support are reusable | `KEEP` | This supports both content and cinema when retargeted later | `cinematic_sound_motif_agent` | Yes | Low |
| Vishwakarma / `agents/vishwakarma/vishwakarma_agent.py` | lines 329 and 399 | creator dashboard / metadata / production support | Mostly technical production scaffolding | `KEEP` | Good production backbone | `film_production_build_agent` | Yes | Low |
| Vishnu / `agents/vishnu/vishnu_agent.py` | lines 38-74 and 112-113 | `cross_platform_sync`, multi-creator orchestration, platform resilience | Useful orchestration layer, but not yet film-specific | `DUPLICATE` | Keep current sync behavior and add a film continuity sibling | `film_continuity_sync_agent` | Yes | Medium |
| Indra / `agents/indra/indra_agent.py` | lines 38-74 | premium distribution, high-value production | Good premium finish / release support | `KEEP` | Useful as downstream polish and release-readiness support | `film_premium_finish_agent` | Yes | Low |
| Hanuman / `agents/hanuman/hanuman_agent.py` | lines 38-78 | approval_gate/repo_write_mode, source breadth, research safety | Approval and source-breadth support, not a creative core | `KEEP` | It is a safe support layer and can remain outside the film core | `approval_and_source_gate_agent` | Yes | Low |
| Agastya / `agents/agastya/agastya_agent.py` | lines 38-83 | research brief, factual re-hook claims, source safety | Strong source-honesty support | `KEEP` | Good reusable research support | `film_research_brief_agent` | Yes | Low |
| Chandra / `agents/chandra/chandra_agent.py` | lines 38-74 | audience intelligence, analytics, trend signals | Audience analytics is valuable but not screenplay authority | `MOVE` | Keep as downstream market/audience intelligence | `film_audience_signal_agent` downstream | Yes | Medium |
| Brahma / `agents/brahma/brahma_agent.py` | lines 40-74 | governance / council coordination | High-level coordination and governance | `KEEP` | Useful backbone with no clear platform drift | `film_governance_coordinator_agent` | Yes | Low |
| Kubera / `agents/kubera/kubera_agent.py` | lines 38-74 | cost, budget, financial gating | Budget gate is production-support logic | `KEEP` | Should stay as a support gate | `film_budget_gate_agent` | Yes | Low |
| Chitragupta / `agents/chitragupta/chitragupta_agent.py` | lines 38-74 | audit trail, lineage tracking, source evidence | Audit/lineage control is reusable and valuable | `KEEP` | Strong provenance support for film development | `film_lineage_audit_agent` | Yes | Low |
| Parashara / `agents/parashara/parashara_agent.py` | lines 38-74 | trend analysis, pattern discovery | Research-oriented, but still trend-led | `REFACTOR` | Film mode should use thematic and market pattern language | `film_pattern_analysis_agent` | Yes, as support | Medium |

## Classification Counts

- `KEEP`: 12
- `REFACTOR`: 6
- `MOVE`: 3
- `REPLACE`: 1
- `DUPLICATE`: 1
- `DELETE`: 0
- `NEEDS_DESIGN_DECISION`: 1

## Top 10 Highest-Risk Agent Drifts

1. `Krishna` still acts as the top arbiter for `script_generation` and recurring-hook enforcement.
2. `Narada` still centralizes trend/distribution logic and platform scoring.
3. `Kama` still turns hook density and retention into a central gate.
4. `Chanakya` still filters through creator and platform-fit language.
5. `Shakti` still frames amplification as engagement and viral velocity.
6. `Arjuna` still exposes `platform_score` in production scoring.
7. `Chandra` still treats audience analytics as a route-level signal, not just downstream intelligence.
8. `Nataraja` still phrases pacing in creator/distribution language.
9. `Vishnu` still centers cross-platform sync, which is useful but not film-core specific.
10. `Ganesha` is still route/router-centric without a film-mode designation decision.

## Reusable Cinema-Compatible Capabilities

1. `Maya` storyboard / visual DNA support.
2. `Tumburu` audio / voice direction.
3. `Vishwakarma` production build support.
4. `Indra` premium finish and release readiness.
5. `Brahma` governance coordination.
6. `Durga` safety and veto control.
7. `Yama` policy and boundary enforcement.
8. `Chitragupta` lineage and audit tracking.
9. `Agastya` source-honest research briefs.
10. `Garuda` downstream distribution and release dispatch.

## Phase 2 Decision

The agent layer is structurally reusable, but it is still tuned toward script generation, trend/research intake, retention, platform analytics, and distribution. The film conversion should therefore introduce film-mode sibling agents or route splits before any broad rewrite.


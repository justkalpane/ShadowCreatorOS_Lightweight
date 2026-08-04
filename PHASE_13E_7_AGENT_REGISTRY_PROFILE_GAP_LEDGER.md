# Phase 13E_7 Agent Registry/Profile Gap Ledger

## 1. Objective

Map the coherence gap between Phase 13E_6 named mythology agent file surfaces and the active agent registry/profile truth surfaces.

## 2. Named Agent Coherence Table

| Worker | File exists | Phase 13E_6 marker | Runtime registry listed | Agent matrix exact entries | Agent matrix director-bound entries | Authority profile present | Current profile role | Gap | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Agni | yes | yes | yes | 1 | 1 | yes | Energy/Momentum / Urgency Injection | Profile role needs cinema-craft overlay for lighting, atmosphere, and finishing. | P1_REQUIRED |
| Arjuna | yes | yes | yes | 1 | 1 | yes | Script Execution / Narrative Warfare | Profile role needs cinema-craft overlay for precision, blocking, staging, and shot discipline. | P1_REQUIRED |
| Aruna | yes | yes | yes | 1 | 5 | yes | Flow Building / Resource Gating / Neural Routing | Profile role needs cinema transition/edit-momentum overlay; duplicate director-bound entries need preservation. | P1_REQUIRED |
| Brahma | yes | yes | yes | 1 | 1 | yes | Governance Keeper / Councils Coordinator | Profile role needs world-building and production-design cinema overlay. | P1_REQUIRED |
| Durga | yes | yes | yes | 1 | 1 | yes | Protection / Veto Logic / Safety Enforcement | Profile role needs protective conflict and ethical-stakes cinema overlay. | P1_REQUIRED |
| Ganesha | yes | yes | yes | 1 | 6 | yes | Neural Index Router / Routing Intelligence | Profile role needs preflight, source separation, and no-fake-PASS cinema gate overlay; duplicate bindings need preservation. | P1_REQUIRED |
| Garuda | yes | yes | yes | 1 | 1 | yes | Distribution Velocity / Rapid Publishing | Content/distribution drift in role; needs aerial vision, scout intelligence, storyboard/shotlist overlay. | P1_REQUIRED |
| Hanuman | yes | yes | yes | 1 | 1 | yes | Speed / Fast-Track Execution | Speed framing is content/runtime biased; needs continuity rescue and impossible-task film repair overlay. | P1_REQUIRED |
| Indra | yes | yes | yes | 1 | 1 | yes | Premium Tier / High-Value Production | Needs production-command, escalation, and stakes deployment cinema overlay. | P1_REQUIRED |
| Kali | yes | yes | no | 0 | 0 | no | MISSING | File-only surface; missing runtime registry listing, class matrix entry, and authority profile. | P0_BLOCKER |
| Kama | yes | yes | yes | 1 | 1 | yes | Engagement / Conversion / Audience Attraction | Content conversion drift in role; needs desire line, relational pull, and packaging-boundary cinema overlay. | P1_REQUIRED |
| Krishna | yes | yes | yes | 1 | 13 | yes | Orchestrator / Decision Arbiter / Multi-Domain Controller | Needs character motivation, dharma complexity, directorial counsel, and subtext overlay; duplicate bindings need preservation. | P1_REQUIRED |
| Maya | yes | yes | yes | 1 | 21 | yes | Visual Production / Creative Visualization | Needs production-design, perception, world texture, animation style overlay; many media bindings must remain downstream. | P1_REQUIRED |
| Narada | yes | yes | yes | 1 | 7 | yes | Operations / Distribution / Optimization | Distribution drift in role; needs truth signal and message-flow overlay with downstream separation. | P1_REQUIRED |
| Nataraja | yes | yes | yes | 1 | 1 | yes | Pacing / Editing / Flow Control | Partially aligned; needs rhythm, movement, choreography, blocking, and edit-cadence overlay. | P2_RECOMMENDED |
| Parashara | yes | yes | yes | 1 | 1 | yes | Trend Analysis / Pattern Discovery | Trend drift in role; needs world-truth research and foresight overlay for film source logic. | P1_REQUIRED |
| Saraswati | yes | yes | yes | 1 | 1 | yes | Knowledge Dissemination / Content Multiplication | Content multiplication drift; needs dialogue, music motif, voice, language, and prosody overlay. | P1_REQUIRED |
| Shakti | yes | yes | yes | 1 | 1 | yes | Creative Force Amplifier / Distribution Velocity | Distribution drift in role; needs creative force, protective intensity, and finishing activation overlay. | P1_REQUIRED |
| Shiva | yes | yes | yes | 1 | 1 | yes | Autonomous Intelligence Loop / Creative Destruction | Needs revision, destructive reset, edit rhythm, and transformation overlay. | P1_REQUIRED |
| Valmiki | yes | yes | yes | 1 | 19 | yes | Research Synthesis / Knowledge Structuring | Needs story origin, poetic foundation, and scene genesis overlay; duplicate bindings need preservation. | P1_REQUIRED |
| Varuna | yes | yes | yes | 1 | 1 | yes | Flow / Liquid Narrative / Adaptability | Partially aligned; needs atmosphere, hidden truth, lighting mood, sound, and emotional weather overlay. | P2_RECOMMENDED |
| Vishnu | yes | yes | yes | 1 | 9 | yes | HA Coordinator / Failover Master | Runtime/failover drift in role; needs continuity preservation and script-supervision overlay. | P1_REQUIRED |
| Vyasa | yes | yes | yes | 1 | 1 | yes | Content Creation / Knowledge Graph Management | Content-engine drift; needs story canon, screenplay structure, and sequence architecture overlay. | P1_REQUIRED |
| Yama | yes | yes | yes | 1 | 11 | yes | Policy/Legality Gate / Governance Enforcement | Needs ethics, source-vs-render, and no-fake-PASS film governance overlay; duplicate bindings need preservation. | P1_REQUIRED |

## 3. Registry/Profile Gap Summary

```text
named_agent_files_present=24
runtime_registry_listed=23
agent_class_matrix_exact_entries=23
authority_profiles_present=23
kali_missing_from_runtime_registry=true
kali_missing_from_agent_class_matrix=true
kali_missing_from_director_authority_profiles=true
legacy_profile_roles_requiring_cinema_overlay=23
duplicate_director_bound_entries_require_preservation=true
```

## 4. P0 Gap

| Gap ID | Surface | Evidence | Required correction | Priority |
| --- | --- | --- | --- | --- |
| E7-P0-001 | Kali registry/profile coherence | `agents/kali/kali_agent.py` exists, but Kali is absent from `agents/AGENT_RUNTIME_REGISTRY.yaml`, `registries/agent_class_matrix.json`, and `agents/common/director_authority_profiles.py`. | Add Kali as an additive named mythology agent registry/profile entry. | P0_BLOCKER |

## 5. P1 Gaps

| Gap ID | Surface | Evidence | Required correction | Priority |
| --- | --- | --- | --- | --- |
| E7-P1-001 | Authority profile roles | Several roles remain content, distribution, routing, runtime, or generic production coded. | Add cinema-specific overlay fields while preserving legacy role strings where compatibility needs them. | P1_REQUIRED |
| E7-P1-002 | Runtime registry | Registry uses `model: flat_narada_pattern` and lacks a 24-craft named-agent cinema overlay. | Add a bounded cinema overlay or marker section for the named mythology agents. | P1_REQUIRED |
| E7-P1-003 | Class matrix | Matrix has `total_agents=114`, `named_director=32`, and no Kali entry. | Add Kali and/or additive cinema metadata consistently without deleting existing entries. | P1_REQUIRED |
| E7-P1-004 | Duplicate director-bound responsibilities | Krishna, Maya, Valmiki, Yama, Vishnu, Narada, Ganesha, and Aruna have multiple director-bound entries. | Preserve duplicate legacy worker entries and avoid broad reassignment in the next patch. | P1_REQUIRED |
| E7-P1-005 | Full Cinema Engine claim boundary | Subagent, skill, subskill, and dirty index alignment remain incomplete. | Keep next patch scoped to registry/profile coherence only. | P1_REQUIRED |

## 6. Non-Implementation Boundary

```text
phase_13e_7_created_docs_only=true
agent_registry_modified=false
agent_class_matrix_modified=false
director_authority_profiles_modified=false
agents_modified=false
runtime_behavior_changed=false
selector_modified=false
active_route_registry_modified=false
pass_claimed=false
runtime_proof_claimed=false
```

# Codex Skills Content Proof

audit_date=2026-05-22
operator_mode=OLD_LOCAL_MAC_CODEX_CHAT

## Summary

codex_skill_count=3
all_skills_exist=true
all_skills_have_yaml_frontmatter=true
all_skills_have_name_description=true

## shadow-content-orchestration

file=.agents/skills/shadow-content-orchestration/SKILL.md
file_exists=true
line_count=64
has_yaml_frontmatter=true
name=shadow-content-orchestration
description=Activates for script, YouTube, Shorts, video, reel, content, topic, storytelling, debate, critique, and context engineering requests; requires repo-first Shadow orchestration and full content engineering output.
activation_triggers_present=true
forbidden_behavior_present=true
required_output_blocks_present=true

```text
---
name: shadow-content-orchestration
description: Activates for script, YouTube, Shorts, video, reel, content, topic, storytelling, debate, critique, and context engineering requests; requires repo-first Shadow orchestration and full content engineering output.
---

# Shadow Content Orchestration

Use this skill for any request involving:

- script
- YouTube
- Shorts
- video
- content
- reel
- voiceover
- context engineering
- topic
- storytelling
- debate
- critique

## Required Behavior

Before answering, run repo-first Shadow orchestration:

1. Read `AGENTS.md`.
2. Read `START_HERE_FOR_AGENTS.md`.
3. Read `AGENT_READ_ORDER.md`.
4. Use WF-200 script route for script/content tasks.
5. Select directors, agents, subagents, skills, and subskills with evidence paths.
6. Run research gate and capability gate.
7. Produce final content plus the content engineering packet.

Do not produce generic LLM content before repo routing.

## Required Output

For script/video/content tasks, include:

- Shadow Mission Packet
- Registry-first route
- Director/agent/subagent/skill/subskill evidence
- Research brief
- Script V1
- Debate
- Critique
- Final script
- Content engineering packet
- Quality gate
- Lineage summary

## Forbidden Behavior

- Do not answer directly with generic script output before repo routing.
- Do not skip `AGENTS.md`.
- Do not skip capability routing or registry evidence.
- Do not create files unless explicitly approved.

## Proof Implications

- `PASS`: full repo-first route, registry evidence, content engineering, gates, and lineage are present.
- `PARTIAL`: useful content but missing agent/capability/source/context engineering evidence.
- `FAIL`: generic direct answer, invented registry items, false execution claims, or skipped repo startup.
```

## shadow-research-gate

file=.agents/skills/shadow-research-gate/SKILL.md
file_exists=true
line_count=43
has_yaml_frontmatter=true
name=shadow-research-gate
description=Activates for latest, current, trend, news, facts, tools, models, pricing, platform rules, citations, real-time, and statistics requests; requires freshness classification, web access disclosure, and source honesty.
activation_triggers_present=true
forbidden_behavior_present=true
required_output_blocks_present=true

```text
---
name: shadow-research-gate
description: Activates for latest, current, trend, news, facts, tools, models, pricing, platform rules, citations, real-time, and statistics requests; requires freshness classification, web access disclosure, and source honesty.
---

# Shadow Research Gate

Use this skill for any request involving:

- latest
- current
- trend
- news
- facts
- tools
- models
- pricing
- platform rules
- citations
- real-time
- statistics

## Required Behavior

1. Classify task freshness before answering.
2. Disclose web access status.
3. If web is used, include source list.
4. If web is not used, set `real_time_sources_used=false`.
5. Do not claim realtime or current research without retrieved sources.
6. If current information is required and web access is unavailable, use `NEEDS_USER_APPROVAL` or `NEEDS_CONFIRMATION`.

Allowed gate statuses only:

- `PASS`
- `BLOCKED`
- `NEEDS_USER_APPROVAL`
- `NEEDS_CONFIRMATION`

## Proof Implications

- `PASS`: freshness classification, research mode decision, source disclosure, and valid gate status are present.
- `PARTIAL`: source limitation exists but is disclosed and gated.
- `FAIL`: fake realtime/source claims, missing source list for web research, or invalid gate status.
```

## shadow-context-engineering

file=.agents/skills/shadow-context-engineering/SKILL.md
file_exists=true
line_count=43
has_yaml_frontmatter=true
name=shadow-context-engineering
description=Activates for script, video, audio, image, music, media output, provider handoff, and context packet requests; requires voice, visual, video, music, editing, platform, and provider-boundary context.
activation_triggers_present=true
forbidden_behavior_present=true
required_output_blocks_present=true

```text
---
name: shadow-context-engineering
description: Activates for script, video, audio, image, music, media output, provider handoff, and context packet requests; requires voice, visual, video, music, editing, platform, and provider-boundary context.
---

# Shadow Context Engineering

Use this skill when:

- script is requested
- video/audio/image/music/media output is implied
- provider handoff is requested
- context packet is requested

## Required Context Engineering Output

For script/video/content tasks, output:

- voice direction
- emotion map
- visual beat map
- facial expression direction
- gesture/body movement direction
- image prompts
- video prompts
- music/SFX cues
- editing plan
- captions/on-screen text
- provider handoff boundary

Do not call media providers. Do not claim generated media. This skill creates context and handoff instructions only.

## Forbidden Behavior

- Do not stop at script-only output unless the user explicitly requests script-only.
- Do not claim voice/image/video/music artifacts were generated.
- Do not omit provider handoff boundary.

## Proof Implications

- `PASS`: all context engineering sections are present with provider boundary.
- `PARTIAL`: script exists but one or more context engineering sections are missing.
- `FAIL`: false media execution claims or provider execution without approval.
```

codex_skills_content_proof_created=true

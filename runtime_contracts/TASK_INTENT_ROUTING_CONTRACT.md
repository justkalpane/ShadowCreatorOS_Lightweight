# Task Intent Routing Contract

This contract is active for every user task after `SHADOW_BOOT_CONFIRMATION`.

## Core Law

- Classify user intent before producing task output.
- Select exactly one primary route from `registries/task_intent_routing_matrix.yaml`; add secondary routes only when the task explicitly spans multiple lanes.
- Use the full local repo estate as authority: `directors/`, `agents/`, `subagents/`, `skills/`, `skills/sub_skills/`, `.agents/skills/`, `registries/`, and `runtime_contracts/`.
- Gumloop reference conversations are benchmark inspiration only. They are not a registry source and must not override local Shadow OS bindings.
- If a required director, agent, subagent, skill, or subskill is missing, mark `NEEDS_CONFIRMATION` and include `create_missing_registry_binding=true`.

## Required Route Fields

Every route decision must include:

```text
route_id=
trigger_terms=
mandatory_files_to_read=
director_selection=
agent_selection=
subagent_selection=
skill_selection=
subskill_selection=
governance_gate=
required_output_sections=
fail_conditions=
```

## Route Families

### TOPIC_DISCOVERY

Triggered by:

- find topic
- pick topic
- choose topic
- trending topic
- content idea
- viral idea

Must route through:

- Krishna / Aruna router layer or current repo equivalent
- Narada trend intelligence
- Chanakya qualification
- research/source gate
- quality/governance gate

Required output:

- topic options
- scores
- reason
- approval gate

### SCRIPT_GENERATION

Triggered by:

- write script
- YouTube script
- Shorts script
- reel script
- voiceover script

Must route through:

- Krishna / Aruna router layer or current repo equivalent
- Vyasa / Valmiki / Saraswati / script intelligence repo equivalents
- script skills
- hook generation
- debate/critique/refinement
- quality governance

Required output:

- 3 hook variants
- final script
- emotion/tone tags
- script quality scorecard
- rewrite if score below threshold

### SCRIPT_REFINEMENT

Triggered by:

- improve script
- refine script
- make it emotional
- make it viral
- make it cinematic
- rewrite

Must route through:

- script refinement directors
- critique/debate skills
- retention skills
- quality governance

### CONTEXT_ENGINEERING

Triggered by:

- context engineering
- convert script to context
- production packet
- video generation prompt
- voice generation prompt
- avatar context
- image prompts
- edit plan

Must route through:

- context engineering skills
- voice/image/video/editing/packaging route
- provider boundary gate

### VOICE_CONTEXT / ELEVENLABS_CONTEXT

Triggered by:

- ElevenLabs
- voice generation
- audio prompt
- SSML
- narration
- voice style

Must route through:

- Saraswati / Tumburu or current repo voice equivalents
- voice skills
- SSML/emotion/prosody rules
- provider boundary gate

### AVATAR_VIDEO_CONTEXT

Triggered by:

- avatar
- HeyGen
- video generation
- Sora
- Seedance
- Higgsfield
- Kling
- Pika
- Runway
- visual scene
- cinematic prompt

Must route through:

- Vishwakarma / Nataraja / Brahma / Maya / Varuna or current repo equivalents
- visual/video skills
- scene/gesture/facial/emotion rules
- provider boundary gate

### EDITING_PACKAGING

Triggered by:

- edit plan
- captions
- thumbnail
- title
- description
- hashtags
- platform packaging

Must route through:

- Garuda / Agni / Maya or current repo equivalents
- packaging/retention skills
- quality gate

### FULL_VIDEO_PIPELINE

Triggered by:

- make complete video
- full pipeline
- generate complete content package

Must route through:

- Krishna + Aruna full orchestrator
- all required lanes
- human approval checkpoints
- provider boundary gate
- no execution unless approved

## Failure Conditions

Mark `FAIL` if:

- no route is selected
- route selection happens after final content generation
- selected repo assets are cited but not read
- no director/agent/subagent/skill/subskill consumption ledger is present
- a script is generated before consumption ledgers
- shallow repo routing only is detected
- generic output appears after bootstrap

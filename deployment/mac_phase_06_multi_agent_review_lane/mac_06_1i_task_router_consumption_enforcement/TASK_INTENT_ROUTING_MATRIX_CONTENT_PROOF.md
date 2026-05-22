# Task Intent Routing Matrix Content Proof

TASK_INTENT_ROUTING_MATRIX_CONTENT_PROOF_STATUS=PASS

matrix_path=registries/task_intent_routing_matrix.yaml
matrix_line_count=599
gumloop_benchmark_only=true
missing_bindings=none_detected
needs_confirmation_entries=global_missing_binding_rule_only
full_video_pipeline_partial_reason=Provider/media execution remains disabled unless explicitly approved; chat-only orchestration and provider-ready context are available.

## Route IDs

- TOPIC_DISCOVERY
- SCRIPT_GENERATION
- SCRIPT_REFINEMENT
- CONTEXT_ENGINEERING
- VOICE_CONTEXT
- AVATAR_VIDEO_CONTEXT
- EDITING_PACKAGING
- FULL_VIDEO_PIPELINE

## Mandatory Bindings By Route

### TOPIC_DISCOVERY

mandatory_directors=Krishna, Aruna, Narada, Chanakya, Yudhishthira
mandatory_agents=agents/krishna/krishna_agent.py, agents/aruna/aruna_agent.py, agents/narada/narada_agent.py, agents/chanakya/chanakya_agent.py, agents/yudhishthira/yudhishthira_agent.py
mandatory_subagents=subagents/wf_100/wf_100_sub_agent.py, subagents/cwf_110/cwf_110_sub_agent.py, subagents/cwf_120/cwf_120_sub_agent.py, subagents/cwf_130/cwf_130_sub_agent.py, subagents/cwf_140/cwf_140_sub_agent.py
mandatory_skills=skills/topic_intelligence/M-001-global-trend-scanner.skill.md, skills/topic_intelligence/M-002-topic-opportunity-miner.skill.md, skills/topic_intelligence/M-008-topic-viability-scorer.skill.md, skills/topic_intelligence/M-016-content-gap-finder.skill.md, skills/system_intelligence/M-073-trend-prediction-engine.skill.md, skills/system_intelligence/M-074-viral-opportunity-scanner.skill.md
mandatory_subskills=SS-220, SS-221, SS-222, SS-223, SS-224

### SCRIPT_GENERATION

mandatory_directors=Krishna, Aruna, Vyasa, Valmiki, Saraswati, Yama
mandatory_agents=agents/krishna/krishna_agent.py, agents/aruna/aruna_agent.py, agents/vyasa/vyasa_agent.py, agents/valmiki/valmiki_agent.py, agents/saraswati/saraswati_agent.py, agents/yama/yama_agent.py
mandatory_subagents=subagents/wf_200/wf_200_sub_agent.py, subagents/cwf_210/cwf_210_sub_agent.py, subagents/cwf_220/cwf_220_sub_agent.py, subagents/cwf_230/cwf_230_sub_agent.py, subagents/cwf_240/cwf_240_sub_agent.py
mandatory_skills=S-201 Hook Optimizer, S-202 First Draft Generation, S-203 Retention Engineer, S-206 Emotion Amplifier, S-208 Governance Safety Checker, S-210 Final Script Packager, M-031 Mrbeast Hook System, M-036 Emotional Spike System, M-040 Story Momentum Engine
mandatory_subskills=SS-230, SS-231, SS-240, SS-241, SS-242, SS-243, SS-244, SS-245

### SCRIPT_REFINEMENT

mandatory_directors=Vyasa, Valmiki, Saraswati, Yama
mandatory_agents=agents/vyasa/vyasa_agent.py, agents/valmiki/valmiki_agent.py, agents/saraswati/saraswati_agent.py, agents/yama/yama_agent.py
mandatory_subagents=subagents/cwf_220/cwf_220_sub_agent.py, subagents/cwf_230/cwf_230_sub_agent.py, subagents/cwf_240/cwf_240_sub_agent.py
mandatory_skills=S-203 Hook Structure Audit, S-204 Clarity Enhancer, S-206 Clarity Retention Refinement, S-209 Emotional Rhythm Tuning, M-039 Re Hook System, M-126 Retention Repair Engine
mandatory_subskills=SS-240, SS-242, SS-243, SS-244

### CONTEXT_ENGINEERING

mandatory_directors=Brahma, Vishwakarma, Saraswati, Nataraja, Varuna
mandatory_agents=agents/brahma/brahma_agent.py, agents/vishwakarma/vishwakarma_agent.py, agents/saraswati/saraswati_agent.py, agents/nataraja/nataraja_agent.py, agents/varuna/varuna_agent.py
mandatory_subagents=subagents/wf_300/wf_300_sub_agent.py, subagents/cwf_310/cwf_310_sub_agent.py, subagents/cwf_320/cwf_320_sub_agent.py, subagents/wf_400/wf_400_sub_agent.py
mandatory_skills=P-301, P-302, P-303, P-304, P-305 context engineering skills
mandatory_subskills=SS-001, SS-101, SS-103, SS-104, SS-112

### VOICE_CONTEXT

mandatory_directors=Saraswati, Tumburu, Varuna
mandatory_agents=agents/saraswati/saraswati_agent.py, agents/tumburu/tumburu_agent.py, agents/varuna/varuna_agent.py
mandatory_subagents=subagents/cwf_430/cwf_430_sub_agent.py, subagents/wf_400/wf_400_sub_agent.py
mandatory_skills=M-231 Voiceover Direction Script, M-238 Compression EQ Specifications, M-240 Audio Mixing Guide, M-162 Voice Identity Cloner, M-163 Speech Emotion Engine
mandatory_subskills=SS-101

### AVATAR_VIDEO_CONTEXT

mandatory_directors=Vishwakarma, Nataraja, Brahma, Maya, Varuna
mandatory_agents=agents/vishwakarma/vishwakarma_agent.py, agents/nataraja/nataraja_agent.py, agents/brahma/brahma_agent.py, agents/varuna/varuna_agent.py
mandatory_subagents=subagents/wf_400/wf_400_sub_agent.py, subagents/cwf_410/cwf_410_sub_agent.py, subagents/cwf_420/cwf_420_sub_agent.py, subagents/cwf_440/cwf_440_sub_agent.py
mandatory_skills=M-216 Shot List Generator, M-217 B Roll Sourcing Strategy, M-221 Motion Graphics Storyboard, M-229 Video Performance Predictor, M-174 Visual Asset Generator
mandatory_subskills=SS-102, SS-103, SS-104, SS-105, SS-106

### EDITING_PACKAGING

mandatory_directors=Garuda, Agni, Maya, Saraswati
mandatory_agents=agents/garuda/garuda_agent.py, agents/agni/agni_agent.py, agents/saraswati/saraswati_agent.py
mandatory_subagents=subagents/wf_500/wf_500_sub_agent.py, subagents/cwf_510/cwf_510_sub_agent.py, subagents/cwf_520/cwf_520_sub_agent.py, subagents/cwf_530/cwf_530_sub_agent.py
mandatory_skills=M-218 Video Editing Script, M-223 Pacing Rhythm Editor, M-225 Thumbnail Designer, M-226 Video SEO Optimizer, M-227 Captions Subtitle Generator, M-230 Platform Specific Video Adapter, D-501 Platform Metadata Generator, D-502 SEO Optimization Specialist
mandatory_subskills=SS-108, SS-234, SS-112

### FULL_VIDEO_PIPELINE

mandatory_directors=Krishna, Aruna, Narada, Vyasa, Valmiki, Saraswati, Brahma, Vishwakarma, Nataraja, Garuda, Yama
mandatory_agents=agents/krishna/krishna_agent.py, agents/aruna/aruna_agent.py, agents/narada/narada_agent.py, agents/vyasa/vyasa_agent.py, agents/valmiki/valmiki_agent.py, agents/saraswati/saraswati_agent.py, agents/brahma/brahma_agent.py, agents/vishwakarma/vishwakarma_agent.py, agents/nataraja/nataraja_agent.py, agents/garuda/garuda_agent.py, agents/yama/yama_agent.py
mandatory_subagents=subagents/wf_010/wf_010_sub_agent.py, subagents/wf_100/wf_100_sub_agent.py, subagents/wf_200/wf_200_sub_agent.py, subagents/wf_300/wf_300_sub_agent.py, subagents/wf_400/wf_400_sub_agent.py, subagents/wf_500/wf_500_sub_agent.py
mandatory_skills=.agents/skills/shadow-content-orchestration/SKILL.md, .agents/skills/shadow-research-gate/SKILL.md, .agents/skills/shadow-context-engineering/SKILL.md, M-168, M-173, M-174, M-175, M-176
mandatory_subskills=SS-001, SS-101, SS-102, SS-104, SS-108, SS-112, SS-240

## Verification Commands

matrix_paths_missing=false
route_ids_present=true
mandatory_binding_sections_present=true
gumloop_source_registry_used=false

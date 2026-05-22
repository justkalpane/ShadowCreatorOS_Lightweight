SHADOW_BOOT_CONFIRMATION
shadow_boot_confirmation_present=true
first_visible_output_is_boot_confirmation=true
AGENTS.md
agents_md_detected=true
agents_md_read=true
repo_first_orchestration_started=true
layman_task_trigger_contract_read=true
generic_direct_answer_avoided=true
shadow_mode=CHAT_ONLY_MODE

## Native Agent Capability Assessment

NATIVE_AGENT_CAPABILITY_ASSESSMENT
repo_read=true
repo_write=false
shell_available=true
git_available=true
github_remote_available=true
web_access_available=UNKNOWN
web_fetch_available=UNKNOWN
web_access_used=false
real_time_sources_used=false
file_search_available=true
code_execution_available=true
package_install_available=NEEDS_CONFIRMATION
browser_available=NEEDS_CONFIRMATION
provider_credentials_available=false
n8n_runtime_available=false
capabilities_used=repo_read,file_search,local_validation
capabilities_not_used=web_research,provider_api,n8n,media_generation
capabilities_requiring_approval=repo_write,commit,push,n8n_execution,provider_execution,media_execution
limitations_disclosed=true

## Task Freshness Classification

TASK_FRESHNESS_CLASSIFICATION
freshness_class=CURRENT_SENSITIVE
current_data_required=true
freshness_reason=The task asks for latest AI video tools this week, which requires web research for current claims.

## Research Mode Decision

RESEARCH_MODE_DECISION
research_mode=repo_only
web_access_available=UNKNOWN
web_access_used=false
real_time_sources_used=false
source_list_present=false
current_fact_confidence=LIMITED
unsupported_claims=latest_tools_this_week

## Research Sufficiency Gate

Research Sufficiency Gate
gate_status=NEEDS_USER_APPROVAL
reason=Current tool names this week require web research approval or a web-enabled runtime before source-backed claims.
allowed_output_scope=Evergreen script about why creators fail when chasing tools without systems, with explicit limitation on latest-tool claims.

## Task-to-Capability Routing

TASK_TO_CAPABILITY_ROUTING
task_family=script_generation,context_engineering_packet,trend_research
capability_matrix_path=registries/native_capability_routing_matrix.yaml
registries/native_capability_routing_matrix.yaml
required_capabilities=repo_read,reasoning,registry_lookup,agent_runtime_index_lookup,skill_registry_lookup,subskill_registry_lookup,native_capability_assessment,tools_connectors_plugins_assessment,source_research_gate,content_engineering_contract
optional_capabilities=web_search,web_fetch
forbidden_by_default=n8n_execution,provider_api,media_generation,commit_push
approval_required_for=web_research,repo_write,n8n_execution,provider_execution,media_generation
missing_required_capabilities=none_for_repo_only_output
gate_result=NEEDS_USER_APPROVAL

## Registry-First Route

Registry-First Route
workflow_route=WF-200 script/content route
director_binding_path=registries/director_binding_wf200.yaml
skill_registry_path=registries/skill_registry_wf200.yaml
subagent_matrix_path=registries/sub_agent_matrix.json
subskill_registry_path=registries/subskill_runtime_registry.yaml

## Director Selection

Director Selection
selected_directors=vyasa,krishna,saraswati,durga,yama
director_evidence_paths=registries/director_binding_wf200.yaml

## Agent Runtime Selection

AGENT_RUNTIME_SELECTION
agent_runtime_index_path=registries/agent_runtime_selection_index.yaml
registries/agent_runtime_selection_index.yaml
selected_agents=vyasa_wf200_script_generation,krishna_wf200_script_debate,saraswati_wf200_script_refinement,durga_wf200_quality_gate,yama_wf200_boundary_gate
agent_evidence_paths=registries/agent_runtime_selection_index.yaml
agent_layer_status=PROVEN_WITH_ACTIVE_INDEX

## Subagent Selection

Subagent Selection
selected_subagents=script_generation,script_debate,script_refinement,quality_gate,boundary_gate
subagent_evidence_paths=registries/sub_agent_matrix.json

## Skill Selection

Skill Selection
selected_skills=shadow-content-orchestration,shadow-research-gate,shadow-context-engineering
skill_evidence_paths=.agents/skills/shadow-content-orchestration/SKILL.md,.agents/skills/shadow-research-gate/SKILL.md,.agents/skills/shadow-context-engineering/SKILL.md

## Subskill Selection

Subskill Selection
selected_subskills=topic_intake,trend_research_gate,script_generation,content_engineering_packet,quality_gate,lineage_summary
subskill_evidence_paths=registries/subskill_runtime_registry.yaml

## Tools/Connectors/Plugins Assessment

TOOLS_CONNECTORS_PLUGINS_ASSESSMENT
tools_available=repo_read,file_search,shell,validator
connectors_active=none_for_provider_execution
plugins_active=none_for_provider_execution
n8n_used=false
providers_called=false
media_artifacts_claimed=false

## Content Mission Brief

CONTENT_MISSION_BRIEF
topic=Latest AI video tools creators should watch this week, and why tool-chasing fails without a content system.
platform=YouTube Shorts
duration=45-60 seconds
audience=creators, editors, solopreneurs
objective=Warn creators not to confuse new tools with a repeatable content operating system.
emotional_promise=Relief from tool overwhelm.
transformation_promise=Move from chasing tools to building a repeatable creative system.

## Research and Source Status

RESEARCH_AND_SOURCE_STATUS
freshness_class=CURRENT_SENSITIVE
research_mode=repo_only
web_access_available=UNKNOWN
web_access_used=false
real_time_sources_used=false
source_list=[]
confidence=LIMITED
note=No current tool list is claimed because web research was not used.

## Script Structure

SCRIPT_STRUCTURE
hook=Every week a new AI video tool goes viral, but that is not why creators win.
setup=Tools can help, but they do not replace a content system.
tension=Creators fail when they chase the newest tool instead of building repeatable ideation, scripting, editing, publishing, and review loops.
payoff=The winning move is tools inside a system.
cta=Build the system first, then plug in the tools.

## Final Script

Final script
"Every week, a new AI video tool looks like the one that will change everything.
But most creators do not fail because they picked the wrong tool.
They fail because they have no system.
No idea pipeline.
No script structure.
No editing rhythm.
No publishing loop.
No review process.
So they jump from tool to tool, hoping the next app will create consistency for them.
AI can speed up your workflow, but it cannot replace a workflow you never built.
The real advantage is not chasing every new tool.
It is building a content system, then using AI to make each step faster.
Tools change every week.
Systems compound every day."

## Timed Beat Map

TIMED_BEAT_MAP
0-5s | spoken_line=Every week, a new AI video tool looks like the one that will change everything. | emotion=curious | pacing=fast hook | facial_expression=raised brows | gesture=phone swipe motion | visual_direction=rapid tool headlines without naming current claims | on_screen_text=New tool every week | b_roll=image of dashboard/tool icons | edit_cue=quick jump cuts | music_sfx_cue=soft riser
5-15s | spoken_line=But most creators do not fail because they picked the wrong tool. | emotion=grounded | pacing=slower | facial_expression=serious | gesture=open palm | visual_direction=creator overwhelmed by tabs | on_screen_text=Wrong problem | b_roll=messy timeline | edit_cue=hard cut | music_sfx_cue=low hit
15-35s | spoken_line=They fail because they have no system: no idea pipeline, no script structure, no editing rhythm, no publishing loop, no review process. | emotion=diagnostic | pacing=stacking rhythm | facial_expression=focused | gesture=counting fingers | visual_direction=workflow checklist | on_screen_text=System beats tool chasing | b_roll=content calendar | edit_cue=checklist pops | music_sfx_cue=ticks
35-55s | spoken_line=AI can speed up your workflow, but it cannot replace a workflow you never built. | emotion=conviction | pacing=firm | facial_expression=direct eye contact | gesture=point to camera | visual_direction=tool inside workflow diagram | on_screen_text=Tools change. Systems compound. | b_roll=loop diagram | edit_cue=zoom in | music_sfx_cue=resolve

## Voice Generation Context

VOICE_GENERATION_CONTEXT
voice_style=clear creator-educator
tone=direct, calm, urgent
pacing=fast hook, measured middle, strong close
pauses=after "no system" and "workflow you never built"
emphasis=wrong tool, no system, systems compound
pronunciation_notes=AI as "A I"
provider_boundary=ElevenLabs-ready direction only; no provider called.

## Image Generation Context

IMAGE_GENERATION_CONTEXT
thumbnail_concept=Creator surrounded by floating AI app windows, with a simple workflow board behind them.
scene_image_prompts=Modern creator desk, laptop with organized content workflow, floating abstract AI video tool panels, high contrast, clean editorial lighting.
style=sharp modern creator economy visual
lighting=bright key light, subtle screen glow
composition=creator centered, tool clutter on one side, system board on the other
negative_prompts=brand logos, fake UI names, cluttered text, distorted hands
provider_boundary=Image prompts only; no image provider called.

## Video Generation Context

VIDEO_GENERATION_CONTEXT
scene_prompts=Creator scrolling through endless tool announcements, then switching to a clean content system board.
camera_motion=fast push-in during hook, stable medium shot during explanation, final close-up on CTA.
character_action=swipe, stop, point to workflow, nod.
transitions=glitch swipe from tool chaos to workflow clarity.
visual_continuity=repeat black-white-green text accents and consistent creator desk setting.
provider_boundary=Sora/Seedance/Higgsfield/HeyGen prompt planning only; no provider called.

## Music/SFX Context

MUSIC_AND_SFX_CONTEXT
music_mood=focused tech pulse
tempo=95-110 BPM
intensity_changes=rise during hook, pull back during diagnosis, lift during close
sfx_moments=notification pings, whoosh cuts, checklist ticks, final low impact
silence_moments=brief pause after "no system"

## Editing Context

EDITING_CONTEXT
retention_cuts=pattern interrupt every 3-5 seconds
zooms=small zoom on "wrong tool" and "no system"
captions=large kinetic captions for key phrases
transitions=tool chaos to workflow board
pattern_interrupts=tab overload, checklist reveal, diagram close
re_hooks=Tools change every week. Systems compound every day.

## Platform Packaging

PLATFORM_PACKAGING
title_ideas=AI Tools Won't Save Bad Systems; Stop Chasing AI Tools; The Real AI Creator Advantage
thumbnail_text=Tools Change. Systems Win.
description=AI video tools are powerful, but creators win when they build repeatable content systems first.
hashtags=#AITools #ContentCreation #CreatorEconomy #YouTubeShorts
pinned_comment=What part of your content system is weakest right now: ideas, scripting, editing, publishing, or review?
cta=Build the system first, then plug in the tools.

## Provider Handoff Boundary

Provider Handoff Boundary
n8n_used=false
providers_called=false
media_artifacts_claimed=false
execution_requires_approval=true

## Quality Gate

Quality Gate
topic_adherence=PASS
emotional_strength=PASS
retention_strength=PASS
originality=PASS
platform_fit=PASS
source_confidence=LIMITED
provider_boundary_compliance=PASS
gate_status=NEEDS_USER_APPROVAL

## Lineage Summary

Lineage Summary
startup_paths=AGENTS.md,START_HERE_FOR_AGENTS.md,AGENT_READ_ORDER.md
contract_paths=runtime_contracts/ENVIRONMENT_TRIGGER_COMPATIBILITY_CONTRACT.md,runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md,runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md
registry_paths=registries/native_capability_routing_matrix.yaml,registries/agent_runtime_selection_index.yaml,registries/director_binding_wf200.yaml,registries/skill_registry_wf200.yaml,registries/sub_agent_matrix.json,registries/subskill_runtime_registry.yaml
skill_paths=.agents/skills/shadow-content-orchestration/SKILL.md,.agents/skills/shadow-research-gate/SKILL.md,.agents/skills/shadow-context-engineering/SKILL.md

## Final Proof Classification

Final Proof Classification
proof_classification=PASS
chat_only_mode_used=true
files_created=false
dossier_artifacts_created=false
internet_first_behavior_detected=false
web_access_used_before_repo_route=false

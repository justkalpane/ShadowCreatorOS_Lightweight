# Critical Registry Content Proof

audit_date=2026-05-22
operator_mode=OLD_LOCAL_MAC_CODEX_CHAT

## Line Counts

```text
registries/native_capability_routing_matrix.yaml line_count=190
registries/agent_runtime_selection_index.yaml line_count=773
```

## Required Task Family Checks

topic_intake=present
topic_qualification=present
trend_research=present
script_generation=present
script_debate=present
script_refinement=present
context_engineering_packet=present
provider_handoff_packet=present
quality_gate=present
lineage_summary=present
consolidated_output_creation=present
full_dossier_creation=present
github_sync=present
n8n_execution_bus=present
voice_generation=present
image_generation=present
video_generation=present
publishing=present
analytics_pull=present

## WF-200 Agent Entry Checks

vyasa_wf200_script_generation=present
krishna_wf200_script_debate=present
saraswati_wf200_script_refinement=present
durga_wf200_quality_gate=present
yama_wf200_boundary_gate=present

## native_capability_routing_matrix.yaml First 120 Lines

```yaml
task_families:
  - task_family: topic_intake
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [file_search]
    forbidden_by_default: [n8n_execution_bus, provider_api]
    approval_required_for: []
    source_research_required_when: "topic has current-event dependency"
    output_mode: chat
    notes: "Normalize request and constraints from repo-first doctrine."

  - task_family: topic_qualification
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [web_search]
    forbidden_by_default: [provider_api, workflow_execution]
    approval_required_for: [web_search]
    source_research_required_when: "latest/current claims appear"
    output_mode: chat
    notes: "Use Research Sufficiency Gate for freshness decisions."

  - task_family: trend_research
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [web_search, web_fetch]
    forbidden_by_default: [provider_api, n8n_execution_bus]
    approval_required_for: [web_search, web_fetch]
    source_research_required_when: "task class is CURRENT_SENSITIVE or REALTIME_REQUIRED"
    output_mode: chat
    notes: "Must disclose research_mode and source list if web is used."

  - task_family: script_generation
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning, registry_lookup, agent_runtime_index_lookup, skill_registry_lookup, subskill_registry_lookup, native_capability_assessment, tools_connectors_plugins_assessment, source_research_gate, content_engineering_contract]
    optional_capabilities: [web_search, web_fetch]
    forbidden_by_default: [n8n_execution, provider_api, media_generation, commit_push]
    approval_required_for: [web_search, web_fetch, repo_write, commit_push, provider_handoff, n8n_handoff]
    source_research_required_when: "script depends on current facts"
    output_mode: chat
    notes: "Registry-first routing and content engineering output are mandatory unless user requests script-only."

  - task_family: script_debate
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [web_search]
    forbidden_by_default: [provider_api, n8n_execution_bus]
    approval_required_for: [web_search]
    source_research_required_when: "debate claims require up-to-date evidence"
    output_mode: chat
    notes: "Debate outcomes must preserve source honesty."

  - task_family: script_refinement
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [web_search]
    forbidden_by_default: [provider_api, n8n_execution_bus]
    approval_required_for: [web_search]
    source_research_required_when: "refinement introduces current claims"
    output_mode: chat
    notes: "Keep gate outputs chat-visible."

  - task_family: context_engineering_packet
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning, registry_lookup, agent_runtime_index_lookup, skill_registry_lookup, subskill_registry_lookup, native_capability_assessment, tools_connectors_plugins_assessment, source_research_gate, content_engineering_contract]
    optional_capabilities: [repo_write, web_search, web_fetch]
    forbidden_by_default: [n8n_execution, provider_api, media_generation, commit_push]
    approval_required_for: [repo_write, web_search, web_fetch, commit_push, provider_handoff, n8n_handoff]
    source_research_required_when: "packet depends on live platform changes"
    output_mode: chat_or_consolidated_file
    notes: "In chat-only mode, context engineering must include voice, visual, image, video, music/SFX, editing, captions, packaging, and provider boundary."

  - task_family: provider_handoff_packet
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [repo_write]
    forbidden_by_default: [provider_api_execution, n8n_execution_bus]
    approval_required_for: [repo_write, provider_api_execution]
    source_research_required_when: "provider behavior/price is current-sensitive"
    output_mode: chat_or_consolidated_file
    notes: "Reference-only by default."

  - task_family: quality_gate
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [repo_write]
    forbidden_by_default: [provider_api, n8n_execution_bus]
    approval_required_for: [repo_write]
    source_research_required_when: "quality metrics depend on current external standards"
    output_mode: chat_or_consolidated_file
    notes: "Final status must match weakest mandatory evidence."

  - task_family: lineage_summary
    default_mode: CHAT_ONLY_MODE
    required_capabilities: [repo_read, reasoning]
    optional_capabilities: [repo_write]
    forbidden_by_default: [provider_api, n8n_execution_bus]
    approval_required_for: [repo_write]
    source_research_required_when: "lineage includes current external evidence"
    output_mode: chat_or_consolidated_file
    notes: "No invented paths or claims."

  - task_family: consolidated_output_creation
    default_mode: CONSOLIDATED_REPO_WRITE_MODE
    required_capabilities: [repo_write]
    optional_capabilities: [git]
    forbidden_by_default: [full_dossier_archive_mode]
    approval_required_for: [file_creation, git_commit, git_push]
    source_research_required_when: "output contains current claims"
    output_mode: file
    notes: "Create one mission output file by default."

  - task_family: full_dossier_creation
```

## agent_runtime_selection_index.yaml First 120 Lines

```yaml
agent_runtime_selection_index:
  - agent_id: "vyasa_wf200_script_generation"
    agent_name: "Vyasa Script Generation Agent"
    agent_file_path: "agents/vyasa/vyasa_agent.py"
    task_family: "script_generation"
    director_binding: "registries/director_binding_wf200.yaml"
    subagent_binding: "registries/sub_agent_matrix.json#CWF-210"
    skill_binding: "registries/skill_registry_wf200.yaml"
    selection_use: "WF-200 script generation owner; cite for script_generation tasks."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "krishna_wf200_script_debate"
    agent_name: "Krishna Script Debate Agent"
    agent_file_path: "agents/krishna/krishna_agent.py"
    task_family: "script_debate"
    director_binding: "registries/director_binding_wf200.yaml"
    subagent_binding: "registries/sub_agent_matrix.json#CWF-220"
    skill_binding: "registries/skill_registry_wf200.yaml"
    selection_use: "WF-200 script debate owner; cite for debate and critique tasks."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "saraswati_wf200_script_refinement"
    agent_name: "Saraswati Script Refinement Agent"
    agent_file_path: "agents/saraswati/saraswati_agent.py"
    task_family: "script_refinement"
    director_binding: "registries/director_binding_wf200.yaml"
    subagent_binding: "registries/sub_agent_matrix.json#CWF-230"
    skill_binding: "registries/skill_registry_wf200.yaml"
    selection_use: "WF-200 script refinement owner; cite for refinement/final shaping tasks."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "durga_wf200_quality_gate"
    agent_name: "Durga Script Quality Gate Agent"
    agent_file_path: "agents/durga/durga_agent.py"
    task_family: "quality_gate"
    director_binding: "registries/director_binding_wf200.yaml"
    subagent_binding: "registries/sub_agent_matrix.json#CWF-240"
    skill_binding: "registries/skill_registry_wf200.yaml"
    selection_use: "WF-200 quality gate support; cite for content quality validation."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "yama_wf200_boundary_gate"
    agent_name: "Yama Boundary Gate Agent"
    agent_file_path: "agents/yama/yama_agent.py"
    task_family: "provider_handoff_packet"
    director_binding: "registries/director_binding_wf200.yaml"
    subagent_binding: "registries/sub_agent_matrix.json#CWF-240"
    skill_binding: "registries/skill_registry_wf200.yaml"
    selection_use: "WF-200 provider/media boundary support; cite for no-execution handoff safety."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "agastya"
    agent_name: "agastya"
    agent_file_path: "agents/agastya.md"
    task_family: "NEEDS_CONFIRMATION"
    director_binding: "registries/director_binding.yaml"
    subagent_binding: "registries/sub_agent_matrix.json"
    skill_binding: "registries/skill_registry.yaml"
    selection_use: "Mapped from registry evidence; validate agent file path in agents/."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "agastyaagent"
    agent_name: "AgastyaAgent"
    agent_file_path: "agents/AgastyaAgent.md"
    task_family: "NEEDS_CONFIRMATION"
    director_binding: "registries/director_binding.yaml"
    subagent_binding: "registries/sub_agent_matrix.json"
    skill_binding: "registries/skill_registry.yaml"
    selection_use: "Mapped from registry evidence; validate agent file path in agents/."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "named_director"
    agent_name: "named_director"
    agent_file_path: "agents/named_director.md"
    task_family: "NEEDS_CONFIRMATION"
    director_binding: "registries/director_binding.yaml"
    subagent_binding: "registries/sub_agent_matrix.json"
    skill_binding: "registries/skill_registry.yaml"
    selection_use: "Mapped from registry evidence; validate agent file path in agents/."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "deep_analysis_|_insight_extraction"
    agent_name: "Deep Analysis | Insight Extraction"
    agent_file_path: "agents/Deep Analysis | Insight Extraction.md"
    task_family: "NEEDS_CONFIRMATION"
    director_binding: "registries/director_binding.yaml"
    subagent_binding: "registries/sub_agent_matrix.json"
    skill_binding: "registries/skill_registry.yaml"
    selection_use: "Mapped from registry evidence; validate agent file path in agents/."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "agent_control_plane_001"
    agent_name: "agent_control_plane_001"
    agent_file_path: "agents/agent_control_plane_001.md"
    task_family: "NEEDS_CONFIRMATION"
    director_binding: "registries/director_binding.yaml"
    subagent_binding: "registries/sub_agent_matrix.json"
    skill_binding: "registries/skill_registry.yaml"
    selection_use: "Mapped from registry evidence; validate agent file path in agents/."
    evidence_status: "PROVEN_BY_FILE_DISCOVERY"
  - agent_id: "agentcontrolplane001agent"
    agent_name: "AgentControlPlane001Agent"
    agent_file_path: "agents/AgentControlPlane001Agent.md"
    task_family: "NEEDS_CONFIRMATION"
    director_binding: "registries/director_binding.yaml"
```

critical_registry_content_proof_created=true

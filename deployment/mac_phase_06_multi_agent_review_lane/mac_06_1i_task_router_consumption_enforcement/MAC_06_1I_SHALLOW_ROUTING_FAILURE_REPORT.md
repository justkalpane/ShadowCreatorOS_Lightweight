# MAC-06.1I Shallow Routing Failure Report

MAC_06_1I_SHALLOW_ROUTING_FAILURE_STATUS=FAIL

bootstrap_confirmed=true
repo_first_orchestration_started=true
directors_selected=false
agents_selected=false
subagents_selected=false
skills_opened_and_read=false
subskills_identified=false
hook_variants_generated=false
content_engineering_complete=false
final_verdict=SHALLOW_REPO_ROUTING_ONLY

root_cause=
Startup docs were read, but task intent routing did not force actual director/agent/subagent/skill/subskill file consumption before script generation.

## Evidence Source

- Reference audit file: `/Users/apple/Desktop/Chatgpt & Codex Test Chat Conversation and workaround.txt`
- Bootstrap mode activated, but the output named repo layers without consuming their files.
- The failure is not a boot failure. It is a routing depth and output-quality enforcement failure.

## Required Correction

- Add task intent routing before content generation.
- Require full local repo registry selection across directors, agents, subagents, skills, and subskills.
- Require consumption ledgers and line-by-line influence map before script output.
- Require hook and script quality gates for script/content tasks.

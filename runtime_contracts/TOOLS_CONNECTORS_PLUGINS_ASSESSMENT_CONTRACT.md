# Tools Connectors Plugins Assessment Contract

Every mission must assess capability layers before claiming execution ability.

## Default Capability Layers

1. Agent-native capabilities
2. Repo-defined tools/connectors/plugins
3. Local machine apps/tools
4. Cloud/web LLM platform tools
5. n8n execution workflows
6. Provider/media APIs

## Required Assessment Block

```text
TOOLS_CONNECTORS_PLUGINS_ASSESSMENT
- item_name
- item_type = tool / connector / plugin / provider / workflow / local_app / web_app
- source_path
- runtime_status = ACTIVE / AVAILABLE_BY_APPROVAL / PLANNED / NOT_ACTIVE / NEEDS_CONFIRMATION
- required_for_task = true/false
- approval_required = true/false
- execution_allowed_now = true/false
- notes
```

## Status Rule

A tool may be available in platform but still `NOT_ACTIVE` for a mission if it is not invoked, not approved, or not needed.

## Runtime Truth Rules

- Do not claim connector/plugin `ACTIVE` unless repo evidence exists and current environment can use it.
- n8n workflows are `NOT_ACTIVE` by default.
- Provider APIs are `NOT_ACTIVE` by default.
- Web research is separate from provider execution.
- Chat/coding-agent reasoning is `ACTIVE` only when the current session can read the repo context for the mission.

## Canonical HyperFrames Assessment

When HyperFrames is part of the mission scope, the assessment must include the
repo-side local provider and its proof chain. The canonical row is:

```text
TOOLS_CONNECTORS_PLUGINS_ASSESSMENT
- item_name=HyperFrames CLI (Local)
- item_type=provider
- source_path=registries/provider_registry.yaml#provider_id=hyperframes_cli_local
- runtime_status=ACTIVE
- required_for_task=true
- approval_required=false
- execution_allowed_now=true
- notes=Use the local HyperFrames provider only with the SS-118 skill chain, original HyperFrames upstream skill docs, and registry asset-event proof.
```

Do not treat `HYPERFRAMES_SKILL_MD_PROOF` or `DAVINCI_ROLE_DECLARATION` as a
replacement for the assessment row. The assessment row is the connector-level
truth, while the skill proof is the skill-level truth.

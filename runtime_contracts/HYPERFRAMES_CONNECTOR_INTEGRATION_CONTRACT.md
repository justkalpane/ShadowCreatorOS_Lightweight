# HyperFrames Connector Integration Contract

## Purpose

This contract defines the repo-side connector blueprint for HyperFrames so the
system can prove when the real local HyperFrames bridge was used, when it was
only planned, and when a fallback path was chosen.

The canonical runtime integration is the local HyperFrames provider entry
`hyperframes_cli_local` plus the SS-116 / SS-118 skill chain and the official
HyperFrames upstream skill docs.

## Canonical Evidence Chain

A HyperFrames claim is only valid when all of the following are referenced:

```text
provider_registry_path=registries/provider_registry.yaml
provider_id=hyperframes_cli_local
skill_spec_path=skills/sub_skills/SS-118-hyperframes-html-renderer.subskill.md
skill_runtime_path=skills/sub_skills/SS-118-hyperframes-html-renderer.py
integrated_skill_paths=
  /Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes/SKILL.md
  /Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes-cli/SKILL.md
  /Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes-registry/SKILL.md
connector_assessment_contract=runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md
route_binding_contract=runtime_contracts/MEDIA_FACTORY_ROUTE_RUNTIME_BINDING_CONTRACT.md
media_bridge_contract=runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md
proof_gate=HYPERFRAMES_SKILL_MD_PROOF
registry_event=assets.jsonl:hyperframes_rendered
```

## Required Assessment Block

When HyperFrames is selected or claimed, the mission output must include a
tools/connectors/plugins assessment row for the canonical local provider:

```text
TOOLS_CONNECTORS_PLUGINS_ASSESSMENT
- item_name=HyperFrames CLI (Local)
- item_type=provider
- source_path=registries/provider_registry.yaml#provider_id=hyperframes_cli_local
- runtime_status=ACTIVE
- required_for_task=true
- approval_required=false
- execution_allowed_now=true
- notes=Canonical local HyperFrames bridge for deterministic HTML/CSS/GSAP rendering; original skill docs and registry asset events are required for proof.
```

The assessment row is not a substitute for `HYPERFRAMES_SKILL_MD_PROOF`. It is
the connector-level truth layer that must travel with the skill proof.

## No Silent Downgrade Rule

If a scene or mission requests HyperFrames-first rendering, the output must not
silently downgrade to generic FFmpeg motion, generic still motion, or a
different renderer without declaring:

```text
ROUTE_DOWNGRADED=true
fallback_reason=
requested_hyperframes_family=
replacement_method=
production_pass_allowed=false
```

## Connector Truth Levels

- `ACTIVE` only when the repo evidence exists and the current environment can
  use the local bridge.
- `AVAILABLE_BY_APPROVAL` only when the bridge is present but execution still
  needs user approval.
- `PLANNED` only when the integration exists as a blueprint and not as a
  callable bridge.
- `NOT_ACTIVE` when the bridge is not usable for the current mission.

## Scope Note

This contract does not install a new cloud connector. It hardens the existing
repo-side HyperFrames bridge so agents cannot claim the renderer was used
without proving the real local integration path.

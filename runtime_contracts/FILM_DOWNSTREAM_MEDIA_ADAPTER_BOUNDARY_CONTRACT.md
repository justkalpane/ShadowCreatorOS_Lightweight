# FILM DOWNSTREAM MEDIA ADAPTER BOUNDARY CONTRACT

Phase: `PHASE_13D_F8`
Status: `ACTIVE_LOCAL_BOUNDARY`

## Scope

`FILM_SCREENPLAY_GENERATION` produces preproduction-only screenplay intelligence.

`MEDIA_FACTORY_HANDOFF` is downstream-only and remains inactive during `script_only` mode.

## Boundary Rules

- `FILM_SCREENPLAY_GENERATION` may generate treatment, synopsis, character, world, visual, and department planning artifacts.
- `FILM_SCREENPLAY_GENERATION` may not trigger media rendering, provider execution, or avatar/video/image generation in `script_only` mode.
- `MEDIA_FACTORY_HANDOFF` may only activate after a dedicated handoff packet schema and explicit future activation.

## Allowed Future Targets

- `Nomi`
- `OpenMontage`
- `LTX`
- `DaVinci Resolve MCP`

## Activation Preconditions

- handoff packet schema exists
- explicit route transition is approved
- `script_only` mode is no longer active
- downstream boundary validator passes

## F8 Truth

- runtime media generation triggered: `false`
- paid provider triggered: `false`
- downstream adapter execution triggered: `false`

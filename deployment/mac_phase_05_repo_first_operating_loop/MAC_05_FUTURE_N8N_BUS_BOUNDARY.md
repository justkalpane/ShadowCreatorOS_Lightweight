# MAC-05 Future n8n Bus Boundary

## Boundary Rule

n8n is not required for topic-to-context engineering in MAC-05 planning.

## Current State

- n8n execution bus is deferred.
- 71 sanitized workflow exports are a reference pool only.
- No workflow import until manual review and explicit approval.

## Manual Review Items

- `CH70BvMePN6ofDNo` (video category)
- `bRQXDXVsPXQgCde8` (image category)

## Allowed in MAC-05 Planning

- Define how future n8n would consume `provider_handoff_packet.json`
- Define execution boundaries and approval gates

## Not Allowed in MAC-05 Planning

- Start/install n8n runtime
- Import workflows
- Activate or execute workflows
- Treat old workflow IDs/webhooks as active truth


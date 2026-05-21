# External Execution Bus Handoff Contract

## Purpose

Define when the lightweight repo-first lane hands off to n8n or providers.

## Boundary

n8n is used only when external execution is needed.

## Examples Of External Execution

- ElevenLabs voice generation
- HeyGen avatar/video generation
- Higgsfield video generation
- Sora / Seedance video generation
- YouTube upload/publishing
- Analytics pulls
- Scheduled monitoring

## Required Gates Before Execution

- Explicit user approval
- Cost gate approval
- Credential boundary cleared
- Provider/runtime selected
- Artifact/status packet destination defined

## Return Packet Requirement

Any execution bus action must return an artifact/status packet to repo/chat with:

- execution request ID
- provider/workflow used
- cost estimate or actual cost when available
- artifacts created
- errors/retries
- lineage update requirement

## Default

No execution by default.


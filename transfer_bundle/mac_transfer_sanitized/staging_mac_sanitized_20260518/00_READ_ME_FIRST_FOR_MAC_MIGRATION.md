# Read Me First For Mac Migration

This repository (C:\ShadowCreatorOS_Lightweight) is the active lightweight migration command center for the future Mac build.

## Why old Windows is quarantined
- The old Windows runtime is preserved for evidence and historical recovery.
- It is reference-only for migration planning, not active Mac runtime truth.

## What Mac build should do first
1. Run MAC-0 baseline audit only.
2. Validate repo transfer integrity.
3. Install approved dependencies in phased order.
4. Run first repo-first dossier proof (no n8n/provider/cloud runtime actions).

## What Mac build must not do first
- Do not import old n8n workflows into active Mac n8n runtime.
- Do not use old DB/profile/binaryData as active runtime.
- Do not use raw private workflow exports by default.

## Core locations
- Technical handoffs: C:\ShadowCreatorOS_Lightweight\handoff
- Deployment phases: C:\ShadowCreatorOS_Lightweight\deployment
- n8n full export: C:\ShadowCreatorOS_Lightweight\archive_reference\n8n_full_environment_reference_20260518_v8
- Migration audits: C:\ShadowCreatorOS_Lightweight\audits

## Transfer safety summary
- Sanitized n8n workflow exports can transfer as reference.
- Raw private exports are forensic-only and excluded from default transfer.
- Old DB/profile/binaryData must not become active Mac runtime.

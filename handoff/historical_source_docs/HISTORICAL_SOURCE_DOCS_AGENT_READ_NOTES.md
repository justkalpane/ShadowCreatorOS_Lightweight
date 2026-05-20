# Historical Source Docs Agent Read Notes

## How Future Agents Should Use Historical Sources

1. Start with active doctrine first:
   - `START_HERE_FOR_AGENTS.md`
   - `AGENT_STARTUP_PROMPT.md`
   - `AGENT_READ_ORDER.md`
   - MAC-05 loop and runtime contracts

2. Pull historical docs only when needed for deeper context:
   - PRD intent
   - previous build trajectories
   - quarantine rationale
   - migration decision history

3. Treat historical docs as reference context, not active commands.

## Interpretation Rules

- If historical guidance conflicts with active MAC-05 doctrine, MAC-05 doctrine wins.
- Old Windows runtime references are non-active by policy.
- n8n/provider execution references are future-layer context unless explicit execution approval exists.
- Historical workflow IDs/webhooks are not active runtime truth.

## Suggested Priority Order for Historical Context

1. `Detailed_PRD_MASTERPIECE_v34_ZERO_LOSS_HARNESS_RESTRUCTURED.txt`
2. `latest Codex entire Build status.txt`
3. `latest Claude entire Build status.txt`
4. `handoff/current_windows_environment/CURRENT_WINDOWS_ENVIRONMENT_HANDOFF_INDEX.md`
5. `handoff/mac_migration/MAC_MIGRATION_ZERO_GAP_TECHNICAL_HANDOFF_V4_COMBINED_MASTER.md`
6. `archive_reference/old_quarantine_manifest/FREEZE_MANIFEST.md`
7. `archive_reference/old_quarantine_manifest/QUARANTINE_STATUS.md`

## Safety Notes

- Do not print or expose secrets from historical files.
- Do not execute old runtime instructions directly from historical docs.
- Do not drift from branch `main` for active production unless user explicitly instructs.


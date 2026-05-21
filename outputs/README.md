# Outputs Folder Policy

## Purpose

This folder holds consolidated mission outputs when repo-write mode is approved.

## Structure

- Normal consolidated mission outputs: `outputs/missions/`
- Archive/old/failed attempts with approval: `outputs/archive/`
- Full dossiers remain under `dossiers/` only when explicitly requested.

## Cleanup

Outputs can be cleaned by the user when not needed and not part of committed history.

## Security

Never store secrets, credentials, provider keys, raw DB snapshots, old runtime state, or raw private workflow exports in `outputs/`.


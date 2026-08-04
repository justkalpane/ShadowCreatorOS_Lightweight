# Visual Output Template Lock Contract

## Purpose

This contract prevents visual output collapse into a shallow one-table summary.

## Locked Template

Required sections for visual media generation draft outputs:

1. Route Verification & System Locks
2. Assumption Verification Table
3. Asset Generation Order
4. Scene-by-scene Transposed Scene Blocks
5. Reasoning layer on every scene block
6. Media Method Distribution
7. B-roll Ratio Breakdown
8. Provider Honesty Gate
9. Local/Cloud/Hybrid Boundary
10. DaVinci/FFmpeg Assembly Plan
11. QC/Proof Registry
12. Final Classification

## Scene Block Schema

Each production scene must use a readable transposed scene block. Wide
17-column storyboard tables may appear only as a summary, never as the primary
scene execution format.

Minimum scene block shape:

```text
### SC-01 — <scene title>
scene_id=SC-01
timecode=0:00-0:15
duration_seconds=15
method=A-roll / cinematic B-roll / motion graphics / hybrid

> Script: <locked script line or paraphrase>

| Layer | Detail |
| --- | --- |
| Visual | ... |
| Motion | ... |
| Audio/SFX | ... |
| Editing | ... |
| Provider/Local Boundary | ... |
| Proof/QC | ... |
| Reasoning | ... |
```

Required scene layers:

- `Visual`
- `Motion`
- `Audio/SFX`
- `Editing`
- `Provider/Local Boundary`
- `Proof/QC`
- `Reasoning`

## Rules

- A giant merged storyboard table may exist only as a summary.
- Every scene block must include a reasoning layer.
- Every scene block must include scene metadata, script line, transposed
  `| Layer | Detail |` table, and the required production layers.
- Missing B-roll ratio breakdown fails the template.
- Provider honesty must be explicit; no fake execution claims.
- Planning-only drafts must not claim asset creation.

## Validation Markers

- `Transposed Scene Blocks`
- `| Layer | Detail |`
- `scene_id=`
- `timecode=`
- `duration_seconds=`
- `> Script:`
- `Reasoning layer`
- `B-roll Ratio Breakdown`
- `Provider Honesty Gate`
- `Local/Cloud/Hybrid Boundary`
- `DaVinci/FFmpeg Assembly Plan`
- `QC/Proof Registry`
- `Asset Generation Order`

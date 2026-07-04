# Root Cause Tree

```text
SCRIPT_FAILURE
├── MODEL_DRIFT
│   ├── Beat blocks exceeded the hard 3-20 second law
│   ├── Structured source rows were not emitted
│   ├── Quality fields were claimed without a real scorecard
│   └── Required influence-map section was omitted
├── ROUTER / ROUTE-GAP
│   ├── Canonical route surface does not require VALIDATION_SCORECARD
│   ├── Canonical route surface does not require script_integrity_lock
│   └── Acceptance-test surface requires both
├── VALIDATOR_FALSE_PASS
│   ├── PASS-like booleans were printed without the score fields behind them
│   ├── Source-proof claims were printed without structured rows
│   └── The transcript carries a false-completion shape
├── SKILL_FAILURE
│   ├── S-202 can default to placeholder re-hook output in non-strict mode
│   ├── S-210 must preserve RECURRING_REHOOK_MAP, DYNAMIC_TIMED_BEAT_MAP, EDITING_CONTEXT, and LINE_BY_LINE_INFLUENCE_MAP
│   └── The final artifact did not preserve the full proof surface
├── CONSUMPTION / GOVERNANCE GAP
│   ├── The required proof names were not carried through consistently
│   ├── Exact-line lineage and line-by-line influence evidence diverged
│   └── Final proof did not reflect the weakest gate
└── CLEAN / NOT PROVEN AS PRIMARY CAUSES
    ├── Isolated agent defect
    ├── Isolated subagent defect
    └── Isolated knowledge-base defect
```

## Primary drift point

The first hard drift is the beat map, because the contract says every block must
stay inside `3-20` seconds and the transcript immediately breaks that law with
`50`, `60`, `65`, `50`, and `30` second blocks.

## Secondary drift point

The next drift is proof serialization. The script says the proof exists, but it
does not serialize the proof in the structured forms the validator expects.


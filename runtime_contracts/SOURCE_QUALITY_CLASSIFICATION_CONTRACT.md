# Source Quality Classification Contract

## Purpose

The research layer must validate source sufficiency, not merely source
existence.

## Claim Classes

Every production-sensitive claim must be classified as one of:

- `VERIFIED`
- `CROSS_VERIFIED`
- `ANECDOTAL_SUPPORT`
- `BACKGROUND_CONTEXT`
- `INFERENCE`
- `NEEDS_CONFIRMATION`
- `UNSUPPORTED`

## Source Sufficiency Gate

For a production-grade real-person script:

```text
minimum_total_sources=3
minimum_non_encyclopedia_sources=2
minimum_source_categories=3
fact_vs_anecdote_map_present=true
```

An encyclopedia record may provide background context. It cannot be the sole
final authority. Interview reporting may support an emotional angle. It cannot
be treated as independently verified fact unless cross-verification is
recorded.

## Required Ledger Fields

```text
SOURCE_LEDGER
source_id=
url=
title=
date=
source_type=
claim_supported=
limitation=

FACT_VS_ANECDOTE_MAP
claim=
source=
classification=
script_usage_allowed=
risk_note=
```


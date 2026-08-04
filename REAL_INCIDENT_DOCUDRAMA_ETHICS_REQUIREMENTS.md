# Real Incident Docudrama Ethics Requirements

## Objective

Real incidents such as the NEET paper issue require source-grounded film treatment.
The film route must not invent facts, quotes, evidence, or archival visuals.

## Required real-incident packet fields

- source_research_status
- source ledger
- fact vs anecdote map
- verified timeline
- uncertainty ledger
- allegation language control
- composite character disclosure
- dramatization boundary
- source-vs-render separation
- no fake archival evidence
- no invented quotes
- no invented real-person actions
- no defamatory unsupported claims
- current-status freshness check
- legal/ethical caution notes
- downstream visual disclaimer needs

## Docudrama ethics rules

| Risk | Required rule | Schema field | Validator needed | Fixture needed |
|---|---|---|---|---|
| False accusation | Do not state allegations as verified fact | allegation language control | yes | yes |
| Outdated facts | Freshness check required for current incidents | current-status freshness check | yes | yes |
| Invented quote | Every quote must be source-grounded | source ledger + quote field | yes | yes |
| Invented real-person scene | No unsupported actions or scenes | fact vs anecdote map | yes | yes |
| Synthetic image shown as real evidence | Separate render from evidence | source-vs-render separation | yes | yes |
| Composite character confusion | Label composites clearly | composite character disclosure | yes | yes |
| Sensationalized tragedy | Tone and ethics constraints required | ethical caution notes | yes | yes |
| Political/legal ambiguity | Respect legal uncertainty | uncertainty ledger | yes | yes |
| Virality pressure overriding accuracy | Accuracy outranks growth | source priority law | yes | yes |
| Missing source ledger | No source-backed claim can be treated as PASS | source ledger | yes | yes |

## NEET fixture implication

NEET-style real-incident short films must fail if they lack:

- source ledger
- fact-vs-anecdote map
- uncertainty ledger
- dramatization boundary
- source-vs-render separation

This is especially important because the audience will often assume a film treatment implies evidence.


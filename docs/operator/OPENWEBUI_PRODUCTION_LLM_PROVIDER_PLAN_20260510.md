# OPENWEBUI_PRODUCTION_LLM_PROVIDER_PLAN_20260510

## Goal
Improve Open WebUI response quality and speed without breaking deterministic Shadow routing.

## Critical Separation
1. Tool routing reliability:
   - solved by direct router (`shadow_creator_os_direct_pipe`)
2. Model quality and latency:
   - improved by optional provider upgrades (OpenAI/Gemini/Perplexity)

Cloud model quality does not replace deterministic routing.

## Recommended Provider Tiers
- OpenAI-compatible high-quality writer model:
  - primary for script polish and long-form refinement
- Gemini OpenAI-compatible endpoint:
  - fast general generation and drafting
- Perplexity/Sonar OpenAI-compatible endpoint:
  - research-heavy topic expansion and fact-path exploration

## Open WebUI Setup Path
Use Open WebUI Admin settings for OpenAI-compatible connections.

Add providers through UI/runtime environment, not repository hardcoding.

## Secret Handling Rules
- Never commit API keys.
- Never place secrets in tracked files.
- Use:
  - Open WebUI Admin connection fields, or
  - local untracked env/source files outside git commits.

## Suggested Runtime Strategy
- Keep local Ollama as fallback and offline mode.
- Keep `Shadow Creator OS Direct` for deterministic orchestration routing.
- Optionally layer provider selection in Operator API by route/task category:
  - local-only default
  - optional OpenAI for script-quality mode
  - optional Gemini for speed mode
  - optional Perplexity for research mode

## Current Scope
- No paid provider keys were added.
- No cloud-provider runtime call path was enabled in this patch set.
- This document is planning-only and safe for commit.

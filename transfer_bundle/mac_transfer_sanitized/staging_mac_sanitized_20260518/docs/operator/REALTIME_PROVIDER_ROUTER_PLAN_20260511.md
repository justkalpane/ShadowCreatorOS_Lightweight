# Realtime Provider Router Plan - 2026-05-11

## Routing Matrix
- real_time_research: Perplexity -> Gemini -> OpenAI -> Anthropic -> Ollama -> local template
- grounded_research: Gemini -> Perplexity -> OpenAI -> Anthropic -> Ollama -> local template
- script/refinement: OpenAI -> Gemini -> Anthropic -> Perplexity -> Ollama -> local template
- thumbnail/metadata: OpenAI -> Gemini -> Anthropic -> Perplexity -> Ollama -> local template
- health/inspect: no LLM call

## Required Env Keys (local machine only)
- OPENAI_API_KEY
- GEMINI_API_KEY
- PERPLEXITY_API_KEY
- ANTHROPIC_API_KEY (optional)
- SHADOW_ENABLE_LIVE_CLOUD_CALLS=true (explicit gate)

## Packet Metadata Contract
Every creative packet should carry:
- provider_used
- model_used
- fallback_chain
- realtime_used
- citations
- provider_skip_reason
- cloud_provider_used
- generated_at

## Validation Steps (after key setup and user approval)
1. Restart Operator API.
2. Run one research job and verify provider_used != local_deterministic_template.
3. Verify ealtime_used=true and citations for research path.
4. Run script job and verify cloud model in metadata.

Generated: 2026-05-11 01:39:53 +05:30

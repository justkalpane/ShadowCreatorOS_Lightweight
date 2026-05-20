async function generate(input = {}) {
  // Placeholder adapter for explicit provider routing metadata.
  // Actual creative body fallback is handled in skill_runtime deterministic template path.
  return {
    status: 'PROVIDER_READY_NOT_EXECUTED',
    provider_skip_reason: 'OLLAMA_FALLBACK_RESERVED',
    model_used: process.env.OLLAMA_MODEL || 'llama3.2:3b',
    realtime_used: false,
  };
}

module.exports = { generate };

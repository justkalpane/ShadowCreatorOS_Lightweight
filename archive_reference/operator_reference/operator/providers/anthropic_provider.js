function isLiveAllowed() {
  return String(process.env.SHADOW_ENABLE_LIVE_CLOUD_CALLS || '').toLowerCase() === 'true';
}

async function generate(input = {}) {
  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return { status: 'PROVIDER_NOT_CONFIGURED', provider_skip_reason: 'ANTHROPIC_API_KEY_MISSING' };
  }
  if (!isLiveAllowed()) {
    return { status: 'PROVIDER_DISABLED_BY_POLICY', provider_skip_reason: 'LIVE_CLOUD_CALLS_DISABLED' };
  }

  return {
    status: 'PROVIDER_READY_NOT_EXECUTED',
    provider_skip_reason: 'LIVE_CALL_INTENTIONALLY_DISABLED_IN_AUDIT_PHASE',
    model_used: process.env.ANTHROPIC_MODEL || 'claude-sonnet-4-20250514',
  };
}

module.exports = { generate };

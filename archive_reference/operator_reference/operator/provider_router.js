const { readYamlSafe, nowIso } = require('./_shared');
const openaiProvider = require('./providers/openai_provider');
const geminiProvider = require('./providers/gemini_provider');
const perplexityProvider = require('./providers/perplexity_provider');
const ollamaProvider = require('./providers/ollama_provider');
const anthropicProvider = require('./providers/anthropic_provider');

class ProviderRouter {
  constructor() {
    // Prefer new config registry; fallback to legacy registries path.
    this.registry =
      readYamlSafe('config/provider_registry.yaml', null) ||
      readYamlSafe('registries/provider_registry.yaml', {});
  }

  listProviders() {
    const providers = Array.isArray(this.registry.providers) ? this.registry.providers : [];
    return {
      providers: providers.map((p) => ({
        provider_id: p.provider_id,
        class: p.class,
        status: p.status,
        phase1_allowed: p.phase1_allowed,
        premium_provider: p.premium_provider,
        runtime_modes: p.runtime_modes || [],
      })),
      generated_at: nowIso(),
    };
  }

  getProviderStatus(providerId) {
    const providers = Array.isArray(this.registry.providers) ? this.registry.providers : [];
    const p = providers.find((x) => x.provider_id === providerId);
    if (!p) return { status: 'not_found', provider_id: providerId };
    return {
      provider_id: p.provider_id,
      status: p.status,
      phase1_allowed: p.phase1_allowed,
      premium_provider: p.premium_provider,
      auth_style: p.auth_style,
      notes: p.notes || null,
      generated_at: nowIso(),
    };
  }

  async generate(input = {}) {
    const taskType = String(input.task_type || 'script_generation');
    const preferredProvider = String(input.preferred_provider || '').trim();
    const cloudLlmRequired = input.cloud_llm_required !== false;
    const routeMode = String(input.route_mode || 'production').toLowerCase();
    const chain = this.selectChain(taskType, preferredProvider);
    const fallbackChain = [];
    const skipReasons = [];

    for (const providerId of chain) {
      fallbackChain.push(providerId);
      const status = this.getProviderStatus(providerId);
      if (status.status === 'not_found') {
        skipReasons.push({
          provider_id: providerId,
          reason: 'PROVIDER_NOT_IN_REGISTRY',
        });
        continue;
      }
      if (status.phase1_allowed === false || String(status.status || '').toLowerCase() === 'deferred') {
        skipReasons.push({
          provider_id: providerId,
          reason: 'PROVIDER_DISABLED_BY_REGISTRY_POLICY',
        });
        continue;
      }

      const result = await this.invokeProvider(providerId, input);
      if (result?.status === 'SUCCESS') {
        return {
          status: 'SUCCESS',
          provider_used: providerId,
          model_used: result.model_used || null,
          realtime_used: Boolean(result.realtime_used),
          citations: Array.isArray(result.citations) ? result.citations : [],
          provider_skip_reason: null,
          fallback_chain: fallbackChain,
          content: result.content || null,
          cloud_provider_used: providerId !== 'ollama_local',
          generated_at: nowIso(),
        };
      }

      skipReasons.push({
        provider_id: providerId,
        reason: result?.provider_skip_reason || result?.status || 'PROVIDER_FAILED',
      });
    }

    const lastReason = skipReasons.length > 0 ? skipReasons[skipReasons.length - 1].reason : 'NO_PROVIDER_AVAILABLE';
    const primaryReasonEntry =
      skipReasons.find((x) => x.provider_id !== 'ollama_local') ||
      (skipReasons.length > 0 ? skipReasons[0] : null);
    const decisiveReason = primaryReasonEntry ? primaryReasonEntry.reason : lastReason;
    // Production hard rule: do not silently pass local deterministic fallback when cloud reasoning is required.
    if (cloudLlmRequired && routeMode === 'production') {
      return {
        status: 'CLOUD_PROVIDER_RATE_LIMITED',
        provider_used: null,
        model_used: null,
        realtime_used: false,
        citations: [],
        provider_skip_reason: decisiveReason,
        fallback_chain: fallbackChain,
        provider_attempts: skipReasons,
        cloud_provider_used: false,
        generated_at: nowIso(),
      };
    }

    return {
      status: 'FALLBACK_REQUIRED',
      provider_used: 'local_deterministic_template',
      model_used: 'template_v1',
      realtime_used: false,
      citations: [],
      provider_skip_reason: lastReason,
      fallback_chain: [...fallbackChain, 'local_deterministic_template'],
      provider_attempts: skipReasons,
      cloud_provider_used: false,
      generated_at: nowIso(),
    };
  }

  selectChain(taskType, preferredProvider = '') {
    if (preferredProvider) {
      return [preferredProvider, 'openai', 'gemini', 'perplexity', 'anthropic', 'ollama_local'];
    }

    const normalized = String(taskType || '').toLowerCase();
    if (normalized.includes('creative_bundle')) {
      return ['gemini', 'openai', 'anthropic', 'perplexity', 'ollama_local'];
    }
    if (normalized.includes('research')) {
      return ['perplexity', 'gemini', 'openai', 'anthropic', 'ollama_local'];
    }
    if (normalized.includes('script') || normalized.includes('refined') || normalized.includes('thumbnail') || normalized.includes('metadata')) {
      return ['openai', 'gemini', 'anthropic', 'perplexity', 'ollama_local'];
    }
    return ['openai', 'gemini', 'perplexity', 'anthropic', 'ollama_local'];
  }

  async invokeProvider(providerId, input) {
    switch (providerId) {
      case 'openai':
        return openaiProvider.generate(input);
      case 'gemini':
        return geminiProvider.generate(input);
      case 'perplexity':
        return perplexityProvider.generate(input);
      case 'anthropic':
        return anthropicProvider.generate(input);
      case 'ollama_local':
        return ollamaProvider.generate(input);
      default:
        return { status: 'PROVIDER_NOT_IMPLEMENTED', provider_skip_reason: 'PROVIDER_NOT_IMPLEMENTED' };
    }
  }
}

module.exports = ProviderRouter;

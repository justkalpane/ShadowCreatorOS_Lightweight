function isLiveAllowed() {
  return String(process.env.SHADOW_ENABLE_LIVE_CLOUD_CALLS || '').toLowerCase() === 'true';
}

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function stripCodeFence(text = '') {
  const trimmed = String(text || '').trim();
  if (trimmed.startsWith('```')) {
    return trimmed.replace(/^```[a-zA-Z]*\s*/,'').replace(/```$/,'').trim();
  }
  return trimmed;
}

function parseJsonLoose(text = '') {
  const cleaned = stripCodeFence(text);
  try {
    return JSON.parse(cleaned);
  } catch (_) {
    return null;
  }
}

function buildPrompt(input = {}) {
  const taskType = String(input.task_type || 'script_generation');
  const topic = String(input.topic || input.prompt || 'AI vs Human').trim();
  if (taskType === 'creative_bundle') {
    return [
      'Return ONLY valid JSON.',
      'Create a creator bundle for this topic.',
      `Topic: ${topic}`,
      'JSON schema:',
      '{',
      '  "research_packet": {"summary":"", "angles":[], "claims":[], "risks":[], "audience_hooks":[]},',
      '  "script_packet": {"hook":"", "intro":"", "body":[], "payoff":"", "cta":""},',
      '  "debate_packet": {"strengths":[], "weaknesses":[], "critique":"", "improvement_notes":[]},',
      '  "refined_script_packet": {"final_script":"", "scene_beats":[], "voiceover_text":""},',
      '  "context_packet": {"audience":"", "tone":"", "structure":[], "visual_direction":"", "context_json":{}},',
      '  "thumbnail_packet": {"thumbnail_ideas":[], "text_overlay_options":[], "composition_notes":""},',
      '  "metadata_packet": {"title_options":[], "description":"", "hashtags":[], "pinned_comment":""}',
      '}',
      'Do not include markdown fences.',
    ].join('\n');
  }
  return [
    `You are generating content for task_type=${taskType}.`,
    `Topic: ${topic}`,
    'Return concise, high-quality creator output.',
  ].join('\n');
}

async function generate(input = {}) {
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    return { status: 'PROVIDER_NOT_CONFIGURED', provider_skip_reason: 'GEMINI_API_KEY_MISSING' };
  }
  if (!isLiveAllowed()) {
    return { status: 'PROVIDER_DISABLED_BY_POLICY', provider_skip_reason: 'LIVE_CLOUD_CALLS_DISABLED' };
  }

  const model = process.env.GEMINI_MODEL || 'gemini-2.5-flash';
  const endpoint = `https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent?key=${encodeURIComponent(apiKey)}`;
  const maxRetries = Number(process.env.GEMINI_MAX_RETRIES || 4);
  const baseDelayMs = Number(process.env.GEMINI_RETRY_BASE_MS || 1200);
  let lastReason = 'GEMINI_REQUEST_ERROR';

  for (let attempt = 0; attempt <= maxRetries; attempt += 1) {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 30000);
    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          contents: [
            {
              role: 'user',
              parts: [{ text: buildPrompt(input) }],
            },
          ],
        }),
        signal: controller.signal,
      });

      const raw = await response.text();
      let payload = {};
      try { payload = raw ? JSON.parse(raw) : {}; } catch (_) { payload = {}; }

      if (!response.ok) {
        lastReason = `GEMINI_HTTP_${response.status}`;
        if (response.status === 429 && attempt < maxRetries) {
          const jitter = Math.floor(Math.random() * 300);
          const delay = Math.min(12000, (baseDelayMs * (2 ** attempt)) + jitter);
          await wait(delay);
          continue;
        }
        return {
          status: 'PROVIDER_FAILED',
          provider_skip_reason: lastReason,
          model_used: model,
        };
      }

      const text =
        payload?.candidates?.[0]?.content?.parts?.map((p) => p?.text).filter(Boolean).join('\n').trim() || '';
      if (!text) {
        return {
          status: 'PROVIDER_FAILED',
          provider_skip_reason: 'GEMINI_EMPTY_RESPONSE',
          model_used: model,
        };
      }

      const taskType = String(input.task_type || '');
      if (taskType === 'creative_bundle') {
        const bundle = parseJsonLoose(text);
        if (!bundle || typeof bundle !== 'object') {
          return {
            status: 'PROVIDER_FAILED',
            provider_skip_reason: 'GEMINI_BUNDLE_PARSE_FAILED',
            model_used: model,
          };
        }
        return {
          status: 'SUCCESS',
          model_used: model,
          realtime_used: false,
          citations: [],
          content: {
            creative_bundle: bundle,
          },
        };
      }

      return {
        status: 'SUCCESS',
        model_used: model,
        realtime_used: false,
        citations: [],
        content: {
          text,
        },
      };
    } catch (err) {
      lastReason = err?.name === 'AbortError' ? 'GEMINI_TIMEOUT' : 'GEMINI_REQUEST_ERROR';
      if (attempt < maxRetries) {
        const jitter = Math.floor(Math.random() * 300);
        const delay = Math.min(12000, (baseDelayMs * (2 ** attempt)) + jitter);
        await wait(delay);
        continue;
      }
      return {
        status: 'PROVIDER_FAILED',
        provider_skip_reason: lastReason,
        model_used: model,
      };
    } finally {
      clearTimeout(timeout);
    }
  }

  return {
    status: 'PROVIDER_FAILED',
    provider_skip_reason: lastReason,
    model_used: model,
  };
}

module.exports = { generate };

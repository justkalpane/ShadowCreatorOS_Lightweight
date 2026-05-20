module.exports = {
  operatorPort: Number(process.env.OPERATOR_PORT || 5050),
  n8nBaseUrl: process.env.N8N_BASE_URL || 'http://127.0.0.1:5678',
  ollamaBaseUrl: process.env.OLLAMA_BASE_URL || 'http://127.0.0.1:11434',
  repoRoot: process.env.SHADOW_REPO_ROOT || 'C:/ShadowEmpire-Git_Restore_01',
};


const { readYamlSafe } = require('./_shared');

class TaskRouter {
  constructor() {
    this.intentRegistry = readYamlSafe('registries/task_intent_registry.yaml', {});
    this.guiRouting = readYamlSafe('registries/gui_task_routing_matrix.yaml', {});
    this.directorMap = [
      { key: 'chanakya', label: 'Chanakya' },
      { key: 'krishna', label: 'Krishna' },
      { key: 'narada', label: 'Narada' },
      { key: 'vyasa', label: 'Vyasa' },
      { key: 'ravana', label: 'Ravana' },
      { key: 'shakuni', label: 'Shakuni' },
      { key: 'saraswati', label: 'Saraswati' },
      { key: 'agni', label: 'Agni' },
      { key: 'yama', label: 'Yama' },
      { key: 'kubera', label: 'Kubera' },
      { key: 'ganesha', label: 'Ganesha' },
      { key: 'vayu', label: 'Vayu' },
      { key: 'aruna', label: 'Aruna' },
    ];
    this.patterns = [
      { intent_id: 'director_critique', re: /\b(activate|critique|review|audit|flaws?|weakness(?:es)?|challenge)\b/i },
      { intent_id: 'new_content_job', re: /\b(create|script|youtube|video|content)\b/i },
      { intent_id: 'generate_topic_ideas', re: /\b(topic|ideas?)\b/i },
      { intent_id: 'generate_script', re: /\b(script|write)\b/i },
      { intent_id: 'generate_thumbnail_concept', re: /\b(thumbnail|image prompt|cover)\b/i },
      { intent_id: 'generate_metadata', re: /\b(metadata|tags?|description|title)\b/i },
      { intent_id: 'approve_output', re: /\bapprove\b/i },
      { intent_id: 'reject_and_remodify', re: /\b(reject|changes|remodify)\b/i },
      { intent_id: 'troubleshoot_error', re: /\b(error|debug|troubleshoot|failed)\b/i },
    ];
  }

  listTaskContracts() {
    return this.guiRouting.gui_tasks || {};
  }

  extractDirectorRequest(message = '') {
    const text = String(message || '').toLowerCase();
    const director = this.directorMap.find((d) => new RegExp(`\\b${d.key}\\b`, 'i').test(text));
    if (!director) return null;
    const critiqueMode = /\b(critique|review|audit|flaws?|weakness(?:es)?|challenge)\b/i.test(text);
    return {
      director_requested: director.label,
      director_key: director.key,
      intent_id: critiqueMode ? 'director_critique' : 'director_invoke',
      requires_reference_context: /\b(above|latest|previous|that script|this script)\b/i.test(text),
    };
  }

  resolveIntent(message) {
    const text = String(message || '').trim();
    if (!text) return 'new_content_job';
    const director = this.extractDirectorRequest(text);
    if (director) return director.intent_id;
    const found = this.patterns.find((p) => p.re.test(text));
    return found ? found.intent_id : 'new_content_job';
  }

  getIntentDef(intentId) {
    const intents = this.intentRegistry.intents || {};
    if (intents[intentId]) return { id: intentId, ...intents[intentId] };
    return null;
  }

  getGuiTaskDef(intentId) {
    const tasks = this.guiRouting.gui_tasks || {};
    if (tasks[intentId]) return tasks[intentId];
    return null;
  }

  resolveTaskFromMessage(message) {
    const text = String(message || '').trim();
    const director = this.extractDirectorRequest(text);
    const intentId = this.resolveIntent(message);
    const intent = this.getIntentDef(intentId) || this.getIntentDef('new_content_job');
    const guiTask = this.getGuiTaskDef(intentId) || this.getGuiTaskDef('new_content_job');
    const allowedModes = intent?.allowed_modes || guiTask?.allowed_modes || ['founder', 'creator', 'operator'];

    return {
      intent_id: intent?.id || 'new_content_job',
      label: intent?.label || 'Create New Content',
      entry_workflow: intent?.entry_workflow || guiTask?.entry_workflow || 'WF-010',
      child_workflows: intent?.child_workflows || guiTask?.child_workflows || [],
      approval_required: Boolean(intent?.approval_required),
      replay_eligible: Boolean(intent?.replay_eligible),
      director_requested: director?.director_requested || null,
      director_key: director?.director_key || null,
      intent_family: director ? 'director_command' : 'content_command',
      requires_reference_context: Boolean(director?.requires_reference_context),
      task_contract: {
        ...(guiTask || {}),
        allowed_modes: allowedModes,
      },
    };
  }
}

module.exports = TaskRouter;

const TaskRouter = require('./task_router');
const axios = require('axios');

class OllamaToolRunner {
  constructor(modeManager, n8nClient) {
    this.taskRouter = new TaskRouter();
    this.modeManager = modeManager;
    this.n8n = n8nClient;
    this.operatorApiUrl = process.env.OPERATOR_API_URL || 'http://127.0.0.1:5002';
  }

  async run(commandText, context = {}) {
    const mode = context.mode || this.modeManager.getDefaultMode();
    const task = this.taskRouter.resolveTaskFromMessage(commandText);
    const route = this.modeManager.getDefaultRoute(mode);
    const routeCheck = this.modeManager.validateRoute(mode, route);
    const modeCheck = this.modeManager.validateModeForTask(mode, {
      id: task.intent_id,
      allowed_modes: task.task_contract?.allowed_modes || task.allowed_modes || [],
    });

    if (!routeCheck.allowed || !modeCheck.allowed) {
      return {
        status: 'blocked',
        reason: modeCheck.reason || routeCheck.reason,
        mode,
        route,
        intent_id: task.intent_id,
      };
    }

    // For content creation tasks, delegate to /operator/new-content-job to ensure WF-001 dossier creation
    if (task.intent_id === 'new_content_job') {
      try {
        const response = await axios.post(`${this.operatorApiUrl}/operator/new-content-job`, {
          topic: commandText,
          context: context.topic_context || 'YouTube video',
          mode,
          route_id: route,
          dossier_id: context.dossier_id,
        });

        return {
          status: response.data.status || 'accepted',
          intent_id: task.intent_id,
          dossier_id: response.data.dossier_id,
          workflow_id: 'WF-010',
          route_id: route,
          mode,
          wf001: response.data.wf001,
          wf010: response.data.wf010,
          operator_result: response.data,
        };
      } catch (error) {
        return {
          status: 'failed',
          intent_id: task.intent_id,
          workflow_id: 'WF-010',
          route_id: route,
          mode,
          error: error.message,
          error_code: error.response?.status || 500,
        };
      }
    }

    // For other tasks, use direct n8n trigger (non-content creation)
    const payload = {
      user_message: commandText,
      mode,
      route_id: route,
      topic: commandText,
      context: context.topic_context || 'YouTube video',
      dossier_id: context.dossier_id,
    };

    const result = await this.n8n.trigger(task.entry_workflow, payload);
    return {
      status: result.status === 'failed' ? 'failed' : 'accepted',
      intent_id: task.intent_id,
      workflow_id: task.entry_workflow,
      route_id: route,
      mode,
      n8n_result: result,
    };
  }
}

// CLI Entry point for npm run operator:ollama
if (require.main === module) {
  (async () => {
    try {
      const ModeManager = require('./mode_manager');
      const OperatorN8nClient = require('./n8n_client');

      // Initialize dependencies
      const modeManager = new ModeManager();
      const n8nClient = new OperatorN8nClient();
      const runner = new OllamaToolRunner(modeManager, n8nClient);

      // Determine input source: CLI args > stdin > interactive
      let userPrompt = null;

      // 1. Check for CLI args (npm run operator:ollama -- "prompt here")
      const args = process.argv.slice(2);
      if (args.length > 0) {
        userPrompt = args.join(' ');
      }

      // 2. Check for stdin (echo "prompt" | npm run operator:ollama)
      if (!userPrompt && !process.stdin.isTTY) {
        const chunks = [];
        for await (const chunk of process.stdin) {
          chunks.push(chunk);
        }
        userPrompt = Buffer.concat(chunks).toString('utf-8').trim();
      }

      // 3. Interactive prompt if TTY
      if (!userPrompt && process.stdin.isTTY) {
        const readline = require('readline');
        const rl = readline.createInterface({
          input: process.stdin,
          output: process.stdout,
        });

        userPrompt = await new Promise((resolve) => {
          rl.question('Enter your content creation prompt: ', (answer) => {
            rl.close();
            resolve(answer);
          });
        });
      }

      if (!userPrompt) {
        console.error('Error: No input provided. Use CLI args, stdin, or interactive prompt.');
        process.exit(1);
      }

      // Run the tool runner with default context
      const result = await runner.run(userPrompt, {
        mode: 'creator',
        topic_context: 'YouTube video',
      });

      // Output result as JSON with additional metadata
      console.log(JSON.stringify({
        status: result.status,
        dossier_id: result.dossier_id || null,
        intent_id: result.intent_id,
        route_id: result.route_id,
        mode: result.mode,
        wf001: result.wf001 || null,
        wf010: result.wf010 || null,
        endpoint_called: result.dossier_id ? '/operator/new-content-job' : null,
        operator_run_used: false,
        operator_new_content_job_used: result.dossier_id ? true : false,
        fake_media_output_claim: false,
        error: result.error || null,
        operator_result: result.operator_result || null,
      }, null, 2));

      process.exit(result.status === 'failed' ? 1 : 0);
    } catch (error) {
      console.error(JSON.stringify({
        status: 'error',
        error: error.message,
        stack: error.stack,
        fake_media_output_claim: false,
      }, null, 2));
      process.exit(1);
    }
  })();
}

module.exports = OllamaToolRunner;


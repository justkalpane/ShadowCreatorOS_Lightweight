#!/usr/bin/env node
const OllamaToolRunner = require('./ollama_tool_runner');
const ModeManager = require('./mode_manager');
const OperatorN8nClient = require('./n8n_client');

async function runTest() {
  const testMessage = 'R9P-B2 correlation proof TOKEN-R9PB2-001: Create a YouTube script outline about AI tools for creators using the Shadow Creator OS local operator.';
  const requestStartTime = Date.now();
  
  console.log('='.repeat(70));
  console.log('R9P-B2: Fresh Dossier Correlation Proof Test');
  console.log('='.repeat(70));
  console.log('');
  console.log('Request Start Time:', new Date(requestStartTime).toISOString());
  console.log('Test Message:', testMessage);
  console.log('');
  console.log('Proof Token: TOKEN-R9PB2-001');
  console.log('');

  const modes = new ModeManager();
  const n8n = new OperatorN8nClient();
  const ollama = new OllamaToolRunner(modes, n8n);

  console.log('Running OllamaToolRunner.run()...');
  console.log('');

  const result = await ollama.run(testMessage, {
    mode: 'creator',
    topic_context: 'YouTube video creation',
  });

  console.log('Result:');
  console.log(JSON.stringify(result, null, 2));
  console.log('');
  console.log('='.repeat(70));
  
  if (result.status === 'accepted' && result.dossier_id) {
    console.log('✓ TEST PASSED - Dossier created: ' + result.dossier_id);
    console.log('  WF-001 status:', result.wf001?.status);
    console.log('  WF-010 status:', result.wf010?.status);
    console.log('  Request start time:', new Date(requestStartTime).toISOString());
  } else if (result.status === 'failed') {
    console.log('✗ TEST FAILED - ' + (result.error || 'Unknown error'));
  } else {
    console.log('? TEST INCOMPLETE - Status: ' + result.status);
  }
  console.log('='.repeat(70));
  
  return { result, requestStartTime };
}

runTest().catch(err => {
  console.error('Test error:', err);
  process.exit(1);
});

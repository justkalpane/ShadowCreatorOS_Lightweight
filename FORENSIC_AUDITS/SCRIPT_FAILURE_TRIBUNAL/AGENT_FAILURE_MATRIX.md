# Agent Failure Matrix

| agent | evidence location | status | proof | conclusion |
| --- | --- | --- | --- | --- |
| KrishnaAgent | `agents/krishna/krishna_agent.py:38-47, 80-83` | CLEAN | The agent already requires source breadth, claim confidence, and weakest-gate rejection. | No isolated Krishna-agent defect is needed to explain the failure. |
| VyasaAgent | `agents/vyasa/vyasa_agent.py:38-47, 80-83` | CLEAN | The agent already requires master-script English, cinematic story, recurring re-hooks, and line-influence bindings. | No isolated Vyasa-agent defect is needed to explain the failure. |
| ValmikiAgent | `agents/valmiki/valmiki_agent.py:38-47, 80-83` | CLEAN | The agent already requires source breadth, claim confidence, and honesty in proof claims. | No isolated Valmiki-agent defect is needed to explain the failure. |

## Agent-layer conclusion

The evidence does not prove a unique agent-layer root cause. The break occurs in
how the route and model serialized the proof, not in a missing agent contract.


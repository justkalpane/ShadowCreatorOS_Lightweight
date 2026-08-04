# Subagent Failure Matrix

| subagent | evidence location | status | proof | conclusion |
| --- | --- | --- | --- | --- |
| Wf200SubAgent | `subagents/wf_200/wf_200_sub_agent.py:44-47, 79-82` | CLEAN | The subagent blocks before output when the lane cannot produce valid packets. | No isolated WF-200 defect is needed to explain the failure. |
| Cwf220SubAgent | `subagents/cwf_220/cwf_220_sub_agent.py:44-47, 79-82` | CLEAN | The subagent critique lane explicitly rejects generic filler and unsupported re-hooks. | No isolated CWF-220 defect is needed to explain the failure. |

## Subagent-layer conclusion

The subagent layer is not the primary root cause in the inspected evidence set.
The failure is higher-level proof collapse.


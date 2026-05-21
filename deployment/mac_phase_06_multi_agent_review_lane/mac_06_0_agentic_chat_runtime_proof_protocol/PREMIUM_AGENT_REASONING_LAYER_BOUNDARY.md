# Premium Agent Reasoning Layer Boundary

## Supported Agent Categories

### Codex

- Can operate with local repo read/write access.
- Proven for dossier production through Dossier #2 and #3.
- Must follow repo doctrine and commit gates.

### Claude

- Can operate from GitHub/repo context if available.
- Can produce chat-only output or review packets.
- Repo-write support depends on user-provided environment.

### ChatGPT

- Can operate from pasted repo context or GitHub-visible files.
- Can produce chat-only mission packets, review packets, and output packets.
- Does not imply local repo write access.

### Kimi

- Can operate as creative/reasoning reviewer if context is provided.
- Can produce chat-only output or review packets.

### DeepSeek

- Can operate as structure/schema/code reviewer if repo context is available.
- Can produce chat-only output or review packets.

### Perplexity

- Can operate as research/source-validation reviewer.
- Must not call paid APIs or execute providers unless explicitly approved.
- User may manually provide review packet back to Codex.

### Gemini Chat/App

- Can operate as chat/app reasoning layer if user chooses.
- Gemini API is not default and must not be called by Codex without explicit approval.

### Antigravity

- Optional repo-aware coding/operator lane if installed and approved.
- Must follow `START_HERE_FOR_AGENTS.md` and MAC-06 contracts.

### Future Repo-Aware Coding Agents

- Allowed only if they can read repo doctrine and return contract-compliant outputs.

## Universal Rules

- Do not fake repo access.
- Do not fake n8n/provider/media execution.
- Do not invent directors, agents, skills, subskills, or runtime status.


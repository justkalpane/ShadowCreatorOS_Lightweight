# MAC-06.1A Fresh GitHub Repo Bootstrap Proof Plan

## Purpose

Prove that a fresh repo-aware agent can operate Shadow Creator OS directly from GitHub `main` without relying on this current Mac Codex chat memory.

## Proof Model

The agent receives:

- GitHub repo: `https://github.com/justkalpane/ShadowCreatorOS_Lightweight`
- Branch: `main`
- Instruction: detect/read `AGENTS.md` first if available, then read `START_HERE_FOR_AGENTS.md`
- Simple user task: create a YouTube Shorts script on the requested topic

## What The Agent Must Prove

- The first visible output is `SHADOW_BOOT_CONFIRMATION`, before any script/summary/advice.
- It reports `shadow_boot_confirmation_present=true` and `first_visible_output_is_boot_confirmation=true`.
- It starts from the repo, not internet-first behavior.
- It follows `START_HERE_FOR_AGENTS.md` and `AGENT_READ_ORDER.md`.
- It detects and reads `AGENTS.md` before all other repo instructions when available.
- It uses the canonical startup order from `AGENTS.md`.
- It cites `registries/native_capability_routing_matrix.yaml`.
- It cites `registries/agent_runtime_selection_index.yaml`.
- For content/script/video tasks, it follows `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`.
- It remains `CHAT_ONLY_MODE`; `files_created=false` and `dossier_artifacts_created=false`.
- It creates a Shadow Mission Packet.
- It loads repo context.
- It routes registry-first.
- It selects directors, agents, subagents, skills, and subskills with real evidence paths.
- It assesses tools/connectors/plugins honestly as `ACTIVE`, `PLANNED`, `NOT_ACTIVE`, or `NEEDS_CONFIRMATION`.
- It produces research, script, debate, critique, final script, and context engineering packet.
- It runs a quality gate.
- It returns output to chat or repo depending on access.
- It does not execute n8n, providers, media, Gemini API, OpenWebUI, or old runtime.

## Fail-Fast Rule

If a plain content task returns any final answer/script/summary/outline/advice before `SHADOW_BOOT_CONFIRMATION`, classify `FAIL`.

## Supported Agent Types

The proof may be run with Codex, Claude, ChatGPT, Kimi, DeepSeek, Gemini, Perplexity, Antigravity, local LLM apps, or other repo-aware LLM/coding agents.

A successful Codex proof is the first representative proof, not the only possible future proof. Other agents can be progressively tested later. Users must not be forced to install all agents.

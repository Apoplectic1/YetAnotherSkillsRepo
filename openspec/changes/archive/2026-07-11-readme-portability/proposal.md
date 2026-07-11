# Proposal: readme-portability

## Why

The README's "What you get" line hard-wires the Claude Code install location ("deployed to `~/.claude/skills/`") and never says these are standard **Agent Skills** — an open format (originated by Anthropic, community-governed at agentskills.io) supported by a large ecosystem: Gemini CLI, OpenAI Codex, Cursor, GitHub Copilot/VS Code, Goose, OpenCode, OpenHands, JetBrains Junie, Roo Code, Kiro, Tabnine, and more (verified 2026-07-10 via agentskills.io's client showcase). Cross-tool reuse is a real selling point the README currently leaves on the table. Truth boundary established up front: **Perplexity and other chat/answer engines are NOT in scope** — they aren't filesystem agents and don't support skills; the README scopes to "Agent Skills-compatible agents" and names verified examples only.

## What Changes

- **"What you get" intro** — reframe from the Claude-only location to the format: the four skills are standard Agent Skills folders; Claude Code is the authored-and-tested home, not the only home.
- **New Usage Notes subsection — "Beyond Claude Code"** — where the compatibility list lives (agentskills.io client showcase), how to install into another tool (copy `skills/*/` into that tool's documented skills directory — `deploy.sh` is Claude-Code-specific), and the two honest degradation caveats: (1) worker-model recommendations are Claude tiers (substitute your stack's strong/cheap tiers); (2) the audit's fan-out wants parallel subagents — tools without orchestration run passes sequentially (slower, same convergence loop). Plus the router caveat: SETUP scaffolds a `CLAUDE.md` router; tools that auto-load a different instructions file (e.g. `AGENTS.md`) need that file to point at / mirror the router.
- **Requirements line in Quick Start** — "any harness that reads `~/.claude/skills/`" becomes "any Agent Skills-compatible agent (see Usage Notes)".
- **No push**: implementation lands on `dev` only; merge to `main` + mirror push is explicitly gated on the user (their instruction 2026-07-10: "No push yet").

## Capabilities

### New Capabilities

(none)

### Modified Capabilities

- `github-distribution`: the "Public README at repo root" requirement's enumerated content changes — Usage Notes gains the portability subsection, and a new scenario covers the cross-tool consumer.

## Impact

- **Edited files:** `README.md` only (public copy). Delta spec for `github-distribution`.
- **Not changed:** skills text, deploy.sh (stays Claude-Code-targeted by design), LICENSE, router.
- **Distribution:** committed on `dev`, NOT merged/pushed until the user says so.

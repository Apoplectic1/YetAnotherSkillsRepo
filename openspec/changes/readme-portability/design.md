# Design: readme-portability

## Context

agentskills.io (fetched 2026-07-10) confirms Agent Skills is an open standard with a broad client showcase — Gemini CLI, OpenAI Codex, Cursor, GitHub Copilot/VS Code, Goose, OpenCode, OpenHands, Junie, Roo Code, Kiro, Tabnine, and dozens more, each documenting its own skills directory. The README currently frames install as Claude-Code-only (`~/.claude/skills/`). The four skills are plain SKILL.md folders and conform to the spec, so the portability claim is true — with two graceful degradations and one adaptation worth stating honestly. Perplexity-class answer engines are out of scope (no filesystem agent, no skills support) and will not be named.

## Goals / Non-Goals

**Goals:**
- README tells a non-Claude-Code consumer: these are standard Agent Skills, where the live compatibility list is, how to install into their tool, and what degrades.
- Claims stay verifiable and rot-resistant: name a handful of marquee adopters, link the live showcase for the rest.

**Non-Goals:**
- No per-tool install matrix (paths/UIs churn; each tool's own docs are canonical — link, don't restate).
- No deploy.sh multi-tool support (stays Claude-Code-targeted; other tools = manual copy per their docs).
- No naming of non-supporting products (scoping does the exclusion politely).
- No push — `dev` commit only, mirror untouched until the user says.

## Decisions

1. **Three README touchpoints, one new subsection** (smallest edit that carries the claim):
   - *"What you get" intro:* "Four skills, deployed to `~/.claude/skills/`:" → "Four skills, shipped as standard [Agent Skills](https://agentskills.io) — authored and tested on Claude Code, loadable by any skills-compatible agent (see [Beyond Claude Code](#beyond-claude-code)):"
   - *Quick Start requirements line:* "any harness that reads `~/.claude/skills/` works" → "or any [Agent Skills](https://agentskills.io)-compatible agent — see [Beyond Claude Code](#beyond-claude-code)".
   - *Usage Notes gains a fourth subheading, "Beyond Claude Code"* (advisory tone, matching the section): the open-format statement + 4-5 marquee adopters + [client showcase](https://agentskills.io/clients) link; install = copy `skills/*/` into the tool's documented skills directory (`deploy.sh` is Claude Code's installer); caveat (a) worker-model recommendations are Claude tiers — substitute the stack's strong/cheap equivalents; caveat (b) the audit fan-out assumes parallel subagents — without orchestration, passes run sequentially (slower, same convergence loop); adaptation (c) setup scaffolds a `CLAUDE.md` router — tools auto-loading a different instructions file (e.g. `AGENTS.md`) point it at or mirror the router.
2. **Placement: Usage Notes subsection, not a new top-level section** — it is advisory guidance, and keeping the top-level section list stable minimizes the spec delta and preserves the OpenSpec-exemplar shape the user chose. Alternative (top-level "Works with" section): rejected — over-weights a secondary message.
3. **Marquee-list rot control** — name only Gemini CLI, OpenAI Codex, Cursor, GitHub Copilot, Goose ("and many others" + live link). The named five are major, verified today, and unlikely to drop the format quietly.
4. **Spec delta = one MODIFIED requirement** — the enumerated Usage Notes contents change; add a "Cross-tool consumer" scenario; also loosen the stale "two-sentence" repo-layout phrasing to "short" (drifted when the OpenSpec credit landed — cheap honest tidy-up inside the same MODIFIED block).

## Risks / Trade-offs

- [Adopter list rots] → five stable names + the live showcase link carries the rest.
- [Overselling portability] → caveats live in the same paragraph as the claim, not a footnote; skills remain "authored and tested on Claude Code."
- [Anchor link breaks if subheading renamed] → two in-README anchors reference `#beyond-claude-code`; renaming the subheading must update both (single-file blast radius).

## Open Questions

(none)

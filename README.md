# YetAnotherSkillsRepo

Claude Code skills, RED/GREEN-tested before they ship. Flagship: the **docs-architecture** family — skills that set up, audit, and maintain AI-navigable project documentation.

Your docs become the agent's persistent memory: a thin always-loaded router (`CLAUDE.md`), a small set of charter'd reference docs, and an append-only journal — kept honest by audits that treat the code as ground truth.

## What you get

Four skills, shipped as standard [Agent Skills](https://agentskills.io) — authored and tested on Claude Code, loadable by any skills-compatible agent (see [Beyond Claude Code](#beyond-claude-code)):

| Skill | What it does | Reach for it when |
|---|---|---|
| [`docs-architecture-setup`](skills/docs-architecture-setup/SKILL.md) | Scaffolds the convention — a `CLAUDE.md` router plus charter'd reference docs — around whatever docs already exist | A new project, or an existing one with scattered, missing, or drifting docs |
| [`docs-architecture-audit`](skills/docs-architecture-audit/SKILL.md) | Verifies the reference docs still match the live code: a fan-out of audit workers converging on one merged, evidence-carrying flag list you adjudicate | After a refactor or rename; before trusting a doc as current; periodic doc-health pass |
| [`docs-architecture-maintain`](skills/docs-architecture-maintain/SKILL.md) | Sweeps the journal — the project's dated, append-only working notes (`docs/`, `NOTEBOOK.md`) — for findings that have hardened into standing truth and promotes them into the reference docs | The journal has accumulated; the reference docs feel behind it |
| [`whats-next`](skills/whats-next/SKILL.md) | Builds a prioritized what-to-work-on view from the ROADMAP, open follow-ups, and audit output | Session planning; "what should I work on next?" |

## Quick Start

Requirements: [Claude Code](https://claude.com/claude-code) — or any [Agent Skills](https://agentskills.io)-compatible agent, see [Beyond Claude Code](#beyond-claude-code) — plus `git` and `bash`.

```bash
git clone https://github.com/Apoplectic1/YetAnotherSkillsRepo.git
cd YetAnotherSkillsRepo
bash deploy.sh        # copies skills/*/ → ~/.claude/skills/
```

Then, in any project, ask Claude Code to **"set up this project's docs"** — the setup skill scaffolds the router and reference set around what already exists. From there, "audit the docs" and "what's next" trigger the rest of the family.

## Why docs-architecture?

- **AI agents are stateless.** Without a deliberate doc layer they re-read, re-grep, and re-derive what they knew yesterday, every session. These skills make the docs the memory: the router always loads, and everything else is one hop away by charter.
- **Docs written for humans drift silently.** Nothing forces them back to the truth until someone trusts a stale claim. The audit treats code as ground truth and requires evidence on every flag — a `file:line` citation or the literal `unverifiable → ask user` — and never guesses stale.
- **One careful read is not an audit.** In baseline testing, a single careful pass surfaced only about half the real issues ([benchmark](docs/2026-06-29-audit-model-benchmark.md)). The audit skill fans out per-section workers plus replicate rounds and loops until a round finds nothing new — then switches worker model, because one model's "done" is that model's ceiling, not the truth.
- **Skill text is tested, not vibed.** Every rule shipped RED→GREEN: watch an unguided agent fail, write the minimal text that fixes it, watch it comply ([design + provenance](docs/docs-architecture-design.md)).

## Updating

```bash
git pull
bash deploy.sh
```

Deploy stamps each copied skill with a marker and prunes any marker-carrying deployed dir whose source is gone — a renamed or removed skill can't leave a stale live copy, so re-running is always safe. Skills from other sources are never touched.

## Usage Notes

### Model selection

Audit workers default to **Sonnet at high effort** — benchmarked at per-pass parity with a frontier model, converging faster. When a model's rounds go dry, switching worker model finds more than running more rounds of the same model. Haiku / medium effort are a cheap first sweep only.

### Conventions assumed

The skills assume the convention they enforce: a `CLAUDE.md` router plus charter'd reference docs — run setup first and it creates them. The journal (dated notes, `NOTEBOOK.md`) is append-only and never currency-audited. Audits are router-anchored: what the router doesn't name is out of scope.

### Safety properties

The audit is report-only until you adjudicate each flag (approve / amend / defer), and it edits documentation only — a doc claim the code violates surfaces as a suspected *code* bug, never silently rewritten to match. Workers that die mid-run (transient API errors) are retried once, and any span still uncovered is named in a coverage note: a visible gap beats false completeness.

### Beyond Claude Code

The skills are standard [Agent Skills](https://agentskills.io) — an open format supported by Gemini CLI, OpenAI Codex, Cursor, GitHub Copilot, Goose, and [many others](https://agentskills.io/clients). `deploy.sh` is Claude Code's installer; for another tool, copy the same `skills/*/` folders into that tool's documented skills directory. Two things degrade gracefully there: the worker-model recommendations are Claude tiers (substitute your stack's strong/cheap equivalents), and the audit's fan-out assumes parallel subagents — without orchestration the passes run sequentially (slower, same convergence loop). One thing to adapt: setup scaffolds a `CLAUDE.md` router; if your tool auto-loads a different instructions file (e.g. `AGENTS.md`), point it at the router or mirror it.

## Repo layout

`skills/` is the product; everything else — `docs/`, `NOTEBOOK.md`, `openspec/` — is the open lab notebook: the RED/GREEN baselines, benchmarks, and design records behind every rule in the skill text (cited in skill footers by the author's local path; in this repo they live under `docs/`). The repo documents itself with the same convention the skills enforce.

The `openspec/` change records are planned with [OpenSpec](https://github.com/Fission-AI/OpenSpec) — spec-driven change workflows for AI coding, and the README whose shape this one borrows. Recommended.

## License

[MIT](LICENSE)

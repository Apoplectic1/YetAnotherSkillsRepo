# YetAnotherSkillsRepo

Claude Code skills, each validated against a test harness before it ships. Flagship: the **docs-architecture** family, skills that set up, audit, and maintain AI-navigable project documentation.

Your docs become the agent's persistent memory: a thin always-loaded router (`CLAUDE.md`), a small set of charter'd reference docs, and an append-only journal, kept honest by audits that treat the code as ground truth.

## What you get

Four skills, shipped as standard [Agent Skills](https://agentskills.io): authored and tested on Claude Code, loadable by any skills-compatible agent (see [Beyond Claude Code](#beyond-claude-code)). Each skill carries small Python scripts that do the counting and checking, so the skill text stays short and the agent spends its judgment on decisions, not inventories.

| Skill | What it does | Reach for it when |
|---|---|---|
| [`docs-architecture-setup`](skills/docs-architecture-setup/SKILL.md) | Scaffolds the convention, a `CLAUDE.md` router plus charter'd reference docs, around whatever docs already exist. Leans an overgrown router down to routing and gotchas: a rule that concerns certain files moves to a path-scoped rule file that loads only when such a file is touched, and a step-by-step procedure moves to a skill. Splits a reference doc that outgrows its budget into one file per topic, the doc becoming their index | A new project, or an existing one with scattered, missing, or drifting docs; a fat `CLAUDE.md` doing reference-doc work; a reference doc too big to read whole |
| [`docs-architecture-audit`](skills/docs-architecture-audit/SKILL.md) | Verifies the reference docs still match the live code: a fan-out of audit workers converging on one merged, evidence-carrying flag list you adjudicate. Also measures what every session loads before it starts, and offers a cheaper single-round run for a release check or a small doc set | After a refactor or rename; before trusting a doc as current; before a release; a periodic doc-health pass |
| [`docs-architecture-maintain`](skills/docs-architecture-maintain/SKILL.md) | Sweeps the journal, the project's dated, append-only working notes (`docs/`, `NOTEBOOK.md`), for findings that have hardened into standing truth and promotes them into the reference docs; rolls a journal that outgrows one file | The journal has accumulated; the reference docs feel behind it |
| [`whats-next`](skills/whats-next/SKILL.md) | Builds a prioritized what-to-work-on view from the ROADMAP, open follow-ups, and audit output | Session planning; "what should I work on next?" |

## Quick Start

Requirements: [Claude Code](https://claude.com/claude-code), or any [Agent Skills](https://agentskills.io)-compatible agent (see [Beyond Claude Code](#beyond-claude-code)), plus `git`, `bash`, and Python 3 (the scripts use the standard library only).

```bash
git clone https://github.com/Apoplectic1/YetAnotherSkillsRepo.git
cd YetAnotherSkillsRepo
bash deploy.sh        # copies skills/*/ into ~/.claude/skills/
```

Then, in any project, ask Claude Code to **"set up this project's docs"**: the setup skill scaffolds the router and reference set around what already exists. From there, "audit the docs" and "what's next" trigger the rest of the family.

## Why docs-architecture?

- **AI agents are stateless.** Without a deliberate doc layer they re-read, re-grep, and re-derive what they knew yesterday, every session. These skills make the docs the memory: a thin always-loaded router maps the doc set, one line per doc saying what lives there, so everything is one hop away at near-zero standing context cost.
- **Everything always loaded is paid for in every session.** Your global instructions, the routers of the folders above a project, and the project's own router all load before the first message. Setup keeps the project's share to routing and the traps worth knowing up front; the audit measures the whole chain, so a router quietly growing into a reference doc gets caught.
- **Docs written for humans drift silently.** Nothing forces them back to the truth until someone trusts a stale claim. The audit treats code as ground truth and requires evidence on every flag (a `file:line` citation or an explicit "unverifiable, ask the user") and never guesses stale.
- **One careful read is not an audit.** A single careful pass finds only about half the real issues. The audit fans out multiple workers over every section and keeps going until a round finds nothing new.
- **Disagreement runs both ways.** When a doc asserts a guarantee (must / always / never) and the code violates it, the audit reports the *code* as the suspect, filed into your project's own backlog, rather than quietly rewriting the doc to match broken behavior.

## Updating

```bash
git pull
bash deploy.sh
```

Deploy stamps each copied skill with a marker and prunes any marker-carrying deployed dir whose source is gone: a renamed or removed skill can't leave a stale live copy, so re-running is always safe. Skills from other sources are never touched.

## Usage Notes

### Model selection

An audit runs on two kinds of model, and maintain reuses the same fan-out.

- **Workers** read the docs section by section. They default to **Sonnet at high effort**, benchmarked at per-pass parity with a frontier model and converging faster. When a model's rounds go dry, switching worker model finds more than running more rounds of the same model. Haiku or medium effort is a cheap first sweep only.
- **The orchestrator** is the session you launch the skill from, so its model is the one you pick for that session. It reads less than the workers combined, but every flag passes through it: it merges and deduplicates the workers' flags, weighs each flag's evidence before you see the list, and writes the fixes you approve. Give it a frontier tier (Claude: Opus or above) at high effort or more. It must also be able to spawn parallel subagents and choose their model, which Claude Code does; without that, see [Beyond Claude Code](#beyond-claude-code).

### Conventions assumed

The skills assume the convention they enforce: a `CLAUDE.md` router plus charter'd reference docs; run setup first and it creates them. The journal (dated notes, `NOTEBOOK.md`, and a `CHANGELOG.md` for shipped history) is append-only and never currency-audited; a journal that outgrows one file rolls its oldest days into a directory beside it (`NOTEBOOK/`), indexed, every entry kept as written. A reference doc that outgrows its budget becomes an index with one file per topic in a directory beside it, and a citation of one of its sections still resolves by a search over both. Audits are router-anchored: what the router doesn't name is out of scope.

### Safety properties

Setup restructures, never destroys: every relocation, including the router lean and a doc split, is a content-preserving move on a clean git tree, landed as a reviewable commit. The scripts only report, except the two that move text (the doc split and the journal rollover), which run dry by default and check that every byte landed. The audit is report-only until you adjudicate each flag (approve / amend / defer), and it edits documentation only: a doc claim the code violates surfaces as a suspected *code* bug, never silently rewritten to match. Workers that die mid-run (transient API errors) are retried once, and any span still uncovered is named in a coverage note: a visible gap beats false completeness.

### Beyond Claude Code

The skills are standard [Agent Skills](https://agentskills.io), an open format supported by Gemini CLI, OpenAI Codex, Cursor, GitHub Copilot, Goose, and [many others](https://agentskills.io/clients). `deploy.sh` is Claude Code's installer; for another tool, copy the same `skills/*/` folders into that tool's documented skills directory. Some things degrade gracefully there: the worker-model recommendations are Claude tiers (substitute your stack's strong and cheap equivalents), the audit's fan-out assumes parallel subagents (without orchestration the passes run sequentially: slower, same convergence loop), and the path-scoped rule files setup writes under `.claude/rules/` load automatically only in Claude Code (elsewhere they are plain files the router names, read on demand). One thing to adapt: setup scaffolds a `CLAUDE.md` router; if your tool auto-loads a different instructions file (e.g. `AGENTS.md`), point it at the router or mirror it.

## Repo layout

**`skills/` is the product: each skill's `SKILL.md` and the scripts beside it. Installing it is all you need.** Everything else is the development workshop behind it and can be ignored by users: `docs/` holds the design records and test evidence behind every rule in the skill text, and `harness/` holds *fictional* fixture projects with deliberately planted defects (test targets for the skills, not templates or examples to copy). `openspec/` holds change-planning records, made with [OpenSpec](https://github.com/Fission-AI/OpenSpec), recommended, and the README whose shape this one borrows.

## License

[MIT](LICENSE)

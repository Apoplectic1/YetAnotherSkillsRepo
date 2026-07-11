# Design: publish-to-github

## Context

The GitHub repo `Apoplectic1/docs-architecture` exists and is empty. This local repo is the source of truth (user convention: local disk = truth, GitHub = distribution). The old README was dissolved 2026-07-10 into DOMAIN/ARCHITECTURE with a fresh public README explicitly deferred to publish time. The user named the OpenSpec README (github.com/Fission-AI/OpenSpec) as the style exemplar and asked for three of its sections adapted: "Why OpenSpec", "Updating OpenSpec", "Usage Notes". The OpenSpec README's full structure was fetched 2026-07-10 for grounding: hero + philosophy line, "see it in action", Why-teams-adopt, Quick Start, docs links, **Why OpenSpec?** (problem-focused bullets, "predictability without the ceremony" voice), comparison, **Updating** (procedural two-step: upgrade package, refresh instructions), **Usage Notes** (advisory subheadings: model recommendations, context hygiene, supported tools), contributing/license tail.

## Goals / Non-Goals

**Goals:**
- A root `README.md` that lets a stranger understand, install, update, and correctly use the four skills — in OpenSpec's direct, problem-first voice, with the three requested sections as the backbone.
- MIT `LICENSE`, remote wiring, `main` pushed — repo publicly usable in one pass.
- Future audits treat README correctly (router names it as public-facing, outside the charter'd reference set).

**Non-Goals:**
- No demo GIF/animation in v1 (candidate follow-up; house recipe exists — ffmpeg two-pass palette). No badges (no CI, no package registry). No npm/package distribution — install is clone + deploy. No rewrite of internal docs for public consumption: the journal/openspec trail publishes as-is, framed as provenance. No `dev` branch push.

## Decisions

1. **README structure** (mapped from the fetched OpenSpec skeleton; three requested sections bolded):

   | # | Section | Content |
   |---|---------|---------|
   | 1 | Hero | `# docs-architecture` + one-liner ("Claude Code skills that set up, audit, and maintain AI-navigable project documentation") + one philosophy line (docs as the agent's persistent memory: a thin always-loaded router + charter'd reference docs + an append-only journal). |
   | 2 | What you get | The four skills in a table — `docs-architecture-setup` / `-audit` / `-maintain` / `whats-next`, one row each: what it does, when it triggers. |
   | 3 | Quick Start | Requirements (Claude Code with skills support); install: `git clone` → `bash deploy.sh` (copies `skills/*/` → `~/.claude/skills/`); first run: "ask Claude to set up your project's docs" → SETUP scaffolds router + reference set. |
   | 4 | **Why docs-architecture?** | Problem-first bullets in the OpenSpec voice: agents re-derive project knowledge every session; docs written for humans drift silently until trusted and wrong. Evidence-backed differentiators (from the repo's own benchmarks): a single careful audit pass finds only ~half the real issues — the audit skill fans out and converges coverage; skill text is RED/GREEN-tested against baseline agent behavior, not written on vibes. |
   | 5 | **Updating** | Procedural, two steps like OpenSpec's: `git pull` → `bash deploy.sh`. One-line note: deploy stamps markers and prunes renamed/removed skills, so re-running is always safe. |
   | 6 | **Usage Notes** | Advisory subheadings mirroring OpenSpec's: *Model selection* (audit workers default Sonnet at high effort — benchmarked at per-pass parity with frontier models; model diversity beats same-model repetition; a haiku/medium pass is a cheap first sweep only); *Conventions assumed* (a CLAUDE.md router + charter'd reference docs — SETUP creates them; the journal is append-only and never currency-audited); *Safety properties* (audit is report-only until you adjudicate; code findings are never auto-applied; dead workers are retried and surfaced in a coverage note). |
   | 7 | Repo layout | Two-sentence orientation: `skills/` is the product; everything else (`docs/`, `NOTEBOOK.md`, `openspec/`) is the open lab notebook — the RED/GREEN provenance behind every rule in the skill text. |
   | 8 | License | MIT. |

2. **"Updating" maps to pull+deploy, not a package manager** — there is no registry artifact; the repo IS the distribution. Alternative considered (publish a zip/release per version): rejected for v1, adds release ceremony with no consumer demand yet.
3. **MIT license** — user-selected over Apache-2.0/none (2026-07-10 AskUserQuestion).
4. **Remote + push mechanics** — prefer `gh` if authenticated (`gh repo view Apoplectic1/docs-architecture` to verify, HTTPS remote via `gh`), else plain `git remote add origin https://github.com/Apoplectic1/docs-architecture.git`; `git push -u origin main`. `main` only: it is the distribution-ready ref (RELEASING.md); `dev` remains local authoring. Wording rule: this is *publishing a mirror*, not moving the repo's home.
5. **Router line, not a charter** — CLAUDE.md's "Excluded from the doc set" list gains `README.md — public GitHub-facing distribution artifact; not a reference doc`. Alternative (add README to the reference set with its own charter): rejected — it would drag marketing copy into every currency audit; README intentionally cites evidence docs rather than duplicating claims, which keeps its drift surface small.
6. **README authored on `dev`, shipped via the normal dev→main merge** — same flow as skill changes; the push to GitHub happens from `main` after merge.

## Risks / Trade-offs

- [Public history is irreversible] → the push is the last task, explicitly separated, run only after README/LICENSE are reviewed on `main`; everything before it is local and reversible.
- [README drift vs. skills] → README is outside the audited reference set by design; mitigated by linking to skill files/evidence docs instead of restating their numbers, and keeping product claims in section 4 few and sourced.
- [Internal absolute paths (`E:\Projects\...`) visible in published docs] → inert; accepted as part of publishing the lab notebook honestly. Not scrubbed (rewriting history would falsify provenance).
- [OpenSpec-style sections imply OpenSpec-scale polish] → scope guarded by Non-Goals: no badges/GIF/comparison table in v1.

## Open Questions

(none — license and section scope resolved with the user 2026-07-10)

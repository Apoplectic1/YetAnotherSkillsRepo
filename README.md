# Docs-Architecture Skills

Four global [Claude Code](https://claude.com/claude-code) skills for keeping a project's
documentation **AI-navigable, current, and single-sourced** — so an agent works in any project the
same way and can *trust* what it reads. Built for a solo dev maintaining a portfolio ("constellation")
of related projects, but they apply to any repo.

---

## Honest TL;DR — read this first

- **They don't make the AI *smarter* at judging your docs.** Testing (RED baselines) showed a capable
  agent already does the per-item judgment well unguided. The skills' real value is
  **completeness, consistency, and trustworthy structure** — the same doc layout in every project,
  outputs that don't quietly miss things, and a manifest of what was/wasn't checked.
- **SETUP is the keeper** — cheap, one-time, high-ROI. Adopt unconditionally.
- **AUDIT / MAINTAIN / whats-next are occasional power tools.** Each fans out several subagents (real
  token cost). Use them at *decision points*, not as a routine ritual. Running them out of obligation
  is process-theater.
- **They do NOT validate cross-project dependencies/contracts.** That is the job of *tests* and the
  *compiler*, not docs. See [What this is not](#what-this-is-not).
- **Stale docs are worse than none** (the agent trusts them). These *help* you stay current; they
  don't do it for you. Adopt only if you'll keep docs current.

---

## The model it assumes

Only `CLAUDE.md` (plus the global `~/.claude/CLAUDE.md` and a tiny memory stub) auto-loads into an
agent's context each session; **everything else is pull-on-demand.** So `CLAUDE.md` is a **router**,
and your docs are "accessible" exactly to the degree it indexes them.

**The canonical doc set** (per project) — each opens with a one-line **charter** (purpose / when to
read), and is *never blank*:

| File | Role |
|---|---|
| `CLAUDE.md` | always-loaded **router** + load-bearing gotchas |
| `ARCHITECTURE.md` | how it works (subsystem mechanics) |
| `ROADMAP.md` | forward plan + a short "Recently shipped" digest |
| `NOTEBOOK.md` | running lab journal (chronological findings) |
| `VERIFICATION.md` | how to build/run/test/verify a change |
| `DOMAIN.md` | the human/strategy home (science/conventions/site-process/UI rules) |
| `docs/YYYY-MM-DD-*.md` | dated journal: decision records, reviews |
| `README.md`, `RELEASING.md` | conditional (public entry / ships) |

**Three tiers:** *journal* (dated capture — `docs/` + `NOTEBOOK`) → *reference* (current truth —
`ARCHITECTURE` / `ROADMAP` / domain / `VERIFICATION`) → *cold-rationale* (evergreen "why", parked off the daily path).
**Git is the changelog** — no `CHANGELOG.md`. Routing is by **convention** for the journal
(`glob docs/*.md` + grep) and **by name** for the small, stable reference set.

---

## The four skills

Each entry: **what it is · does · does *not* do · when · how**.

### 1. `docs-architecture-setup` — the spine (adopt unconditionally)
- **Is:** bootstraps or standardizes a project's doc skeleton.
- **Does:** creates the canonical set (charter-guarded), writes `CLAUDE.md` as a router, normalizes
  drifted filenames to the convention, respects scope-exclusions, and is **non-destructive**
  (restructure/merge/rename — never delete; clean tree + review the diff before commit). **Idempotent**
  — safe to re-run on an existing project to re-converge it.
- **Does NOT:** judge whether content is *correct or current* (that's AUDIT); write your content for
  you (thin-but-charter'd is the right state for a new project); recurse into sub-projects or vendored
  trees (flags-and-skips a nested project — run it from there).
- **When:** a new project; an existing one with no router / scattered docs / inconsistent names;
  onboarding a project into a portfolio that shares this convention.
- **How:** invoke the skill; it surveys the tree, scaffolds the canonical set (domain doc is always
  `DOMAIN.md`), and routes.

### 2. `docs-architecture-audit` — drift catcher (occasional)
- **Is:** checks docs against reality on two axes — **placement** (does a section match its doc's
  charter?) and **currency** (does each claim still match the live code?).
- **Does:** fans out independent passes + a cross-reference pass, merges + dedupes, **loops until
  dry**; every currency flag carries a `file:line` citation or `unverifiable → ask`; classifies
  **descriptive** (code wins → fix the doc) vs **prescriptive** (plan wins → code-absence isn't
  staleness); emits evidence-carrying flags → you adjudicate → fix.
- **Does NOT:** auto-edit (it proposes; you decide); **validate cross-project contracts** (it checks a
  doc against *its own* code only); guarantee full coverage in a *single* pass (different passes find
  different subsets — hence loop-until-dry); audit the journal or `archive/`.
- **When:** after a refactor/rename; before you trust a doc for a real decision; a periodic health
  check. Token-heavy → **not** every session.
- **How:** invoke; it orchestrates the fan-out and returns the merged flag list.

### 3. `docs-architecture-maintain` — graduate & prune (occasional; needs a journal)
- **Is:** promotes hardened findings out of the journal into the reference tier, then prunes the
  source so nothing duplicates.
- **Does:** classifies each journal item **graduate / keep / archive / prune-only**; every `graduate`
  carries a **disposition** (`stub` / `cross-ref` / `archive`) that **preserves the why/when**;
  reuses AUDIT's fan-out for completeness.
- **Does NOT:** do anything useful if you keep **no journal** (nothing to graduate); graduate *into* an
  already-bloated reference doc (that's a SETUP/AUDIT *split* job first); delete the dated record
  (graduate-without-prune = duplication; prune-by-deletion = lost why — it does neither).
- **When:** periodically, once `docs/` + `NOTEBOOK.md` have accrued findings worth consolidating.
- **How:** invoke; fan-out → flags → adjudicate → apply.

### 4. `whats-next` — backlog triage (occasional; the planning layer)
- **Is:** answers *"what should I work on next?"* in a way you can trust.
- **Does:** sweeps **every** backlog source (working tree, ROADMAP futures/limitations, gotchas,
  journal pending-items, code `TODO`/`FIXME`, OpenSpec, audit findings, cross-repo blockers);
  separates **live-actionable** from **accepted-constraint** (so it doesn't cry wolf on every
  by-design gotcha); returns a categorized/prioritized backlog **+ a coverage manifest** (what it
  swept / couldn't) **+ an accepted-constraints list**.
- **Does NOT:** decide for you (it *proposes* priority; you own the call); confirm the items are still
  *true* (run AUDIT first — stale docs → stale backlog); replace your judgment on sequence.
- **When:** planning a session; building a backlog; "am I seeing everything?"
- **How:** invoke; fan-out → manifest + prioritized backlog.

---

## How they compose

```
SETUP  (once / per new project)
  │   establishes the structure every other skill relies on
  ▼
AUDIT  (when drift is suspected — refactor, rename, "can I trust this doc?")
  │   currency-checks first, so the backlog below isn't built on stale claims
  ▼
MAINTAIN  (periodically, as the journal accrues)
  ▼
whats-next  (when planning — composes AFTER audit)
```

---

## What this is *not*

- **Not a cross-project contract validator.** These are doc-hygiene *per project*. Validating
  "consumer A's assumption about a shared library's API still holds" belongs to **tests**
  (consumer-driven contract tests), the **compiler/build** (a structural continuity check, free in a
  typed language), and **one constellation-level dependency map** — *not* these skills. Docs
  *describe* contracts; tests *validate* them.
- **Not a substitute for deciding or designing.** Documenting a design does not validate it.
- **Not a daily ritual** (except SETUP's always-on output). The fan-out skills earn their token cost
  at decision points only.

---

## Install / deploy

Source of truth is **this repo** (version-controlled). Deploy to the live location with:

```bash
bash deploy.sh        # copies skills/*/ → ~/.claude/skills/
```

**Copy, not symlink/move:** the deployed copy is a disposable build artifact — **edit skills here**,
then re-run `deploy.sh`. Never edit `~/.claude/skills/` directly. Branches: `dev` (authoring),
`main` (distribution-ready).

---

## How they were built (for anyone extending them)

Authored with the `superpowers:writing-skills` discipline — **TDD for documentation**: RED (watch an
*unguided* agent attempt the task and see how it falls short) → write the skill → GREEN (watch a
guided agent comply) → REFACTOR (close the gap the test revealed). Two hard-won method lessons are
baked into the design:

- **Validate a skill on a project it was *not* derived from.** The source project is a poisoned
  fixture — either already-conformant (so nothing fails) or it literally contains the spec (so an
  "unguided" agent just reads it). Both happened here; a sibling project was the clean test.
- **Disk-verify agent claims.** A validation pass once asserted a broken reference that `grep`
  showed was already fixed. Trust the disk, not the claim.

Full design rationale, the tier model, and per-skill RED/GREEN provenance:
[`docs/docs-architecture-design.md`](docs/docs-architecture-design.md).

---

## Cost, honestly

`SETUP` is cheap (one-time, light upkeep). `AUDIT` / `MAINTAIN` / `whats-next` each spawn several
subagents per run — real tokens, well spent at a decision point, wasted as routine. The doc structure
itself is **low-maintenance by construction** (git-as-changelog, convention-routing, charter-guards),
which is the main defense against the stale-docs-are-worse-than-none failure mode.

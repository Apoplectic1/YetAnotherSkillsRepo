---
name: docs-architecture-setup
description: Use when bootstrapping or standardizing a project's documentation for AI navigation — a new project, or an existing one with no CLAUDE.md router, scattered/missing docs, or inconsistent ARCHITECTURE/ROADMAP. Also when onboarding a project into a portfolio that shares a doc convention.
---

# Docs-architecture setup

Bootstrap a project so an agent navigates it the same way as every other: one always-loaded
`CLAUDE.md` **router** pointing to a canonical, **charter-guarded** doc set. The set is a rule,
never inferred from sibling repos. `python survey.py <dir>` (beside this SKILL.md) reports the
tree against the rules below, one line per finding with the rule it keys; the plan acts on its
lines, and on the tests only a reader can make (S5's honesty, S7's content, S8's scope).

## Safety (highest priority)
- **S1.** Consolidating = **merge** (drop nothing); moving history = **move**, not delete;
  a rename keeps content. Unsure whether something is still needed: `archive/`, never delete.
- **S2.** Apply on a **clean git tree** (commit first) and **present the diff for review
  before committing**.
- **S3.** Not a git repo? **Create the net first**: `git init` + commit the originals (or
  snapshot them to `archive/pre-setup/`) before any restructuring. A pure scaffold (new files
  only) may proceed, noting the tree is unversioned.
- **S4.** A large or diverse project: survey fully before touching anything; several small
  reviewed applies over one big one.

## The enforced set: every file, charter-guarded
| File | Role |
|---|---|
| `CLAUDE.md` | always-loaded **router** + the gotchas every session needs (S7, S8) |
| `ARCHITECTURE.md` | subsystem mechanics (how it works) |
| `ROADMAP.md` | forward-looking design + a short Recently-shipped digest |
| `NOTEBOOK.md` | running **lab notebook** (dated findings); rolls into `NOTEBOOK/` past its budget (T1) |
| `VERIFICATION.md` | how to verify a change, even if just "= `dotnet test`, CI at X" |
| `DOMAIN.md` | the human/strategy home (science, conventions, site process, UI rules) |
| `docs/` | journal: dated records, `YYYY-MM-DD-<slug>.md` or the pattern the router states (B2) |
| `CHANGELOG.md` | **conditional**: shipped history (append-only, dated, newest first), created when history accrues; rolls like NOTEBOOK |
| `README.md`, `RELEASING.md` | **conditional**: public entry point; a project that ships |

- **S5.** **Charter-guard:** every file opens with a one-line charter (purpose, when to read).
  A thin file states an honest status ("verification = the test suite"; "no subsystems yet"),
  **never blank**. NOTEBOOK and VERIFICATION are the two files runs omit: create them.
- **S6.** The domain doc is **always named `DOMAIN.md`**: never elicit a content-specific
  name, never rename an existing one; whatever the content is lives there; absent, create it
  charter'd-thin.
- **S7.** **Lean an encountered fat router in this run:** reference content inside
  `CLAUDE.md` (glossary, contract/API prose, conventions, subsystem mechanics: anything
  neither routing nor a load-bearing gotcha) **moves now** to its charter home (glossary and
  authoring conventions to `DOMAIN.md`; mechanics and contracts to `ARCHITECTURE.md`) as an
  S1 move with a router pointer where needed, each move named in the run report. The trigger
  is **content, never size**: a gotcha-dense router stays, a small glossary still moves; a
  hybrid block splits (the gotcha line stays, the body moves). B2 forbids overwriting an
  existing setup, not relocating its off-charter weight: "noted as a follow-up" is the job
  left undone.
- **S8.** **Always-on is a scope, not a size.** An item loads at launch (the router, an
  ancestor router, a `.claude/rules/` file without `paths:`) only if it passes **breadth**
  (every session launched here needs it) and **stability** (it changes less often than a
  release); that test is what "load-bearing" means. S7 decides *where* a thing lives; this
  decides *whether it loads every time*. A block or line that fails **moves now** behind one
  always-on trigger line, to the home its need is keyed to: files in this repository → a
  **path-scoped rule file** (`.claude/rules/<name>.md` with `paths:`; it loads on a matching
  file's first touch, so never for a command-only session and never for a sibling
  repository's files); an activity (a build, a bench run, a release step) → a **skill**
  (`.claude/skills/<name>/SKILL.md`, loaded on invocation; B1 allows it); prose → a
  reference-doc **section** read by heading; keyed to neither → one router line. The trigger
  line names the home and when to reach for it; the router names every rule file and skill it
  writes. **The budget is per file, 200 lines:** the survey's chain row (`chain_budget.py`)
  marks each file over its own line and reports the ancestors' and the owner's shares as
  theirs, never chased from below. **The number detects, the test decides:** a router under
  its line still moves a block that fails.

## Tiers & routing: teach these in CLAUDE.md
- **T1.** **journal** (dated capture) = `docs/YYYY-MM-DD-*.md` + `NOTEBOOK.md` +
  `CHANGELOG.md`. Past its budget (40 KB) a journal's oldest whole days roll by date into a
  directory named for it (`NOTEBOOK/`, `CHANGELOG/`; the maintain skill's `rollover.py`,
  with an `INDEX.md`). Three-way split: a small finding from the work → NOTEBOOK; a
  **shipped unit → CHANGELOG**; a substantial standalone record → `docs/`.
- **T2.** **reference** (current truth) = ARCHITECTURE / ROADMAP / DOMAIN / VERIFICATION,
  edited in place.
- **T3.** **cold rationale** (optional) = lengthy, cold *and* evergreen "why" → a dated
  `docs/` note + a one-line reference back; all three or it stays put.
- **T4.** The router names reference docs **by name** and the journal **by convention**
  (`glob docs/*.md` + grep), never an enumerated list; its journal line states the
  dated-record pattern and that a dated citation ("NOTEBOOK 2026-01-22") or a section
  citation ("ARCHITECTURE § Build chain") resolves by grep over the file and its directory.
- **T5.** **A reference doc past its budget splits by topic, never by judgment:** the survey
  marks one (40 KB, many `##` topics), and a run's own moves can push one past it; `python
  split_doc.py <doc>` (beside this SKILL.md; a dry run first, then `--apply`; `--reindex`
  after a part is edited) moves each `##` section
  byte for byte into a directory named for the doc, one charter'd file per topic, the doc
  left as the index; the router keeps naming the doc. Never below `##`. Not this rule: cold
  rationale extracts (T3), a design slot stays whole (B5), a journal rolls (T1; the script
  refuses it).

## archive/ and the changelog
- **A1.** `archive/` is **archival-only**: not current-design-relevant, deletable (git is
  the backstop). Still current? It stays live.
- **A2.** **Shipped history lives in `CHANGELOG.md`**; `ROADMAP.md` keeps a short
  Recently-shipped **digest + pointer**, never a long history, and `archive/` never holds
  shipped history. Relocating an embedded history is an S1 move.

## Boundaries (the survey names the shape; the rule is the action)
- **B1.** **Never scaffold into** vendored trees (`vendor/`, `third_party/`, forked
  upstreams), generated output (`bin/`, `obj/`, `dist/`, `target/`) or tooling (`.claude/`,
  `openspec/`); their READMEs are not this project's docs. The router notes them excluded
  and marks archived openspec design docs (`changes/archive/*/design.md`) as records the
  **maintain** sweep reads. Under `.claude/` only what S8 moves there, a rule file or a
  skill, each named by the router.
- **B2.** **Coexist, never clobber:** augment an existing setup, never overwrite a present
  `CLAUDE.md`, `openspec/` or `.claude/`. Normalize filenames to the **project's stated**
  dated-record pattern (the router's journal line; the default is `YYYY-MM-DD-<slug>.md`),
  align casing; never impose the default over a pattern the project states (a rename breaks
  every citation of the file: S1 reaches names).
- **B3.** A **sub-project** (its own router or `.git`) is its own unit: **flag-and-skip**,
  note it excluded in the root router, report "run this skill from `<sub-dir>`". Not a
  submodule or vendoring call.
- **B4.** A **container root** (no first-party content: sub-projects and tooling only) gets
  the **router plus at most two thin portfolio docs**, never the rest of the set: a portfolio
  `DOMAIN.md` chartered *cross-repo truth only* (shared terms, cross-store disambiguations,
  cross-repo contracts by pointer), created when such truth exists (the S7 lean surfaces it),
  never by default; and a thin status `ROADMAP.md`. **Owner rule:** what one project's code
  defines lives in that project's docs; the portfolio DOMAIN points *down* by name,
  sub-projects point *up*, **never mutual**. Leaning a container router sends cross-repo
  reference prose here, not to ROADMAP and not kept as router prose (a one-line
  disambiguation gotcha may stay).
- **B5.** **Design-heavy, code-light:** a large standalone design doc **is the project's
  DESIGN slot**. Keep it whole: charter it, route it by name, scaffold the rest
  charter'd-thin pointing into it ("mechanics live in `<doc>` §N until code lands"); it
  graduates into ARCHITECTURE/ROADMAP as code arrives (a later MAINTAIN job). Never split,
  relocate or archive it.
- **B6.** A container root's `.gitignore` **names each nested repository** (`/alpha/`, a
  reason per line), never a wildcard (`/*/` plus exceptions), which silently drops a new
  directory. On encounter, rewrite by name in the run (the same directories stay out; a
  comment only on a line of its own).

## Procedure
1. `python survey.py <dir>`: the shapes (B3 to B6), the set and each charter, what the
   router names and notes, the chain row, journals and reference docs past budget, embedded
   history, the ignore file, the git state. Act on its lines; the content tests are yours.
2. **Create/align** the enforced set, charter-guarded (S5, S6).
3. **Write `CLAUDE.md`** as the router (T4; exclusions noted; the gotchas every session
   needs: S8).
4. **Don't force content**: thin-but-charter'd is correct for a new or sparse project.

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md

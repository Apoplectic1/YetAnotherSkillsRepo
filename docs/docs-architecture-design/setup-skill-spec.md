# docs-architecture-design: SETUP-skill spec (Phase 3 design — grounded in target projects) (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § SETUP-skill spec (Phase 3 design — grounded in target projects)" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## SETUP-skill spec (Phase 3 design — grounded in target projects)

Grounded 2026-06-28 in a survey of the projects the skills will first run on (sibling C#/.NET
Astronomy projects + this one): **TargetPlanner (TP)**, **TargetSchedulerManager (TSM)**,
**Library** (shared, multi-consumer), **XisfFileManager (XFM)**, **IntervalScheduler (IS)**,
**WBPP** (the genesis project). Enforce the *shape*, not a rigid filename list:

> **Derivation snapshot (2026-06-28) — historical record.** The survey rows and target
> statements below describe the constellation as it stood at derivation. It has since
> converged via SETUP runs: TSM `0b61237` 2026-06-28 (incl. `UI-CONVENTIONS`→`DOMAIN.md`);
> Library `337f081` 2026-06-28 + a full applied AUDIT + charter'd-thin `DOMAIN.md`
> (`275527c` 2026-07-07); TP `e20d401` 2026-07-07; XFM full set on disk, journal now
> date-prefixed; WBPP's `OBSERVING.md` still pending its re-run. **Current truth lives in
> each project's own docs — do not re-derive it from these rows.** (Stamped by the
> 2026-07-10 self-audit. Nuance: Library shows no `docs/` dir — git can't track an empty
> directory, so an enforced-but-empty journal dir has no on-disk existence until used.)

**Enforce the canonical filename SET, not just the principles** (user directive 2026-06-28):
consistent names across projects are what make switching frictionless — `ARCHITECTURE.md` is
*always* the deep-dive; `VERIFICATION.md` *always* answers "how do I verify a change here." So
SETUP creates the full named set every time (charter-guarded — see reconciliation below), with
only README/RELEASING genuinely conditional *(container roots excepted — router-only; encoded
2026-07-07)*.

| Doc | Enforcement | Survey evidence / note |
|---|---|---|
| `CLAUDE.md` (router) | **enforced — universal** | the router; in all 5 already |
| `ARCHITECTURE.md` | **enforced by name** | **Library + XFM lack it** (180 / 77 .cs) → scaffold (charter-guarded if thin) |
| `ROADMAP.md` | **enforced by name** | all 5 have it |
| `NOTEBOOK.md` | **enforced by name** | the lab-notebook home — present even if empty (charter'd; invites use as findings accrue) |
| `VERIFICATION.md` | **enforced by name** | always answers "how do I verify a change here" — even when that's just "= `dotnet test`, CI at X" (so it's useful for the test-backed apps too, *revising* the earlier "conditional") |
| `docs/` + `YYYY-MM-DD-*` journal | **enforced — the tier** | all have `docs/`; convention varies (TP subdirs, XFM **undated**) → standardize |
| `DOMAIN.md` (domain/strategy doc) | **enforced by name — always `DOMAIN.md`** | name **fixed** 2026-07-07 (superseded the elicited-name model); existing per-project docs — TSM `UI-CONVENTIONS`, Library `PCL InterOp`, WBPP `OBSERVING` — predate the rename, untouched until re-run |
| `README.md` | conditional (public/GitHub entry) | distinct audience from CLAUDE.md; TP has one |
| `RELEASING.md` | conditional (project ships) | TP has one |

**Domain-doc name fixed to `DOMAIN.md` (user, 2026-07-07).** Superseded the original *elicited,
content-specific* name (OBSERVING / UI-CONVENTIONS / PCL InterOp). A single canonical filename
makes cross-project switching frictionless (same rationale as the rest of the enforced set) and
drops a per-run naming prompt; SETUP now always creates/keeps `DOMAIN.md` and never renames an
existing one. Per-project domain docs already under other names predate this and stay untouched
until each project is re-run.

**Hard scope-exclusion list — the key new requirement the survey surfaced.** SETUP never
scaffolds into, and AUDIT never scans: **vendored** trees (Library `PCL/` + its `3rdparty/`
lz4/zstd, each with their own READMEs; WBPP `nsg-v8-fork/`), **generated** artifacts
(`BenchmarkDotNet.Artifacts`, `bin`/`obj`), and **tooling** dirs (`.claude/`, `.superpowers/`,
`openspec/`). Without this, an audit of Library drowns in vendored docs.

**Adopted (AUDIT) — router-anchored scope (surfaced by the WBPP re-apply, 2026-06-28; shipped
in AUDIT's Scope section).**
A flat dir-glob exclusion is too coarse: a vendored tree can hold a *router-listed project doc*
(`nsg-v8-fork/NOTICE.md` is the fork's own playbook, in the router — but the Library `PCL/`
READMEs are *not*). Better rule: **in-scope iff the router names it** (∪ the canonical set ∪ the
journal convention); the vendored/generated/tooling exclusions become the *default for unrouted
files*, not a hard wall. This dissolves the "excluded-tree-with-an-included-leaf" case. Pairs
with the **re-fork lifecycle**: fork *source* = read-only ground-truth (AUDIT currency-checks
references *against* it, never edits it); the fork *playbook* (router-named) = a maintained doc.
*(Status 2026-07-06: AUDIT's Scope section ships router-anchored scope — this gate-note had gone
stale; SETUP keeps the flat exclusion list, correct for bootstrap since the router doesn't exist
yet when SETUP runs.)*

**Sub-projects vs vendored — distinct cases (user policy, 2026-06-28).** *Vendored* = third-party
(exclude the source; keep only router-named leaves correct, per above). A *sub-project* is the
user's OWN nested project with its own governance — detect it by its **own router / `.git`**.
Policy: **the root project's `.md` suite governs the whole tree**; SETUP does **not** scaffold a
canonical set into every sub-dir, and a root run **never reaches into a sub-project to restructure
its docs**. On encountering a sub-project it **flags-and-skips** (reports it + any unconventional
names) and notifies the user to **run the skill from the sub-project's dir** to govern it as its
own unit. Cross-boundary references (root↔sub) are kept correct/consistent. Clean per-sub-project
recursion *from* the root is an acceptable **future** enhancement, but flag-and-skip is the safe
v1. *(Status 2026-07-06/07: AUDIT had already shipped flag-and-skip; SETUP's side is now encoded
after RED→GREEN — baseline no-touch held 4/4, but 0/4 gave the run-from-sub-dir redirect, so SETUP
gained the structural flag-and-skip + redirect line. See the fix-batch behavioral record in § The phased arc.)*

**Coexist, never clobber:** TSM already has `openspec/` + opsx + `.superpowers/sdd/`; TP has
`.claude/skills/verify-ui`. SETUP augments an existing setup.

**Enforce names, not content — the charter-guard reconciliation.** Enforcing the full named set
is what makes switching projects frictionless; the empty-stub worry is resolved by the **charter
line** — an enforced file is *never blank*. It carries its purpose + either content or an honest
status ("verification = `dotnet test`"; "no subsystems yet"). A thin charter'd file is *legible*
("nothing substantial here yet") and a ready home the moment content accrues — not hollow. So
SETUP **creates the full set every time**, charter-guarded; content scales with the project.

**Project-shape variance SETUP must handle:** the survey spans populated apps (TP 95 .cs), a
multi-project lib (Library 180 .cs / 11 projs), and a **design-heavy / code-light** project
(**IS**: 3 .cs but a **75 KB `SCHEDULER_DESIGN.md`** + stub ARCHITECTURE/ROADMAP). So SETUP must
not assume code-rich — a big standalone design doc is architecture-in-waiting: treat it as the
project's **DESIGN slot** — keep it whole under its existing name and route it by name (the
seed that graduates into ARCHITECTURE/ROADMAP as code lands), don't force-split it.
VERIFICATION is enforced even pre-code (charter'd-thin; the earlier "moot pre-code" position
was revised — see the enforced-set table).

**First customers / killer demo:** TP's **125 KB ROADMAP + 70 KB ARCHITECTURE** (and Library's
33 KB ROADMAP) are the pre-split WBPP state → the SETUP+AUDIT skills' first real targets, TP the
lean/split demo. XFM is critical/daily-use (*upstream* of WBPP's XFM keyword contract; a
Library migration was then thought imminent — per Library's `CONSUMERS.md` it remains
aspirational, zero references), so cross-project doc consistency there compounds.


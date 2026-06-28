---
name: docs-architecture-setup
description: Use when bootstrapping or standardizing a project's documentation for AI navigation — a new project, or an existing one with no CLAUDE.md router, scattered/missing docs, or inconsistent ARCHITECTURE/ROADMAP. Also when onboarding a project into a portfolio that shares a doc convention.
---

# Docs-architecture setup

## Overview
Bootstrap a project so an agent navigates it the **same way as every other project**: one
always-loaded **router** (`CLAUDE.md`) pointing to a **canonical, enforced doc set**, each file
**charter-guarded** (never blank). **Carry the set as a rule** — do NOT infer it from sibling
repos (a sibling may not exist, and inference drifts between projects).

## Safety — never lose existing documentation
SETUP **restructures; it does not destroy.** Consolidating = **merge** (drop nothing); moving
history = **move**, not delete; renames preserve content. If unsure whether something is still
needed → **move it to `archive/`**, never delete. Run the apply on a **clean git tree** (commit
first) so every change is recoverable, and **present the diff for review before committing.** A
large/diverse project (many existing docs) is a *later* target, not a first one — prove the skill
on a small project first.

## The enforced set — create every one, charter-guarded
| File | Role |
|---|---|
| `CLAUDE.md` | always-loaded **router** + load-bearing gotchas (kept thin) |
| `ARCHITECTURE.md` | subsystem mechanics (how it works) |
| `ROADMAP.md` | forward-looking design + a short "Recently shipped" digest |
| `NOTEBOOK.md` | running **lab notebook** (chronological empirical findings) |
| `VERIFYING.md` | how to verify a change — *even if* just "= `dotnet test`, CI at X" |
| domain doc (**elicit its name**) | the human/strategy home (e.g. `OBSERVING` / `DOMAIN` / `UI-CONVENTIONS`) |
| `docs/` | journal: `YYYY-MM-DD-<slug>.md` per-topic dated records |
| `README.md`, `RELEASING.md` | **conditional** — public/GitHub entry; project that ships |

**Charter-guard:** every file opens with a one-line charter (purpose / when to read). A thin file
states an honest status ("verification = `dotnet test`"; "no subsystems yet") — **never blank**. A
charter'd-thin file is legible and a ready home; a blank file is noise.

## Tiers & routing (teach these in CLAUDE.md)
- **journal** (dated capture) = `docs/YYYY-MM-DD-*.md` (per-topic records) **+** `NOTEBOOK.md`
  (lab notebook). Split: *small finding from doing the work* → NOTEBOOK; *substantial standalone
  record* (decision/review/design) → `docs/`.
- **reference** (current truth) = ARCHITECTURE / ROADMAP / domain — edited in place.
- **cold-rationale** (optional) = lengthy *evergreen* "why" not needed for immediate reasoning →
  a dated `docs/` note + a one-line reference back. Extract only when lengthy AND cold AND
  evergreen (not code-coupled).
- **CLAUDE.md routes** reference docs **by name**; the journal **by convention** (`glob docs/*.md`
  + grep), never an enumerated growing list.

## `archive/` & changelog — do not blur
- `archive/` = **archival-only**: not-current-design-relevant, deletable (git is the backstop).
  Routing test: *"still current-design-relevant?"* No → `archive/` (or just let git hold it);
  Yes → it stays live.
- **git is the changelog** + a short "Recently shipped" digest in `ROADMAP.md`. **No
  `CHANGELOG.md`**; **never** route shipped-history into `archive/`.

## Hard scope-exclusions — never scaffold into; CLAUDE.md notes them excluded
**vendored** (`PCL/`, `nsg-v8-fork/`, `*/3rdparty/`), **generated** (`bin`/`obj`,
`BenchmarkDotNet.Artifacts`), **tooling** (`.claude/`, `.superpowers/`, `openspec/`). Their own
READMEs are not this project's docs and are not audited.

## Coexist, never clobber
Augment an existing setup — don't overwrite a present `CLAUDE.md` / `openspec/` / `.claude/`.
Normalize filenames to the convention (no spaces; align casing).

## Procedure
1. **Survey** the tree: existing docs + detect the scope-exclusions.
2. **Create/align** the enforced set, each charter-guarded; **elicit the domain-doc name**.
3. **Write `CLAUDE.md`** as the router (reference by name; journal by convention; exclusions noted;
   load-bearing gotchas only).
4. **Don't force content** — thin-but-charter'd is correct for a new/sparse project.

## Common mistakes (observed when unguided)
- Dropping **`NOTEBOOK.md`** / **`VERIFYING.md`** (the two agents reliably omit).
- **Inferring** the set from a sibling instead of carrying it (drifts; fails with no sibling).
- Routing shipped-history into `archive/`, or inventing a `CHANGELOG.md` — use git + a ROADMAP digest.
- Scaffolding/auditing **into vendored or generated** trees.
- Leaving **blank stubs** instead of charter-guarding them.

Full rationale + the worked example: `../../docs/docs-architecture-design.md`.

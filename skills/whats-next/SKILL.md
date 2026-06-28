---
name: whats-next
description: Use when asked "what should I work on next?", "what's the backlog?", or to prioritize a project's open work — a synthesized, prioritized backlog swept across every source (roadmap, known-limitations, gotchas, journal pending-items, code TODO/FIXME, audit findings, cross-repo blockers) with a coverage manifest and an accepted-constraints list. Composes after an audit (stale docs → stale backlog).
---

# What's next (backlog triage)

## Overview
Answer "what's next?" by **sweeping every backlog source**, separating **live-actionable** work from
**accepted constraints**, and returning a **categorized, prioritized** backlog **plus a coverage
manifest**. Baseline finding (clean-fixture RED): an unguided "what's next" gives a decent ranked
list but **omits the two things that make it trustworthy** — a **coverage manifest** ("did I see
everything?") and an explicit **accepted-constraint list** ("I considered X; it's by-design; skip
it"). Prioritization is innate; this skill guarantees the two missing pieces + sweep completeness.

## When to use
- "What should I work on next?" / planning a session / building a backlog / "am I seeing everything?"
- **After** an audit (`docs-architecture-audit`): stale docs → stale backlog, so currency-check first.
- Consumes the sibling skills' outputs (audit flags, maintain's residue) as backlog inputs.
- NOT for doc hygiene itself — this is the planning layer on top (setup/audit/maintain do the docs).

## Sweep every source — the checklist (don't skip a row; manifest what you can't reach)
| Source | Yields |
|---|---|
| working tree + `git status` / `log` | uncommitted WIP to finish; recent direction |
| ROADMAP "Future directions" / "Next" / Known-limitations | planned features + accepted limits |
| `CLAUDE.md` + docs gotchas | hazards — but most are *accepted constraints*, not work (see crux) |
| journal `docs/` + `NOTEBOOK.md` "pending / open items" | un-promoted decisions, open questions |
| code `TODO` / `FIXME` (note **whose** — fork-owned vs vendored/upstream) | actionable only if fork-owned |
| OpenSpec `changes/` (active vs archived) | in-flight work |
| **audit findings** (`docs-architecture-audit` output) | doc-drift fixes |
| cross-repo blockers / consumers | dependencies + sequencing |
| tests / build status | red = urgent |

## The crux — live-actionable vs accepted-constraint (or it cries wolf)
A gotcha / limitation is **work** only if it's a *live* problem. Most are **accepted constraints**
(by-design, "do not re-litigate", deferred-by-decision, vendored/upstream). Treat as actionable
**only** when it carries a live marker — a `TODO`/`FIXME` you own, an audit code-drift flag, a
ROADMAP "Next" item, or an explicit pending/open marker. Everything else → the accepted-constraint
list (shown, not actioned). **Default to accepted when unsure** — a false "todo" on every gotcha
trains the user to ignore the output.

## Categorize + prioritize
Bucket each actionable item: **{ urgent (red tests / broken) · deferred-fix · future-feature ·
doc-debt }**. Rank by value × (1 / effort) × risk; give a **top-N with a recommended sequence** (what
unblocks / de-risks what). Tag effort (XS/S/M/L) + risk. Priority is a *proposal* — the user owns the call.

## Fan out for completeness
**REQUIRED:** use the fan-out from **docs-architecture-audit** (independent passes + merge +
loop-until-dry). Passes agree on the core but the *margins* are a coin-flip — different passes surface
different long-tail items. Merge them.

## Two REQUIRED outputs (the baseline omits both)
1. **Coverage manifest** — a table over every source row above: **swept** (with what it yielded) or
   **not reached** (and why — no run logs, vendored, sibling repo). The "am I seeing everything?"
   answer; without it the list reads complete when it isn't.
2. **Accepted constraints — "considered, not work"** — the items that surfaced but are by-design /
   decided / vendored, each with the one-line reason to skip. Shows the work; prevents re-litigation.

## Common mistakes
- **No coverage manifest** — the #1 omission; the backlog looks complete when it isn't.
- **Crying wolf** — flagging accepted constraints / vendored TODOs / "do-not-re-litigate" items as work.
- **Skipping the audit-first step** — building a backlog on stale doc claims.
- **Single pass** — margins are a coin-flip; fan out + merge.
- **A flat list** — no buckets, no top-N, no sequence is a dump, not a plan.

Full rationale + the RED baseline (clean vs spec-contaminated fixture): `../../docs/docs-architecture-design.md`.

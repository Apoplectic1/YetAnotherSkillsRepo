---
name: docs-architecture-maintain
description: Use when a project's journal (dated docs/ notes + NOTEBOOK) has accrued findings that may have hardened into standing truth, when the reference docs feel behind the journal, or for a periodic journal-health sweep. Assumes the docs-architecture conventions (a CLAUDE.md router + charter'd reference set).
---

# Docs-architecture maintain (graduate & prune)

A periodic sweep that promotes **hardened standing truth out of the journal into the reference
tier**, then **prunes the source** so nothing duplicates. Not a currency or placement audit
(`docs-architecture-audit`), not bootstrap (`docs-architecture-setup`). The linchpin: every
`graduate` carries **both a target and a source-disposition**; graduating without pruning
makes the duplication the system exists to prevent, and pruning by deletion loses the
why/when. `python sweep.py <dir>` (beside this SKILL.md) prints the sweep's sources and
budgets with the rule each keys, and `sweep.py <dir> --check` reads the run's report back for
what M13, M14 and M16 require; what graduates, where, and with which disposition is the
sweep's own judgment.

## Classify: every journal item
- **M1.** `graduate`: a standing truth (recurs, decided, now-true) not yet single-sourced in
  the reference tier → the reference doc its **charter** selects.
- **M2.** `keep`: a still-contextual finding; *intentional cold rationale* a reference doc
  cites; or a single source the reference tier points INTO. A healthy journal is mostly `keep`.
- **M3.** `archive`: a fully resolved or superseded dated `docs/` record → `archive/`. A
  NOTEBOOK or CHANGELOG entry is never archived by judgment; it rolls out by date (M17).
- **M4.** `prune-only`: a closed item still sitting in an open list → strike it.

## The linchpin: a source-disposition, REQUIRED on every graduate
- **M5.** `stub`: leave the dated *measurement or derivation* as the evidence behind the
  lifted guidance.
- **M6.** `cross-ref`: replace the now-duplicated prose with a one-line pointer *up* to the
  reference doc.
- **M7.** `archive`: the whole dated `docs/` record is spent (never a rolled entry, M19).
- **M8.** **Never delete the why/when**: a dated entry records when and why; stub or archive
  it, never erase.
- **M9.** Don't over-graduate, and **check every target at apply time**: a target the sweep
  script marks past its budget, or one a content test finds dominated by content a split
  would relocate, is a **SETUP T5 split job first** (`split_doc.py`, by `##` topic into a
  directory named for the doc, the doc left as the index), never more content. Applying the
  promotion and flagging the split afterward is the violation. Bloated → hold (M14).
- **M14.** A held graduate is **recorded in the dated report** (standing claim, target,
  disposition) and **one ROADMAP open line** names the pending split job and its shape,
  deduplicated across holds; the split runs as its own adjudicated job, then each held
  promotion lands in the part whose heading it belongs under. Healthy targets in the same
  sweep apply normally.

## The journal's size: roll over by date, never by judgment
- **M17.** **Before the fan-out, roll over any journal past its budget** (`NOTEBOOK.md`,
  `CHANGELOG.md`; 40 KB by default; the sweep script marks them): `python rollover.py
  <journal>` (a dry run first, then `--apply`) moves the oldest whole days into a directory
  named for the file, one frozen file per period named by its first date, `INDEX.md` there
  listing every rolled entry (`journal_index.py`); entries keep their text, a dated citation
  resolves by grep over the file and the directory, and a line-anchored pointer
  (`NOTEBOOK.md:412`) breaks, so grep for those first. The rollover also runs on its own
  whenever a journal passes the budget.
- **M18.** **Open threads never roll out unannounced.** The dry run lists the entries about
  to roll; carry each still-open item (not closed by a later entry, tracked in no ROADMAP)
  as one line into the live file's "Open threads (carried at a rollover)" section, naming
  the rolled file, *then* apply. `whats-next` reads the live file only.
- **M19.** **A rolled file is frozen** (the M11 treatment): a graduate from one takes
  `cross-ref` written in the reference doc, or `stub`; never M6 in place, never M7. The
  sweep records the newest rolled file it covered as its **watermark** (M16); the next sweep
  slices by the live file and the rolled files newer than the last watermark, which the sweep
  script lists.

## Sources: one class beyond the dated journal
- **M11.** Archived openspec design docs (`openspec/changes/archive/*/design.md`; the sweep
  script lists them) are a **first-class source**, whatever a router's generic `openspec/`
  exclusion says. A graduate from one takes **`cross-ref` only**, written as the pointer in
  the reference doc; the archived file is never stubbed, trimmed or relocated.

## Portfolio truth
- **M15.** A **portfolio-level** graduate (the truth spans repos, or no doc in this repo's
  set can own it) targets the **container's portfolio `DOMAIN.md`** where one exists
  (pointers one-way; M9 and M14 apply). None exists → **flag-and-ask**: the dated report
  records it with its portfolio-level classification and one ROADMAP open line asks for the
  placement; **never improvise** it into the container router, a sibling's docs or a new
  cross-repo pointer.

## Code bugs: a report-only channel
- **M12.** A journal claim with **contract force** (must / always / never / aborts-on-X)
  that current code *violates* → a report-only **`flag-code-bug`** (claim + `file:line`)
  *alongside* the entry's normal classification; the **code is the suspect**, never the
  entry. Corroboration (a test, another doc) strengthens a flag, **never substitutes** for
  guarantee language; dated records agreeing on an old value are history, and design-time
  values in archived designs (M11) are never contracts. MAINTAIN never edits code.
- **M13.** Surviving flags **persist before the run ends**: full evidence in the dated
  `docs/YYYY-MM-DD-maintain-report.md` (the project's dated form), one deduplicated line per
  adjudicated-surviving bug in the ROADMAP's open list; adjudication deferred → one line
  pointing at the report.

## The report: accounting
- **M16.** The dated report **ends with the REQUIRED accounting slot**, which
  `sweep.py --check` reads back: the prune/archive candidates found (or the line "prune
  candidates: none found"), a one-line **net reference-tier delta** (added vs removed or
  struck), and the **watermark** (the newest rolled file covered, or "no rolled files").
  Silence is not a legal value for any of the three.

## Coverage
- **M10.** **REQUIRED:** reuse the fan-out from **docs-architecture-audit** (independent
  workers, structured flags, merge + dedup, loop until dry); the slices are the sources the
  sweep script lists (the live journal, the rolled files newer than the watermark, the dated
  records, the archived designs), never one 300 KB file.

## Flag schema (every worker)
```
- source:        journal file + section/topic
- classify:      graduate | keep | archive | prune-only
- target:        reference doc (for graduate), chosen by charter
- disposition:   stub | cross-ref | archive        REQUIRED for every graduate (a rolled entry: stub or cross-ref)
- standing-claim: the durable truth being promoted (for graduate)
- evidence:      why it's standing (recurs / decided / already-cited), or why keep
- code-bug:      optional report-only flag-code-bug (M12): contract claim + file:line
- action:        one line
```

## Procedure
1. `python sweep.py <dir>`: the journals against their budget (M17), the rolled files newer
   than the last watermark (M19), the dated records, the archived designs (M11), the targets
   past their budget (M9, M14), the last report.
2. **Roll over** any journal past its budget (M17), carrying open threads first (M18).
3. **Fan out** graduation workers over the slices (M10) → schema'd flags; **merge + dedup +
   loop until dry**.
4. **Adjudicate** per item (graduate / keep / archive / prune-only).
5. **Apply**: promote → the reference doc; disposition the source (M5 to M7); hold into a
   bloated target (M14); persist code-bug flags (M13) and portfolio-level graduates (M15);
   update the router if a doc moved. Re-verify (nothing duplicated, no why/when lost), close
   with the accounting slot (M16), and run `sweep.py <dir> --check`.

Full rationale + RED/GREEN provenance:
https://github.com/Apoplectic1/YetAnotherSkillsRepo/blob/main/docs/docs-architecture-design.md

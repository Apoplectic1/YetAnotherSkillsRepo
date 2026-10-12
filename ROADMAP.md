# ROADMAP.md — forward plan

**Charter:** forward-looking design + a short Recently-shipped digest (shipped history →
`CHANGELOG.md` when it accrues; git backstops commits). The design doc's own open-items
section closed 2026-07-07 with nothing open.

## Open
- **Always-on pilot on the HDL tree** (2026-10-12, consumer adoption after `always-on-budget`;
  from HDL sessions, each repository from its own): HlsLibrary's router (39.9 KB, 397 lines:
  the 12.6 KB element maps to the class READMEs that already hold them, the 16.2 KB of HLS
  synthesis gotchas to a path-scoped rule file on the HLS sources or a skill, about 9 KB
  left), the ATML umbrella's DOMAIN (past the budget, four headings) read by section, then the Arty's
  26.6 KB, 346-line router. `python ~/.claude/skills/docs-architecture-audit/chain_budget.py
  <dir>` before and after; the HDL chain is 83 KB, 2.1x the budget, today. The owner's global
  file (26.7 KB, 187 lines) is a third of every chain on the machine and the owner's own call.
  The Arty's ARCHITECTURE split landed 2026-10-12 (seven parts, byte-exact, the first field
  apply of T5; docs only). The ATML umbrella's ten held promotions stay held: they are Arty
  work, and the Arty is halted at contract v5 with no further work until an unhalt (its
  ROADMAP; the 2026-09-26 maintain report sequences the landings after it). The three
  routers' leans (HlsLibrary 39.9 KB, the Arty's 26.6 KB, the umbrella's 12.9 KB) and the
  umbrella's DOMAIN and ROADMAP splits were planned by SETUP reps the same day; the two
  changes they waited on (`s8-field-fixes`, `split-doc-field-fixes`) shipped that evening,
  so they run next, from HDL sessions against the deployed text, each repository from its
  own, re-planned (the per-file line and the homes' triggers change each lean's shape; the
  plans in the pilot record are the starting point). The Arty's lean, docs and `.claude/`
  only, is the owner's call under the halt, as the split was.
- **Portfolio-convention consumer adoption** (post-`b4-portfolio-domain`, shipped
  2026-07-26): in their own sessions. (a) Astronomy container: done (the portfolio
  `DOMAIN.md` exists since 2026-08-16 and the router's Data-flow hubs point into it; found
  by the 2026-10-12 release-close audit). (b) TSM + siblings: resolve the glossary loop to
  one-way pointers against the portfolio DOMAIN (TP and IS point up; TSM's loop unverified).
- **Deferred until a second skill family onboards** (decided 2026-07-10: flat `skills/` stays):
  restructure into per-family dirs (`skills/docs-architecture/…`) — requires deploy.sh
  two-level glob + prune re-verify, README/CLAUDE/ARCHITECTURE link updates, one commit.
  Trigger: onboarding `diagnose`/`graphify`/etc. into this repo.

## Recently shipped

- 2026-10-12: **Tools over prose, MAINTAIN: `sweep.py`, and the text to its actions** (change `maintain-tools-first`; 10.7 KB to 8.7 KB; a regression GREEN, five families, nothing restored; the family 38.7 KB to 29.3 KB over the day)
- 2026-10-12: **Tools over prose, AUDIT: `scope.py`, and the text to its actions** (change `audit-tools-first`; 13.4 KB to 10.2 KB; a regression GREEN, five families, one clause restored and re-run to a pass: R29's cheap-run mapping)
- 2026-10-12: **Tools over prose, SETUP: `survey.py`, and the text to its actions** (change `setup-tools-first`; 14.6 KB to 10.4 KB; a regression GREEN, five families, every cell that fired held)
- 2026-10-12: **S8 field fixes: the budget per file, the homes' load triggers, B1's skill** (change `s8-field-fixes`; five clauses status-noted, RED no failure; the held-under-halt cell: the halt's terms decide)
- 2026-10-12: **`split_doc.py` field fixes: a journal refused, the scan kept inside the unit, stale lines listed, dated headings warned** (change `split-doc-field-fixes`; T5's same-run and single-part cases status-noted, RED 2/2 no failure)

The full history, every shipped unit as a dated entry, is `CHANGELOG.md` (newest
first).

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
  ROADMAP; the 2026-09-26 maintain report sequences the landings after it). Applied
  2026-10-12 with the trimmed text (`docs/2026-10-12 - hdl-leans.md`): HlsLibrary's
  router 39.9 KB to 5.1 KB with its set scaffolded, the umbrella's 12.8 KB to 7.1 KB with
  ARCHITECTURE opened, DOMAIN and ROADMAP split and the CHANGELOG rolled. Still open: the
  Arty's router lean (26.6 KB, 346 lines; deferred under the halt, the owner's call), the
  HDL router's and the owner's global file's own leans (the chains stay at 1.2x to 1.3x,
  all of it theirs), and the umbrella's `ROADMAP/next-in-order.md`: its items carry
  `###` headings since 2026-11-05, which serve a reader and no tool (T5 never cuts below
  `##`); closed the same day at 32.8 KB by the doc's own charter, a done item keeps one
  line, the six done items' text moved byte for byte to a dated record.
- **Portfolio-convention consumer adoption** (post-`b4-portfolio-domain`, shipped
  2026-07-26): in their own sessions. (a) Astronomy container: done (the portfolio
  `DOMAIN.md` exists since 2026-08-16 and the router's Data-flow hubs point into it; found
  by the 2026-10-12 release-close audit). (b) TSM + siblings: resolve the glossary loop to
  one-way pointers against the portfolio DOMAIN (TP and IS point up; TSM's loop unverified).
- **Strike superfluous text, by review** (proposed 2026-10-25 from a consumer's field finding:
  its ROADMAP, NOTEBOOK and overview document had accrued session narrative, "what landed in
  which commit" lists, old-to-new mappings, effort levels, tooling and presentation tweaks, and
  an attribution on nearly every sentence; none of it bears on the design, every token is paid
  on every read, and no skill removes it: M2 keeps it, M8 and M17 protect it, AUDIT checks
  currency, and the MAINTAIN spec denies reference-tier deletion authority). The shape as
  sketched: a MAINTAIN step with appended rule IDs, over the journal and the reference tier,
  that only proposes. A strike candidate passes three tests: no design weight (it states no
  fact, decision or its reason, rejected alternative, open item or gotcha; narrative only);
  nothing cites it (section names, ids, anchors, rule IDs and dated citations searched); and
  the owner reviews every candidate before anything is removed, each listed verbatim with its
  location, the tests it meets and the commit that keeps the record, declined items recorded so
  the next sweep does not re-offer them. M8 and M17 stay as they are for the graduate step.
  Open: A1 (MAINTAIN strikes in both tiers, the review replacing the spec's no-deletion
  clause as the safeguard) or A2 (MAINTAIN strikes the journal, AUDIT gains a strike lens for
  the reference tier). Harness: a fixture variant with planted superfluous text and planted
  look-alikes (a cited section, a rejected alternative with its reason, an attribution that
  records an acceptance); RED on the current skill, GREEN lists the plants verbatim and none of
  the look-alikes and removes nothing before approval; `sweep.py --check` reads the new slot.
  Pairs with a writing-time rule in the consumer's router (the journal charter narrowed to
  findings that affect the design or how it is built and checked), cheaper than any sweep.
  Deferred by the owner: a diversion from the consumer's design work.
- **Deferred until a second skill family onboards** (decided 2026-07-10: flat `skills/` stays):
  restructure into per-family dirs (`skills/docs-architecture/…`) — requires deploy.sh
  two-level glob + prune re-verify, README/CLAUDE/ARCHITECTURE link updates, one commit.
  Trigger: onboarding `diagnose`/`graphify`/etc. into this repo.

## Recently shipped

- 2026-10-12: **Field fixes from the EP7314600 run: the scripts, not the text** (no change; three plan reps on a sensitive repository and the applies there; the scope seed states a convention once; twelve fixture outputs byte-exact on fresh copies)
- 2026-10-12: **Tools over prose, MAINTAIN: `sweep.py`, and the text to its actions** (change `maintain-tools-first`; 10.7 KB to 8.7 KB; a regression GREEN, five families, nothing restored; the family 38.7 KB to 29.3 KB over the day)
- 2026-10-12: **Tools over prose, AUDIT: `scope.py`, and the text to its actions** (change `audit-tools-first`; 13.4 KB to 10.2 KB; a regression GREEN, five families, one clause restored and re-run to a pass: R29's cheap-run mapping)
- 2026-10-12: **Tools over prose, SETUP: `survey.py`, and the text to its actions** (change `setup-tools-first`; 14.6 KB to 10.4 KB; a regression GREEN, five families, every cell that fired held)
- 2026-10-12: **S8 field fixes: the budget per file, the homes' load triggers, B1's skill** (change `s8-field-fixes`; five clauses status-noted, RED no failure; the held-under-halt cell: the halt's terms decide)

The full history, every shipped unit as a dated entry, is `CHANGELOG.md` (newest
first).

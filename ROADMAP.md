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
  In the same sessions, the Arty's ARCHITECTURE (70.4 KB, seven topics) splits with
  `python ~/.claude/skills/docs-architecture-setup/split_doc.py ARCHITECTURE.md` (dry run
  first: it lists every section citation to check; the apply on a scratch copy reconstructed
  the doc byte for byte, 2026-10-12), after which the ATML umbrella's ten held promotions can
  land in their parts.
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

- 2026-10-12: **A reference doc past its budget splits by topic: SETUP T5, `split_doc.py`**
- 2026-10-12: **Always-on is a scope, not a size: SETUP S8, AUDIT R30, `chain_budget.py`**
- 2026-10-12: **AUDIT scoped modes: `release-close` and `small-set`, R29**
- 2026-10-12: **AUDIT scope from the routers: `spec-change` shipped, two halves status-noted**
- 2026-10-12: **the rolled-journal index lists bold-lead entries under a bare date heading**

The full history, every shipped unit as a dated entry, is `CHANGELOG.md` (newest
first).

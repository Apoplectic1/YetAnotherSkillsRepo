# Docs audit, 2026-10-12: release-close mode after five changes

A `docs-architecture-audit` run in `release-close` mode (R29) on this repo the day five
changes shipped (`rolled-index-titled-entries`, `audit-scope-from-routers`,
`audit-scoped-modes`, `always-on-budget`, `reference-doc-split`) and the design doc was
split by T5. Two workers through a Workflow at Sonnet/high (365k tokens): the lens over the
reference tier (router, ARCHITECTURE, ROADMAP, DOMAIN, VERIFICATION, RELEASING, the design
index and its thirteen parts) and the cross-reference pass with the chain row. One round, no
loop, no model switch; a full run would have added per-section workers, further rounds and
a second model. Merged: thirteen flags, none dropped. Adjudicated by the owner the same
day, all approved; applied in the commit that carries this report.

**Chain row (R30):** 36.8 KB, 9,421 tokens, within the 10,000 budget; this project's part
1,089 tokens; the owner's global file 6,846; no file over 200 lines.

## Flags and dispositions

| # | Axis | Location | Finding | Action | Disposition |
|---|---|---|---|---|---|
| 1 | placement | ROADMAP § Recently shipped | 12.4 KB of entries, 23 of them, no CHANGELOG.md (A2, R25) | move-to CHANGELOG.md | applied: CHANGELOG.md created, the entries moved verbatim, a five-line digest left, the router's journal lines updated |
| 2 | currency | design part "How Claude accesses docs" | "only three files auto-load": now a chain (R30) | fix-doc | applied |
| 3 | currency | router journal line, NOTEBOOK charter, design tier part | pattern `YYYY-MM-DD-<slug>` while six records use `YYYY-MM-DD - <name>` | fix-doc | applied: the dash form stated as the pattern for new records, older names kept |
| 4 | currency, prescriptive | ROADMAP consumer adoption (a) | the Astronomy portfolio DOMAIN exists since 2026-08-16 | graduate | applied: (a) marked done, (b) stays |
| 5 | currency | ROADMAP pilot item | "ATML DOMAIN (40 KB)": 44 KB | fix-doc (R28) | applied: de-valued |
| 6 | currency | ROADMAP pilot item | "71 section citations": 86 | fix-doc (R28) | applied: de-valued |
| 7 | currency | VERIFICATION | "the HDL tree's six" INDEX files: seven | fix-doc (R28) | applied |
| 8 | currency | router | "thirteen parts" | fix-doc (R28) | applied: "one part per `##` heading" |
| 9 | currency | five design parts | positional pointers ("the tier section above") after the split | fix-doc | applied: each names its heading |
| 10 | currency | harness README, both catalogs | fixture sizes stated before the final cuts | fix-doc | applied: measured sizes |
| 11 | placement (R30) | router § Load-bearing gotchas, the openspec CLI block | fails breadth: one activity's gotchas, nine lines | move-to `.claude/rules/openspec.md` | applied: path-scoped on `openspec/**`, a trigger line left; the first S8 move in this repo |
| 12 | currency | github-distribution spec, scenario "Design doc stays at its published path" | the doc split at the same path; the scenario's wording predates T5 | spec-change | persisted: ROADMAP "Spec wording cleanup" |
| 13 | currency | audit spec, the 2026-10-12 status note "no R29 was added" | R29 now exists as scoped modes | spec-change | persisted: the same ROADMAP line |

## Checked and found current

Rule numbers R1 to R30, S1 to S8, T1 to T5, M1 to M19 and the four scripts exist as cited;
the deployed skills are byte-identical to `skills/*`; `dev` and `main` agree; sixteen
backticked paths in the router, ARCHITECTURE and VERIFICATION resolve; the design index's
thirteen part links resolve; the two live section citations into the design doc (both in
NOTEBOOK) resolve by grep into `the-phased-arc.md`.

## Unsure, not acted on

Whether TSM's glossary loop (consumer adoption (b)) is resolved: TP and IS point up to the
portfolio DOMAIN, TSM itself unverified from here. Whether the shift-left gotcha beside the
openspec block (four lines, archive-time) also fails breadth: left in the router, since the
archive-time question is the repo's own workflow and every change here ends in one.

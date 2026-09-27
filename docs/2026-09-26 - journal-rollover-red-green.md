# 2026-09-26: journal-rollover RED/GREEN results

**Charter:** dated validation record for `journal-rollover`. Origin: the HDL tree's maintain
sweep of the same day (a 311 KB NOTEBOOK, three workers for one file; the owner's decision to
roll journals over by date into a directory named for the file; the pilot on seven journals).
The HDL tree is deriving evidence and is poisoned for this rule; the fixture is TidePool plus
the new `big-journal` variant (`harness/tidepool-fixture-variants/big-journal/`, cells RO1 to
RO5 in `harness/catalog-tidepool.md`) and the reefstack container for the ignore rule. Reps
Sonnet at high through the Agent tool, labelled so; the orchestrating session's own global
instructions leaked into every rep (one RED rep named its report with the owner's spaced date
form, which only that context supplies): conservative for the GREEN-delta claim, disclosed.

## Gating outcomes

- **MAINTAIN rollover (M17 to M19): RED confirmed 2/2, GREEN 2/2.** Both RED reps left the
  57 KB journal whole. One said it outright: "there's no archive mechanism for individual
  NOTEBOOK bullets"; the other annotated a journal entry in place and kept the file. Neither
  carried the open thread anywhere (it was `keep`, "genuinely still open, nothing to do").
  Both GREEN reps ran the dry run, carried the 2025-12-09 thread into "Open threads (carried
  at a rollover)", did not carry the 2026-01-15 thread (closed by the live 2026-06-12 entry),
  applied, and named the watermark in the report. Disk-verified in every rep: the rolled file
  `NOTEBOOK/2025-10-06.md` at 37 021 bytes, byte-identical across both GREEN reps and to the
  orchestrator's reference run; `INDEX.md` present; the live file at about 21 KB with the
  rollover note; the ARCHITECTURE citation of 2026-01-22 resolving by grep into the rolled
  file; live plus rolled entries reconstructing the baseline byte for byte (GREEN rep 1's one
  difference is an M6 cross-ref applied to a live entry, a legal disposition); no code touched.
  Across all four reps the rest of the M-stack held: the M11 cross-ref into the archived
  station-curation design, the M12 timeout flag on `tides.py:25` with M13 persistence, the
  M16 slot.
- **SETUP B6, a container root's ignore file by name: RED confirmed (prompt-only probe).**
  With the current text the rep left the `/*/` file as is, found no rule addressing it, and
  correctly predicted that a new `NOTEBOOK/` would be silently ignored. Ships as B6 and a
  requirement.
- **SETUP B2, the project's stated dated-record pattern: RED confirmed (prompt-only probe).**
  The rep renamed the three spaced files to the hyphen form under B2 and said nothing in the
  text lets a project's stated convention override it, calling the router's own line "exactly
  the kind of off-charter inconsistency this skill exists to correct". Ships as the B2 clause.
- **AUDIT R14 over a rolled file: NO-FAIL.** The worker treated `NOTEBOOK/2026-01-04.md` as
  journal by inheritance from the router's journal line and emitted no flags for the
  superseded value, while naming the ambiguity. Status-noted in the delta spec; no audit
  text. The router line SETUP now writes carries it.
- **whats-next over rolled files: NO-FAIL.** The rep read the 18 KB live file only, listed the
  carried thread (future-feature), treated the rolled closed item as closed, and marked the
  rolled files "not reached, carry-forward invariant" in the manifest, adding that the depth
  was its own call. Status-noted; no text.

## Shipped

MAINTAIN M17 to M19 plus procedure step 1, the M3 and M7 narrowing, the M10 slices and the
M16 watermark; the scripts `rollover.py` and `journal_index.py` beside the maintain SKILL.md
(both entry forms; replay on the pilot's inputs reproduces the pilot's committed files byte
for byte). SETUP: T1's overflow directories, T4's journal line, B2's stated pattern, B6. The
design doc's tier section (three members, the rollover principle). Change record:
`openspec/changes/archive/2026-09-26-journal-rollover`.

## Notable

- The fixture's own NOTEBOOK is a newest-first bullet list, not `##` headings: the second
  entry form became a requirement on the way to the fixture, not from the field.
- The bullet form's index lines are the first 110 characters of the bullet, since a bullet
  has no title; readable enough in the runs, and a reason to prefer titled `##` entries in a
  journal SETUP creates.
- Two RED reps and two GREEN reps all found the same planted timeout bug and the same M11
  graduate: the sweep's judgment is stable across the text change; only the size mechanism
  moved, which is what the change claims.

# audit-tools-first: design

## Context

The second trim, after `setup-tools-first` the same evening. AUDIT's 30 rules carried the
family's most rationale (the benchmark figures behind R18 to R22) and its most reader-side
detection (R12 to R17, R25, R30, R29's phrase list). The design doc's "Tools over prose"
part states the shape; this change applies it to AUDIT.

## Decisions

- **D1: the scope is a list the script prints, not a procedure the worker follows.** What the
  router names, the canonical set, a split index's parts, a router-named dated doc or spec
  or leaf in an excluded tree are in; the journal, archives, excluded trees, unnamed specs
  and sub-projects are out; each line carries its rule. The judgments stay: a router-named
  dated doc's role is what the router's line says of it (the script quotes the line).
- **D2: the cross-reference pass gets a seed.** Every backtick path and every "DOC § Heading"
  citation in the in-scope docs is resolved against the tree (a heading in the doc or its
  split directory; a `root CLAUDE.md` citation against the ancestors); what does not resolve
  is listed, and a basename found elsewhere is named as a rename-orphan candidate. Code
  identifiers stay the workers' (a symbol is a claim, not a path).
- **D3: the lens is an option.** R29's release-close phrases are a grep; `--lens release`
  lists the lines, the workers judge each (RC1 to RC3 are real waits in the same words).
- **D4: the chain row comes with its largest items.** `chain_budget.py` beside the script
  runs the same way; the scope script keeps the total, the project's part and the three
  heaviest files, which is what the coverage note's row needs.
- **D5: the regression gate**, as for SETUP: no RED, one report-only rep per family, a
  failing cell names the clause restored.

- **D6: the clause the regression restored.** R29's second sentence, "The user names one,
  or asks for one round or a cheap run and the run names which fits and says so", had been
  cut as redundant with the first; the release-lens rep, asked to "run the audit cheaply",
  read "invoked by the user, never chosen by the run" literally and ran the full text
  instead. The sentence is the mapping from a user's wording to a mode, not rationale, and
  it came back whole.

## Verification

Script-level: `scope.py` byte-exact on three fresh baselined fixture copies (the base
TidePool, `audit-scope` from `PulseMonitor/`, the `fat-chain` root); the spaced dated name
the PulseMonitor rep caught (`docs/YYYY-MM-DD - name.md` not read as a path) fixed before the
ship. The regression GREEN per D5: five report-only reps (344k tokens), t1 with O1, CB1,
CB4 and DV2, SS1, SS2, SP1, SP2, SC1 to SC3, CH1 and CH2 held, RL1 to RL6 found and RC1 to
RC3 held; SM2 failed on the cut sentence and was re-run with it restored (D6; the result in
the record). The record: `docs/2026-10-12 - audit-tools-first-regression.md`.

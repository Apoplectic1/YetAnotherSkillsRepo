# Reference-doc split: RED/GREEN record (2026-10-12)

Change `reference-doc-split` (the ROADMAP's "The split job's owner", queued 2026-09-26).
Fixtures: TidePool with the `fat-topics` overlay (a 40.3 KB ARCHITECTURE of eighteen `##`
mechanics topics true to code) for the split, the existing `fat-arch` overlay (25 KB of
rationale essays) as the control, and `fat-topics` plus the fat-arch NOTEBOOK entries for
MAINTAIN (FA1's graduate targets ARCHITECTURE). Cells SD1 to SD5 in
`harness/catalog-tidepool.md`. Method: plan-only single-agent reps through a Workflow at
Sonnet/high (RED four, 325k tokens; GREEN four, 300k). Derivation evidence: `split_doc.py`
dry-run on the Arty's 70.4 KB ARCHITECTURE (seven topics, 71 section citations listed) and
applied on a scratch copy (seven parts, the preamble plus parts reconstruct the original byte
for byte, a 2.1 KB index); the apply on the real repo is consumer work from an HDL session.

## Cells and results

| Cell | Plant or probe | RED (current text) | GREEN (candidate) |
|---|---|---|---|
| SD1 | SETUP, "ARCHITECTURE.md feels unwieldy", the 40 KB doc | 2/2 kept whole: "the skill has no rule for splitting a large reference doc, and none that makes size a trigger for T2 docs"; one rep added that a split would break every internal § cross-reference | 2/2 T5 cited, the dry run run, eighteen parts named, the doc as the index, the router naming it plus a note, "ARCHITECTURE § Window scoring" resolving by grep into `ARCHITECTURE/window-scoring.md`; T3, B5 and a by-charter redistribution each ruled out by the right rule |
| SD2 | SETUP on the fat-arch control (rationale essays) | extract-cold under T3, "don't fan out into ARCHITECTURE-cache.md" | no split (the script refused: under budget); keep whole with a heading-read hint, T3 offered as borderline since the essays are code-coupled |
| SD3 | every under-budget doc | untouched | untouched |
| SD4 | MAINTAIN, the CO-OPS graduate aimed at the 40 KB doc | the hold right (M9, M14: nothing written, the report entry, the source untouched); the ROADMAP line "via a setup/audit split job", no shape, the landing place guessed | the hold with the shape: "Split ARCHITECTURE.md by ## topic into ARCHITECTURE/ with the doc left as the index (SETUP T5, split_doc.py)"; the promotion lands in "Requests and the network budget" |
| SD5 | section citations | the whole-doc reps resolve them in the file | the split reps resolve them by grep over the file and the directory, the dry run's sixteen listed for review |

## What RED taught

- **The gap was an absence, stated by every rep.** Both SETUP reps looked for a size rule for
  the reference tier, found T1's budget "explicitly for journals", and kept the doc whole with
  a correct reading of T3 and B5; the MAINTAIN rep held correctly and wrote a ROADMAP line
  that named a job nobody could run. The text needed a rule and a tool, not a correction.
- **The citation worry is the objection the mechanism answers.** A rep argued a split "would
  break every internal § cross-reference" under S1 and B2; T5's heading-keeps-its-text plus
  the dry run's citation list is the reply, and GREEN's reps used both.
- **A tripwire fixture has to trip, again.** The fat-topics doc took three cuts (17, 30, 38,
  then 40.3 KB) to pass the budget: true-to-code mechanics prose is denser than it reads.
  The fixture ends 0.3 KB over, which one GREEN rep noticed and asked about; the budget is a
  line by design, and the rule says "past its budget".

## What GREEN taught

- **The script carried the decision.** Both split reps ran the dry run first and planned
  around its output (parts, sizes, the sixteen citations); the control rep ran it too and
  took its refusal as the rule's answer. A tool the rule names is read as part of the rule.
- **The control shows the rule telling the two diseases apart, with a wrinkle.** The
  fat-arch rep refused the split and judged T3 borderline because the essays mix rationale
  with named constants; the catalog expected extract-cold. Both readings keep the doc out
  of `ARCHITECTURE/`, which is the control's purpose; whether code-coupled rationale
  extracts is T3's own threshold question, older than this change and not acted on.
- **Open questions the reps raised, not acted on:** whether to wait when a doc is barely
  over the line; no rule for a doc that is over-detailed rather than over-long; whether a
  journal entry may split into a keep and a graduate (MAINTAIN, raised before).

## Shipped

SETUP T5 and `split_doc.py` beside it; MAINTAIN M9 and M14 naming the shape and the landing
part; AUDIT R12 reaching the parts through the index and R19 resolving a section citation in
the doc or its directory; the design doc's tier section (the overflow rule's other half);
the three specs; the fixtures and `harness/split-fixture/index.expected.md`. The Arty's
apply is queued with the always-on pilot.

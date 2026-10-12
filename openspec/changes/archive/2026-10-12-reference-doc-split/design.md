# reference-doc-split: design

## Context

The journal got its size mechanism on 2026-09-26 (rollover by date into a directory named
for the file). The reference tier had only a hold: M9 and M14 stop a promotion into a
bloated doc and name "the split job, setup/audit territory", which no skill described. The
HDL maintain sweep held ten promotions against three docs past 40 KB; the Arty's
ARCHITECTURE is 70.4 KB in seven `##` topics, every one a live reference section. The owner
chose (2026-10-12) a directory split by `##` topic, scripted, with the Arty applied from an
HDL session after the ship.

## Decisions

- **D1: by `##` heading, never by judgment.** A heading is the author's own topic boundary;
  it needs no judgment and never drifts, as a date range does not. The script moves each
  section byte for byte into `<DOC>/<slug>.md` and never splits below `##`: a single topic
  past the budget stays one part (the Arty's 24 KB Board app does).
- **D2: the doc stays as the index.** Its charter and preamble, a split note, one line per
  part (the heading as written, the file and size, the first prose sentence). The router
  keeps naming the doc; nothing new is routed. A reader who opens ARCHITECTURE.md finds the
  map and the parts by glob, the T4 primitive.
- **D3: citations by grep, as for the journal.** A part keeps its `## ` heading line, so
  "ARCHITECTURE § Build chain" resolves by `grep -n` over the file and the directory; the
  dry run lists every section citation it finds (71 on the Arty, 16 intra-doc on the
  fixture) for the operator to check before `--apply`. RED's SETUP reps cited exactly this
  risk ("a split would break every internal § cross-reference") as a reason to leave the
  doc whole; the mechanism answers it.
- **D4: the same budget, a different test.** 40 KB is one read unit and one worker's slice
  for a reference doc as for a journal. The split is for a doc whose weight is many topics;
  a doc heavy with cold rationale extracts (T3, R11) and a design doc in a code-light project
  stays whole (B5). The fat-arch control exists to show the rule telling them apart.
- **D5: no new home.** A part is the same section, in the same tier, under the same
  charter, in its own file. A redistribution by charter into sibling docs is the shape a
  consumer's own split produced (TSM's SUBSYSTEMS beside its specs, "two homes for one
  truth") and the one this rule refuses.
- **D6: MAINTAIN names the shape, AUDIT reaches the parts.** M9 and M14 point at T5 and the
  script, and a held promotion lands in the part whose heading it belongs under; R12 takes
  the parts into scope through the index, R19's pass resolves a section citation in the file
  or the directory.
- **D7: the Arty is a dry run here, an apply there.** The dry run is the derivation
  evidence (seven parts, byte-exact on a scratch copy, 2.1 KB index); the apply edits an
  HDL repository and is consumer work from its own session, queued with the always-on pilot.

## What RED showed (2026-10-12)

Four plan-only reps through a Workflow at Sonnet/high (325k tokens). On the 40 KB
`fat-topics` doc both SETUP reps kept it whole: "the skill has no rule for splitting a large
reference doc, and none that makes size a trigger for T2 docs". On the `fat-arch` control
the rep extracted the essays under T3 and refused to "fan out into ARCHITECTURE-cache.md",
as the rule wants. The MAINTAIN rep held the CO-OPS graduate under M9 and M14 correctly and
wrote the ROADMAP line "via a setup/audit split job" with no shape, guessing the landing
place. The fixture itself took three cuts to pass the budget (17, 30, 38, then 40.3 KB):
true-to-code mechanics prose is dense, and a tripwire fixture has to trip.

## Verification

Script-level: the apply on scratch copies of the Arty's ARCHITECTURE and of the fixture
reconstructs each byte for byte; `harness/split-fixture/index.expected.md` is the fixture's
index with `--today 2026-10-12`. Reps: RED four, GREEN four, both through a Workflow at
Sonnet/high. Record: `docs/2026-10-12 - reference-doc-split-red-green.md`.

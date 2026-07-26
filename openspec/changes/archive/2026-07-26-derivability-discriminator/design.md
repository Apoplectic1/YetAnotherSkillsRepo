# derivability-discriminator — design

## Context

The tier model already rejects derivable-fact caches at the *structural* level (no manifest
files; convention-routing; git-as-changelog), and R8 handles plain value drift — but R8's
only remedy is `fix-doc`, which re-caches. The missing piece is claim-level: when is a
stale value worth maintaining at all? Reference docs should carry only what code can't
yield (rationale, contracts, gotchas, expensive cross-file derivations); a rationale-free
count is a grep cached in prose.

## Goals / Non-Goals

**Goals:** reps propose deletion/de-valuing as the default fix for stale rationale-free
derivable trivia; the user adjudicates as always.

**Non-Goals:**
- No autonomous deletion beyond the normal adjudicate-then-apply flow.
- No new flag action or schema field (removal is a `fix-doc` fix-shape).
- Not a license to strip *useful* numbers: contract values (R7 territory), gotcha values,
  and rationale-bearing figures (e.g. a benchmark number justifying a recommendation) are
  explicitly out of the discriminator's reach.
- No MAINTAIN/SETUP text this round (graduation of trivia is rarer; revisit if field
  evidence shows it).

## Decisions

- **D1 — discriminator, not prohibition.** Both conditions must hold: (a) cheaply derivable
  (one grep/read from code), AND (b) rationale-free (no why, no guarantee, no gotcha
  attached). Either fails → normal fix-doc. Form per DOMAIN match-form-to-failure:
  conditional keyed to an observable predicate (reps *comply* today, output has the wrong
  fix-shape → positive recipe/conditional, not a prohibition table).
- **D2 — deletion proposed, value-update offered.** The flag's proposed fix leads with
  removal/reword; the value-update rides as the stated alternative so adjudication is a
  real choice, not a fait accompli.
- **D3 — R28, appended** (IDs append-only), placed thematically in the Currency section.
- **D4 fixture ripple contained.** D4 stays the R25 live-section control (must still be
  *flagged*); only the GREEN fix-shape expectation changes. Add one control cell: a
  rationale-bearing number (e.g. a value tied to a stated why) that must NOT get a deletion
  proposal — guards against over-firing.

## Risks / Trade-offs

- [Over-firing: reps delete useful status values] → two-condition gate + the
  rationale-bearing control cell in GREEN + micro-variants before full reps.
- [RED fails to reproduce (reps already propose deletion)] → no-failure gate: status-note in
  specs, no text ships. Prior evidence (all reps to date re-cached) makes this unlikely.
- [Word growth] → single rule, ~+60–80 words, within precedent.

## Migration Plan

None (no back-compat by policy). Ships dev → RED/GREEN → main → deploy.sh.

## Open Questions

None blocking — final wording after RED classification, per house method.

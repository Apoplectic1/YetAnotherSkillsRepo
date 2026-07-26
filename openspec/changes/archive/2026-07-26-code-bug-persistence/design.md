# code-bug-persistence — design

## Context

AUDIT R3/R4/R7 establish the family's code posture: skills edit documentation only; code
findings are reports (`flag-code-bug`, `revisit-plan`), handed off to the dev/diagnose flow
and `whats-next`; a contract the doc asserts and the code violates makes the *code* the
suspect (never `fix-doc` a contract into agreement with buggy code). Two gaps, both field-hit
2026-07-26 (MAINTAIN-on-TSM, NOTEBOOK entry):

1. "Handed off" has no disk representation — a run's bug flags survive only in the chat.
2. MAINTAIN has no code-bug channel at all: its schema is
   `graduate | keep | archive | prune-only`, so a worker that verifies a journal claim
   against code and finds the code wrong has no in-schema way to say so.

`whats-next` already sweeps ROADMAP open items, dated journal docs, and `flag-code-bug`
outputs as backlog sources — the consumption side exists; only the persistence side is
missing.

## Goals / Non-Goals

**Goals:**
- Surviving report-only flags land in the *target project's* own doc tiers before the run
  ends: one line per bug in ROADMAP § Open + full evidence in a dated
  `docs/YYYY-MM-DD-<skill>-report.md`.
- MAINTAIN gains an in-schema, report-only code-bug channel with R7's cardinal-sin
  protection (code is the suspect; never reclassify the journal claim as stale/archive
  because code disagrees).
- Zero new machinery: reuse the tiers `whats-next` already sweeps.

**Non-Goals:**
- No fix rounds, fix orchestration, or code edits inside any doc skill (honesty posture:
  docs describe contracts; tests/compiler validate them; fixing is dev/diagnose work).
- No new tracking artifact (no `BUGS.md`) — off-charter machinery; ROADMAP § Open *is* the
  backlog surface.
- No whats-next or SETUP text changes.

## Decisions

- **D1 — Persist into the target project's tiers, not a new file.** ROADMAP § Open
  one-liners + dated `docs/` report. Alt considered: dedicated `BUGS.md` (new charter, new
  sweep source, drifts) and chat-only status quo (the field failure). The doc system itself
  is the bug tracker.
- **D2 — Report always; ROADMAP lines for survivors.** The dated report (full flags +
  evidence + coverage note) is mandatory every run that produced report-only flags — that is
  the no-loss guarantee. ROADMAP § Open gets one line per *adjudicated-surviving* bug; if the
  user defers adjudication, a single ROADMAP line points at the unadjudicated report instead
  (so nothing silently vanishes, but unvetted flags don't pollute the backlog).
- **D3 — MAINTAIN channel is an additional report-only flag type, not a fifth classify
  value.** A journal item's disposition (keep/graduate/…) is orthogonal to "the code it
  describes is buggy" — an entry can be `keep` AND evidence of a live bug. Mirrors AUDIT,
  where `flag-code-bug` is an action alongside doc actions. Exact wording finalized after
  RED classifies the failure form (DOMAIN § Match the form to the failure — persistence
  omission is likely a REQUIRED-slot fix; the MAINTAIN channel is a positive recipe).
- **D4 — Contract semantics mirror R7.** Journal claim with contract force
  (must/always/never, or corroborated) violated by code → `flag-code-bug`, code is the
  suspect. Plain drift with no guarantee → normal MAINTAIN classification (the journal
  records history; a stale finding is not a bug report).
- **D5 — Dedup before ROADMAP insert.** The apply step checks the target ROADMAP § Open for
  an existing line on the same defect before adding one (repeat runs must not accrete
  duplicates).
- **D6 — Rule IDs appended, never renumbered** (DOMAIN § Authoring conventions): AUDIT next
  free = R27; MAINTAIN next free = M12 (+M13 if channel and persistence split cleanly).

## Risks / Trade-offs

- [ROADMAP § Open bloat on frequent runs] → D5 dedup + one-line format + survivors-only
  (D2); the report carries the detail, not ROADMAP.
- [Rule derived from a field finding on TSM] → per VERIFICATION method rule, text ships only
  via synthetic RED→GREEN on TidePool with a **new plant class** (journal-claim-vs-buggy-code
  cell + a persistence cell); plants are not derived from TSM specifics, so the fixture stays
  non-poisoned for this rule.
- [RED may not reproduce (agents might persist unprompted)] → then the no-failure gate
  applies: status-note in specs, no text ships (family precedent: 2026-07-07 right-sizing).
  RED reps must include a mutating MAINTAIN run whose bug flags' fate is observable on disk.
- [Word-count growth in two SKILL.md files] → keep within family precedent (~+100 words per
  skill max); hybrid-rulebook form keeps rules one bullet each.
- [Target project lacks a ROADMAP/docs convention (never SETUP)] → out of scope: AUDIT and
  MAINTAIN already assume the docs-architecture conventions (SETUP must have run first).

## Migration Plan

None (no back-compat by policy): text ships via `dev` → RED/GREEN → `main` → `deploy.sh`.
Rollback = redeploy prior `main`.

## Open Questions

None blocking — final rule wording deliberately deferred to the RED failure classification.

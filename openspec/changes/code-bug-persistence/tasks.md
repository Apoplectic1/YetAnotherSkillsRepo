# code-bug-persistence — tasks

## 1. Fixture — new plant class (non-derived from TSM)

- [ ] 1.1 Extend `harness/tidepool-fixture/` with a journal-claim-vs-buggy-code plant: a
      dated journal entry asserting a contract (must/always/never) that the fixture's code
      visibly violates (catalog id CB1), plus a control entry with plain no-contract drift
      (CB2, must NOT flag)
- [ ] 1.2 Add a persistence-observability cell: fixture ROADMAP with an § Open section
      (empty of bug lines) so RED/GREEN can check on disk whether flags landed (CB3), and
      one pre-existing open bug line to test dedup (CB4)
- [ ] 1.3 Record CB1–CB4 in `harness/catalog-tidepool.md` with expected outcomes per skill

## 2. RED — current skill text (1–2 reps per arm)

- [ ] 2.1 RED MAINTAIN rep(s) on the fixture copy: observe how bug evidence is (mis)handled
      with no in-schema channel — capture verbatim rationale; verify on disk that nothing
      persisted (reset contract after each mutating rep)
- [ ] 2.2 RED AUDIT rep(s): run to apply with `flag-code-bug` findings adjudicated real;
      verify on disk whether report/ROADMAP lines exist (expected: chat-only loss)
- [ ] 2.3 Classify each RED failure per DOMAIN § Match the form to the failure (omission →
      REQUIRED slot; wrong shape → positive recipe); if a rep persists unprompted, invoke
      the no-failure gate for that half (status-note, no text)

## 3. Candidate text

- [ ] 3.1 Draft AUDIT R27 (persistence rule: dated report + ROADMAP § Open survivors +
      deferred-pointer + dedup) and the step-5 wording touch; IDs append-only
- [ ] 3.2 Draft MAINTAIN M12 (code-bug channel, R7-mirror cardinal-sin protection) and M13
      (persistence, same contract as R27); flag-schema row addition
- [ ] 3.3 Word-count check both SKILL.md deltas against family precedent (~+100 words/skill)

## 4. GREEN — candidate text injected

- [ ] 4.1 GREEN MAINTAIN rep(s): CB1 flagged report-only with claim+code evidence, journal
      entry NOT demoted; CB2 clean; report + ROADMAP § Open lines disk-verified; CB4 not
      duplicated
- [ ] 4.2 GREEN AUDIT rep(s): same persistence checks through apply; deferred-adjudication
      variant produces the single pointer line
- [ ] 4.3 Apply reset contract after every mutating rep (`git reset --hard <marker> &&
      git clean -fd`)

## 5. Ship

- [ ] 5.1 Apply validated text to `skills/docs-architecture-audit/SKILL.md` and
      `skills/docs-architecture-maintain/SKILL.md` on `dev`
- [ ] 5.2 Record RED/GREEN provenance entry in `docs/docs-architecture-design.md`; scorecard
      to a dated `docs/` record or NOTEBOOK; update ROADMAP Recently-shipped; disposition
      the NOTEBOOK 2026-07-26 field entry (stub → pointer once graduated)
- [ ] 5.3 `openspec sync` / archive the change (`--yes`, judge by output text); merge
      `dev` → `main`, `deploy.sh`, push mirror

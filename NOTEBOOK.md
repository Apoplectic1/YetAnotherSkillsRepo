# NOTEBOOK.md — lab notebook

**Charter:** chronological empirical findings from working on the skills — small
observations that don't warrant a standalone dated note. Newest at the top. Substantial
records go to `docs/YYYY-MM-DD-<slug>.md` (existing example: the 2026-06-29 audit
worker-model benchmark).

- 2026-07-10 — **first self-audit** (AUDIT on this repo: 4 rounds, 16 workers,
  Sonnet→Opus→Fable; 36 findings, zero code-contract violations). Lessons: (a)
  **running-commentary tense is the dominant staleness class** (17 of 18 design-doc flags) —
  "awaits / in-flight / queued" rots within days; write past-tense immediately or stamp a
  date. Systemic cure: the SETUP-spec survey is now an explicit dated derivation snapshot.
  (b) **Model diversity beat same-model reps**, exactly as the 2026-06-29 benchmark
  predicted — 17/9/10 new finds per tier, each catching what the prior tier's dry rounds
  missed. (c) **Mid-audit edits ripple** — adding VERIFICATION's third method rule made
  README's "two lessons" stale within the hour (caught by the loop, round 3). (d) `deploy.sh`
  was add/refresh-only — a renamed skill would have left a stale live copy; now
  marker-stamps + prunes.
- 2026-07-07 — **openspec CLI gotchas** (hit during the round-2 archive): (a) the spec
  validator requires SHALL/MUST on a requirement's **lead line** — put the normative verb in
  the first sentence, not after a "When…" clause; a requirement only gets validated when its
  file is *updated*, so offenders can hide in specs created by an earlier change. (b)
  `openspec archive` **exits 0 on validation abort** — check the output text, never the exit
  code, and don't chain it with `&&`.

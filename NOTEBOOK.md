# NOTEBOOK.md — lab notebook

**Charter:** chronological empirical findings from working on the skills — small
observations that don't warrant a standalone dated note. Newest at the top. Substantial
records go to `docs/YYYY-MM-DD-<slug>.md` (existing example: the 2026-06-29 audit
worker-model benchmark).

- 2026-07-13 — **fat-router-lean backlog item refined** (disposition of the user's held
  q1.txt question, now deleted; source: ecological field finding 1 — both skill generations
  left a 24 KB router's glossary/contract weight in place, and the audit didn't placement-flag
  it). Two linked pieces, both gated on RED→GREEN: **(a) lean rule** — SETUP relocates
  off-charter router weight to charter-selected reference docs on encounter (glossary →
  DOMAIN.md; abbreviations-for-CLI-use are an authoring convention, squarely DOMAIN charter),
  plus one AUDIT clarifying clause making the router itself explicitly placement-audited.
  Leaning: content test ("reference content vs routing/gotchas") over a numeric size
  threshold, with the ~40 KB perf line as the *why*. Est. ~450–500k subagent tokens
  (SETUP 2+2 reps + narrow AUDIT probe; `harness/tidepool-fixture` + fat-router variant —
  not poisoned: rule derives from the TP ecological run, not TidePool). **(b) B4 amendment**
  — portfolio-shared DOMAIN.md at a container root (user's Astronomy-portfolio glossary
  idea): collides with shipped B4 ("router only; portfolio-level set is noise"), so it's a
  rule change with a single-sourcing design question (per-project DOMAIN.md cross-refs up?).
  Cheap probe first: run SETUP at `E:\Projects\VisualStudio\Astronomy` and observe (expected:
  router-only per B4; old non-portfolio projects get B3 flag-and-skip lines — not a blocker).
- 2026-07-10 — **openspec archive prompts interactively** (third CLI gotcha, joins the
  2026-07-07 pair): `archive` asks "Proceed with spec updates?" and dies in a
  non-interactive shell ("User force closed the prompt", exit 1 — *after* printing
  "Task status: ✓ Complete"). Run `openspec archive <name> --yes`; keep judging by output
  text, never exit code.
- 2026-07-10 — **AUDIT worker-death hardening** (field RED: TSM's `tsm-docs-audit` run,
  `wf_ed9d6885-ddb` — a Round-1 section worker (ROADMAP.md 73-260) died on an API
  `server_error` mid-response; the script's `filter(Boolean)` absorbed the null: no retry, no
  named gap). Synthetic RED on a non-derived fixture split 1/2 — the omission is
  non-deterministic, text ships. Wrinkle worth keeping: hand-rolled JSON parsing is what
  *organically* prompts retry thinking; the real `schema` API moves validation to the tool
  layer, leaving `agent()→null` as the sole failure surface — exactly the path forgotten in
  the field. GREEN 2/2 (retry-once keyed on null/throw; coverage note naming dead spans +
  what covered them). Skill: step 1 retry-once, step 3 coverage note, one mistakes bullet.
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

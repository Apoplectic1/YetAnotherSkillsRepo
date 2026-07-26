# m9-hold-on-bloat — design

## Context

M9 today: "Don't over-graduate — and never graduate into an already-bloated reference doc:
an oversized target is a **setup/audit split job first**, not more content." The TSM field
RED shows the gap is procedural: the rep classified correctly, then at apply time had no
sanctioned disposition for "graduate whose target is bloated" — so it applied and flagged
after. The failure class (DOMAIN table) is *knows the rule, skips it under pressure* →
prohibition + red-flag, paired with a positive hold-recipe so the graduate has somewhere
legitimate to go (the M13 report infrastructure shipped earlier today makes the hold cheap).

## Goals / Non-Goals

**Goals:** a bloated target never gains content from a sweep; held graduations survive on
disk (report + ROADMAP line); the split stays a separately-adjudicated job.

**Non-Goals:**
- MAINTAIN does not perform the split (M9 already assigns it to setup/audit; structural
  surgery mid-sweep is scope creep).
- No numeric bloat threshold in skill text — the content test stands (fat-router-lean
  precedent: content test over size threshold, the ~40 KB perf line is the *why*).
- No change to classification (graduate stays graduate — only the apply disposition changes).

## Decisions

- **D1 — harden M9 in place + append M14** (R21 precedent for in-place hardening; IDs
  append-only for the new procedure). M9 carries the prohibition + red-flag ("stuff-then-ask
  is the failure, not compliance"); M14 carries the positive recipe (hold → report + ROADMAP
  split-job line → split as its own job → promote into split homes). Prohibition alone
  invites a new rationalization ("so I'll just drop the graduate"); the recipe closes it —
  M8's never-lose-the-why applies to held graduations too.
- **D2 — hold rides M13's persistence rails.** Held graduations are entries in the dated
  maintain report (full standing-claim + target + disposition) plus one ROADMAP open-line
  for the split job (not one line per held graduate — the report carries the list).
- **D3 — RED shape: prompt-only probes + one on-disk rep.** Fat-router taught that small
  synthetic fixtures under-reproduce scale-dependent failures (0/3 small vs 2/2 real). A
  prompt-only scenario probe (t3/R21 precedent) states the target's size/shape explicitly,
  removing the scale problem from RED; one on-disk rep against a genuinely fattened TidePool
  ARCHITECTURE (~25 KB+, generated) confirms the behavior where file reality, not framing,
  carries the signal. GREEN mirrors both.
- **D4 — non-derived fixtures only.** TSM (the deriving project) is poisoned for this rule;
  TidePool + prompt scenarios are the validation surface.

## Risks / Trade-offs

- [RED under-reproduces on synthetic scale] → D3's two-shape RED; if both shapes pass clean,
  the no-failure gate applies (status-note, no text) despite the field evidence — the field
  RED then argues for a real-project probe before retry, not for shipping untested text.
- [Over-holding: reps hold graduations to healthy docs] → GREEN control: a normal-sized
  target must still receive its promotion in the same run.
- [Held graduations forgotten] → they persist in the report + the ROADMAP split-job line is
  exactly what `whats-next` sweeps; the follow-up is tracked, not remembered.

## Migration Plan

None (no back-compat by policy). Ships dev → RED/GREEN → main → deploy.sh, batched with
`derivability-discriminator`.

## Open Questions

None blocking — final wording after RED classification, per house method.

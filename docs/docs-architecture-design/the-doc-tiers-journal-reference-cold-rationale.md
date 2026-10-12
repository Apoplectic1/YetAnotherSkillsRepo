# docs-architecture-design: The doc tiers: journal · reference · cold rationale (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § The doc tiers: journal · reference · cold rationale" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## The doc tiers: journal · reference · cold rationale

Resolves the two-patterns tension. (Latent already — `NOTEBOOK.md`'s own header says
findings "should graduate into DOMAIN.md / ROADMAP.md"; this formalizes it.) **Refined
2026-06-28 (the CC-tuning split) from two tiers to three** — adding *cold rationale* for
lengthy evergreen "why" that isn't needed for immediate reasoning.

```
JOURNAL  (capture; the user's divide-and-conquer instinct — KEEP IT) — THREE members
  (two at first; CHANGELOG since 2026-07-12), each with an overflow directory since 2026-09-26:
  • docs/YYYY-MM-DD - <name>.md = per-topic substantial dated records (decision/review/design;
                               the project's stated pattern, older files keep the hyphen form)
  • NOTEBOOK.md              = the running lab notebook (short chronological empirical findings)
  • CHANGELOG.md             = shipped units, dated, newest first
  • NOTEBOOK/, CHANGELOG/     = a journal's rolled-over periods: frozen files by first date + INDEX.md
  split: small finding-from-doing-the-work → NOTEBOOK; shipped unit → CHANGELOG;
  substantial standalone record → docs/
  append-only · dated · never retconned (edits only via graduation-prune) · legibly historical
  answers "what did we decide/find on date X"
        │  GRADUATE: fold standing truth upward, then PRUNE the source;
        │  the dated entry remains as the why/when record (or → archive/)
        ▼
REFERENCE  (truth; the ONE always-current source per topic)
  ROADMAP · ARCHITECTURE · DOMAIN · VERIFICATION
  topic-organized · edited in place · superseded prose deleted
  answers "what is true about subsystem X right now"
        │  EXTRACT: lengthy evergreen *reasoning* not needed for immediate
        │  reasoning → a dated cold doc + a one-line reference back
        ▼
COLD RATIONALE  (the *why*, kept but off the daily path)
  docs/YYYY-MM-DD-<topic>-rationale.md
  dated · evergreen reasoning · referenced, never inlined
  answers "WHY is this the right principle" (signal-processing / design theory)
```

Journal = retrieval + capture; reference = synthesis + truth; cold rationale = the lengthy
*why* a reference decision is correct, parked so the daily-path doc stays scannable.
**Graduation (with prune) is what stops the journal becoming the stale pile that defeats
synthesis.** Pruning is the linchpin: graduate without deleting the source and you've created
the duplication you were avoiding.

**The extract discriminator (what's safe to cold-store).** Extract to cold rationale ONLY
content that is BOTH (a) **cold** — not needed for immediate reasoning — AND (b) **evergreen
reasoning**, not code-coupled: it explains *why a principle holds* and would still be true if
the code were never written. Anything naming a **file / function / flag / value** stays in the
audited reference tier. (CC worked example: "why high sigma sheds the noise tail" / "denoise
late" → cold doc; `configureAutoCC` → ROADMAP; `ccDarkK = 18` → DOMAIN.) Extract
**selectively** — fragmentation hurts synthesis, so split only when the why is genuinely
lengthy *and* cold.


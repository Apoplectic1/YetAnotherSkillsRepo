# DOMAIN.md — consumers, posture & authoring conventions

**Charter:** the human/strategy home — who these skills serve, the honesty posture, when to
reach for each skill, and authoring conventions. Not mechanics (`ARCHITECTURE.md`) or
process records (`docs/`).

## Consumer portfolio
Built for a solo dev maintaining a constellation of related projects; the skills themselves
are project-agnostic. **First customers:** the Astronomy constellation — TargetPlanner,
TargetSchedulerManager, Library, XisfFileManager, IntervalScheduler — plus WBPP itself
(`WBPP_BXT_NSG`, the genesis project).

## Honesty posture
- The skills don't make the agent *smarter* at judging docs — RED baselines showed capable
  agents judge individual items well unguided. The value is **completeness, consistency,
  trustworthy structure**: the same layout in every project, outputs that don't quietly
  miss things, a manifest of what was/wasn't checked.
- **SETUP is the keeper** — cheap, one-time, high-ROI; adopt unconditionally. AUDIT /
  MAINTAIN / whats-next are **occasional power tools** (each fans out subagents — real
  token cost): decision-point tools, not rituals. Running them out of obligation is
  process-theater.
- **Not a cross-project contract validator** — docs *describe* contracts; *tests* and the
  *compiler* validate them. Not a substitute for deciding or designing.
- **Stale docs are worse than none** (the agent trusts them). The structure is
  low-maintenance by construction (git-as-changelog, convention-routing, charter-guards),
  but staying current is the human's job — keep skill text and docs from overclaiming.

## When to reach for each skill
- **SETUP** — new/onboarding project; no router; scattered docs. Idempotent (re-run to
  re-converge). Doesn't judge content correctness (AUDIT's job) or write content for you.
- **AUDIT** — after a refactor/rename; before trusting a doc for a real decision; periodic
  health pass. Proposes, never auto-applies; one pass ≠ coverage (hence its fan-out).
- **MAINTAIN** — the journal has accrued findings worth graduating. Pointless with no
  journal; never graduates into a bloated doc (split first); preserves the why/when.
- **whats-next** — session planning; "am I seeing everything?". Proposes priority, you own
  the call. Run AUDIT first when doc currency is in doubt — stale docs → stale backlog.

## Authoring conventions
- Author skills with the `superpowers:writing-skills` skill (naming, frontmatter, structure).
- LF line endings (enforced via `.gitattributes`).

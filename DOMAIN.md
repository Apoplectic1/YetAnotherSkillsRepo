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
Vendored 2026-07-26 from `superpowers:writing-skills` v6.2.0 (plugin since retired; upstream
distribution: the `claude-plugins-official` marketplace). That skill's *testing* half was
already absorbed into this repo's RED/GREEN harness — `VERIFICATION.md` is the authority
there; this digest is the *authoring* half. Frozen snapshot: upstream updates no longer flow.

### Frontmatter & naming
- Two YAML fields only: `name`, `description` (≤1024 chars total).
- `name`: letters/numbers/hyphens; verb-first, named for the action or core insight
  (gerunds work well for processes).
- `description`: third person, starts "Use when…", **triggering conditions only** — concrete
  symptoms/situations and keywords an agent would search for; aim <500 chars. **Never
  summarize the skill's workflow** — a description that sketches the process becomes a
  shortcut the agent follows *instead of reading the body* (empirically observed upstream:
  a workflow-summarizing description caused one review where the body's flowchart required two).

### Body shape
- Overview states the core principle in 1–2 sentences; when-to-use lists symptoms *and* when
  NOT to use; quick-reference table for scanning; common-mistakes section.
- Token economy: heavy reference (100+ lines) goes to a separate file, everything else inline;
  one excellent example beats many; no narrative storytelling ("in session X we found…"); no
  multi-language example dilution.
- Flowcharts ONLY for non-obvious decision points or loops agents exit too early — never for
  reference material, code, or linear steps.
- Cross-reference other skills by name with explicit requirement markers (`**REQUIRED:** …`);
  never `@`-links (they force-load, burning context).

### Match the form to the failure (rule-writing)
Classify the RED failure before wording the fix — the form that bulletproofs one failure type
measurably backfires on another:

| Baseline failure | Right form |
|---|---|
| Knows the rule, skips it under pressure | Prohibition + rationalization table + red-flags list |
| Complies, but output has the wrong shape | Positive recipe/contract — state what the output IS |
| Omits an element from something it already produces | REQUIRED slot in the template it fills |
| Behavior should depend on a condition | Conditional keyed to an observable predicate |

No nuance clauses — "unless it matters" reopens the negotiation. Exemption clauses don't
scope ("doesn't apply to X" still suppresses X) — restructure so the rule can't reach the
exempt part.

### The iron law
No skill change without a failing test first — new skills AND edits, no
"simple addition" exceptions. RED baseline before writing, GREEN with candidate text,
refactor to close the loopholes testing exposes. When iterating wording, micro-test variants
(fresh-context reps + a no-guidance control; read every flagged match manually) before full
scenario runs. This repo's implementation of the law **is** the harness: `VERIFICATION.md`.

### Repo mechanics
- LF line endings (enforced via `.gitattributes`).

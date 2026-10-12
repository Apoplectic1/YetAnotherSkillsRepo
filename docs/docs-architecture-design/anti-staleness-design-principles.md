# docs-architecture-design: Anti-staleness design principles (part of ../docs-architecture-design.md)

> One topic of `../docs-architecture-design.md`, split out on 2026-10-12 when the file passed its
> budget; the heading keeps its text, so "docs-architecture-design § Anti-staleness design principles" resolves by grep over
> the file and `docs-architecture-design/`. The index is `../docs-architecture-design.md`.

## Anti-staleness design principles

Staleness danger scales as **(how always-on) × (how duplicated) × (how volatile / code-coupled)**.
Antidotes, in severity order:

1. **Keep the always-on layer thin + routing-only.** A wrong fact in CLAUDE.md/MEMORY is in
   the agent's head *before it reads anything*, every session. Push volatile detail **down**
   into on-demand reference docs read fresh. (= the "always-on lean," approved.) Since
   2026-10-12 the layer is a scope, not a size: an item stays always-on only if every
   session launched there needs it and it changes less often than the audit cadence; the
   chain a session loads is measured (the section "Always-on budget" below).
2. **Single-source every fact; cross-reference, never copy.** Duplication is the #1 drift
   source. Charters enforce one home per fact.
3. **Make currency legible.** Dated journal files are *good* here (self-evidently snapshots).
   The danger is **undated reference prose** silently gone stale → use grep-pointers ("grep
   the headers, they drift" — WBPP's ARCHITECTURE.md did this at survey time) or
   last-verified stamps on volatile sections.
4. **Docs describe *why / contract*, not line-by-line *how*.** The tighter prose mirrors exact
   code, the faster it rots; point at code (always current) for the "how."
5. **Cold rationale (tier 3) stays evergreen-only.** Lengthy "why" extracted to a dated cold
   doc must be *reasoning*, never code-coupled facts. The AUDIT skill **currency-checks the
   reference tier against code**, but only **decision-consistency-checks** cold docs (does the
   reasoning still match the decision?) — so a code-coupled fact parked in a cold doc escapes
   the currency sweep (stale-prone *and* unaudited). Extract selectively; fragmentation hurts
   synthesis.

**`archive/` — strict archival-only convention (user, 2026-06-28).** `archive/` holds **only
not-current-design-relevant** material — superseded / done / obsolete. It is **deletable without
losing current information**; **git is the backstop** for the history. Nothing an agent needs for
*current* work lives here. The routing **test** is exactly that criterion — *"still
current-design-relevant?"* No → `archive/` (or just let git hold it); Yes → it stays in the live
set (journal / reference / a short ROADMAP digest). Physical separation makes the tier legible.
(Distinct from `openspec/changes/archive/`, OpenSpec's completed-change store.)

**Shipped history / "changelog": `CHANGELOG.md`, journal tier (user, 2026-07-12 — supersedes
the 2026-06-28 "git is the changelog / no CHANGELOG.md" rule; decision record:
`docs/2026-07-12-changelog-convention-adopted.md`).** Shipped history lives in **`CHANGELOG.md`**
— append-only, dated, newest first, never currency-audited; created when history accrues
(conditional, like README). `ROADMAP.md` keeps only a short "Recently shipped" digest plus a
one-line pointer; never a long dated history embedded in ROADMAP. Unchanged: **never route
shipped-history into `archive/`** (a still-referenced changelog isn't archival), and git remains
the commit-level backstop — the changelog holds the curated *story* (design summaries, test
counts, rationale) that `git log` doesn't. The three-way journal split: finding → NOTEBOOK ·
shipped unit → CHANGELOG · substantial record → `docs/YYYY-MM-DD-*.md`. (The old rule's
"redundant with git" rationale fell against curated real-world history — RED→GREEN round 3,
`docs/2026-07-13-round3-red-green-results.md`.)

**Journal rollover (user, 2026-09-26; change `journal-rollover`).** A journal is one file
that grows forever, and judged archival (M3) breaks the dated citations the reference tier
makes into it. So a journal past its budget (40 KB by default, about 10k tokens: one read
unit, one worker's slice) rolls its oldest whole days into a directory named for the file
(`NOTEBOOK/`), one frozen file per period named by its first date, each under the budget,
half the budget kept live; entries move byte for byte; an `INDEX.md` lists every rolled entry
by date and title (a bold-lead bullet under a bare date heading is an entry titled by its bold
run, so a journal in that form reads as a router; change `rolled-index-titled-entries`,
2026-10-12) and never goes stale, since the files it indexes never change. A dated citation resolves by
grep over the file and the directory, so no pointer changes. Open threads are carried into
the live file before their entry rolls; a graduate from a rolled entry takes `cross-ref` in
the reference doc or `stub`, never an edit; a sweep records the newest rolled file it covered
and the next reads only what is newer. The scripts ship with the maintain skill. Piloted on
seven journals of the HDL tree the same day; the prerequisite found there: a container root
that ignores `/*/` drops the overflow directory silently, so a container's ignore file names
its repositories (SETUP B6).

**Reference-doc split (user, 2026-10-12; change `reference-doc-split`).** The overflow
rule's other half. A reference doc past the same budget whose weight is many `##` topics
splits by heading into a directory named for it (`ARCHITECTURE/`), one charter'd file per
topic, bodies byte for byte, the doc itself left as the index (charter, split note, one line
per part); the router keeps naming the doc, and a heading keeps its text so a section
citation ("ARCHITECTURE § Build chain") resolves by grep over the file and the directory.
Never below `##`: a single topic past the budget stays one part. A heading needs no judgment
and never drifts, as a date range does not; the shape avoided is a redistribution by charter
into sibling docs, which a consumer's own split showed makes two homes for one truth. A doc
bloated by cold rationale extracts instead (T3); a design doc in a code-light project stays
whole (B5). MAINTAIN's held promotions (M14) land in the part their heading names; AUDIT
reaches the parts through the index. `split_doc.py` ships with the setup skill; dry-run on
the Arty's 70 KB ARCHITECTURE (seven topics, 71 section citations listed) is the derivation
evidence, the apply queued as consumer work.

OpenSpec role: **workflow/task only** (explore / propose rituals). It is *not* a third
knowledge home — durable knowledge stays in `.md` docs. `openspec/specs/` stays sparse by
choice. (Decision records like the NSG-drizzle note belong in `docs/`, not as spec deltas —
the friction that surfaced this.)

`graphify-out/` — **deleted** 2026-06-28 and not used for this project: a static graph
snapshot competes with always-current native tools, is low-value at this repo's scale, and its
staleness actively works against the meta-goal (it asserts relationships authoritatively).


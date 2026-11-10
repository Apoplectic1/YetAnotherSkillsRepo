# github-distribution Specification

## Purpose
The public GitHub distribution channel for this skills repo (`github.com/Apoplectic1/YetAnotherSkillsRepo`): what the public README must contain, the license, remote/push mechanics, and the consumer update flow. Distribution only — the local repo remains the source of truth.

## Requirements

### Requirement: Public README at repo root
The repo SHALL carry a root `README.md` written purely for public GitHub consumers —
potential-user-focused only — containing in order: a hero, a four-skill table, a Quick Start,
a **Why docs-architecture?** section, an **Updating** section, a **Usage Notes** section, a
short repo-layout orientation (product vs. development workshop), and a license line.

#### Scenario: The three requested sections are present
- **WHEN** the README is inspected for structure
- **THEN** it contains "Why docs-architecture?", "Updating", and "Usage Notes" sections
  whose content roles match the OpenSpec README exemplar (problem-first bullets; procedural
  pull+deploy steps; advisory subheadings)

### Requirement: The README's opening takes a stranger from the skills to a first run
The README's hero SHALL carry the name, a one-liner and one philosophy line; its four-skill
table (`docs-architecture-setup`, `docs-architecture-audit`, `docs-architecture-maintain`,
`whats-next`) SHALL say what each does and when it triggers, introduced as standard Agent
Skills (open format, linked to agentskills.io); and its Quick Start SHALL give the
requirements, the clone, `bash deploy.sh` and the first run.

#### Scenario: Stranger can install and run
- **WHEN** a reader who has never seen the repo follows README top to bottom
- **THEN** they learn what the four skills do, install them with clone + `bash deploy.sh`,
  and know to ask Claude Code to set up their project's docs as the first action

### Requirement: The README's Why section is problem-first, with no evidence figures
The README's **Why docs-architecture?** section SHALL be problem-first and plain-language,
with no benchmark figures and no links into internal evidence docs.

#### Scenario: The Why section carries no benchmark figure
- **WHEN** the README's **Why docs-architecture?** section is read
- **THEN** it opens on the problem in plain language, and it carries no benchmark figure and
  no link into an internal evidence doc

### Requirement: The README's Usage Notes cover models, conventions, safety and portability
The README's **Usage Notes** section SHALL cover model selection, the conventions assumed,
the safety properties, and a Beyond-Claude-Code portability subsection.

#### Scenario: Cross-tool consumer
- **WHEN** a reader using a non-Claude-Code agent (e.g. Gemini CLI, Codex, Cursor) reads the
  README
- **THEN** they learn the skills are standard Agent Skills, find the live compatibility list
  (agentskills.io client showcase), know to copy `skills/*/` into their tool's documented
  skills directory, and see the degradation caveats (Claude model tiers; sequential passes
  without subagent orchestration) and the CLAUDE.md-router adaptation before relying on the
  skills there

### Requirement: Development minutiae stay out of the README but for the repo-layout paragraph
The README MUST NOT carry development/testing minutiae — benchmark numbers, skill-internal
rules, RED/GREEN mechanics, fixture detail — anywhere except the single repo-layout paragraph,
which is the one place the workshop (`docs/`, `harness/`, `openspec/`) is described and which
MUST label fixture projects under `harness/` (e.g. TidePool) as fictional test targets with
planted defects, not templates or examples.

#### Scenario: Fresh observer meets the fixture
- **WHEN** a reader browsing the public tree encounters `harness/tidepool-fixture/` (a
  fictional project with deliberately planted defects)
- **THEN** the README's repo-layout paragraph has already told them it is a test target for
  the skills — fictional, defect-seeded, not a template or example — and no other README
  section mentions fixtures or testing mechanics at all

### Requirement: The README's portability claims stay within the verified ecosystem
Portability claims MUST stay within the verified Agent Skills ecosystem (named adopters
verified against agentskills.io; no chat/answer engines).

#### Scenario: Only verified adopters are named
- **WHEN** the README names the tools the skills run in beyond Claude Code
- **THEN** each named tool is an adopter agentskills.io lists, and no chat or answer engine
  is named

### Requirement: MIT license
The repo MUST carry an MIT `LICENSE` file at the repo root, and the README's license section MUST name MIT.

#### Scenario: License present and consistent
- **WHEN** the repo root is listed and the README read
- **THEN** `LICENSE` exists with MIT text (copyright holder = the repo owner) and README says MIT

### Requirement: Distribution remote publishes main only
The repo SHALL have an `origin` remote pointing at `github.com/Apoplectic1/YetAnotherSkillsRepo` (renamed from `docs-architecture` 2026-07-10; GitHub redirects the old name), and publication SHALL push only `main` (the distribution-ready ref); `dev` remains a local authoring branch.

#### Scenario: Publish
- **WHEN** publication runs
- **THEN** `git remote -v` shows `origin` → `Apoplectic1/YetAnotherSkillsRepo`, `main` is pushed with upstream tracking, and no `dev` branch exists on the remote

### Requirement: Consumer update flow is pull plus deploy
The README's Updating section SHALL document the consumer update flow as `git pull` followed by `bash deploy.sh`, and SHALL note that deploy stamps markers and prunes renamed/removed skills so re-running is always safe.

#### Scenario: Consumer updates
- **WHEN** a consumer with a prior install follows the Updating section after skills changed upstream
- **THEN** their `~/.claude/skills/` copies match the pulled `main`, with any renamed/removed skill pruned rather than left stale

### Requirement: README is excluded from the audited reference set
The project CLAUDE.md router SHALL name `README.md` in its excluded-from-the-doc-set list as the public GitHub-facing distribution artifact, so router-anchored audits do not treat it as a charter'd reference doc.

#### Scenario: Audit scope unaffected
- **WHEN** a docs-architecture audit runs on this repo after publication
- **THEN** README.md is out of scope by the router's exclusion list, and no worker currency-audits its marketing copy as reference-doc claims

### Requirement: Skill footers cite provenance by public GitHub URL
Each shipped `skills/*/SKILL.md` SHALL end with a single provenance link — the public GitHub
URL of the canonical design doc (`docs/docs-architecture-design.md` on `main`) — so deployed
copies are self-contained for public consumers. Skill text SHALL NOT cite evidence docs by
author-local absolute path, and benchmark figures ride in skill text as uncited claims (the
benchmark doc is not referenced by name from skill text).

#### Scenario: Deployed skill is self-contained
- **WHEN** a public consumer reads a deployed SKILL.md outside this machine
- **THEN** its only provenance reference is the resolvable GitHub URL of the design doc
  (no `E:\...` or other author-local paths anywhere in the text)

### Requirement: Repo-side descriptions of the citation form match the footer convention
Repo-side descriptions of the citation form (README lab-notebook line, root CLAUDE.md gotcha)
SHALL match the convention "Skill footers cite provenance by public GitHub URL" states.

#### Scenario: The repo describes the footer's form
- **WHEN** the README's lab-notebook line or the root CLAUDE.md gotcha describes how a skill
  cites its provenance
- **THEN** it describes the footer's single public GitHub URL of the design doc, and no
  author-local path

### Requirement: The design doc stays at its published path
The design doc SHALL stay at its published path. Since 2026-10-12 the design doc is the index
of a T5 split (`docs/docs-architecture-design/`) at the same path, so the URL still resolves;
a split keeps the path, a move or a rename does not.

#### Scenario: Design doc stays at its published path
- **WHEN** repo maintenance considers moving or renaming `docs/docs-architecture-design.md`
- **THEN** the root CLAUDE.md gotcha blocks it — the published URL in every deployed skill
  footer must remain valid on `main`; a T5 split, which leaves the file in place as the
  index, is allowed

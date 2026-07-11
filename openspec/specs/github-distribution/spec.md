# github-distribution Specification

## Purpose
The public GitHub distribution channel for this skills repo (`github.com/Apoplectic1/YetAnotherSkillsRepo`): what the public README must contain, the license, remote/push mechanics, and the consumer update flow. Distribution only — the local repo remains the source of truth.
## Requirements
### Requirement: Public README at repo root
The repo SHALL carry a root `README.md` written purely for public GitHub consumers, containing in order: a hero (name + one-liner + one philosophy line), a four-skill table (`docs-architecture-setup`, `docs-architecture-audit`, `docs-architecture-maintain`, `whats-next` — what each does, when it triggers), a Quick Start (requirements + clone + `bash deploy.sh` + first run), a **Why docs-architecture?** section (problem-first, evidence-backed), an **Updating** section, a **Usage Notes** section (model selection, conventions assumed, safety properties), a two-sentence repo-layout orientation (product vs. lab notebook), and a license line. The README MUST NOT restate benchmark numbers or skill-internal rules beyond section 4's few sourced claims — it links to the skill files and evidence docs instead.

#### Scenario: Stranger can install and run
- **WHEN** a reader who has never seen the repo follows README top to bottom
- **THEN** they learn what the four skills do, install them with clone + `bash deploy.sh`, and know to ask Claude Code to set up their project's docs as the first action

#### Scenario: The three requested sections are present
- **WHEN** the README is inspected for structure
- **THEN** it contains "Why docs-architecture?", "Updating", and "Usage Notes" sections whose content roles match the OpenSpec README exemplar (problem-first bullets; procedural pull+deploy steps; advisory subheadings)

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


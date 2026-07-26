# github-distribution — delta: readme-audience-rule

## MODIFIED Requirements

### Requirement: Public README at repo root
The repo SHALL carry a root `README.md` written purely for public GitHub consumers —
potential-user-focused only — containing in order: a hero (name + one-liner + one philosophy
line), a four-skill table (`docs-architecture-setup`, `docs-architecture-audit`,
`docs-architecture-maintain`, `whats-next` — what each does, when it triggers) introduced as
standard Agent Skills (open format, linked to agentskills.io), a Quick Start (requirements +
clone + `bash deploy.sh` + first run), a **Why docs-architecture?** section (problem-first,
plain-language — no benchmark figures and no links into internal evidence docs), an
**Updating** section, a **Usage Notes** section (model selection, conventions assumed,
safety properties, and a Beyond-Claude-Code portability subsection), a short repo-layout
orientation (product vs. development workshop), and a license line. The README MUST NOT
carry development/testing minutiae — benchmark numbers, skill-internal rules, RED/GREEN
mechanics, fixture detail — anywhere except the single repo-layout paragraph, which is the
one place the workshop (`docs/`, `harness/`, `openspec/`) is described and which MUST label
fixture projects under `harness/` (e.g. TidePool) as fictional test targets with planted
defects, not templates or examples. Portability claims MUST stay within the verified Agent
Skills ecosystem (named adopters verified against agentskills.io; no chat/answer engines).

#### Scenario: Stranger can install and run
- **WHEN** a reader who has never seen the repo follows README top to bottom
- **THEN** they learn what the four skills do, install them with clone + `bash deploy.sh`,
  and know to ask Claude Code to set up their project's docs as the first action

#### Scenario: The three requested sections are present
- **WHEN** the README is inspected for structure
- **THEN** it contains "Why docs-architecture?", "Updating", and "Usage Notes" sections
  whose content roles match the OpenSpec README exemplar (problem-first bullets; procedural
  pull+deploy steps; advisory subheadings)

#### Scenario: Cross-tool consumer
- **WHEN** a reader using a non-Claude-Code agent (e.g. Gemini CLI, Codex, Cursor) reads the
  README
- **THEN** they learn the skills are standard Agent Skills, find the live compatibility list
  (agentskills.io client showcase), know to copy `skills/*/` into their tool's documented
  skills directory, and see the degradation caveats (Claude model tiers; sequential passes
  without subagent orchestration) and the CLAUDE.md-router adaptation before relying on the
  skills there

#### Scenario: Fresh observer meets the fixture
- **WHEN** a reader browsing the public tree encounters `harness/tidepool-fixture/` (a
  fictional project with deliberately planted defects)
- **THEN** the README's repo-layout paragraph has already told them it is a test target for
  the skills — fictional, defect-seeded, not a template or example — and no other README
  section mentions fixtures or testing mechanics at all

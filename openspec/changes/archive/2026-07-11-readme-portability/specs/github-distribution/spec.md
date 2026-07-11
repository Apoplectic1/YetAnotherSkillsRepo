# github-distribution — delta spec (readme-portability)

## MODIFIED Requirements

### Requirement: Public README at repo root
The repo SHALL carry a root `README.md` written purely for public GitHub consumers, containing in order: a hero (name + one-liner + one philosophy line), a four-skill table (`docs-architecture-setup`, `docs-architecture-audit`, `docs-architecture-maintain`, `whats-next` — what each does, when it triggers) introduced as standard Agent Skills (open format, linked to agentskills.io), a Quick Start (requirements + clone + `bash deploy.sh` + first run), a **Why docs-architecture?** section (problem-first, evidence-backed), an **Updating** section, a **Usage Notes** section (model selection, conventions assumed, safety properties, and a Beyond-Claude-Code portability subsection), a short repo-layout orientation (product vs. lab notebook), and a license line. The README MUST NOT restate benchmark numbers or skill-internal rules beyond the Why section's few sourced claims — it links to the skill files and evidence docs instead. Portability claims MUST stay within the verified Agent Skills ecosystem (named adopters verified against agentskills.io; no chat/answer engines).

#### Scenario: Stranger can install and run
- **WHEN** a reader who has never seen the repo follows README top to bottom
- **THEN** they learn what the four skills do, install them with clone + `bash deploy.sh`, and know to ask Claude Code to set up their project's docs as the first action

#### Scenario: The three requested sections are present
- **WHEN** the README is inspected for structure
- **THEN** it contains "Why docs-architecture?", "Updating", and "Usage Notes" sections whose content roles match the OpenSpec README exemplar (problem-first bullets; procedural pull+deploy steps; advisory subheadings)

#### Scenario: Cross-tool consumer
- **WHEN** a reader using a non-Claude-Code agent (e.g. Gemini CLI, Codex, Cursor) reads the README
- **THEN** they learn the skills are standard Agent Skills, find the live compatibility list (agentskills.io client showcase), know to copy `skills/*/` into their tool's documented skills directory, and see the degradation caveats (Claude model tiers; sequential passes without subagent orchestration) and the CLAUDE.md-router adaptation before relying on the skills there

export const meta = {
  name: 'audit-model-compare',
  description: 'Compare AUDIT worker accuracy across opus/sonnet/haiku on the TargetPlanner fixture (read-only, fixed fan-out)',
  phases: [
    { title: 'audit:opus', detail: '6 section workers + cross-ref, model=opus' },
    { title: 'audit:sonnet', detail: '6 section workers + cross-ref, model=sonnet' },
    { title: 'audit:haiku', detail: '6 section workers + cross-ref, model=haiku' },
  ],
}

// ---- experiment parameters (held constant across models) --------------------
const PROJECT = (args && args.project) || 'E:\\Projects\\AI\\TargetPlanner'
const MODELS = (args && args.models) || ['opus', 'sonnet', 'haiku']
const EFFORT = (args && args.effort) || 'high'

// ---- structured flag schema (mirrors the AUDIT SKILL.md schema) -------------
const FLAG_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    flags: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          location: { type: 'string', description: 'doc § + quoted phrase' },
          axis: { type: 'string', enum: ['placement', 'currency'] },
          modality: { type: 'string', enum: ['descriptive', 'prescriptive', 'na'] },
          claim: { type: 'string' },
          finding: { type: 'string' },
          evidence: { type: 'string', description: 'file:line / symbol  OR  "unverifiable → ask user"' },
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
          action: { type: 'string', enum: ['fix-doc', 'move-to', 'cross-ref+delete', 'graduate', 'revisit-plan', 'flag-code-bug', 'keep'] },
        },
        required: ['location', 'axis', 'modality', 'claim', 'finding', 'evidence', 'severity', 'action'],
      },
    },
  },
  required: ['flags'],
}

// ---- shared audit rules (the SKILL.md contract, condensed) -------------------
const RULES = `You are a docs-architecture AUDIT worker. Audit on two axes:
- PLACEMENT: does this content belong in CLAUDE.md per its router/charter role (always-loaded router + load-bearing gotchas, kept thin)? Off-charter content that belongs in ARCHITECTURE/ROADMAP/DOMAIN/VERIFICATION/README → action move-to <doc>, or cross-ref+delete if duplicated.
- CURRENCY: is each factual claim still true vs the LIVE code? Classify modality first:
  * descriptive (how it IS — present tense "is/does/returns", architecture/gotchas): code wins. Mismatch = stale doc → action fix-doc. EXCEPTION: if the doc asserts a contract/guarantee (must/always/never/aborts-on-X) and the code VIOLATES it, the CODE is the suspected bug → action flag-code-bug (report-only). NEVER fix-doc a contract into agreement with code you suspect is buggy.
  * prescriptive (how it SHOULD/WILL be — "will/planned/TODO", roadmap-future): the plan wins. Code-not-matching is EXPECTED, never flag as stale. (plan already satisfied → graduate; plan contradicted by structure → revisit-plan.)

CONSERVATIVE EVIDENCE (required): every currency flag carries EITHER a real code citation (file:line or symbol you actually read) OR the literal marker "unverifiable → ask user". NEVER guess stale. Key on content, not filename.

IMPORTANT — sibling library is absent: the Astronomy.Core / Astronomy.NINA sibling library is NOT present in this repo (the csproj references ..\\..\\Library which does not resolve here). If a claim depends on Library code you cannot read, you MUST mark it "unverifiable → ask user" — do NOT guess stale and do NOT assume it is correct.

Verify currency by actually reading and grepping the TP-side source under ${PROJECT}\\TargetPlanner\\ (≈80 .cs files). Cite file:line for every currency verdict.

Return ONLY genuine issues as structured flags. If the section is clean, return an empty flags array. Do not invent issues to fill quota. Do not edit any file.`

function sectionPrompt(title, locateHint, focus) {
  return `${RULES}

PROJECT: ${PROJECT}
TASK: Audit ONLY the section titled "${title}" in ${PROJECT}\\CLAUDE.md. ${locateHint}
Ignore all other sections of CLAUDE.md — other workers cover them.
Focus hints (non-exhaustive — find anything real, not just these): ${focus}

Read the section, then read/grep the relevant TP-side source to verify each factual claim. Emit one flag per real issue in the schema.`
}

const UNITS = [
  {
    key: 'glossary',
    title: 'Glossary',
    locate: 'Covers the Apps/plugins vocabulary and the Architecture/refactor + domain term definitions.',
    focus: 'Do the named types/files (TargetSelection, ChartContext, ChartCoordinator, NightDate, PlanningPolicy, EnsureAsync, etc.) still exist at the cited paths/symbols? Is the "..\\CLAUDE.md" parent-portfolio reference valid (does that parent file exist)? Any term describing code that has since changed shape?',
  },
  {
    key: 'conventions',
    title: 'Conventions worth knowing before editing',
    locate: 'Bullets on RA decimal hours, signed hemispheres, type-alias usings, defaults/settings, Location.Elevation, target sources, CheckedListBox owner-draw, logging/Diagnostics.',
    focus: 'Verify each convention against the actual .cs (e.g. RightAscension type/units, the DupeAwareCheckedListBox subclass, TargetRow wrappers + TargetForRow, Log.Diag categories, settings file paths). Flag any claim the code contradicts.',
  },
  {
    key: 'architecture',
    title: 'Architecture',
    locate: 'The prose + bullets on Selection/Cache/Rendering/Orchestration + the Threading paragraph.',
    focus: 'Do ChartCacheStore axes, EnsureAsync surface, the four IAltitudeSubChart impls, ChartCoordinator pipeline/debounce, and the threading/perf claims match the code? Cite file:line.',
  },
  {
    key: 'deps-build',
    title: 'External dependencies that are easy to miss + Build / run',
    locate: 'Audit BOTH the "## External dependencies that are easy to miss" section AND the "## Build / run" + "## Tool preference for symbol queries" sections (build bullets currently live under Tool preference).',
    focus: 'Verify NuGet package versions, TargetFramework, project/test invocation commands against the .csproj files. PLACEMENT: are the build bullets correctly placed (an empty "## Build / run" heading with build content under "## Tool preference")? Note the sibling-library path claims are unverifiable per the rule above.',
  },
  {
    key: 'core-contract',
    title: 'Core consumer contract',
    locate: 'Guarantees Core makes of consumers: IReadOnlyList returns, DateTime.Kind UTC contract, signed-degree inputs, no static mutable state.',
    focus: 'These claims are about the sibling Astronomy.Core library, which is ABSENT here — apply the unverifiable rule strictly. PLACEMENT: does a detailed Core-API contract belong in the TP router, or in ARCHITECTURE/DOMAIN?',
  },
  {
    key: 'docmap',
    title: 'Documentation map + What this is',
    locate: 'Audit the "## Documentation map" section AND the intro "## What this is" paragraph.',
    focus: 'Does the doc map accurately list the docs that exist (DOMAIN.md, VERIFICATION.md, NOTEBOOK.md, docs/ layout)? Are the routing/exclusion claims true? Are the "What this is" code claims (TargetScanner, SkyCentroid, Button_Graph_Click entry point, GetImageLibraryTargets) current?',
  },
]

function crossrefPrompt() {
  return `${RULES}

PROJECT: ${PROJECT}
TASK: This is the CROSS-REFERENCE pass. Do NOT re-audit section contents. Instead check INBOUND references and links across the whole project tree:
- Every Markdown link / file reference in ${PROJECT}\\CLAUDE.md and the other reference docs (ARCHITECTURE.md, ROADMAP.md, DOMAIN.md, VERIFICATION.md, README.md, RELEASING.md): does the target file/anchor exist? Flag dangling links and rename-orphans.
- The Glossary's "..\\CLAUDE.md" parent-portfolio reference: does that parent file exist relative to ${PROJECT}? (It is one directory up.)
- Code comments or .csproj/.cs references that point at doc files which were renamed/moved.
- Doc-to-doc references that name a section/doc that no longer exists.

For each problem emit a flag (axis=placement or currency as appropriate, action fix-doc or move-to). Cite the referrer file:line and the missing target. Do not edit anything.`
}

// ---- run: fan out all (model × unit) + (model × crossref), max concurrency --
const tasks = []
for (const model of MODELS) {
  for (const u of UNITS) {
    tasks.push(() =>
      agent(sectionPrompt(u.title, u.locate, u.focus), {
        label: `${model}:${u.key}`, phase: `audit:${model}`,
        model, effort: EFFORT, agentType: 'Explore', schema: FLAG_SCHEMA,
      }).then(r => ({ model, key: u.key, flags: (r && r.flags) || [] })))
  }
  tasks.push(() =>
    agent(crossrefPrompt(), {
      label: `${model}:crossref`, phase: `audit:${model}`,
      model, effort: EFFORT, agentType: 'Explore', schema: FLAG_SCHEMA,
    }).then(r => ({ model, key: 'crossref', flags: (r && r.flags) || [] })))
}

const all = (await parallel(tasks)).filter(Boolean)

// ---- group results by model -------------------------------------------------
const byModel = {}
for (const model of MODELS) byModel[model] = { units: {}, totalFlags: 0 }
for (const r of all) {
  byModel[r.model].units[r.key] = r.flags
  byModel[r.model].totalFlags += r.flags.length
}
for (const model of MODELS) {
  log(`${model}: ${byModel[model].totalFlags} flags across ${Object.keys(byModel[model].units).length} workers`)
}

return { project: PROJECT, effort: EFFORT, models: MODELS, byModel }

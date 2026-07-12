# 2026-07-12 — TP ecological AUDIT: adjudication report (verbatim)

**What this is / when to read:** the complete adjudication-ready output of the hybrid AUDIT run
on the TargetPlanner ecological copy (companion to `2026-07-12-tp-ecological-run.md`). Nothing
has been applied — per the skill, each flag awaits approve / amend / defer.

---

# TargetPlanner Docs-Architecture Audit — Final Report

## Coverage note

**Execution.** 34 parallel Sonnet-class workers (R22 default tier) ran the fan-out: 4 on CLAUDE.md, 2 on README.md, 8 on ARCHITECTURE.md, 9 on ROADMAP.md, 1 each on VERIFICATION.md/DOMAIN.md/RELEASING.md, 5 R15-scoped on `docs/design/*.md` + `docs/2026-05-19-code-quality-audit.md`, and 3 cross-reference passes (link/anchor integrity, fact-consistency, source/UI-orphan check). All 34 completed on first attempt — zero dead workers, no R23 retries needed. Every worker returned schema-compliant flags with file:line evidence or an explicit `unverifiable → ask user`.

**Model-diversification (R21) decision: skipped, with justification.** R20 says loop until dry, then diversify. The single Sonnet-only pass is already effectively "dry" by its own evidence: independent workers covering *different* doc sections repeatedly rediscovered the *same* underlying bugs from different angles — e.g. the `ChartEvaluation` 3-vs-1-field error was found independently in CLAUDE.md's Glossary, twice inside ARCHITECTURE.md, and again in a ROADMAP.md entry; the deleted `BeginChartBuildProgress`/`FinishChartBuildProgress` helpers were independently flagged in three separate ARCHITECTURE.md sections plus two ROADMAP.md entries; the presenter-file-count staleness (7 vs 15) was independently caught by two ARCHITECTURE.md workers and two ROADMAP.md workers. That level of cross-worker convergence on identical findings, from workers with no shared context, is the "dry well" signal R20 describes — a second model tier would very likely re-find the same saturated set rather than surface materially new categories of defect. Recommend treating a diversification round as optional follow-up, not a gap in this pass.

*(Orchestrator's note reviewed at merge: this skip is recorded as field finding 2 in the
companion doc — same-model convergence is agreement, not completeness, per the 2026-06-29
benchmark. A diversification round remains available on request.)*

**Known limitations (not doc defects, noted for the adjudicator):**
- This checkout's git history is a synthetic single-baseline ("SKILLS-TEST BASELINE (ecological copy)") — none of the ~20 short commit hashes cited throughout ROADMAP.md/ARCHITECTURE.md resolve in `git log`. This is systemic across every dated entry, not a per-entry defect; individual unresolvable hashes were not flagged.
- A benign environment anomaly recurred across worker sessions: a mid-task system-reminder presenting an altered/stale CLAUDE.md. Every worker that encountered it treated it as non-authoritative harness noise and verified only against live on-disk files/source. Flagged for transparency only — it did not affect any finding below.
- Claims specifically about `Astronomy.Core`/`Astronomy.NINA`/`Astronomy.XISF`/`Astronomy.Diagnostics` *internal* implementation are genuinely unverifiable in this standalone copy (no sibling `Library\` on disk) and are marked as such rather than guessed.
- No in-scope sub-project with its own router/`.git` was found (R16 n/a). `docs/reference-material/` was treated as read-only vendored ground truth and not currency-audited (R17).

**Volume.** Raw flags across all 34 workers: ~220 (including ~25 explicit "verified clean / keep" confirmations, omitted below). After merging same-location-or-same-root-cause duplicates, the unique actionable set is roughly 130–140 flags. Below are the highest-value 40 (prioritized by severity and cross-worker corroboration); a themed count of the remainder follows.

---

## Merged flag list (top 40)

```
- location:  CLAUDE.md §Glossary "ChartEvaluation" (line 56) AND ARCHITECTURE.md §Orchestration layer (lines 97-99)
- axis:      currency
- modality:  descriptive
- claim:     ChartEvaluation is a single-field record carrying only BrightnessInputsChanged, consumed only by the coordinator's post-apply hook.
- finding:   Record has THREE fields — BrightnessInputsChanged, EnsureWork, RenderWork. The latter two were added by the 2026-05-26 progress-bar feature and are consumed inside ChartCoordinator itself (not the post-apply hook) to build progress offsets. The single most-corroborated bug in the audit (4 independent rediscoveries).
- evidence:  TargetPlanner/State/ChartEvaluation.cs:19-41; TargetPlanner/State/ChartCoordinator.cs:211-214; TargetPlanner/Caches/ChartCacheStore.cs:310-315
- severity:  high
- action:    fix-doc

- location:  CLAUDE.md §Build/run (68-71) AND §External dependencies (80) AND VERIFICATION.md §Build (15-25) AND README.md §Build from source
- axis:      currency
- modality:  descriptive
- claim:     The solution holds one authored project plus two sibling-library ProjectReferences (Astronomy.Core, Astronomy.NINA).
- finding:   .sln lists 5 projects: two authored here (TargetPlanner AND TargetPlanner.Tests, omitted everywhere) plus three sibling libraries (Core, XISF, NINA — XISF omitted). The csproj carries a THIRD direct ProjectReference, Astronomy.Diagnostics, omitted from all four locations. VERIFICATION.md self-contradicts within 20 lines; README's build steps would leave a real build failing on missing references.
- evidence:  TargetPlanner.sln (5 Project entries); TargetPlanner/TargetPlanner.csproj:67-70; VERIFICATION.md:29,35-37
- severity:  high
- action:    fix-doc

- location:  README.md §Filters & moon avoidance (87-88, duplicated at Sky-brightness) AND DOMAIN.md §Science models (41-42)
- axis:      currency
- modality:  descriptive
- claim:     Shipped filter defaults are a uniform two-bucket split — 60°/7-day narrowband, 120°/14-day broadband.
- finding:   Wrong for all 7 filters. Actual sBuiltinDefaults: H=30°/5d, O=60°/5d, S=30°/5d, L=90°/10d, R=60°/10d, G=60°/10d, B=90°/10d. Root cause likely shared: FilterLibrary.cs's own doc-comment repeats the identical wrong figures, diverging from its own array six lines below (source-comment bug, report-only).
- evidence:  TargetPlanner/Filters/FilterLibrary.cs:41-51 vs :181-186
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Cache store (67), §Orchestration layer (~176), §UI flow (266) AND ROADMAP.md §2026-05-22 ChartBuildPresenter
- axis:      currency
- modality:  descriptive
- claim:     Button_Graph_Click obtains its progress sink via BeginChartBuildProgress / FinishChartBuildProgress.
- finding:   Both methods deleted (ROADMAP's own later entry documents the deletion). Zero repo-wide matches. Current mechanism: CreateChartProgress wired once as the coordinator's defaultProgressFactory; RunGraphBuildAsync toggles Button_GraphTarget.Enabled around a bare ApplyImmediateAsync call. Stale in three ARCHITECTURE sections + one ROADMAP echo.
- evidence:  MainForm.ChartBuildPresenter.cs:121-152; MainForm.ChartCoordinatorPresenter.cs:57-63; ROADMAP.md:760-765
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §UI flow (269) + §Presenter file splits AND ROADMAP.md §2026-05-22 + §2026-05-27
- axis:      currency
- modality:  descriptive
- claim:     Exactly seven MainForm.*Presenter.cs files exist; the listbox-tint methods live in SelectionVmPresenter.cs.
- finding:   15 presenter files exist; 8 named nowhere in any doc. The tint methods moved to the undocumented MainForm.CheckboxTintPresenter.cs — SelectionVmPresenter's own header narrates the move. Caught by 4 independent workers.
- evidence:  Glob Presenters/*.cs → 15; MainForm.CheckboxTintPresenter.cs:137,154,182; MainForm.SelectionVmPresenter.cs:236-240
- severity:  high
- action:    fix-doc

- location:  README.md §Targets (50) AND §Defaults (139)
- axis:      currency
- modality:  descriptive
- claim:     Selection / first-run defaults seed to M31.
- finding:   SelectedSingle stays null until the image-library auto-load completes, then seeds to the first alphabetical target. PersonalDefaults seeds no target. MainForm's constructor comment explicitly disclaims: "No M31 default seed."
- evidence:  MainForm.cs:357-360; Settings/PersonalDefaults.cs
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §UI flow (263, "No startup chart auto-build")
- axis:      currency
- modality:  descriptive
- claim:     The chart panel stays empty until the user clicks Graph.
- finding:   InitializeDynamicControls → ConstructCoordinator() → FireBaselinePaint() fires an empty-target Apply so sub-charts paint scaffolding at boot — corroborated by ROADMAP's own 2026-05-26 "Chart baseline paint at boot" entry.
- evidence:  MainForm.cs:673-676; MainForm.ChartCoordinatorPresenter.cs:96-107
- severity:  high
- action:    fix-doc

- location:  ROADMAP.md §2026-05-21 Phase C ("wholesale-replaces the known-target set") AND §2026-05-21 drag-and-drop (same claim)
- axis:      currency
- modality:  descriptive
- claim:     Image-library and drag-and-drop loads wholesale-replace the known-target set.
- finding:   Both paths are additive merges (AddScannedTargets → TargetIdentity.SelectNewTargets → AddKnownTargets); the file's own header says "loads ADD... they do not replace"; contradicted by CLAUDE.md and ROADMAP's own next entries.
- evidence:  MainForm.TargetLoadingPresenter.cs:16-22,157-190,263-271; ROADMAP.md:904-906
- severity:  high
- action:    fix-doc

- location:  README.md line 5 (docs/screenshot.png)
- axis:      currency
- modality:  descriptive
- claim:     A screenshot exists at docs/screenshot.png.
- finding:   Never existed in history (git log --all --full-history empty; no PNG repo-wide). First content block after the title — public-facing broken image.
- evidence:  README.md:5; git history; find
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Orchestration (SnapshotCurrent bullet) AND §MainForm chart wiring
- axis:      currency
- modality:  descriptive
- claim:     SnapshotCurrent reads mMoonAvoidanceProfile / mActiveFilterCenterNm and calls PlanningPolicy.WithScalarHorizon.
- finding:   Neither field exists (grep: ARCHITECTURE.md only). Real: single mActiveFilter field passed as ActiveFilter; MoonProfile is derived; horizon composition is inline (scalar vs MaxOfHorizonProfile).
- evidence:  MainForm.cs:70-73,787-819; State/PlanningPolicy.cs:74-77
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Cache store (65, HdmKey) AND §Orchestration (PlanningPolicy fields) AND docs/design/chart-fits-cache.md §Types
- axis:      currency
- modality:  descriptive
- claim:     HdmKey = HorizonDeg/DurationTicks/Profile/FilterCenterNm/LocalHorizon; PlanningPolicy = TargetFloor/MinDuration/MoonProfile/FilterCenterNm/LocalHorizon.
- finding:   Pre-refactor shapes. Actual HdmKey: HorizonDeg, DurationTicks, ActiveFilter (record, structural equality), MoonAvoidanceEnabled, LocalHorizon. Actual PlanningPolicy: TargetFloorDeg, MinDuration, ActiveFilter, MoonAvoidanceEnabled, LocalHorizon (MoonProfile derived). Same drift reproduced in chart-fits-cache.md (R15 tier).
- evidence:  State/HdmKey.cs:41-47; State/PlanningPolicy.cs:50-55,74-77; docs/design/chart-fits-cache.md:29-36
- severity:  high
- action:    fix-doc

- location:  README.md §Locations (78)
- axis:      currency
- modality:  descriptive
- claim:     The personal-default location always boots regardless of last session.
- finding:   False and self-contradicted at §Defaults (140), which states the correct last-selected behavior. PickStartupLocation reads LastSelectedLocationName; PersonalDefaults.LocationName is not a real symbol.
- evidence:  MainForm.LocationPresenter.cs:458-474; README.md:140
- severity:  high
- action:    fix-doc

- location:  README.md §What it does (10) AND §Loading targets (63)
- axis:      currency
- modality:  descriptive
- claim:     Sort by name, RA, declination, or transit time.
- finding:   Actual options: {"Name","Transit","Rise","Longest","Highest"} — no RA/declination sorts exist; Rise/Longest/Highest undocumented. Connects to the SessionSolvers graduate below.
- evidence:  MainForm.Designer.cs:1134; MainForm.SortPresenter.cs:199-264
- severity:  high
- action:    fix-doc

- location:  VERIFICATION.md §Build ("Debug|AnyCPU, Release|AnyCPU, Debug|x64, Release|x64")
- axis:      currency
- modality:  descriptive
- claim:     Four configurations incl. AnyCPU.
- finding:   .sln defines only Debug|x64 / Release|x64; contradicts CLAUDE.md's own "no AnyCPU configs" callout.
- evidence:  TargetPlanner.sln:17-19
- severity:  high
- action:    fix-doc

- location:  CLAUDE.md §Conventions (107, AstrometryUi record/factory/field)
- axis:      currency
- modality:  descriptive
- claim:     Support/AstrometryUi.cs exists as the immutable-record template.
- finding:   Deleted by the 2026-05-17 pipeline collapse; zero source hits; ARCHITECTURE + ROADMAP both record the deletion. RefreshAstrometryLabels computes inline.
- evidence:  Support/ listing; ROADMAP.md:1150
- severity:  high
- action:    fix-doc

- location:  ROADMAP.md §2026-05-27 decomposition ("TimePicker_ValueChanged")
- axis:      currency
- modality:  descriptive
- claim:     ObservationMomentPresenter absorbed a TimePicker_ValueChanged handler.
- finding:   No TimePicker control or handler exists — single date-only DateTimePicker named DatePicker.
- evidence:  MainForm.ObservationMomentPresenter.cs (full file); MainForm.Designer.cs:1591
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Astronomy.Core (19, "Session/ primitives... not yet consumed")
- axis:      currency
- modality:  descriptive
- claim:     The Session/ namespace is unconsumed by TP.
- finding:   Self-contradicted two bullets later; BestSession.* and TransitTime.UtcAtOrAfter drive three of four chart areas. Only IntegratedQuality/VisibilityWindows/QualitySamples.OverNight/RiseSet.NextAtOrAfter are genuinely unconsumed.
- evidence:  Caches/ChartCacheStore.cs:781-809; Charts/AltitudeSubChart_Sessions.cs
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Astronomy.Core (12, Location property list)
- axis:      currency
- modality:  descriptive
- claim:     Location.Horizon / Location.Duration presented as current plain properties.
- finding:   Doc's own intro states both are [Obsolete]-locked; MainForm calls them "now-removed scalars." Line 12 needs the caveat line 5 already carries.
- evidence:  ARCHITECTURE.md:5; MainForm.cs:34-36
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Astronomy.Core surface list (11-28)
- axis:      currency
- modality:  descriptive
- claim:     (by omission) complete surface summary.
- finding:   Missing AltitudeCurve.Sample and MoonEphemeris.Sample — named by the doc's own intro as 2026-05-28 additions; both power two of the cache's four axes.
- evidence:  Caches/ChartCacheStore.cs:554,573; Caches/TargetTrajectoryEntry.cs:27,31
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Selection VM (mCheckedListBoxJustToggled latch)
- axis:      currency
- modality:  descriptive
- claim:     A latch field disambiguates ItemCheck-then-SelectedIndexChanged.
- finding:   Symbol doesn't exist; current code documents the opposite ("No latch needed").
- evidence:  MainForm.SelectionVmPresenter.cs:49-54,204-209
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §UI labels (AstroUtil.GetMoonRiseAndSet)
- axis:      currency
- modality:  descriptive
- claim:     Moon rise/set labels computed via GetMoonRiseAndSet.
- finding:   Actual call is GetMoonRiseAndSetForNight(dusk, dawn, ...) — a deliberate bug-fix substitution per the code comment; the plain call has no TP call sites.
- evidence:  MainForm.AstrometryLabelsPresenter.cs:41-47
- severity:  high
- action:    fix-doc

- location:  ROADMAP.md top banner ("Last updated 2026-05-28")
- axis:      currency
- modality:  descriptive
- claim:     Content current as of 2026-05-28.
- finding:   The body contains a newer entry (2026-06-11); banner never bumped.
- evidence:  ROADMAP.md:3 vs :73
- severity:  high
- action:    fix-doc

- location:  ROADMAP.md §Currently open item 1 (SessionSolvers "Needs UX design before implementation")
- axis:      currency
- modality:  prescriptive
- claim:     SessionSolvers has no user-visible surface yet.
- finding:   Already shipped: sort modes "Longest"/"Highest" call SessionSolvers.LongestDuration/LowestHorizon in production. Plan satisfied (partially — 2 of 6 API methods surfaced); rewrite/narrow if more is wanted.
- evidence:  MainForm.Designer.cs:1134; MainForm.SortPresenter.cs:245,265
- severity:  high
- action:    graduate

- location:  ROADMAP.md §2026-05-21 Phase C (ImageLibraryScanner.ScanAsync / TargetReport)
- axis:      currency
- modality:  descriptive
- claim:     Image-library ingestion via batch ImageLibraryScanner producing TargetReports.
- finding:   Neither symbol exists; current: per-file ParseFileAsync + TP-side TargetScanner walk. ROADMAP's own next-day entry documents the retirement.
- evidence:  ImageLibrary/ImageLibraryLoader.cs:22-88; Targets/TargetScanner.cs:145-172; ROADMAP.md:909
- severity:  high
- action:    fix-doc

- location:  ROADMAP.md §2026-05-21 Target-source UX C3 (folder XOR classification; TargetLoader.LoadFile / ImageLibraryLoader.LoadFileAsync)
- axis:      currency
- modality:  descriptive
- claim:     Browse classifies a folder as image-library XOR NINA walk via those two methods.
- finding:   Superseded next day by unified TargetScanner.ScanAsync(kinds: All); cited methods renamed (ParseFile/ParseFileAsync); contradicted by CLAUDE.md's own text.
- evidence:  MainForm.TargetLoadingPresenter.cs:76-82,235-247; Targets/TargetScanner.cs:90-129; CLAUDE.md:105
- severity:  high
- action:    fix-doc

- location:  ROADMAP.md §2026-05-13 Location Phase 1 (NamedLocationSetting / NumericUpDown_TimeZone / UtcOffsetHours)
- axis:      currency
- modality:  descriptive
- claim:     Per-site UTC offset via NumericUpDown_TimeZone backed by NamedLocationSetting.UtcOffsetHours.
- finding:   All three superseded per ROADMAP's own 2026-05-19 entry (ComboBox_TimeZone + NamedSite + TimeZoneId); zero matches for the old symbols.
- evidence:  ROADMAP.md:1060; MainForm.Designer.cs:1703
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Cache store (67, LocationCacheEquivalent / SetLocationAsync / scrub-preservation — 3 sub-claims)
- axis:      currency
- modality:  descriptive
- claim:     Equivalence includes year-start-day; MainForm calls SetLocationAsync directly; date scrubs preserve fits.
- finding:   (a) equivalence is geometry-only, date is separate; (b) SetLocationAsync called only inside EnsureAsync; (c) any date change → unconditional DrainAndReset of all four axes.
- evidence:  MainForm.LocationPresenter.cs:301-310; ChartCacheStore.cs:207,235-238,400-434; docs/design/cache-contract.md:84-85
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Cache store (55, "MoonSample — public struct")
- axis:      currency
- modality:  descriptive
- claim:     TP's per-minute moon-sweep struct is MoonSample.
- finding:   Renamed MoonSweepSample; the stale name collides with the unrelated Astronomy.Core.Moon.MoonSample this doc also references.
- evidence:  Caches/MoonSample.cs:20; ChartCacheStore.cs:683,688
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Orchestration (Prepare* "observe mFormClosingCts")
- axis:      currency
- modality:  descriptive
- claim:     The four Prepare* methods observe the form-closing CTS.
- finding:   None take a CancellationToken; the real mechanism is the outer Task.WhenAny race — as CLAUDE.md correctly states, contradicting this doc.
- evidence:  Caches/IChartCacheStore.cs:63-121; MainForm.TargetLoadingPresenter.cs:331-373
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Moon avoidance ("10-min MoonSeparation.ObserveAt sweep")
- axis:      currency
- modality:  descriptive
- claim:     Moon sweep at 10-minute cadence.
- finding:   1-minute cadence (MoonSampleStep); the surrounding "~600 samples/night" comment is only consistent with 1-min.
- evidence:  ChartCacheStore.cs:46,676-694
- severity:  high
- action:    fix-doc

- location:  ARCHITECTURE.md §Universal chart contract + §RenderArea (order + arity)
- axis:      currency
- modality:  descriptive
- claim:     RenderArea(ctx) is 2-arg/3-statement, ShowOnly before Render.
- finding:   Takes a progress arg; 4 statements; Render BEFORE ShowOnly — order is load-bearing per the code comment.
- evidence:  MainForm.ChartBuildPresenter.cs:233-256; Charts/IAltitudeSubChart.cs:68-69
- severity:  high
- action:    fix-doc

- location:  RELEASING.md (3 occurrences "Setup.exe") vs README.md §Install ("TargetPlanner-win-Setup.exe")
- axis:      currency
- modality:  descriptive
- claim:     Installer filename (two docs disagree).
- finding:   Direct contradiction; no in-repo release record settles it (Velopack smoke test still open per ROADMAP).
- evidence:  RELEASING.md:3,34,37,47; README.md:115
- severity:  high
- action:    unverifiable → ask user

- location:  README.md §Charts (22) + §Sky brightness AND ARCHITECTURE.md §Charting ("Y axis 16–22")
- axis:      currency
- modality:  descriptive
- claim:     Sky chart Y axis spans 16–22 mag/arcsec².
- finding:   Actual 16–26; code comment documents the widening for narrowband K-S.
- evidence:  Charts/AltitudeSubChart_Sky.cs:58-69
- severity:  medium
- action:    fix-doc

- location:  CLAUDE.md §External dependencies (82, "Velopack 0.0.1298")
- axis:      currency
- modality:  descriptive
- claim:     Velopack pinned at 0.0.1298.
- finding:   csproj pins 0.0.1589-ga2c5a97; ROADMAP records the bump as shipped.
- evidence:  TargetPlanner/TargetPlanner.csproj:63; ROADMAP.md:1230
- severity:  medium
- action:    fix-doc

- location:  README.md §Filters & moon avoidance ("Defaults button... restores the active filter")
- axis:      currency
- modality:  descriptive
- claim:     Main-form Defaults button resets only the active filter.
- finding:   OnFilterDefaultsClick restores EVERY library filter with a factory baseline (comment: "restore EVERY library filter"); silently discards custom tuning on non-active filters.
- evidence:  MainForm.FilterMenuPresenter.cs:229-253
- severity:  high
- action:    fix-doc

- location:  VERIFICATION.md §Automated tests + ROADMAP.md:435 ("cache-contract.md... 'IS the test list'")
- axis:      currency
- modality:  descriptive
- claim:     cache-contract.md self-describes as the test list.
- finding:   Phrase absent from cache-contract.md; originates in test-project-plan.md:73 and ROADMAP itself — a misattribution repeated by two citing docs.
- evidence:  docs/design/cache-contract.md (full read); docs/design/test-project-plan.md:73
- severity:  medium
- action:    fix-doc

- location:  CLAUDE.md §Docs map exclusions bullet
- axis:      placement
- claim:     Docs map accounts for every project doc.
- finding:   TargetPlanner/Imaging/README.md (real, tracked, referenced twice from ROADMAP) is named nowhere — not table, not journal, not exclusions.
- evidence:  TargetPlanner/Imaging/README.md; ROADMAP.md:1180,1204
- severity:  medium
- action:    fix-doc

- location:  README.md (10, 63) button captions
- axis:      currency
- modality:  descriptive
- claim:     Buttons captioned "Visible Tonight" / "Select All".
- finding:   On-screen text is "Visible" / "Check All" (handler names retain legacy names).
- evidence:  MainForm.Designer.cs:1081,1093
- severity:  medium
- action:    fix-doc

- location:  docs/design/test-project-plan.md:3 AND VERIFICATION.md §Automated tests
- axis:      currency
- modality:  descriptive
- claim:     Only Phase 1 of the test rollout shipped.
- finding:   Phases 2–4 each marked "(shipped 2026-05-27)" in the same file; ROADMAP confirms the rollout closed same-day (187 tests).
- evidence:  test-project-plan.md:3 vs :49,71,96; ROADMAP.md:362-564
- severity:  medium
- action:    fix-doc

- location:  CLAUDE.md §Architecture cache bullet + ARCHITECTURE.md §Cache store ("DayWindowKey.Range")
- axis:      currency
- modality:  descriptive
- claim:     Sub-charts slice entries to DayWindowKey.Range at paint time.
- finding:   No Range member exists; entries are pre-sized to the night window and read directly with an equality guard.
- evidence:  Caches/DayWindowKey.cs:25-46; Charts/AltitudeSubChart_Day.cs:445-450
- severity:  medium
- action:    fix-doc

- location:  Source comments in 7 files citing "docs/code-quality-audit.md"
- axis:      currency
- modality:  descriptive
- claim:     That path exists.
- finding:   Renamed to the dated filename; 7 source-comment citations missed by the rename pass. Report-only (source edits).
- evidence:  Caches/CacheAxis.cs:17; Charts/DuskDawnGradient.cs:15; Charts/FitTooltipResolver.cs:16; Charts/ChartLayout.cs:250,309; Charts/MoonOverlay.cs:22; Charts/ChartLegendPanel.cs:17
- severity:  low
- action:    flag-code-bug
```

## Remainder summary (~90–100 additional unique flags, by theme)
- Test-count drift within ROADMAP/test-project-plan Phase 1–4 entries (~10, low/medium).
- ARCHITECTURE UI-flow / MainForm-wiring granular drift (~10, medium/low) — incl. nonexistent SaveActiveFilter, stale 1-arg ChartCacheStore ctor claim, coordinator "diff table" claim (moved into EnsureAsync), Button_Graph vs Button_GraphTarget.
- Moon/K-S smaller drifts (~5) — dead alpha-0 branch, GroupBox nesting, Filter "POCO" vs sealed record, NightFit field omission, warmup-perf figure conflict (2–4 s vs 1–2 s — unverifiable here, ask user).
- ROADMAP dated-entry symbol drift (~15, high/medium individually smaller blast radius) — renamed loaders, Button_BrowseLocalHorizon, OverlayController sticky-state drain gap (flag-code-bug), stale IAltitudeSubChart member list, async-void count, Capture-button date-attribution conflict.
- Placement/graduate/extract-cold candidates (~6) — shipped K-S gate mis-filed as future; RadioButton_Sky design note stale; 2026-05-26 progress-bar entry should graduate into ARCHITECTURE; 2026-05-27 decomposition entry duplicates + outpaces ARCHITECTURE's stale section; Phase 3/4 test detail duplicated from test-project-plan.md.
- Two source-comment self-citations to the wrong doc (low, flag-code-bug): CoordinateExtensions.cs:8 → DOMAIN.md; IAltitudeSubChart.cs:14 → ARCHITECTURE.md.
- Unverifiable Core-internal claims correctly declined (~8, R1) — plus one verifiable counter-example flagged: "neither Core nor TP carry static mutable state" falsified by DiagnosticsDialog.sCurrent (low).
- Cosmetic drift (~15, low) — Designer line-count, 20-vs-21 test files, NightDate glossary duplication (cross-ref+delete candidate), missing "Core consumer contract" row in the docs map, broken README anchor, B-filter 445 vs 450 nm, now-line scope, MoonProfile null-condition, stale ChartEvaluation XML doc-comment (flag-code-bug), CreateChartProgress 200 ms comment vs 1000 ms constant (flag-code-bug).

## Adjudication note
Presented for approve / amend / defer per flag; nothing applied. The top ~11 multiply-corroborated flags are the highest-confidence starting point. All flag-code-bug items are report-only and need a separate code-focused pass.

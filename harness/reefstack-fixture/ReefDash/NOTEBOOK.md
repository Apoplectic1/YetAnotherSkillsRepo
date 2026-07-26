# NOTEBOOK.md — ReefDash lab notebook

- 2026-07-18 — **Decided (portfolio-wide, after the June false-alarm streak): a "salinity
  event" is a ≥0.8 ppt swing within 10 minutes as measured by PulseMonitor's probe.** Every
  app must use this exact definition — dash alerting (here), DoseKeeper's dosing lockout,
  and journal tagging — or the apps disagree about whether an event happened. Standing
  truth, but it spans all three apps and has no obvious home in this repo's docs; not yet
  written anywhere authoritative.
- 2026-07-09 — Ring buffer at 5 s polling holds ~4 h of points before chart decimation
  matters; fine for now.

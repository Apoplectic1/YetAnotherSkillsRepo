# fat-arch variant — NOTEBOOK entries to prepend (newest-first, above 2026-07-04)

- **2026-07-08** — Decided (standing rule, after the La Push retry discussion): CO-OPS
  client resilience policy — exactly one retry with a 2 s backoff on any 5xx, then fail
  loud; never retry a 4xx (it's a request bug, not weather). Applies to every current and
  future fetch path. Not yet written up in ARCHITECTURE.
- **2026-07-06** — Decided (standing verification practice): every scoring change must add
  a regression test pinning the previous score for one reference window from the Pillar
  Point 2026-05-06 logbook set, so calibration drift is loud. Not yet in VERIFICATION.

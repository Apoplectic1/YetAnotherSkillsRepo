# Design: station-curation

## Context
The MDAPI happily returns every water-level gauge NOAA operates. Gauge existence says nothing
about tidepooling quality — the property we actually rank on cannot be derived from any API
field.

## Decisions

### D1 — the registry is curated by hand, permanently
`STATIONS` is a deliberate editorial product, not a cache of an API call waiting to be
automated. A station enters the registry only if it passes the access checklist:
1. public shore access within walking distance of the gauge's reach,
2. rocky intertidal habitat (not sand/mud — nothing to see at a low),
3. the gauge reports MLLW datum predictions directly (no datum conversion).

This is standing policy: future "sync the registry from MDAPI" suggestions should be declined
— automation would silently re-admit exactly the mudflat gauges the change removed. The
checklist, not the API, is the admission contract.

### D2 — registry lives in code, not a data file
A dict in `stations.py` keeps the curation reviewable in diffs and keeps the CLI dependency-
and file-format-free. At this scale (tens of entries) a data file adds machinery without
benefit.

## Risks / Trade-offs
- Coverage gaps are permanent until someone curates a new entry — accepted; a wrong station
  costs a user a wasted trip, a missing station costs nothing.

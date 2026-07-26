# ARCHITECTURE.md — TidePool

**Charter:** module mechanics and data flow. How the system works today.

## Module map (`src/tidepool/`)
- `stations.py` — curated station registry (`STATIONS` dict) + on-disk metadata cache
  (`CACHE_TTL_HOURS = 6` — deliberately short of a day: NOAA re-fits station harmonics
  within hours after storm events, and 6 h keeps a same-day return trip fresh without
  hammering the MDAPI; one JSON file per station under `~/.tidepool/cache`).
- `tides.py` — NOAA CO-OPS client: hi/lo predictions, MLLW datum, english units, 30 s
  timeout; `low_tides()` filters the lows for the planner.
- `plan.py` — window scoring: three weighted factors (tide height 0.5, daylight fit 0.3,
  moon phase 0.2); `sun_events()` / `moon_phase_days()` wrap `astral` with function-local
  imports.
- `export.py` — CSV writer, nine columns (`CSV_COLUMNS`), returns row count.
- `cli.py` — argparse entry point; four subcommands: `stations`, `tides`, `plan`, `export`.

## Data flow
station id → `tides.fetch_predictions` (network, cached metadata) → `low_tides` →
per-low `plan.score_window` (needs `sun_events` + `moon_phase_days`) → ranked windows →
terminal table or `export.export_csv`.

## Design constraints
- Pure-math core: everything in `plan.py` except the astral wrappers is deterministic and
  unit-testable with no network or dependency footprint.
- Scoring weights are a deliberate balance — rationale in
  `openspec/changes/archive/2026-06-08-three-factor-scoring/design.md`.
- The CLI never writes anywhere except an explicit `--out` path and the cache directory.

## Prediction pipeline — design narrative

### Why a thin client and not a wrapper library
`tides.py` is deliberately the thinnest possible layer over the NOAA CO-OPS `datagetter`
endpoint: assemble query parameters, issue the request, unwrap the `predictions` key. There
is no retry logic, no response caching, and no abstraction over "prediction source" that
would let a second provider be swapped in later. NOAA CO-OPS is, for the foreseeable future,
the only source TidePool will ever talk to — it is the authoritative U.S. government source,
it is free, and it needs no API key. Building a provider-agnostic interface for a swap that
will likely never happen would add indirection every future contributor has to read through
to understand what is, underneath, a single HTTP GET. The project's engineering philosophy —
most visible in the pure-math design of `plan.py` — treats needless abstraction as a cost,
not a virtue, and the client is held to the same standard. A consequence is that resilience
(retries with backoff, degrading to a cached forecast when the network is down) is out of
scope for `tides.py` itself; a caller that needs to survive a transient blip adds that at the
call site, because an interactive CLI invocation and a hypothetical future batch job want
different resilience postures, and baking one policy into the client would force it on both.

### Datum and unit choices, and why they are non-negotiable
Every value that leaves `tides.py` is in MLLW feet. This is not an arbitrary default — it is
the datum the entire domain model is built around. DOMAIN.md defines a good tidepooling
window in MLLW terms directly, and `plan.py`'s height factor is calibrated against that same
datum. If the client ever emitted a different datum, every downstream number would be
silently wrong while still looking plausible: a datum mismatch does not throw, it just
produces numbers off by a station-specific offset, and it surfaces in the field rather than
in review, when a "great minus tide" turns out to be a mediocre one. Because of that risk
profile, the request's datum and unit parameters are treated as load-bearing constants of the
client, not configuration a future feature should expose. The project's gotcha list captures
the same point from the other direction: tide heights are MLLW feet everywhere, never mix
datums — the enforcement point for that rule is this one request parameter block. The
local-time parameter matters for the same reason in a different place: daylight-fit scoring
compares a low-tide timestamp against a sunrise/sunset computed in local time, and fetching
predictions in GMT would silently shift every window by the station's UTC offset.

### Interval choice: hi/lo events, not the full curve
CO-OPS can return a dense six-minute curve or a sparse hi/lo event list; TidePool always
requests the sparse form. The planner's unit of interest is a low-tide event — a window is
built *around* a low, not around an arbitrary curve point — so the dense form would only add
parsing work with no scoring benefit, while multiplying payload size for a multi-week horizon
in a tool that is expected to feel instant. The one place a dense curve would eventually earn
its keep is the "offline tide harmonics" direction in ROADMAP.md, which is part of why that
direction is scoped as a future rewrite of the prediction layer rather than an incremental
change to `tides.py`.

### The low/high split and where filtering lives
`fetch_predictions` returns every event NOAA reports, highs and lows both, because the raw
response is cheap to keep intact and a future caller (a "show the full curve" view, say)
might want the highs too. `low_tides()` is a separate filter that exists purely to give the
planner exactly the rows it wants without every caller repeating the same list comprehension.
Keeping the filter as its own function keeps `fetch_predictions`'s contract narrow — "what
NOAA returned" — rather than conflating it with "what the planner wants," which are
conceptually different questions that happen, today, to be answered by the same station data.

### Failure-mode philosophy: fail loud, fail early
`fetch_predictions` calls `resp.raise_for_status()` before touching the body. There is no
try/except around the call, no fallback to stale predictions, and no partial-result path for
a malformed response — a network failure or a bad payload surfaces as an uncaught exception
that stops the command dead. This is deliberate: a trip planned around a stale or partially
wrong prediction set is a trip planned around bad information, and that becomes visible only
when someone is standing on a rock at what they believed was a low that never happened.
Against that, a loud crash costs a user nothing but a re-run. That asymmetry is why the
client has no fallback path, and why none is planned — resilience decisions belong to the
caller, made explicitly, not defaulted inside the client.

### The unauthenticated, rate-limited surface, and alternatives not taken
No API key means no signup and no secret to manage, which is a large part of why TidePool
ships as a zero-configuration tool — but the endpoint is rate limited per source IP rather
than per account, since there is no authentication to key a quota on. That is the reason the
station metadata cache exists at all: every avoidable request is one less competing for a
shared, opaque IP-level budget. A local harmonic-constituent solver was considered as an
alternative to calling the API at all, and was set aside for the initial versions because
harmonic reconstruction is a meaningfully larger effort than an HTTP client and the curated
station list is small enough that the network dependency has not been painful in practice —
it remains the most-cited future direction precisely because "works with no network, in the
field where cell coverage is often poor" is a real benefit for this tool specifically.

## Cache subsystem — design rationale and lifecycle

### What is cached, and what is not
It is easy to misread `stations.py`'s cache as a tide-prediction cache; it is not. It holds
*station metadata* — coordinates and descriptive information keyed by station id — not
predictions, which are re-fetched on every planning run and never touch this cache at all.
Station metadata is close to static: coordinates do not move, and while NOAA does
occasionally re-fit a station's harmonics after a storm, the metadata TidePool actually
caches changes far less often than predictions do. That distinction is why the TTL can be
measured in hours rather than minutes, and why the cache needs to know nothing about the
scoring model or planning horizon — its whole job is "is this station's metadata still fresh
enough to trust," a question with a single, simple, time-based answer.

### Why cache metadata at all, given how small the registry is
With eighteen curated stations, the entire `STATIONS` dict already lives in memory the
instant `stations.py` is imported, so there is no in-memory lookup cost to avoid. The cache
insulates repeat invocations from the cost — and, more importantly, the shared rate-limit
risk — of any metadata enrichment that would otherwise mean a round trip to NOAA on every
single command. A user checking `tides` for one station, then `plan` for another, then
re-running `plan` with a different `--days` value, should not pay a network round trip for
information that has not changed since the last invocation; the cache turns "did this change
recently" into a cheap local mtime check instead.

### The TTL: six hours, and the reasoning behind that number
`CACHE_TTL_HOURS` is 6, chosen rather than defaulted. No expiry at all would be simplest, but
risks showing metadata that no longer reflects reality after a post-storm re-fit — and storms
disproportionately precede the dramatic low tides that make for interesting trips. A full
24-hour TTL was considered and rejected because it does not comfortably support a same-day
return trip: a user checking conditions in the morning and planning a return visit that
evening should not be looking at metadata approaching a full day stale. Six hours comfortably
covers a single day's multiple planning sessions while staying short enough that a post-storm
re-fit is unlikely to sit stale for more than a few hours before the next natural session
picks up the refreshed data — a balance point, not a formula, which is why the rationale is
documented directly on the constant rather than left for a future contributor to guess at.

### File-per-station JSON: why not one file, why not a database
Each station's metadata lives in its own JSON file under `~/.tidepool/cache`, named by
station id. A single shared cache file was rejected because freshness is evaluated per
station via that file's own mtime, and a shared file would tie every station's freshness to
whichever station was fetched most recently. A database — even SQLite — was also rejected as
disproportionate: eighteen small JSON files under a dotfile directory is a cache a user can
inspect, delete, or read directly without tooling, which matters for a CLI audience and for a
maintainer debugging a stale-cache report in the field with nothing but the file system.

### Freshness as a pure function of file modification time
`cache_fresh()` derives freshness entirely from the file's on-disk mtime rather than storing
an expiry timestamp inside the cached JSON. This keeps the cached payload exactly the station
metadata, nothing more, and keeps `read_cache()` trivial: read, parse, return, with no
bookkeeping fields that exist only to serve the cache's own logic. The trade-off is that
anything touching the file's mtime outside the intended write path — a backup restore, a
manual edit — can desynchronize freshness from reality; that has not been a problem given the
file's location under a dotfile directory nothing else is expected to touch.

### Missing, stale, and corrupted cache handling
A missing file is the ordinary cold-start case: `cache_fresh()` reports `False` and the
caller fetches and repopulates it. A stale file is treated identically to a missing one —
there is no "use it anyway, it's probably close enough" partial-trust path, echoing the
prediction client's fail-loud stance: whether stale data is good enough is the caller's
decision, made explicitly. A corrupted or unparseable file is not defended against inside
`read_cache()` at all; a malformed JSON file raises during parsing rather than being silently
deleted and re-fetched, on the theory that a corrupted file is itself a symptom worth
surfacing, not quietly working around.

### Cache scope, and future-proofing under offline harmonics
The cache's contract is narrow — given a station id, say whether it is fresh and hand it
back — and knows nothing about the planning horizon or scoring weights. That narrowness is
why the design constraints call out the cache directory as the *only* implicit write surface
in the entire tool; everything else needs an explicit `--out` path. If the "offline tide
harmonics" direction in ROADMAP.md is eventually built, the cache's role shifts rather than
disappears: a local solver still benefits from caching station metadata, but the reason to
check freshness shifts from "is the network round trip worth avoiding" toward "has NOAA
republished revised constituents." The file-per-station layout and TTL-based freshness check
would likely carry over unchanged; only the payload inside each file would need revisiting —
one reason the cache was kept decoupled from `tides.py` and `plan.py` rather than folded into
either.

## Scoring engine — factor design essays

### Why a weighted sum instead of a rule engine
`score_window` combines tide height, daylight fit, and moon phase as a single weighted sum,
each factor pre-normalized to 0.0–1.0 before its weight applies. The more obvious alternative
— a cascade of hard pass/fail filters — was set aside because tidepooling windows are not
naturally binary. A borderline window (mediocre height at a very good moon phase, or a very
good height slightly outside the comfortable daylight margin) is often still a reasonable
trip, just not an outstanding one, and a filter cascade can only admit or reject, not express
that distinction. A weighted sum lets every factor register its opinion proportionally, so a
window weak on one axis but strong on another still surfaces with a score reflecting the
balance. The deliberate exception is the daylight factor, discussed below, which *is* a hard
boundary rather than a graded one — because DOMAIN.md's safety framing treats "ends after
sunset" as a floor, not a discount, and the model honors that distinction explicitly rather
than blending it into the sum's shape.

### The tide-height factor: saturation, not a step function
The height factor is 1.0 at or below `GOOD_TIDE_FT` and falls off linearly to 0.0 at two and
a half feet above it. A step function was the simpler alternative and was rejected because it
manufactures false precision at the boundary — a low exactly at threshold and one a tenth of
a foot above it are practically identical conditions, but a step function would score them as
maximally different. A linear falloff lets windows just above ideal still register as
respectable rather than being scored as though no better than a window with no exposed
intertidal zone at all. Heights below the threshold saturate to full credit rather than
rewarding ever-more-negative values without bound; DOMAIN.md already distinguishes an
exceptional "minus tide" qualitatively, and treating "at or below ideal" as uniformly
excellent avoids a second breakpoint that would cost more complexity than the distinction is
worth to the ranking.

### The daylight-fit factor: a hard floor dressed as a graded factor
Structurally this factor looks like the others — a value between 0.0 and 1.0 — but its
boundary behavior is categorically different: outside sunrise-to-sunset it is exactly 0.0,
full stop, with no partial credit for a low a few minutes after sunset. This mirrors DOMAIN.md
directly: arriving at a low after dark is not a slightly-worse trip, it is not one the planner
should be recommending, and the model encodes that as a hard zero on this one factor rather
than a steep-but-nonzero falloff. Inside daylight, the factor grades on margin from the nearer
edge, saturating once that margin reaches an hour — matching DOMAIN.md's own guidance to
arrive roughly an hour before the low, since the window closes fast on the flood. A low with
less than that margin is one where the arrival buffer starts eating into either safety margin
or the usable window itself, so the factor stops rewarding additional margin once a
comfortable buffer already exists.

### The moon-phase factor: spring tides as a graded signal
This factor rewards proximity to the nearest new or full moon and falls linearly to zero at
the halfway point between syzygies, the quarter moons where range is smallest. It exists
because the height factor alone under-represents a real domain fact: spring tides expose more
of the intertidal zone than the predicted height fully captures on its own, since that height
is itself a product of where a station sits in the spring/neap cycle. Rather than fold that
relationship into the height factor's own shape — tangling two conceptually separate signals
into one number — the two are kept independent and left to the weighted sum to balance. Moon
phase is graded, not a hard neap-tide filter, for the same reason as the height factor's
saturation choice: a borderline window near a quarter moon is demoted, not discarded, because
a mediocre low in good daylight at a neap can still be a fine trip for someone without the
flexibility to wait for the next spring cycle.

### Why three factors, and the weighting philosophy
Three factors is a deliberate stopping point: each answers a genuinely different question —
how exposed will the intertidal zone be (height), can it be safely seen and navigated
(daylight), and is this a particularly good point in the tidal cycle to be doing this at all
(phase). A fourth factor, sea state, is the most frequently discussed future addition, since
DOMAIN.md already notes swell can override an otherwise excellent score — but it is
deliberately absent today because it depends on marine forecast data the project does not yet
ingest, and a weighted factor for data the tool cannot fetch would imply a safety check that
is not actually happening. The weighted-sum shape generalizes to an additional factor without
a rewrite, which is part of why it was chosen over three factors hard-coded into a single
combined formula. The weights themselves place the most trust in height, treat daylight as
substantial but secondary, and let phase act closer to a tiebreaker: height is the most direct
measurement of exposure, daylight answers whether that exposure is safely usable, and phase is
a proxy that correlates with but does not replace an actual predicted height — a window with
an excellent phase score but a mediocre height is still, in the end, a mediocre-height trip.

### Alternatives considered for combining factors
A multiplicative combination was considered because it has an appealing property: any factor
collapsing to zero forces the whole score to zero, folding the daylight factor's hard-boundary
behavior into every factor "for free." It was set aside because it would also zero out windows
for reasons that should only demote them — a below-average moon phase would drag down an
otherwise excellent window disproportionately, contradicting the rationale for treating phase
as a graded nudge rather than a filter. The weighted sum keeps that distinction intact: only
the daylight factor can zero a window outright, because only it represents an actual domain
floor rather than a graded preference, and it earns that behavior through its own internal
logic rather than the combination formula treating every factor as equally capable of a veto.

## CLI & export surface — UX decisions

### Why the subcommands mirror the data-flow order
The four subcommands — `stations`, `tides`, `plan`, `export` — trace the same path data takes
through the system, from least to most processed: list what stations exist, look at raw
predictions for one, turn predictions into ranked windows, persist those windows to a file.
This mirrors a first-time user's likely path: someone new to TidePool starts by asking what
stations exist before knowing enough to ask for a specific station's tides, and only reaches
scoring and export once the raw predictions look right. Each subcommand is also a legitimate
stopping point on its own — a user who only wants to sanity-check raw predictions has no
reason to be forced through scoring and export, which is why `tides` is a first-class
subcommand rather than an internal helper `plan` happens to call.

### Default horizons: 7 days for `tides`, 14 for `plan` and `export`
`tides` defaults to a one-week window because a tides check is typically a quick sanity
look — a week is enough to see a spring/neap transition without overwhelming a terminal
command meant to be glanceable. `plan` and `export` default to two weeks because planning
benefits from a wider horizon: two weeks comfortably spans a full spring/neap half-cycle,
which matters directly for the moon-phase factor — a shorter horizon could, depending on
where in the lunar cycle it ran, miss the better half of the current cycle and only ever show
the weaker half. Widening the planning horizon was a direct consequence of adding the
moon-phase factor; a shorter one would systematically undersell what that factor surfaces.

### The minimum-score threshold
`plan` filters its printed output to windows scoring at or above a threshold set comfortably
above the midpoint of the possible range, to keep default output focused on windows genuinely
worth attention rather than dumping every low in the horizon regardless of quality. Left
unfiltered, a two-week horizon at most stations produces enough low-tide events that the
useful signal — the handful of genuinely good windows — would be buried in a long list of
daylight-adequate-but-unremarkable ones. The threshold is a flag, not a hard-coded floor,
specifically so a user on a tighter schedule can lower it and see everything in range rather
than being told nothing is worth their time — the default is a curation choice for the common
case, not a statement about what the tool considers valid.

### Why `export` writes a file while `plan` only prints
`plan` and `export` share the exact same window-computation and ranking logic — the same
internal helper — and differ only in what happens to the result afterward. `plan` is for a
human looking at a terminal right now; `export` is for someone who wants the ranked windows
available outside the terminal — in a spreadsheet, shared with a co-planner, or kept as a
record. Rather than bolt an optional `--out` flag onto `plan`, or have `export` duplicate the
ranking logic, the shared helper computes the windows once and each subcommand decides what to
do with the result. This guarantees the two can never disagree with each other about a given
station and date range, because underneath they are the exact same computation.

### CSV column design
The exported CSV carries date, window start and end, low-tide time and height, score, both
station id and name, and moon phase in days. Every column was chosen to make the CSV
independently useful without cross-referencing anything else — station id and name together
mean a spreadsheet spanning multiple stations needs no lookup table, and the raw moon-phase
value alongside the score lets a reader see *why* a window scored as it did rather than
trusting an opaque number. Window start and end are derived from the low-tide time with the
same one-hour arrival margin DOMAIN.md recommends, included as their own columns so an
import into a calendar-adjacent tool does not have to recompute that margin. Columns that
would require data the pipeline does not yet compute — sunrise/sunset themselves, rather than
just their contribution to the score — were left out; the column set reflects what the
pipeline actually produces today rather than anticipating a future scoring change.

### stdout versus stderr, and export destinations
`plan` writes ranked windows to stdout, one line per window. `export` writes nothing about the
windows to the terminal — the CSV file is the actual output — but prints a one-line
confirmation of how many windows were written and where, sent to stderr rather than stdout, so
a piped or redirected stdout stream stays clean while the human-facing confirmation still
appears on the terminal. The `--out` flag defaults to a plain relative filename in the current
directory rather than anywhere under the cache directory: an exported CSV is a user-owned
artifact the tool should never touch again once written, while the cache directory holds
files the tool manages and may rewrite on its own schedule — keeping exports off that path
means a future change to cache eviction can never touch a file a user is treating as a
personal record, honoring the design constraint that the CLI's only implicit write surface is
the cache directory itself.

### Future direction: iCal export
ROADMAP.md pairs a future iCal exporter with the existing CSV one. Because `export_csv`
consumes the same list-of-window-dicts structure `plan` already prints from, an iCal exporter
would slot in as a sibling consuming that identical structure, reachable from the same
`export` subcommand rather than a parallel command or a parallel window-computation path. The
CSV's window start/end columns are themselves exactly the fields an iCal event needs for its
start and end times — not a coincidence, since once the CSV format settled on carrying
explicit window boundaries rather than only a low-tide timestamp, a second export format
consuming those same boundaries became a considerably smaller step.

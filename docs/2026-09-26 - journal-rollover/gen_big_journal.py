"""Generate the big-journal TidePool fixture variant: a newest-first bullet NOTEBOOK of about
85 KB, the base fixture's seven entries verbatim at the top, about 170 generated older entries
below, with the planted cells RO1 (an open thread never closed), RO2 (an open thread closed
by a later base entry) and RO3 (a dated citation from ARCHITECTURE into an old entry).
Deterministic (seeded)."""
import datetime
import os
import random
import sys

base = sys.argv[1]      # harness/tidepool-fixture/NOTEBOOK.md
outdir = sys.argv[2]    # harness/tidepool-fixture-variants/big-journal
rng = random.Random(20260926)

orig = open(base, encoding='utf-8', newline='').read()
head, sep, entries = orig.partition('\n- **2026-07-04**')
entries = sep.lstrip('\n') + entries

stations = ['Monterey', 'Pillar Point', 'La Push', 'Neah Bay', 'Port Townsend', 'Crescent City',
            'Bodega Bay', 'Yaquina Head', 'Cape Arago', 'Santa Cruz', 'Point Reyes', 'Tofino',
            'Cannon Beach', 'Fort Bragg', 'Salt Creek', 'Shi Shi']
mains = [
    ("NOAA quirk", "the hi/lo endpoint returned {n} predictions for a 7-day span at {st}; the API pads the range to whole days in station-local time, so the first and last day can be partial. `low_tides()` now takes the window bounds from the request, not the payload."),
    ("NOAA quirk", "MDAPI metadata for {st} arrived with `timezonecorr` as a string where every other station gives an integer; `int()` at the cache boundary, once, with a note in `stations.py` so nobody removes it."),
    ("NOAA quirk", "a {k}-second stall on the predictions endpoint at {st} with no error and no body; the 30 s timeout caught it. Second time this month; the retry stays at one attempt, the plan is to surface the stall in the table footer rather than retry harder."),
    ("NOAA quirk", "predictions for {st} came back in GMT despite `time_zone=lst_ldt`; the station has no DST rule in NOAA's table. Handled by reading `timezonecorr` and converting locally; the cached metadata carries the rule, so the fix costs nothing warm."),
    ("Field report", "{st}, {k} pools checked at the {h:.1f} ft low: the score of {sc:.2f} matched the day (clear, calm, a long slack). Logbook row added, with the two anemone beds on the north shelf marked for the next visit."),
    ("Field report", "{st}: the {h:.1f} ft low landed {m} minutes after sunset; the planner had scored it {sc:.2f} on the strength of the height alone. The daylight factor's 1 h margin is too generous at this latitude in winter; noted for the scoring revisit, not changed."),
    ("Field report", "{st}: swell of {k} ft closed the lower shelf even at a {h:.1f} ft low. Swell is out of model, as the calibration said; a `--swell` hint on `plan` is a candidate and stays unqueued until a second season of logbook rows says it matters."),
    ("Field report", "{st} at dawn: the {h:.1f} ft low was fine but the access road was gated until 08:00; the planner cannot know that. A per-station `notes` field in the registry would carry it; recorded, not queued."),
    ("Scoring", "re-ran the three-factor model over {n} logbook days from {st}: {sc:.0%} of the remembered good days score at or above 0.75; the misses are all swell or fog days. Weights unchanged, the calibration note stands."),
    ("Scoring", "tried a moon-phase weight of 0.3 (from 0.2) on the {st} set: {k} more spring-tide days rank in the top ten, two of them logbook duds. Reverted the same hour; the 0.2 weight stays and the reason is now written down."),
    ("Scoring", "the daylight factor's linear ramp gives a {h:.1f} ft low at civil twilight a score {sc:.2f} below the same low in full sun at {st}; a cosine ramp would flatten that. Sketched on paper, not queued: the linear ramp is easier to explain in DOMAIN."),
    ("Cache", "cold start for {n} stations: {sc:.1f} s; warm: 0.{k} s. The per-station JSON files under `~/.tidepool/cache` total {n} KB. Fine at this scale, and the TTL does what it should."),
    ("Cache", "a stale cache file for {st} (edited by hand during an investigation) was read back without complaint; there is no checksum, by design: the file is the cache, not a record, and a bad one costs one refetch."),
    ("Cache", "the 6 h TTL expired mid-session at {st} and the second `plan` refetched metadata silently; correct, and the {m} ms it cost was invisible in the terminal. No change."),
    ("CLI", "`plan --days {k}` for {st} prints {k} rows; past 21 days the table is unreadable in a terminal and `export` is the right tool. Capped the table at 21 with a hint, no change to `export`."),
    ("CLI", "`stations` output was sorted by id, which puts {st} far from its neighbours; sorted by state then name since today, the ids still shown."),
    ("CLI", "`tides {st}` with a misspelt station printed a traceback; now a one-line error naming the nearest registry matches ({k} candidates by prefix)."),
    ("Export", "CSV rows for {st}: the `moon_phase_days` column carries two decimals; the logbook wants one. Left at two, the CSV is for machines and the logbook is typed by hand anyway."),
    ("Export", "opened a {n}-row export in a spreadsheet: the ISO timestamps parse, the station name with a comma ({st}, WA) was quoted correctly by the csv module. Nothing to do."),
    ("astral", "sunrise at {st} from `astral` differs from NOAA's solar table by {m} s; irrelevant at the 1 h margin. Recorded so nobody chases it again."),
    ("astral", "`astral` raised on a date past 2100 in a unit test; clamped the planner's horizon to 365 days, which the CLI already enforced, so the library layer now agrees with the CLI."),
    ("Tests", "the pure-math suite ran in {m} ms on the laptop; added a case for a low exactly at the {h:.1f} ft filter boundary at {st}, which the old test set never touched."),
    ("Tests", "a flaky assertion in the daylight test depended on the machine's timezone; pinned the test to UTC and the {st} fixture, and it has been quiet for {k} runs."),
]
details = [
    "The cached metadata was {k} days old at the time.",
    "Recorded in the logbook the same evening.",
    "The run used the {st} registry entry as committed on that day.",
    "No code changed; this is a finding.",
    "Two people asked about this on the trip, which is why it is written down.",
    "The same thing was seen once in {mon}, not written down then.",
    "Timing on the laptop, plugged in, nothing else running.",
    "Checked against NOAA's own page for {st}, which agrees.",
    "A follow-up would need a second season of data to be worth anything.",
    "The change is one line and the test covers it.",
    "Worth remembering when the {st} trip comes round again.",
    "The number is approximate; the terminal timestamp has second resolution.",
]
months = ['October', 'November', 'December', 'January', 'February', 'March']
open_never = ("Open: the {st} station's harmonic constants were refit by NOAA on {d}, and the "
              "cached metadata still shows the old epoch; whether `plan` should warn when a "
              "station's epoch changes under a cached file is undecided. The two options are a "
              "warning line in the table footer or a silent refetch when the epoch differs. "
              "Revisit before the next {st} trip.")
open_closed = ("Open: metadata for {st} arrived with a three-byte prefix that `json.loads` "
               "rejected; cause unknown, the fetch retried clean and the cache was rewritten. "
               "Watch for it on the next cold fetch of a Washington station.")
cite_target = ("Decided: the metadata cache TTL is 6 hours, not a day. NOAA re-fits station "
               "harmonics within hours after a storm, and a same-day return trip should see the "
               "refit; 6 h keeps that without hammering the MDAPI (about {n} calls a day at "
               "worst, measured over the {st} trip). `CACHE_TTL_HOURS = 6` from today, and the "
               "reason is this entry.")

plants = {datetime.date(2025, 12, 9): open_never.format(st='Neah Bay', d='2025-11-30'),
          datetime.date(2026, 1, 15): open_closed.format(st='Port Townsend'),
          datetime.date(2026, 1, 22): cite_target.format(n=rng.randint(40, 90), st='Monterey')}
start = datetime.date(2025, 10, 6)
end = datetime.date(2026, 3, 28)
pool = [start + datetime.timedelta(days=i) for i in range((end - start).days) if
        (start + datetime.timedelta(days=i)) not in plants]
dates = sorted(rng.sample(pool, 165))
gen = []
for d in dates:
    st = rng.choice(stations)
    kind, form = rng.choice(mains)
    vals = dict(st=st, n=rng.randint(24, 240), k=rng.randint(3, 14), m=rng.randint(20, 900),
                h=rng.uniform(-1.8, 1.4), sc=rng.uniform(0.3, 0.95), mon=rng.choice(months))
    text = form.format(**vals)
    for _ in range(rng.randint(1, 2)):
        text += ' ' + rng.choice(details).format(**vals)
    gen.append((d, f"{kind} ({st}): {text}"))
gen.extend(plants.items())
gen.sort(key=lambda t: t[0], reverse=True)


def wrap(s, width=88, indent='  '):
    words, lines, cur = s.split(' '), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return ('\n' + indent).join(lines)


body = ''.join(f"- **{d.isoformat()}**: {wrap(t)}\n" for d, t in gen)
out = head + '\n' + entries.rstrip('\n') + '\n' + body
os.makedirs(outdir, exist_ok=True)
open(os.path.join(outdir, 'NOTEBOOK.md'), 'w', encoding='utf-8', newline='').write(out)
open(os.path.join(outdir, 'ARCHITECTURE-append.md'), 'w', encoding='utf-8', newline='').write(
    "- The 6 h cache TTL is a decision, not a default: the reasoning and the NOAA refit\n"
    "  behaviour behind it are in the NOTEBOOK entry of 2026-01-22.\n")
print(len(out.encode()), 'bytes;', len(gen), 'generated entries; first', gen[-1][0], 'last', gen[0][0])

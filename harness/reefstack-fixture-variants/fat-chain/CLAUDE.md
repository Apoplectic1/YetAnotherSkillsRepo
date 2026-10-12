# ReefStack portfolio — parent map

This directory is a **container** holding the independent repos of the reef-tank automation
portfolio. Keep this file thin — a map, not detail; per-repo specifics live in each repo's
own `CLAUDE.md`. Portfolio status lives in [`ROADMAP.md`](ROADMAP.md). Launch sessions from
the subproject you're working in; this map still loads as an ancestor.

## Active projects

| Repo | What it is | Consumes |
|---|---|---|
| **PulseMonitor** | Sensor daemon — polls probes every 10 s, sole writer of `readings.db`. | — |
| **ReefDash** | Desktop dashboard — live charts + event feed. | readings.db (read-only) |
| **DoseKeeper** | Dosing-pump controller — schedules doses, safety lockouts. | readings.db (read-only) |

## Data contracts

- **`readings.db`** — the portfolio's telemetry store. SQLite in WAL mode, written **only**
  by PulseMonitor's poll loop (every 10 s, table `readings(ts, probe_id, kind, value)`,
  kinds temp/salinity/ph/par); ReefDash and DoseKeeper open read-only connections and must
  tolerate WAL checkpoints mid-read. Consumers never write — a stray write corrupts the
  single-writer assumption and desyncs the WAL.
- **`config.db`** — a working name that currently denotes **two different stores; don't
  conflate them**: (1) PulseMonitor's local probe-calibration store (`src/calib.py`,
  shipped, private to that repo) and (2) the **planned portfolio-wide settings service**
  (owner: DoseKeeper, unbuilt) that would hold shared thresholds and the quiet-window
  bounds for all three apps.
- **Quiet window** — the 02:00–04:00 maintenance stretch: dosing locked out, alerts
  suppressed, portfolio-wide. All three apps must honor the same bounds; today each
  hard-codes them.

## Other directories

`scripts/` — portfolio convenience tooling (build-all); not a project, touch only if asked.

## Probe calibration and the ADC gotchas (learned on the 2026-07 recalibration)

Calibration runs on the bench before a probe goes into the tank; PulseMonitor's poll loop
refuses an uncalibrated channel. The procedure, and what bites when it is done by hand.

- **Two-point calibration, the low standard first, always.** The ADC's offset register is
  written from the low reading and the gain register from the high; writing the gain first
  bakes the uncorrected offset into it, and the probe reads 0.3 to 0.5 units high across the
  range until it is recalibrated. `calib.py` enforces the order; a hand calibration through
  the REPL does not, and the two July recalibrations that drifted were both hand runs.
- **Salinity standards are labeled at 25 °C; the bench is not at 25 °C.** Read the bench
  thermometer and apply the 2 percent per degree correction to the label value before
  entering it, or every tank reading inherits the bench's offset. `calib.py` asks for the
  bench temperature for this reason; "25" typed from habit is the commonest error in the
  calibration log.
- **The pH isolation board inverts the sign of the raw count.** The driver un-inverts it. A
  probe wired past the isolation board (the bring-up wiring) reads inverted and calibrates
  "successfully" onto a mirror-image curve. Before accepting a pH calibration, check that the
  raw count falls when the probe goes from the pH 7 standard into the pH 4 standard.
- **PAR calibrates against the reference cell, never a standard solution.** There is no PAR
  standard; the reference cell is read at the same spot under the same lamp, and the probe's
  gain is set to match it. Doing this under the tank light instead of the bench lamp gives a
  gain that is right for that lamp's spectrum only, and the dawn ramp reads 15 percent low.
- **The ADC's input mux settles in 40 ms; the driver waits 50.** A calibration that polls
  faster than that (the `--fast` flag, meant for the bench scope) reads the previous channel's
  residue on the first sample and the offset lands on it. `--fast` is for watching, not for
  calibrating; the flag is refused in `calibrate` since the second July run.
- **Channel 3 sits next to the pump relay and picks up its switching.** A calibration taken
  while a dose is running (the relay chattering) has 2 to 3 counts of noise on channel 3;
  the gain computed from it is off by up to 4 percent. Calibrate during the quiet window, or
  with DoseKeeper's lockout engaged.
- **Temperature compensation is applied by the driver, not the ADC.** The ADC gives a raw
  count; the driver applies the probe's temperature coefficient from the calibration record
  using the temp probe's *last* reading. If the temp probe is itself uncalibrated or
  unplugged, every compensated kind (salinity, pH) silently uses the default 25 °C. The log
  line "compensation: default" is the tell.
- **A calibration record is keyed by probe serial, not by channel.** Moving a probe to
  another channel carries its calibration with it; replacing a probe on the same channel
  does not, and the new probe reads with the old probe's curve until it is calibrated. The
  poll loop's "uncalibrated channel" refusal keys on the serial for this reason.
- **The salinity probe's cell constant drifts with biofilm; recalibrate monthly, not on
  drift alone.** Drift shows as a slow downward trend that the event detector never sees
  (it looks for swings). A monthly recalibration against the low standard catches it; the
  high standard alone does not, because the gain compensates for the cell constant and the
  offset does not.
- **Standards older than 90 days read low.** The salinity standards absorb water through the
  cap seal; a 90-day-old standard reads about 0.2 ppt below its label. The calibration
  record carries the standard's open date; `calib.py` warns past 60 days and refuses past 90.
- **The ADC's internal reference is 2.048 V; the probe amplifiers run on 3.3 V.** A raw count
  at the ADC's full scale means the amplifier is saturated, not that the probe is at range.
  Saturation during calibration (a standard too strong for the gain stage) makes the gain
  computation divide by a clipped value; the driver flags a count within 1 percent of full
  scale as "clipped" and refuses the point.
- **The pH probe needs 60 s in each standard before the reading is stable; the script waits
  90.** A hand calibration that reads at 20 s (the display looks stable) catches the probe
  mid-settle and the slope comes out 2 to 3 percent shallow. The slope is the number the
  event detector's threshold is scaled by, so this error lands on event detection.
- **Never calibrate with the probe cable coiled on the bench supply.** The supply's switching
  couples into the cable and the ADC reads a 50 Hz ripple; averaging hides it in the
  display and not in the offset. Lay the cable out; the July noise hunt ended there.
- **The calibration log is append-only and lives beside the store, not in it.** `calib.py`
  writes `calibration.log` next to `config.db` so a corrupted store still leaves the history
  readable; a recalibration after a store rebuild starts from the log's last record.
- **Entering a standard's value in the wrong unit is silent.** The salinity field accepts ppt
  and the pH field accepts pH; a conductivity value in mS/cm typed into the salinity field
  calibrates to nonsense that reads plausible in the tank (30-ish). The script shows the
  computed cell constant after the second point; outside 0.8 to 1.2 it is the unit.
- **The bench reference thermometer is itself calibrated yearly; check its sticker.** An
  uncalibrated bench thermometer puts its error into every temperature-compensated standard
  value. The sticker date is in the calibration log header since July.
- **`calibrate --dry-run` writes the record anyway.** A known bug in `calib.py` (ROADMAP,
  PulseMonitor): the dry run computes and prints, then falls through to the write. Until it
  is fixed, a dry run is a real calibration; do not use it to "try" a standard.
- **Recalibrating the temp probe invalidates the compensated kinds' last readings.** The
  driver compensates salinity and pH with the temp probe's last reading; after a temp
  recalibration that reading is from the old curve until the next poll tick. The first tick
  after a temp recalibration is marked `stale_comp` in the store and the dashboard hides it.
- **The ADC board's jumper J4 selects single-ended or differential inputs; the probes are
  single-ended.** A board that arrives with J4 in the differential position (both spares did)
  reads every channel at half scale and calibrates onto that, so the clipping check never
  fires and the range is silently halved. Check J4 before the first calibration of a board.
- **Calibration values live in `config.db`, the *private* one.** The planned portfolio
  settings service (the other thing called `config.db`) will never hold them; a calibration
  is per probe and per board, not portfolio-wide, and nothing in ReefDash or DoseKeeper
  reads it.
- **The offset drifts with the ADC's temperature, about 1 count per 10 °C.** The board sits
  in the cabinet at 30 to 35 °C in summer and the bench is at 22; a bench calibration is 1
  count off in the cabinet. The driver's `cabinet_offset` field in the record corrects it;
  leave it at 0 only for a board that lives on the bench.
- **A probe that reads exactly 0.0 after calibration is unplugged, not reading zero.** The
  ADC floats to mid-scale on an open input and the offset calibration brings mid-scale to
  0.0. The driver checks for an input within 2 counts of mid-scale for three ticks and marks
  the channel `open`; the calibration script does not, so an unplugged probe calibrates.
- **Calibrate salinity before pH when both are due.** The pH compensation uses the salinity
  reading (the ionic-strength term) as well as the temperature; calibrating pH first uses
  the old salinity curve for the compensation term and the pH slope comes out slightly off.
  The order is documented in `calib.py --help` and not enforced.
- **The spare ADC board has a different reference (2.5 V).** Its counts are 22 percent lower
  for the same input; a calibration record from the main board applied to the spare (the
  record is keyed by probe serial, not board) reads 22 percent high. The record carries a
  board id since July; the driver refuses a record from another board.

## Pump bring-up gotchas (DoseKeeper, learned on the two-part dosing bench, 2026-08)

What bites when a dosing pump is added or replaced. Every one cost a wet bench.

- **A peristaltic pump's ml-per-second is per tube, not per pump.** The calibration record
  keys on the pump id; a tube change (every 6 months, the tube hardens) needs a
  recalibration or the dose drifts 10 to 15 percent low within a month. The bench
  `calibrate-pump` run writes the tube's install date; `dose` warns past 150 days.
- **Priming a dry tube takes 40 s at full speed; the first dose after a tube change is short
  by that volume.** `prime` runs the pump until the flow sensor sees liquid and logs the
  volume; a dose run without a prime after a tube change delivers air for 40 s and the log
  says it dosed. The scheduler refuses the first dose on a tube with no prime record.
- **Two pumps on one relay board share the 12 V rail; running both at once browns the rail
  and both run slow.** The scheduler serializes doses for this reason (one pump at a time);
  a hand run from the REPL does not, and two REPL doses at once deliver about 70 percent.
- **The flow sensor reads pulses; below 0.4 ml/s it misses them.** A pump calibrated for a
  trickle dose reads zero flow and the dose aborts on the "no flow" guard. Set a trickle
  dose as a shorter run at normal speed, never a slower run.
- **The relay's "on" is active-low on the Rev B board and active-high on Rev C.** The driver
  reads the board revision from the ID resistor; a board with the resistor unpopulated (one
  of the Rev C spares) reads as Rev B and every pump runs when it should be off. Check the
  resistor before the first bench run of a new board.
- **A dose during a WAL checkpoint on `readings.db` is fine; a dose log write during one is
  not.** DoseKeeper's own log is a separate file for this reason; writing the dose log into
  `readings.db` was the first design and it lost dose records on checkpoints.
- **The lockout gate reads the event flag from the last poll tick, up to 10 s old.** A
  salinity event that starts 9 s before a scheduled dose does not stop it; the dose runs
  and the event's duration-plus-30-minutes lockout starts after. The scheduler's 15 s
  pre-dose re-check closes most of that window, not all of it.
- **`dose --ml` takes ml; the pump API takes seconds.** The conversion uses the tube's
  calibrated ml-per-second; a dose on an uncalibrated tube is refused, and a dose on a
  stale calibration (past 150 days) runs with a warning. Never call the pump API from a
  script with seconds; the conversion is the only place the calibration is honored.
- **The bench supply's current limit trips at 1.8 A; a pump stall draws 2.2 A.** A stalled
  pump (a pinched tube) trips the supply and the driver sees a brown-out on every pump, not
  a stall on one. The tank supply has no limit; a stall there runs hot until the thermal
  cutout. The driver's stall detection (no pulses for 3 s at full drive) exists for the
  tank case and is bypassed on the bench by `--bench`.
- **Dose records are append-only and the scheduler reads only the last 48 hours of them.**
  The two-part dosing logic (alkalinity, then calcium 20 minutes later) finds its partner
  dose in that window; a clock set back more than 48 hours (the bench Pi after a battery
  change) makes every dose look partnerless and the second part is skipped silently.

## Vocabulary (every app)

The words the three apps share, so a reading means the same thing on every screen.

- **Reading**: one row of `readings`: a timestamp, a probe id, a kind, a value in the kind's
  unit (°C, ppt, pH, µmol/m²/s). Never a derived number; a derived number is a *metric*.
- **Kind**: one of temp, salinity, ph, par. The set is fixed in PulseMonitor's `SCHEMA.md`;
  a new kind is a schema change, not a configuration.
- **Probe id**: the probe's serial, not its channel. A probe keeps its id across channels and
  boards.
- **Poll tick**: one pass of PulseMonitor's loop, every 10 s; one reading per probe per tick.
- **Salinity event**: a swing of at least 0.8 ppt within 10 minutes as measured by
  PulseMonitor's probe (decided 2026-07-18, portfolio-wide). DoseKeeper locks out for the
  event's duration plus 30 minutes; ReefDash tags the feed.
- **Lockout**: any condition that blocks DoseKeeper's queue: an event, the quiet window, a
  manual hold. The queue holds, never drops.
- **Quiet window**: the 02:00 to 04:00 maintenance stretch; dosing locked out, alerts
  suppressed, in all three apps.
- **Drift**: a slow monotonic change in a kind over hours, below the event threshold; shown
  amber on the dashboard, never an alert.
- **Checkpoint**: a WAL checkpoint on `readings.db`; a consumer mid-read sees a transient
  error and retries, never a partial row.
- **Dose**: one pump run, in ml, logged by DoseKeeper with its pump and its time; a dose that
  a lockout held is *queued*, not *missed*.
- **Metric**: a number derived from readings (a daily mean, a drift slope); computed by the
  consumer, never stored in `readings.db`.

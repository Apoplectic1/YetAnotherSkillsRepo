# Proposal: station-curation

## Why
Enumerating stations from the NOAA MDAPI surfaces hundreds of gauges that are useless for
tidepooling (harbor pilings, river mouths, industrial piers). Users pick a plausible-looking
station and plan a trip to a mudflat.

## What Changes
- Replace MDAPI enumeration with a curated in-code registry (`STATIONS`).
- `stations` subcommand lists the curated set only.

## Impact
- `src/tidepool/stations.py` — registry replaces the MDAPI list call.

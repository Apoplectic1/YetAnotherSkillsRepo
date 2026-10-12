# Probe wiring

The probe channel map on the ADC board (`src/probes.py`, `CHANNELS`):

| Probe | Channel |
|---|---|
| temp | 0 |
| salinity | 1 |
| ph | 2 |
| par | 3 |

All four probes share the 3.3 V rail; the pH probe sits behind the isolation board.

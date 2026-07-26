# Design: three-factor-scoring

## Context
Two-factor scoring (height 0.6, daylight 0.4) is blind to the spring/neap cycle. DOMAIN
knowledge: the best lows cluster around syzygy; neaps rarely produce workable windows. The
ranking should encode that, not leave it to the user's almanac.

## Decisions

### D1 — moon phase enters as a third weighted factor, not a filter
A hard neap filter would drop legitimate borderline windows (a −0.5 ft neap low in July
daylight is still a fine trip). A weighted factor demotes without hiding. Weights rebalance
to tide height 0.5, daylight fit 0.35, moon phase 0.15 — height stays dominant because a
mediocre low at perfect syzygy is still a mediocre low.

### D2 — phase factor shape: linear distance from nearest syzygy
`moon_phase_factor` computes days from the nearest new/full moon and falls off linearly,
reaching 0.0 at quarter moons (distance normalized by 7.0 days — half a lunar quarter cycle
each side). Cheaper than a tide-range lookup and good enough: range correlates with phase
distance almost monotonically at the stations we carry.

### D3 — height falloff extended
With three factors, the height factor's falloff relaxes from the old +2.0 ft cutoff to reach
zero at +3.0 ft, so marginal heights still differentiate instead of flat-lining at 0.

## Risks / Trade-offs
- Phase proxies range; a perigean spring (king tide) scores no higher than an ordinary
  spring. Acceptable — king-tide lows saturate the height factor anyway.

# Nautical units

Charts and soundings use their own lengths, and two of them are in the length
table: the nautical mile and the fathom. Both are ordinary linear factors
anchored to the meter like everything else in
[`why-a-base-unit.md`](why-a-base-unit.md), so they combine freely with the
metric and imperial entries — a depth in fathoms converts to meters, and a
distance in nautical miles converts to statute miles, without either pair
being stored explicitly.

- `nmi` — the international nautical mile, exactly 1852 m. Note that it is a
  separate entry from `mi`; the two differ by about 15 percent, so mixing
  them up is a silent wrong answer rather than an error.
- `ftm` — the fathom, exactly 1.8288 m, which is six feet. Depths on older
  charts are given in fathoms, and `unitconv 20 ftm ft` returns `120.0 ft`.
- `ch` and `lnk` — the surveyor's chain and link, which turn up in coastal
  and harbour survey work rather than at sea, and are covered alongside the
  other historical entries in [`history-of-units.md`](history-of-units.md).
- The cable, the shackle, and the knot are all absent. The first two are
  defined as fractions of a nautical mile that vary by navy and by era; the
  knot is a speed, and the command converts lengths, masses, and
  temperatures only — see [`limitations.md`](limitations.md).

Because the knot is not a unit the command handles, speed work is a two-step
job: convert the distance, then divide by the time yourself. Twelve knots is
twelve nautical miles per hour, so the distance run in one hour is:

```bash
unitconv 12 nmi km
```

```
12.0 nmi = 22.224 km
```

That example is tidy because 1852 is exact in decimal. Conversions that
cross into imperial are not — `unitconv 5 nmi mi` prints
`5.753897240117713 mi`, with the full float precision described in
[`usage.md`](usage.md). Round at the point of use if you want a figure fit
for a log entry.

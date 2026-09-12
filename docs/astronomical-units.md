# Astronomical distances

The length table reaches well past everyday scales, so distances in the sky
convert the same way anything else does — look up two factors, multiply by
one and divide by the other. Nothing about the arithmetic changes at
10^16 metres; see [`why-a-base-unit.md`](why-a-base-unit.md) for why one
shared base is what makes that true.

These are the entries worth knowing at that end of the table:

- `pc` — the parsec, 3.0856775814913673e16 m, sized by the geometry of a
  parallax measurement rather than by convention. Where it came from is in
  [`history-of-units.md`](history-of-units.md).
- `Tm` — the terametre, 1e12 m, a thousand gigametres. Sits between
  interplanetary and interstellar scales.
- `Gm` — the gigametre, 1e9 m. Useful for distances inside a solar system,
  where kilometres run to ten or more digits.
- `km` and `mi` — still available, and still the units most results end up
  being quoted in.
- `au` and light-years are *not* in the table. Asking for either is an
  unsupported unit error, not a silent zero.

So a parsec in kilometres is one call, with no `pc`-to-`km` factor stored
anywhere:

```bash
unitconv 1 pc km
```

```
1.0 pc = 30856775814913.67 km
```

The usual precision caveat applies, and it bites harder here. Results are
double-precision floats printed without rounding, so a value at parsec scale
carries roughly sixteen significant digits and the trailing ones are an
artifact of the binary representation rather than a measurement. Converting
between the far ends of the table — `pc` to `mil`, say — spans more than
twenty orders of magnitude and should be treated as approximate. Round at the
point of use, as described in [`usage.md`](usage.md).

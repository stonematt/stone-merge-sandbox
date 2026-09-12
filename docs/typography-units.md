# Typographic units

Type is measured in points and picas, and neither of those is in the length
table. `unitconv 1 pt mm` is an unsupported unit error, not a silent zero —
the same treatment `au` gets in [`astronomical-units.md`](astronomical-units.md).
What the table does carry is the unit that printing and platemaking work
shares with engineering: the thousandth of an inch, spelled two ways.

- `mil` — one thousandth of an inch, 2.54e-05 m. The usual name in US trade
  practice, and the one to reach for with paper and plate thicknesses.
- `th` — the thou, the same 2.54e-05 m under its British name. The two
  entries are interchangeable; `unitconv 1 mil th` returns `1.0`.
- `agt` — the agate, 0.00181 m. A 5.5-point measure, about 1/14 in, used to
  size newspaper classified and small-ad column depth.
- `in`, `mm`, and `cm` — the units a point measurement usually has to land
  in, whether for a page size or a press setting.
- `pt` and `pica` are absent, as is the older Didot point. Their sizes are
  definitional rather than measured, and which definition applies depends on
  the typesetting system; see
  [`history-of-units.md`](history-of-units.md) for how that kind of ambiguity
  played out in other units.

That means point arithmetic is a two-step job: convert the point count to
inches or mils yourself, then hand that to the command. A PostScript point
is exactly 1/72 in, so one point is about 13.8889 mil:

```bash
unitconv 13.8889 mil mm
```

```
13.8889 mil = 0.35277806 mm
```

A pica is twelve points, or 1/6 in — roughly 166.667 mil, which comes out at
`4.2333418 mm`. Both figures inherit the precision of the fraction you typed
in, on top of the usual float caveats in [`usage.md`](usage.md), so treat the
trailing digits as noise rather than as a measurement of anything.

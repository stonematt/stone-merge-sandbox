# Troubleshooting

Nearly every failed `unitconv` run ends in the same message — `error:
cannot convert 'X' to 'Y'` — because the command makes one check before it
converts anything: are both units in the same table? If they are not, it
stops there and exits `1` without printing a result. The message names the
two units but not which of them was the problem, so it reads the same
whether you crossed categories, misspelled an abbreviation, or typed a real
unit in the wrong case. For the three arguments and the conversions that do
work, see [`usage.md`](usage.md); for branching on the exit code from a
script, see [`scripting.md`](scripting.md).

Working through the causes in order of how often they bite:

- **Crossed categories.** Length, mass, and temperature are separate
  tables, and no pair spanning two of them converts — `unitconv 3 ft kg`
  fails by design, not for want of a factor. See
  [`why-a-base-unit.md`](why-a-base-unit.md).
- **Wrong case.** Length and mass abbreviations are matched exactly, so
  `KM`, `Ft`, and `KG` are all unknown units. Temperature is the exception:
  `c`, `f`, and `k` are lowercased before use, so `unitconv 20 C F` works.
- **`Mm` versus `mm`.** The megametre and the millimetre differ only in
  case, as do `Gm` and a mistyped `gm`. These are the one place where a
  capitalization slip converts successfully and quietly gives you an answer
  nine orders of magnitude off.
- **A unit that is not in the table.** The tables are wide but finite, and
  some omissions are deliberate — see
  [`astronomical-units.md`](astronomical-units.md) for the far end of the
  length table and what it leaves out.
- **A non-numeric value.** This one fails differently: `argparse` rejects
  it before any conversion is attempted, printing a usage line and exiting
  `2` rather than `1`.

When a conversion succeeds but the number looks wrong, the cause is usually
formatting rather than arithmetic. `unitconv` never rounds, so `70 kg`
comes back as `154.3235835294143 lb` and some results carry the usual
floating-point noise in their trailing digits — see
[how rounding is handled](usage.md#how-rounding-is-handled) if you need
fixed decimals. A result that is off by a clean factor of ten is a units
problem instead, and worth checking against the case-sensitivity notes
above. Temperature has its own edge: the scales are converted with offsets
rather than a shared base unit, and nothing stops you from converting a
value below absolute zero, so
[`temperature-scales.md`](temperature-scales.md) covers what those
conversions do and do not check.

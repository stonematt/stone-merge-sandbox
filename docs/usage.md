# Usage

If you do not have the `unitconv` command yet, see
[`installation.md`](installation.md). For the short version of this page —
install, one conversion, the supported units — see
[`quickstart.md`](quickstart.md). For how changes get from a branch to a
tagged release, see [`release-process.md`](release-process.md); for what to
record in `CHANGELOG.md` along the way, see
[`changelog-conventions.md`](changelog-conventions.md).

`unitconv` takes three positional arguments: a numeric value, the unit to
convert from, and the unit to convert to. It prints the converted value to
standard output.

```bash
unitconv <value> <from_unit> <to_unit>
```

Length and mass conversions use a simple linear factor table, so any pair of
units within the same category can be combined directly, for example
`unitconv 3 ft yd` or `unitconv 2 lb oz`. Temperature conversions between
Celsius (`c`), Fahrenheit (`f`), and Kelvin (`k`) are handled separately since
they are not simple linear scalings of a shared base unit — see
[`temperature-scales.md`](temperature-scales.md) for how those conversions
work and what they do not check.

Mixing categories, such as converting a length to a mass, is not supported
and will print an error message with a non-zero exit code.

## Common conversions

Miles to kilometres:

```bash
unitconv 5 mi km
```

```
5.0 mi = 8.04672 km
```

Kilograms to pounds:

```bash
unitconv 70 kg lb
```

```
70.0 kg = 154.3235835294143 lb
```

Celsius to Fahrenheit:

```bash
unitconv 20 c f
```

```
20.0 c = 68.0 f
```

Note that the echoed input value is reformatted: the argument is parsed as a
float, so `5` is printed back as `5.0`.

### How rounding is handled

`unitconv` does not round. Results are printed with Python's default float
formatting, which means you get the full precision of the underlying
double — hence `154.3235835294143` rather than `154.32` for the mass example
above. Some conversions look tidy anyway, either because the factor is exact
in decimal (`mi` to `km` is defined as 1609.344) or because the arithmetic
happens to land on a round number (20 °C to 68 °F), but that is a property of
those particular inputs, not a formatting rule. Conversions that are not
exactly representable in binary floating point may also show the usual
artifacts in the trailing digits. If you need a fixed number of decimal
places, round at the point of use — for example by piping the output through
`printf`, or by calling `convert_length`, `convert_mass`, and the temperature
helpers directly and rounding the returned float yourself.

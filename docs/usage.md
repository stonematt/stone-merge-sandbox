# Usage

If you do not have the `unitconv` command yet, see
[`installation.md`](installation.md). For the short version of this page —
install, one conversion, the supported units — see
[`quickstart.md`](quickstart.md). This page covers the command; to call
`unitconv` as a Python library instead, see
[`api-reference.md`](api-reference.md); for calling the command from a shell
script — exit codes, parsing the output line, batch loops — see
[`scripting.md`](scripting.md). For how changes get from a branch to a
tagged release, see [`release-process.md`](release-process.md); for what to
record in `CHANGELOG.md` along the way, see
[`changelog-conventions.md`](changelog-conventions.md). For the far end of
the length table — the parsec, the gigametre, and what is deliberately
absent — see [`astronomical-units.md`](astronomical-units.md). For showing
one value in several units at once, see
[`comparison-tables.md`](comparison-tables.md). For what to check when a
conversion errors out or returns a number that looks wrong, see
[`troubleshooting.md`](troubleshooting.md). For points, picas, and the
thousandth-of-an-inch units that stand in for them, see
[`typography-units.md`](typography-units.md). For what the command does not
do at all — the categories, formats, and flags that are absent — see
[`limitations.md`](limitations.md).

`unitconv` takes three positional arguments: a numeric value, the unit to
convert from, and the unit to convert to. It prints the converted value to
standard output.

```bash
unitconv <value> <from_unit> <to_unit>
```

No completion scripts ship with the command, but the unit abbreviations take
well to tab completion — [`shell-completion.md`](shell-completion.md) has a
bash and a zsh function you can add yourself.

Length and mass conversions use a simple linear factor table, so any pair of
units within the same category can be combined directly, for example
`unitconv 3 ft yd` or `unitconv 2 lb oz`. Each table is anchored to a single
base unit — the meter for length, the gram for mass — which is what lets any
pair combine without a factor being stored for that specific pair; see
[`why-a-base-unit.md`](why-a-base-unit.md). The two tables cover a mix of
everyday, historical, and scientific units — for where the less obvious ones
came from, and why some of their factors look so specific, see
[`history-of-units.md`](history-of-units.md). Temperature conversions between
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
helpers directly and rounding the returned float yourself. Those functions,
their arguments, and the errors they raise are documented in
[`api-reference.md`](api-reference.md).

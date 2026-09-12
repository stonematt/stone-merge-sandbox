# Rounding behaviour

`unitconv` never rounds. This page covers what that means for the numbers you
get back, and how to get a fixed number of decimal places when you want one.
For everyday invocation see [`usage.md`](usage.md); for why the command works
in plain floats rather than `Decimal`, see
[`design-notes.md`](design-notes.md); for the absent `--precision` flag
alongside the other deliberate omissions, see
[`limitations.md`](limitations.md).

## Results carry the full precision of the double

Results are double-precision floats printed with Python's default float
formatting, so the output shows every digit the double holds:

```bash
unitconv 70 kg lb
```

```
70.0 kg = 154.3235835294143 lb
```

There is no `--precision`, `--round`, or `--sig-figs` flag, and no config
file that sets one. How wide the number prints is a property of the value,
not a setting you can change.

## Tidy-looking results are a coincidence, not a rule

A conversion that prints a short number has not been rounded for you — it
landed there on its own. That happens when the factor is exact in decimal
(`mi` to `km` is defined as 1609.344), or when the arithmetic works out
evenly:

```bash
unitconv 5 mi km
```

```
5.0 mi = 8.04672 km
```

Read this as a property of those particular inputs. Change the value or the
unit pair and the tidiness goes away.

## Expect trailing-digit artifacts

Values that are not exactly representable in binary floating point show the
usual artifacts, including on conversions where the exact answer is a whole
number:

```bash
unitconv 1 st lb
```

```
1.0 st = 13.999999999999998 lb
```

A stone is defined as exactly 14 pounds, so the last digits here are the
representation, not a bad factor. If a result looks wrong only in its
trailing digits, this is usually why — see
[`troubleshooting.md`](troubleshooting.md) for the rest of the checklist.

## Round at the point of use

Because the command hands back everything it has, rounding is the caller's
job. From a shell, format the result field:

```bash
unitconv 70 kg lb | awk '{printf "%.2f\n", $4}'
```

```
154.32
```

From Python, call the conversion helpers directly and round the float
yourself:

```python
>>> from unitconv.convert import convert_length
>>> round(convert_length(0.1, "ft", "m"), 4)
0.0305
```

Those functions, their arguments, and the errors they raise are documented in
[`api-reference.md`](api-reference.md); [`scripting.md`](scripting.md) covers
parsing the output line in a shell script, and
[`comparison-tables.md`](comparison-tables.md) covers rounding a column of
values for display.

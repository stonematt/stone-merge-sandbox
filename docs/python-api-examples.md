# Python API examples

`unitconv` is a library before it is a command, and everything the command
does is available to import. This page is a set of worked examples for
calling it from Python — the imports, the four shapes of call, and the two
behaviours that most often surprise a first-time caller. For the signatures
and the reasoning behind them, see
[`api-reference.md`](api-reference.md); this page assumes you have read
none of it and want working code. For the command-line equivalent, see
[`usage.md`](usage.md); for driving the command from a shell script
instead, see [`scripting.md`](scripting.md).

## Importing

The six public functions are re-exported from the package root, so a plain
import is enough:

```python
from unitconv import convert_length, convert_mass

print(convert_length(1, "mi", "km"))
print(convert_mass(1, "lb", "kg"))
```

```
1.609344
0.45359237
```

Length and mass each take a value and two unit abbreviations, and return a
plain `float`. Nothing is rounded — see
[`rounding.md`](rounding.md) for why, and for how to round at the point of
use.

## Temperature

Temperature does not fit the three-argument shape, because there is no
factor to multiply by. It is four named functions instead, with Celsius as
the hub:

```python
from unitconv import celsius_to_fahrenheit, fahrenheit_to_celsius
from unitconv import celsius_to_kelvin

print(celsius_to_fahrenheit(100))
print(celsius_to_kelvin(fahrenheit_to_celsius(98.6)))
```

```
212.0
310.15
```

Fahrenheit and Kelvin have no direct conversion; chain through Celsius as
the second line does. These four functions do no validation — any float is
a legal input, including temperatures below absolute zero.

## Handling an unknown unit

An unrecognised unit raises `ValueError`. The message names the unit and
lists every unit the table accepts, which makes it long but means the
caller rarely has to consult the docs:

```python
from unitconv import convert_length

try:
    convert_length(1, "m", "kg")
except ValueError as exc:
    print(str(exc)[:40])
```

```
unsupported unit: 'kg' (supported: Gm, M
```

This is also what a cross-category call looks like. There is no guard that
recognises `kg` as a mass unit and reports a category mismatch — it is
simply not in the length table, so it reads as unsupported. Catching
`ValueError` around the call covers both cases.

## Two things to watch

**Units are matched exactly as typed.** The library does no case folding,
and case is load-bearing in the length table: `mm` is a millimetre and `Mm`
is a megametre.

```python
from unitconv import convert_length

print(convert_length(1, "m", "mm"))
print(convert_length(1, "m", "Mm"))
```

```
1000.0
1e-06
```

Both calls succeed, so a mis-cased unit here is a wrong answer rather than
an exception. Normalise unit strings that come from user input or a data
file before passing them in — but normalise to the exact table spelling,
not with `.lower()`, which would turn a megametre into a millimetre.

**Some units accept a spelled-out name.** The less familiar abbreviations
have a long form that is matched case-insensitively:

```python
from unitconv import convert_length

print(convert_length(1, "cicero", "mm"))
```

```
4.513
```

The abbreviation always works; the long form is a convenience for the
handful of units where `cic` or `emu` would not be recognisable. For which
units those are, see [`typography-units.md`](typography-units.md) and
[`api-reference.md`](api-reference.md).

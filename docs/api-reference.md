# API reference

This page documents `unitconv` as an importable Python package — the
functions, their arguments, and what they return. For the `unitconv`
command-line tool, see [`usage.md`](usage.md); this page does not repeat the
CLI's behaviour. For why the length and mass tables are built around a single
base unit, see [`why-a-base-unit.md`](why-a-base-unit.md).

## Imports

Six conversion functions are re-exported from the package root:

```python
from unitconv import (
    convert_length,
    convert_mass,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
)
```

The package also exposes `__version__`. The factor tables `FACTORS_LENGTH`
and `FACTORS_MASS` are *not* re-exported at the package root — import those
from the submodule directly:

```python
from unitconv.convert import FACTORS_LENGTH, FACTORS_MASS
```

## Length and mass

```python
convert_length(value: float, from_unit: str, to_unit: str) -> float
convert_mass(value: float, from_unit: str, to_unit: str) -> float
```

Both look up a factor for each unit and return
`value * from_factor / to_factor`. Because every factor is expressed against
a single base unit — the meter for length, the gram for mass — any two units
in the same table can be combined without a factor being stored for that
specific pair.

Unit keys are **case-sensitive**: `Gm` (gigameter) is a valid length unit,
`gm` is not. This differs from the CLI, which lowercases the temperature
units before dispatching.

An unrecognised unit raises `ValueError`, chained from the underlying
`KeyError`:

```python
convert_length(1, "m", "parsec")
```

raises `ValueError` with the message:

```
unsupported unit: 'parsec'
```

The message names the offending unit, not the pair. Note that the parsec
*is* supported — under the key `pc`. To enumerate the valid keys at runtime,
read `FACTORS_LENGTH` and `FACTORS_MASS`; the tables grow over time, so
prefer that over a hard-coded list.

There is no cross-category guard at this layer. `convert_length` only ever
consults `FACTORS_LENGTH`, so asking it for a mass unit raises `ValueError`
on the lookup rather than returning a nonsensical number.

## Temperature

```python
celsius_to_fahrenheit(value: float) -> float
fahrenheit_to_celsius(value: float) -> float
celsius_to_kelvin(value: float) -> float
kelvin_to_celsius(value: float) -> float
```

Temperature is handled by four single-argument functions rather than a table,
because the scales differ by offset as well as by factor — see
[`temperature-scales.md`](temperature-scales.md). These functions raise
nothing and validate nothing: values below absolute zero convert as happily
as any other number.

Celsius is the hub. There is no direct Fahrenheit-to-Kelvin function, so
compose two calls through Celsius.

### A worked example

Converting normal body temperature, 98.6 °F, to Kelvin:

```python
from unitconv import celsius_to_kelvin, fahrenheit_to_celsius

fahrenheit = 98.6
kelvin = celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))
print(kelvin)
```

```
310.15
```

Results are returned as plain floats with no rounding applied, so composing
calls accumulates the usual binary floating-point artifacts. The round trip
above happens to land clean, but many conversions do not — `convert_mass(1,
"st", "lb")` returns `13.999999999999998`, not `14.0`. Round at the point of
use if you need a fixed number of decimal places; see
[`usage.md`](usage.md#how-rounding-is-handled).

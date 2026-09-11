# Temperature scales

Background on the one conversion category that is not a factor table. For the
general argument reference, see [`usage.md`](usage.md).

## Why temperature is special

Length and mass conversions are pure scalings: every unit is recorded as "how
many base units per 1 of this unit", so converting is one multiplication and
one division. Temperature scales do not share a zero point, so no single
factor can describe the relationship between them — Celsius and Fahrenheit
differ in both the size of a degree and where the scale starts, and Kelvin
starts somewhere else again.

That means temperature gets its own code path rather than an entry in a
factor table. `unitconv` accepts `c`, `f`, and `k`, and treats Celsius as the
pivot: the input is converted to Celsius first, then out to the requested
scale. A conversion between the same unit is returned untouched.

## A worked example

Converting body temperature from Fahrenheit to Kelvin exercises both halves of
the pivot, since neither end of the conversion is Celsius:

```bash
unitconv 98.6 f k
```

```
98.6 f = 310.15 k
```

Internally that is two steps. First Fahrenheit to Celsius, subtracting the
offset and rescaling the degree:

```
(98.6 - 32) × 5/9 = 37.0
```

Then Celsius to Kelvin, which is an offset only — a Kelvin and a degree
Celsius are the same size:

```
37.0 + 273.15 = 310.15
```

Going the other direction works the same way, and shows the float behaviour
described in [`usage.md`](usage.md#how-rounding-is-handled) rather than
anything specific to temperature:

```bash
unitconv 300 k f
```

```
300.0 k = 80.33000000000004 f
```

## Details worth knowing

Temperature unit names are matched case-insensitively, so `unitconv 20 C F`
works where an uppercase length unit would not. The echoed input preserves
whatever case you typed:

```bash
unitconv 20 C F
```

```
20.0 C = 68.0 F
```

Only the three single-letter abbreviations are recognised — spelled-out names
like `kelvin` are not, and are reported as an unconvertible pair. The same
error appears if you pair a temperature unit with a length or mass unit, since
there is no meaningful conversion between the categories:

```bash
unitconv 20 c m
```

```
error: cannot convert 'c' to 'm'
```

There is also no physical range checking. Values below absolute zero convert
arithmetically without complaint, so `unitconv -500 c k` reports a negative
Kelvin value rather than an error. If your inputs need to be physically
plausible, validate them before calling.

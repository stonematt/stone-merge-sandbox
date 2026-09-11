# Quickstart

The shortest path from a clone to a working conversion. For the full argument
reference and more examples, see [`usage.md`](usage.md); for install options
beyond the one below, see [`installation.md`](installation.md).

## Install

`unitconv` is pure standard library, so a clone and an editable install are
all it takes:

```bash
git clone https://github.com/stonematt/stone-merge-sandbox.git
cd stone-merge-sandbox
pip install -e .
```

## Convert something

The command takes three positional arguments — a value, the unit to convert
from, and the unit to convert to — and prints the result:

```bash
unitconv 10 km mi
```

```
10.0 km = 6.2137119223733395 mi
```

Two things to notice in that output. The input is echoed back as `10.0`
because the value is parsed as a float, and the result is not rounded: you
get the full precision of the underlying double. Round at the point of use if
you need fewer decimal places.

Temperature works the same way, and is one of the cases where the answer
happens to come out tidy:

```bash
unitconv 100 c f
```

```
100.0 c = 212.0 f
```

## Which units are supported

Any two units in the same category can be combined. Length accepts `mm`,
`cm`, `m`, `km`, `in`, `ft`, `yd`, `mi`, `nm`, `pc`, and `rop`; mass accepts
`mg`, `g`, `kg`, `dr`, `oz`, `ozt`, `lb`, and `st`; temperature accepts `c`,
`f`, and `k`.

Crossing categories is an error rather than a silent surprise — it prints to
standard error and exits non-zero:

```bash
unitconv 2 m kg
```

```
error: cannot convert 'm' to 'kg'
```

The same message appears, with the offending unit named, if you pass a unit
the tables do not know about.

# Performance notes

Short version: a single conversion is too fast to be worth measuring, and
process startup costs roughly a hundred thousand times more than the
arithmetic it wraps. If `unitconv` ever feels slow, the cause is how often
you start the command, not what it does once started. For calling the
command from a shell script, see [`scripting.md`](scripting.md); for calling
it as a library instead, see [`api-reference.md`](api-reference.md).

## What a conversion costs

Length and mass conversions are two dictionary lookups and one multiply-
divide against a base unit, so the cost does not grow as the tables grow —
adding units makes the table bigger without making any conversion slower.
There is no search over pairs of units and no factor stored per pair; see
[`why-a-base-unit.md`](why-a-base-unit.md) for why that design was chosen.
Temperature conversions are pure arithmetic with no table at all, which is
why they are the fastest of the three.

Rough figures from a developer laptop (Python 3.12), good for orders of
magnitude rather than exact comparison:

| Operation | Approximate cost |
| --- | --- |
| Temperature conversion | 0.05 µs |
| Length or mass conversion, unit given as an abbreviation | 0.2 µs |
| Length or mass conversion, unit given as a spelled-out name | 0.6 µs |
| Rejected conversion (unsupported unit) | 2.8 µs |
| `import unitconv` | 3–8 ms |
| One `unitconv` command invocation | ~21 ms |

Two things are worth reading off that table. Spelled-out names such as
`cicero` cost about three times an abbreviation, because they miss the
first dictionary lookup and fall through to a normalising pass. And a
rejected unit costs more than ten successful conversions, because the error
message lists every supported unit and sorts them to do it. Both are
irrelevant at human scale and both matter if you are looping.

## Startup dominates

About half of the ~21 ms of a command invocation is the Python interpreter
starting up, and most of the rest is imports — `argparse` for the command
line, and the standard library `re` module, which the conversion code pulls
in solely to normalise spelled-out unit names. The conversion itself is
under a microsecond of that 21 ms.

The practical consequence is for batch work. A shell loop that calls
`unitconv` once per row pays the full startup cost per row, so ten thousand
conversions take minutes rather than the few milliseconds the arithmetic
needs. If you are converting more than a few hundred values, import the
functions and loop inside one Python process instead:

```python
from unitconv.convert import convert_length

for value in values:
    print(convert_length(value, "mi", "km"))
```

That pays the import cost once. [`scripting.md`](scripting.md) covers the
shell-loop approach and its exit codes, which is the right choice when the
volume is small enough that startup does not matter.

## What is not optimised

Nothing is cached or memoised, and nothing is loaded lazily — the unit
tables are plain dictionaries built when the module is imported. This is
deliberate rather than an oversight: a lookup that already costs a fraction
of a microsecond has no room for a cache to pay for itself, and a cache
keyed on unit names would add a failure mode without removing a real cost.

There are also no benchmarks in the test suite. The figures above were
measured by hand and are not enforced anywhere, so treat them as a
description of the current implementation rather than a guarantee. If a
change makes conversions meaningfully slower, no test will catch it — see
[`contributing.md`](contributing.md) for what the suite does check.

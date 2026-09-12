# Design notes

This page collects the design decisions behind `unitconv` that show up in
day-to-day use — the shape of the code, and the behaviour that shape causes.
For the reasoning behind the factor tables themselves, see
[`why-a-base-unit.md`](why-a-base-unit.md); for the separate temperature path,
see [`temperature-scales.md`](temperature-scales.md); for the list of things
the command does not do, see [`limitations.md`](limitations.md). Everyday
invocation is covered in [`usage.md`](usage.md).

## Two layers, two sets of rules

`unitconv` is a library (`unitconv.convert`) with a thin command-line wrapper
(`unitconv.cli`) on top. The wrapper owns argument parsing, category dispatch,
error printing, and exit codes; the library owns the arithmetic. That split is
what makes [`scripting.md`](scripting.md) and
[`api-reference.md`](api-reference.md) two different stories rather than one.

The consequence worth knowing is that the two layers do not accept exactly the
same inputs. `convert_length` and `convert_mass` accept a spelled-out name as
well as an abbreviation, case-insensitively:

```python
>>> convert_length(1, "cicero", "m")
0.004513
```

The command does not:

```bash
unitconv 1 cicero m
```

```
error: cannot convert 'cicero' to 'm'
```

The command matches unit arguments against the tables exactly before it calls
the library, so only the abbreviation (`cic`) reaches the conversion function.
Spelled-out names and alternate casing are a library affordance, not a CLI one.

## Category is inferred, not declared

There is no `--length` or `--category` flag. The command decides which
conversion to run by looking up both unit arguments, in a fixed order:
temperature first (case-insensitively, against `c`, `f`, `k`), then length,
then mass. The first table that contains *both* units wins; if none does, the
conversion is refused rather than guessed.

This keeps the common case to three arguments and no ceremony, and it is why
mixing categories is an error rather than a surprising number — `km` and `lb`
never both appear in one table. It also means unit names have to stay unique
across categories. The length and mass tables are disjoint today, and a new
unit that collided with an existing name would silently resolve to whichever
table is checked first; see [`contributing.md`](contributing.md) before adding
one.

## Floats, one conversion at a time

Conversions are ordinary double-precision floating point — `value *
from_factor / to_factor` — not `Decimal` or `Fraction`. That is a deliberate
trade: it keeps the tables readable as plain numbers and the command fast to
start, at the cost of the usual trailing-digit artifacts. Nothing is rounded on
your behalf, which is covered in
[`usage.md`](usage.md#how-rounding-is-handled).

Each invocation performs exactly one conversion and exits. There is no REPL, no
stdin mode, and no batch flag, so converting a column of values means a shell
loop — [`scripting.md`](scripting.md) has the pattern. The command also has no
runtime dependencies beyond the Python standard library, which is what lets
[`installation.md`](installation.md) stay as short as it is.

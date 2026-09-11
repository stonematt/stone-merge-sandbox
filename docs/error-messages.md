# Error messages

This page explains what `unitconv` prints when a conversion does not work,
and — just as important — the cases where it prints a number instead of an
error. For the command's arguments and supported conversions, see
[`usage.md`](usage.md). For branching on exit codes in a shell script, see
[`scripting.md`](scripting.md); for the exceptions the library functions
raise when you import them, see [`api-reference.md`](api-reference.md).

Every error goes to standard error, and nothing is written to standard
output. A failed run captured with a bare `$(...)` therefore yields an empty
string, not an error message.

## `error: cannot convert 'x' to 'y'`

This is the only error the command itself formats, and it covers three
different problems. The message names both units but does not say which one
it objected to:

```bash
unitconv 3 ft kg
```

```
error: cannot convert 'ft' to 'kg'
```

The three causes, in rough order of how often they bite:

1. **The two units are in different categories.** Length, mass, and
   temperature are separate tables, and no conversion crosses between them —
   `ft` to `kg` above, or `c` to `ft`.
2. **One of the units is not in the table.** `unitconv 1 ft parsec` fails
   because the parsec is stored under the key `pc`, not `parsec`.
   Abbreviations are the keys; spelled-out names are never accepted.
3. **The case does not match.** This one is worth its own section.

### Worked example: case-sensitive unit keys

Length and mass units are matched exactly as typed. Temperature units are
not — the command lowercases them before dispatching. So this works:

```bash
unitconv 1 C F
```

```
1.0 C = 33.8 F
```

and this, which looks equivalent, does not:

```bash
unitconv 1 FT m
```

```
error: cannot convert 'FT' to 'm'
```

The fix is to type `ft`. The trap is that most keys are lowercase, so
lowercasing everything out of habit mostly works — until it doesn't:
`Gm` (gigameter) is a valid length key and `gm` is not, so an unconditional
`tr A-Z a-z` in a wrapper script will break that one unit while fixing the
rest. Match the table rather than normalising.

Note also that the echoed units in a *successful* line come back exactly as
you typed them, not canonicalised — `1.0 C = 33.8 F` above, not `1.0 c`.

## Argument errors

A malformed command line is rejected by `argparse` before any conversion is
attempted. These print a usage line first and exit `2` rather than `1`:

```bash
unitconv abc ft m
```

```
usage: unitconv [-h] value from_unit to_unit
unitconv: error: argument value: invalid float value: 'abc'
```

Passing a fourth argument produces `unitconv: error: unrecognized
arguments: kg`, and omitting arguments produces `unitconv: error: the
following arguments are required: to_unit` (naming whichever are missing).

The distinction from the previous section matters when scripting: exit `1`
means the units were the problem and a different pair might work, while exit
`2` means the command line itself was malformed.

## What is *not* an error

`unitconv` validates that it knows both units. It does not validate that the
result is physically meaningful, so several situations that feel like errors
produce a number and exit `0` instead:

- **Temperatures below absolute zero.** Nothing checks for them.
  `unitconv -500 k c` reports `-500.0 k = -773.15 c` quite happily.
- **`nan` and `inf`**, which Python's float parser accepts, pass straight
  through: `unitconv nan ft m` prints `nan ft = nan m`.
- **Overflow**, which becomes `inf` silently rather than raising.
- **Converting a unit to itself**, which is computed rather than
  short-circuited for length and mass, and so can return a value a hair off
  from the input on some pairs.

The one to watch is a unit key that means something other than what you
assumed, because the result looks entirely reasonable:

```bash
unitconv 5 mi nm
```

```
5.0 mi = 8046720000000.0 nm
```

`nm` is the nanometer, not the nautical mile. The answer is correct and
about twelve orders of magnitude from what someone reaching for nautical
miles wanted. `mu` (micron) sits one keystroke from `mi` with a similar
hazard. When a result is surprising, check the key against
`FACTORS_LENGTH` or `FACTORS_MASS` before assuming the conversion is wrong —
see [`api-reference.md`](api-reference.md) for reading those tables at
runtime, and [`history-of-units.md`](history-of-units.md) for what the less
obvious abbreviations refer to.

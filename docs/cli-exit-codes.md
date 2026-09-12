# CLI exit codes

`unitconv` reports the outcome of a run through its exit code, so a caller
can tell a failed conversion from a successful one without reading the
output. This page is the reference for what each code means and how to
check it. For the command's arguments and the conversions it supports, see
[`usage.md`](usage.md); for the surrounding shell patterns — capturing the
output line, batch loops — see [`scripting.md`](scripting.md); for working
out why a particular call failed, see
[`troubleshooting.md`](troubleshooting.md).

## The codes

| Code | Meaning |
| --- | --- |
| `0` | The conversion succeeded and the result is on standard output. |
| `1` | The units are not convertible — unknown, or from different categories. |
| `2` | The arguments were rejected before any conversion was attempted. |

`unitconv --help` also exits `0`.

## Where the output goes

A successful run prints its one result line to standard output and nothing
to standard error. Both failure codes do the reverse — the message goes to
standard error and standard output stays empty, so a bare `$(...)` capture
of a failed call yields an empty string rather than an error message.

```bash
unitconv 3 ft kg
echo "exit: $?"
```

```
error: cannot convert 'ft' to 'kg'
exit: 1
```

## Telling `1` and `2` apart

The distinction is worth keeping, because it says whether a retry is worth
attempting. Code `1` means the command line was well formed and the units
were the problem, so a different pair might work. Code `2` means
`argparse` never got as far as converting anything — a value that is not a
number, or a missing argument — and no choice of units will help.

```bash
unitconv abc ft m
echo "exit: $?"
```

```
usage: unitconv [-h] value from_unit to_unit
unitconv: error: argument value: invalid float value: 'abc'
exit: 2
```

## Capitalisation exits `1`

Length and mass units are matched exactly as typed, so a capitalised
abbreviation is an unknown unit rather than a recognised one, and exits
`1`:

```bash
unitconv 5 MI km
```

```
error: cannot convert 'MI' to 'km'
```

Temperature is the exception: `c`, `f`, and `k` are lowercased before
dispatch, so `unitconv 20 C F` succeeds and exits `0`. A script that builds
unit names from user input or a data file should lowercase them before
calling, or an otherwise valid pair will come back as an exit `1` that
looks like an unsupported unit.

## Branching on the code

The shell's `if` already tests for exit `0`, so the common case needs no
explicit comparison:

```bash
if result=$(unitconv 5 mi km); then
    echo "got: $result"
else
    echo "conversion failed" >&2
fi
```

Compare `$?` directly only when `1` and `2` call for different handling —
reporting an unusable unit pair back to the caller, say, while treating a
malformed argument as a bug in the script itself. For looping over many
values and parsing the result line, see [`scripting.md`](scripting.md).

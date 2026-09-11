# Scripting with unitconv

This page covers calling `unitconv` from a shell script — what to check, what
to parse, and when to stop shelling out altogether. For the command's three
arguments and the conversions it supports, see [`usage.md`](usage.md). For
tab completion at an interactive prompt, see
[`shell-completion.md`](shell-completion.md). If the script is itself Python,
skip this page and import the functions directly — see
[`api-reference.md`](api-reference.md).

## Exit codes

`unitconv` distinguishes three outcomes, and a script should branch on the
exit code rather than on the text of the output:

| Code | Meaning |
| --- | --- |
| `0` | The conversion succeeded; the result is on standard output. |
| `1` | The units are not convertible — unknown, or from different categories. |
| `2` | `argparse` rejected the arguments, such as a value that is not a number. |

Codes `1` and `2` both write to standard error and print nothing to standard
output, so a bare `$(...)` capture of a failed call yields an empty string.
That distinction is worth keeping: code `1` means the units were the problem
and a different pair might work, while code `2` means the command line was
malformed and retrying with other units will not help.

```bash
unitconv 3 ft kg
```

```
error: cannot convert 'ft' to 'kg'
```

## Parsing the output line

A successful run prints one line in a fixed five-field shape:

```
<value> <from_unit> = <result> <to_unit>
```

The converted number is always the fourth whitespace-separated field, which
makes `awk` the shortest way to pull it out:

```bash
unitconv 5 mi km | awk '{print $4}'
```

```
8.04672
```

Two properties of that line matter when parsing it. The echoed value is
reformatted — the argument is parsed as a float, so `5` comes back as `5.0`.
The units, by contrast, are echoed exactly as typed, including case: the CLI
lowercases temperature units before dispatching but prints your spelling
back, so `unitconv 20 C F` reports `20.0 C = 68.0 F`. Do not rely on the
echoed units being canonical.

The result is unrounded, full-precision float output — see
[how rounding is handled](usage.md#how-rounding-is-handled). Round in the
script if you need fixed decimals:

```bash
printf '%.2f\n' "$(unitconv 70 kg lb | awk '{print $4}')"
```

```
154.32
```

## Batch conversions

For a handful of values, a loop over the command is fine. Capture the output
and let the exit code drive the branch, so an unconvertible pair is reported
rather than silently producing an empty result:

```bash
for unit in km kg zz; do
    if out=$(unitconv 5 mi "$unit" 2>&1); then
        echo "ok:   $out"
    else
        echo "skip: $out"
    fi
done
```

```
ok:   5.0 mi = 8.04672 km
skip: error: cannot convert 'mi' to 'kg'
skip: error: cannot convert 'mi' to 'zz'
```

Redirecting standard error into the capture with `2>&1` is what puts the
error message into `$out` on the failing iterations; without it the message
still reaches the terminal, but `$out` is empty and the script has nothing to
report.

This pattern costs one Python interpreter start per conversion, which is
invisible for a dozen values and painful for a few thousand. At that scale,
call the library once from a single Python process instead of looping in the
shell — `convert_length`, `convert_mass`, and the temperature helpers are
documented in [`api-reference.md`](api-reference.md).

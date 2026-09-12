# Known limitations

`unitconv` converts one value between two units of the same kind, and that is
the whole of it. This page collects the boundaries of that job in one place —
the things the command does not do, as opposed to the things it does badly.
For a conversion that errors out or returns a number you did not expect, the
diagnostic steps are in [`troubleshooting.md`](troubleshooting.md); for the
library entry points behind the command, see
[`api-reference.md`](api-reference.md).

- **Three categories only.** Length, mass, and temperature. Volume, time,
  area, speed, pressure, and data sizes are not in the tables, and there is
  no mechanism for adding a category at runtime.
- **Unit names are exact.** Length and mass units are matched as literal
  table keys, so `KM`, `Ft`, and `KG` all fail — only temperature accepts any
  casing. Plurals and spelled-out names (`meters`, `kilogram`) are not
  aliases. Note that `Mm` and `mm` are different units, as are `Gm` and `gm`,
  so a stray shift key changes the answer by nine orders of magnitude rather
  than producing an error.
- **No physical range checks.** Values are taken as given, which means
  `unitconv -500 c k` reports `-226.85000000000002 k` instead of rejecting a
  temperature below absolute zero. Negative lengths and masses convert just
  as willingly.
- **One conversion per invocation.** There is no stdin mode, no batch mode,
  and no way to ask for several target units at once; see
  [`comparison-tables.md`](comparison-tables.md) for the shell loop that
  stands in for the last of those.
- **The output line is fixed.** No `--format`, no JSON, and no
  `--precision` — results carry Python's full float repr, and the echoed
  input is reformatted as a float, so `5` comes back as `5.0`.
- **No introspection or configuration.** There is no `--list-units`, no
  `--version` flag, no config file, and no environment variables. The unit
  tables are readable only by importing the module or reading
  [`comparison-tables.md`](comparison-tables.md).

Two of these are deliberate rather than pending. The absence of rounding
keeps the command from quietly discarding precision that a caller may need,
which is why the fix for ugly trailing digits is to round at the point of use;
and the absence of unit aliases keeps the table unambiguous in the cases where
two plausible spellings mean genuinely different sizes. The remaining entries
are simply unimplemented, and nothing in the current design prevents them
being added.

Failures are quiet and consistent, which is the part worth relying on: an
unknown unit or a cross-category pair prints `error: cannot convert 'X' to
'Y'` to standard error and exits 1, a non-numeric value exits 2 with an
argparse usage line, and neither writes anything to standard output. The exit
codes and the parsing rules that follow from them are documented in
[`scripting.md`](scripting.md).

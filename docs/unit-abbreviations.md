# Unit abbreviations

Every unit is named by a short abbreviation, and those abbreviations are the
only spelling the command accepts — there is no long form, no plural, and no
alias table. `unitconv 5 mi km` works; `unitconv 5 miles km` does not, and
fails the same way an unknown unit would. The abbreviations for length and
mass are looked up as exact strings, so case matters for them: `Gm` is the
gigametre and `mm` is the millimetre, but `MM` and `gm` are not units at all.
Temperature is the exception — `c`, `f`, and `k` are lowercased before the
lookup, so `unitconv 20 C F` behaves exactly like `unitconv 20 c f`.

A few abbreviations sit close enough to each other to be worth reading twice
before you type them:

- `nm` is the nanometre and `nmi` is the nautical mile. They differ by twelve
  orders of magnitude, and nothing warns you about picking the wrong one —
  see [`nautical-units.md`](nautical-units.md).
- `mil` and `th` are two names for the same length, a thousandth of an inch.
  Either works; [`typography-units.md`](typography-units.md) covers where
  each one is conventional.
- `rd` and `prc` — the rod and the perch — are likewise the same length, as
  are `ch` and `lnk` at chain and link scale. See
  [`history-of-units.md`](history-of-units.md).
- `mu` is the micrometre, written out rather than as `µ`, so the table stays
  typeable from an ASCII keyboard.
- `dr` is the dram and `dg` the decigram: adjacent on the keyboard, a factor
  of about seventeen apart in the mass table.

Because the command picks a category by finding both units in the same
table, a mistyped abbreviation usually surfaces as `error: cannot convert`
rather than as a wrong number — a length paired with a mass has no table to
land in. The silent failures are the ones where the typo is itself a valid
unit in the same category, which is why the pairs above are worth a second
look. [`troubleshooting.md`](troubleshooting.md) walks through what to check
when a conversion errors out or returns something implausible.

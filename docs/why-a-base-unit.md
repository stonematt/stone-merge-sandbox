# Why every table has a base unit

`unitconv` stores each unit as a single number: how many base units make up
one of it. Length uses the meter as its base, mass uses the gram. That choice
is what keeps `FACTORS_LENGTH` and `FACTORS_MASS` small enough to read at a
glance, and it is why adding a unit to either table is a one-line change.

## The alternative is a pairwise table

Without a shared base, a conversion table has to answer every question
directly: how many feet in a chain, how many chains in a rod, how many rods
in a mile. That is a factor for every *pair* of units. The length table
currently holds 18 units, which is 153 distinct pairs — and each new unit
added would require 18 more entries, not one.

Routing through a base unit turns that multiplication back into addition. Each
unit needs to know its relationship to the meter and nothing else; the
relationship between any two units falls out of the arithmetic. Both
`convert_length` and `convert_mass` are three lines for exactly this reason —
look up two factors, multiply by one and divide by the other.

## A worked example

The historical surveying units make the point well, because the numbers
between them are memorable but the numbers to the meter are not. The table
knows only these two facts:

```python
"rd": 5.0292,     # a rod is 5.0292 m
"ch": 20.1168,    # a chain is 20.1168 m
```

Neither entry mentions the other. But ask for the conversion and you get the
surveyor's answer exactly:

```bash
unitconv 1 ch rd
```

```
1.0 ch = 4.0 rd
```

Four rods to the chain — which is how the units were defined, but that fact
was never written down anywhere in the table. The same two factors also give
`unitconv 1 ch ft` as 66 ft and `unitconv 1 mi ch` as 80 ch, none of which
required a `ch`-to-`ft` or `mi`-to-`ch` entry.

This also explains something about the factors themselves. They look
oddly specific — `20.1168` rather than a round number — because the base unit
absorbs all of the awkwardness. The relationships *between* the units in a
family are usually clean; it is their relationship to the meter that is not.
See [`history-of-units.md`](history-of-units.md) for where several of these
definitions came from.

## Where the pattern breaks down

A base unit only works when every unit in the category is a pure scaling of
it, so that a conversion is one multiplication and one division. Temperature
is not. Celsius and Fahrenheit differ by an offset as well as a scale, and
"0 °C" does not mean "zero of anything" the way 0 m does — so no table of
factors can express the conversion.

That is why temperature lives in its own set of named functions
(`celsius_to_fahrenheit` and friends) rather than a third factor table, and
why it is the one category where adding a scale means adding code instead of
a table entry. See [`temperature-scales.md`](temperature-scales.md) for how
those conversions are handled.

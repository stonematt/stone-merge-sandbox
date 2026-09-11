# Conversion comparison tables

A comparison table is one value shown in several units at once — a metre in
centimetres, inches, feet, and yards, side by side. `unitconv` has no flag
for this, and does not need one: because each category is anchored to a
single base unit, the same input converts to every other unit in its table
independently. Loop over the target units and collect the lines. The loop
shape, the exit-code check, and the point at which shelling out stops paying
for itself are all in [`scripting.md`](scripting.md).

```bash
for unit in cm in ft yd; do unitconv 1 m "$unit"; done
```

```
1.0 m = 100.0 cm
1.0 m = 39.37007874015748 in
1.0 m = 3.280839895013123 ft
1.0 m = 1.0936132983377078 yd
```

What makes a table readable is mostly the choice of rows, and that is on you
rather than the command:

- **Stay inside one category.** A row that mixes a length and a mass exits
  with code `1` and prints nothing to standard output, so a table built by a
  naive loop will simply have a hole in it.
- **Keep the span narrow.** Neighbouring units compare well; `pc` next to
  `mil` does not. The far end of the length table has its own page,
  [`astronomical-units.md`](astronomical-units.md).
- **Round for display.** Columns of unrounded doubles are what makes a table
  hard to scan — pipe each result through `printf`, as in
  [how rounding is handled](usage.md#how-rounding-is-handled).
- **Pick a base that is not a surprise.** Converting *from* the category's
  base unit keeps the rows easy to sanity-check by eye; see
  [`why-a-base-unit.md`](why-a-base-unit.md).
- **Temperature is not a table of factors.** Celsius, Fahrenheit, and Kelvin
  convert by offset as well as scale, so a comparison row there means three
  separate calls — see [`temperature-scales.md`](temperature-scales.md).

For more than a handful of rows, build the table in Python instead. One
process calling `convert_length` or `convert_mass` in a loop avoids an
interpreter start per cell and hands you floats you can format however the
table needs; the functions are documented in
[`api-reference.md`](api-reference.md).

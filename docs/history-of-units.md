# A short history of the units

Background on where the entries in the two factor tables came from. The
tables mix units that were defined by pacing out a field with units that were
defined by a telescope, which is why some factors are round numbers and
others are not. For the argument reference, see [`usage.md`](usage.md); for
the one category that is not a factor table, see
[`temperature-scales.md`](temperature-scales.md).

## Bodies, fields, and roads

The oldest units in the length table are the ones you could reproduce without
instruments. The inch, foot, and yard all trace back to body measurements,
and the units above them were built for laying out land: the rod (`rd`, also
called the pole or perch) is five and a half yards, four rods make a
surveyor's chain, and forty rods make a furlong — originally the length of a
ploughed furrow. The rope (`rop`) is a twenty-foot builder's and surveyor's
cord from the same family.

Travel distances were standardised later and regionally. The mile descends
from the Roman *mille passus*, a thousand double paces, but the English
statute mile was fixed at 5,280 feet by Parliament in 1593 — a number chosen
so the mile would come out to a whole eight furlongs rather than anything
tidy in feet. The Japanese ri (`ri`) went through the same kind of
reconciliation: it is 36 *chō*, and the Meiji-era weights and measures reform
pinned it to the metre at 3,927.27 m, which is the value the table uses.

### A worked example

The rod looks like the awkward unit in that chain, but it is the one doing
the work. Ask for a mile in rods and the answer is exact:

```bash
unitconv 1 mi rd
```

```
1.0 mi = 320.0 rd
```

That 320 is 8 furlongs × 40 rods, and it only lands on a whole number
because 5,280 feet was picked to make it do so. The rod itself is the
untidy-looking half:

```bash
unitconv 1 rd ft
```

```
1.0 rd = 16.5 ft
```

So the fractional factor in the table (`5.0292` metres) is not an
approximation of anything — it is 16.5 feet exactly, and the roundness of
the mile is the derived fact.

## Trade weights

The mass table carries the consequences of measuring goods for sale. Two
ounce systems survive in it: the avoirdupois ounce (`oz`) of 437.5 grains,
used for general goods, and the troy ounce (`ozt`) of 480 grains, still the
unit for precious metals. They differ by about 9.7%, which is the sort of
discrepancy worth checking before trusting a number that just says "ounces".
The dram (`dr`) is a sixteenth of the avoirdupois ounce, and the stone (`st`)
is fourteen pounds — a retail bulk unit that stuck around in Britain for
body weight.

The two outliers came from other trade systems entirely. The mina (`mna`) is
Mesopotamian, sixty shekels to the mina and sixty mina to the talent,
following the same sexagesimal counting as the hour; actual standards varied
by city and period, and the table uses 430 g. The picul (`pcl`) is a
Chinese and Southeast Asian unit that started as a shoulder-pole load — as
much as one person could carry — and was later standardised for export trade
at 133⅓ pounds, or 60.478982 kg.

Only the pound and ounce have modern exact definitions, from the 1959
international yard and pound agreement, which is why `lb` is the very
specific 453.59237 g.

## Units from the lab and the sky

The metric entries work differently: `mm`, `cm`, `km`, `nm`, and `Gm` are all
just SI prefixes on the metre, so there is nothing historical in their
factors beyond powers of ten. The metre behind them has moved, though — from
a fraction of the Earth's meridian in 1793 to a defined fraction of the
distance light travels in a second, since 1983.

The parsec (`pc`) is observational rather than decimal. It is the distance at
which one astronomical unit subtends one arcsecond — the parallax angle a
star shows as the Earth crosses its orbit — so its size is set by the
geometry of the measurement, not by convention. The name dates to 1913.

The x unit (`xu`) is the one obsolete entry. It was introduced for X-ray
wavelengths in the early twentieth century, defined against the lattice
spacing of a calcite crystal, back when that spacing was known more
precisely than the metre relationship was. That relationship had to be
measured rather than declared, which is why its factor is a handful of
significant figures (`1.0021e-13`) rather than an exact value. Treat
conversions through `xu` as approximate.

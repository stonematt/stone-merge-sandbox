# Usage

`unitconv` takes three positional arguments: a numeric value, the unit to
convert from, and the unit to convert to. It prints the converted value to
standard output.

```bash
unitconv <value> <from_unit> <to_unit>
```

Length and mass conversions use a simple linear factor table, so any pair of
units within the same category can be combined directly, for example
`unitconv 3 ft yd` or `unitconv 2 lb oz`. Temperature conversions between
Celsius (`c`), Fahrenheit (`f`), and Kelvin (`k`) are handled separately since
they are not simple linear scalings of a shared base unit.

Mixing categories, such as converting a length to a mass, is not supported
and will print an error message with a non-zero exit code.

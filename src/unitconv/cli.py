"""Command-line interface for unitconv."""

import argparse
import sys

from .convert import (
    FACTORS_LENGTH,
    FACTORS_MASS,
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    convert_length,
    convert_mass,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)

TEMP_UNITS = {"c", "f", "k"}


def _convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit == to_unit:
        return value

    celsius = value
    if from_unit == "f":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "k":
        celsius = kelvin_to_celsius(value)

    if to_unit == "f":
        return celsius_to_fahrenheit(celsius)
    if to_unit == "k":
        return celsius_to_kelvin(celsius)
    return celsius


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="unitconv", description="Convert a value between units."
    )
    parser.add_argument("value", type=float, help="the numeric value to convert")
    parser.add_argument("from_unit", help="unit to convert from")
    parser.add_argument("to_unit", help="unit to convert to")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    from_unit = args.from_unit
    to_unit = args.to_unit

    try:
        if from_unit.lower() in TEMP_UNITS and to_unit.lower() in TEMP_UNITS:
            result = _convert_temperature(args.value, from_unit, to_unit)
        elif from_unit in FACTORS_LENGTH and to_unit in FACTORS_LENGTH:
            result = convert_length(args.value, from_unit, to_unit)
        elif from_unit in FACTORS_MASS and to_unit in FACTORS_MASS:
            result = convert_mass(args.value, from_unit, to_unit)
        else:
            print(f"error: cannot convert {from_unit!r} to {to_unit!r}", file=sys.stderr)
            return 1
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"{args.value} {from_unit} = {result} {to_unit}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

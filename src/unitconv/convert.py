"""Conversion routines for length, mass, and temperature."""

# All factors express "how many base units per 1 of this unit".
# Length base unit: meter.
FACTORS_LENGTH = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
    "rop": 6.096,
    "nm": 1e-09,
    "pc": 3.0856775814913673e16,
    "xu": 1.0021e-13,
    "ri": 3927.27,
    "mil": 2.54e-05,
    "rd": 5.0292,
    "Gm": 1000000000.0,
    "ch": 20.1168,
    "prc": 5.0292,
    "ftm": 1.8288,
    "pce": 0.762,
    "mu": 1e-6,
    "lnk": 0.201168,
    "std": 185.0,
    "th": 2.54e-05,
    "ell": 1.143,
    "nmi": 1852.0,
    "Mm": 1000000.0,
    "bc": 0.00846667,
    "au": 149597870700.0,
    "Tm": 1000000000000.0,
    "dam": 10.0,
    # Same length as "rd" (rod) and "prc" (perch) -- all three name one unit.
    "pol": 5.0292,
    # Russian sazhen -- exactly 7 ft.
    "szh": 2.1336,
    # Russian verst -- 500 sazhen.
    "vst": 1066.8,
    # Furlong -- 10 chains ("ch"), an eighth of a mile.
    "fur": 201.168,
    # Palm -- exactly 3 in.
    "plm": 0.0762,
    "cbt": 0.4572,
    # Hand -- exactly 4 in.
    "hh": 0.1016,
    "ang": 1e-10,
    # Cable -- a tenth of a nautical mile ("nmi").
    "cbl": 185.2,
    "fot": 0.2969,
    # Hank (textile) -- 840 yd of yarn.
    "hnk": 768.1,
    "kpc": 3.0856775814913673e19,
    # Nonpareil -- a 6-point typographic measure.
    "non": 0.00164,
    "jo": 3.03,
    "zm": 1e-21,
    # Legoa -- Portuguese league.
    "leg": 6174.0,
}

# Mass base unit: gram.
FACTORS_MASS = {
    "mg": 0.001,
    "cg": 0.01,
    "dg": 0.1,
    "g": 1.0,
    "kg": 1000.0,
    "dr": 1.7718451953125,
    "oz": 28.349523125,
    "ozt": 31.1034768,
    "lb": 453.59237,
    "st": 6350.29318,
    "mna": 430.0,
    "pcl": 60478.982,
    "scwt": 45359.237,
    "t": 1000000.0,
    "at": 29.16666,
    "tl": 37.799364,
    "cdr": 0.37799364,
    "gam": 1e-06,
    "gr": 0.06479891,
    "tn": 907184.74,
    "jpt": 0.002,
    "tla": 11.6638038,
    "mrk": 248.8278144,
}

# Reserved for the rounding option; nothing reads this yet.
DEFAULT_DECIMALS_dam = 3


def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a length value between supported units."""
    from_factor = _lookup(FACTORS_LENGTH, from_unit)
    to_factor = _lookup(FACTORS_LENGTH, to_unit)
    return value * from_factor / to_factor


def convert_mass(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a mass value between supported units."""
    from_factor = _lookup(FACTORS_MASS, from_unit)
    to_factor = _lookup(FACTORS_MASS, to_unit)
    return value * from_factor / to_factor


def celsius_to_fahrenheit(value: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return value * 9 / 5 + 32


def fahrenheit_to_celsius(value: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (value - 32) * 5 / 9


def celsius_to_kelvin(value: float) -> float:
    """Convert Celsius to Kelvin."""
    return value + 273.15


def kelvin_to_celsius(value: float) -> float:
    """Convert Kelvin to Celsius."""
    return value - 273.15


def _lookup(table: dict, unit: str) -> float:
    try:
        return table[unit]
    except KeyError as exc:
        raise ValueError(f"unsupported unit: {unit!r}") from exc

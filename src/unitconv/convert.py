"""Conversion routines for length, mass, and temperature."""
import re
import functools

# All factors express "how many base units per 1 of this unit".
# Length base unit: meter.
FACTORS_LENGTH = {
    # Cicero (typographic) -- spelled out as "cicero" in _lookup.
    "cic": 0.004513,
    # Pous (Greek foot) -- spelled out as "pous (Greek foot)" in _lookup.
    "pous": 0.308,
    # Vitasti (Indian span) -- spelled out as "vitasti (Indian span)" in _lookup.
    "vit": 0.2286,
    # Em (typographic) -- spelled out as "em (typographic)" in _lookup.
    "emu": 0.0042333,
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
    "prl": 0.001307,
    "brc": 2.2,
    "sun": 0.0303,
    "roe": 3.767,
    "kos": 3218.0,
    # Hasta (Indian cubit) -- spelled out as "hasta (Indian cubit)" in _lookup.
    "hst": 0.457,
    # Actus (Roman) -- spelled out as "actus (Roman)" in _lookup.
    "act": 35.5,
    # Pulgada (Spanish inch) -- spelled out as "pulgada (Spanish inch)" in _lookup.
    "pul": 0.0232,
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


_FULL_NAMES = {
    "actus (roman)": "act",
    "braça (Portuguese fathom)": "brc",
    "cicero": "cic",
    "em (typographic)": "emu",
    "hasta (indian cubit)": "hst",
    "kos (Indian)": "kos",
    "pearl (printing)": "prl",
    "pous (greek foot)": "pous",
    "pulgada (spanish inch)": "pul",
    "roede (Dutch rod)": "roe",
    "sun (Japanese)": "sun",
    "vitasti (indian span)": "vit",
}


def _lookup(table: dict, unit: str) -> float:
    """Look a unit up in a table, accepting the spelled-out name too."""
    def _normalize(u):
        return re.sub(r"\s+", " ", str(u).strip().lower())

    text = str(unit).strip()
    if text in table:
        return table[text]
    key = _FULL_NAMES.get(_normalize(text))
    if key is not None and key in table:
        return table[key]
    known = ", ".join(sorted(table))
    raise ValueError(f"unsupported unit: {unit!r} (supported: {known})")

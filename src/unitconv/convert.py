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
    # Fut (Russian foot) -- same length as "ft"; spelled out as "fut (Russian foot)" in _lookup.
    "fut": 0.3048,
    # Voet (Dutch foot) -- distinct from the Dutch rod "roe" above.
    "voe": 0.2831,
    # Light-minute -- exactly 60 s of light in vacuum (299792458 m/s).
    "lmin": 17987547480.0,
    # El (Dutch ell) -- "ell" above is the English one (1.143 m).
    "eld": 0.687,
    # Zettametre -- 1e21 m; the counterpart to the zeptometre "zm" (case-sensitive).
    "Zm": 1e21,
    # Agate (typographic) -- a 5.5-point measure, about 1/14 in.
    "agt": 0.00181,
    # Legua (Spanish league) -- the Castilian league; "pul" above is the Spanish inch.
    "lgu": 4190.0,
    # Vara castellana (surveying) -- the Castilian vara; "pul" above is the Spanish inch.
    "vac": 0.8382,
    # Vershok (Russian) -- 1/16 of an arshin; "fut" above is the Russian foot.
    "vshk": 0.04445,
    # Twip (typographic) -- a twentieth of a point, 1/1440 in.
    "twp": 0.0000176389,
    # Bu (Japanese) -- 1/10 of a sun, 1/100 of a shaku.
    "jbu": 0.00303,
    # Tum (Swedish inch) -- the pre-metric Swedish inch; "in" above is the English one.
    "tum": 0.0247,
    # Femtometre -- 1e-15 m; also known as the fermi in nuclear physics.
    "fm": 1e-15,
    # Lieue (French league) -- "lgu" above is the Spanish (Castilian) league.
    "lieu": 4444.0,
    # Pixel (96 dpi) -- the CSS reference pixel, 1/96 in.
    "pxl": 0.0002645833,
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
    "mnd": 37324.2,
    "fg": 1e-15,
    "clv": 3628.74,
    "fun": 0.375,
    "drc": 3.207,
    "lib": 460.0,
    "kan": 3750.0,
    "Da": 1.6605390666e-24,
    # Long hundredweight -- 112 lb; "scwt" above is the short (100 lb) one.
    "cwt": 50802.34544,
    # Sack (wool) -- 26 st (364 lb).
    "sck": 165107.62,
    # Troy pound -- 12 ozt; "lb" above is the avoirdupois (16 oz) one.
    "lbt": 373.2417216,
    # Libra (Portuguese) -- "lib" above is the Castilian one (460 g).
    "libp": 459.0,
    # Megagram -- same magnitude as the tonne "t"; distinct from "mg" (case-sensitive).
    "Mg": 1000000.0,
    # Arroba (Spanish) -- 25 libras; "lib" above is that libra (460 g).
    "arb": 11502.9,
    # Candy (Indian) -- bulk trade measure, ~500 lb.
    "cdy": 226500.0,
    # Petagram -- 1e15 g; the counterpart to the femtogram "fg" (case-sensitive).
    "Pg": 1e15,
    # Quintal (Portuguese) -- the Portuguese arroba is not "arb" above (that one is Spanish).
    "qpt": 58750.0,
    # Seer (Indian) -- roughly 1/40 of the maund "mnd" above.
    "ser": 933.10,
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
    "fut (russian foot)": "fut",
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

"""Tests for unitconv.convert."""

import pytest

from unitconv.convert import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    convert_length,
    convert_mass,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


def test_convert_length_meters_to_km():
    assert convert_length(1000, "m", "km") == pytest.approx(1.0)


def test_convert_length_inches_to_cm():
    assert convert_length(1, "in", "cm") == pytest.approx(2.54)


def test_convert_length_miles_to_km():
    assert convert_length(1, "mi", "km") == pytest.approx(1.609344)


def test_convert_length_parsec_to_miles():
    assert convert_length(1, "pc", "mi") == pytest.approx(1.917351157671304e13)


def test_convert_length_ri_to_miles():
    assert convert_length(1, "ri", "mi") == pytest.approx(2.4402924421379146)


def test_convert_length_unsupported_unit_raises():
    with pytest.raises(ValueError):
        convert_length(1, "m", "parsec")


def test_convert_mass_kg_to_lb():
    assert convert_mass(1, "kg", "lb") == pytest.approx(2.20462262, rel=1e-6)


def test_convert_mass_oz_to_g():
    assert convert_mass(1, "oz", "g") == pytest.approx(28.349523125)


def test_convert_mass_decigram_to_kg_and_back():
    assert convert_mass(1, "dg", "kg") == pytest.approx(0.0001)
    assert convert_mass(0.0001, "kg", "dg") == pytest.approx(1.0)


def test_convert_mass_stone_to_kg_and_back():
    assert convert_mass(1, "st", "kg") == pytest.approx(6.35029318)
    assert convert_mass(6.35029318, "kg", "st") == pytest.approx(1.0)


def test_convert_mass_troy_ounce_to_kg_and_back():
    assert convert_mass(1, "ozt", "kg") == pytest.approx(0.0311034768)
    assert convert_mass(0.0311034768, "kg", "ozt") == pytest.approx(1.0)


def test_convert_mass_dram_to_kg_and_back():
    assert convert_mass(1, "dr", "kg") == pytest.approx(0.0017718451953125)
    assert convert_mass(0.0017718451953125, "kg", "dr") == pytest.approx(1.0)


def test_convert_mass_mina_to_kg_and_back():
    assert convert_mass(1, "mna", "kg") == pytest.approx(0.43)
    assert convert_mass(0.43, "kg", "mna") == pytest.approx(1.0)


def test_convert_mass_stone_to_lb():
    assert convert_mass(1, "st", "lb") == pytest.approx(14.0)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0)


def test_fahrenheit_to_celsius_roundtrip():
    original = 98.6
    celsius = fahrenheit_to_celsius(original)
    assert celsius_to_fahrenheit(celsius) == pytest.approx(original)


def test_celsius_to_kelvin_and_back():
    assert celsius_to_kelvin(0) == pytest.approx(273.15)
    assert kelvin_to_celsius(273.15) == pytest.approx(0.0)

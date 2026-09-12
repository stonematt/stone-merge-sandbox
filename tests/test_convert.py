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


def test_convert_length_gigametre_to_miles():
    assert convert_length(1, "Gm", "mi") == pytest.approx(621371.1922373339)


def test_convert_length_perch_to_miles():
    assert convert_length(1, "prc", "mi") == pytest.approx(0.003125)


def test_convert_length_pace_to_miles():
    assert convert_length(1, "pce", "mi") == pytest.approx(0.0004734848484848485)


def test_convert_length_link_to_miles():
    assert convert_length(1, "lnk", "mi") == pytest.approx(0.000125)


def test_convert_length_thou_to_miles():
    assert convert_length(1, "th", "mi") == pytest.approx(1.5782828282828283e-08)


def test_convert_length_nautical_mile_to_miles():
    assert convert_length(1, "nmi", "mi") == pytest.approx(1.1507794480235425)


def test_convert_length_barleycorn_to_feet():
    assert convert_length(1, "bc", "ft") == pytest.approx(0.02777778871391076)


def test_convert_length_astronomical_unit_to_feet():
    assert convert_length(1, "au", "ft") == pytest.approx(490806662401.57477)


def test_convert_length_terametre_to_feet():
    assert convert_length(1, "Tm", "ft") == pytest.approx(3280839895013.123)


def test_convert_length_decametre_to_metres_and_back():
    assert convert_length(1, "dam", "m") == pytest.approx(10.0)
    assert convert_length(10.0, "m", "dam") == pytest.approx(1.0)


def test_convert_length_pole_to_metres_and_back():
    for magnitude in (0.001, 1.0, 1000.0):
        metres = convert_length(magnitude, "pol", "m")
        assert metres == pytest.approx(magnitude * 5.0292)
        assert convert_length(metres, "m", "pol") == pytest.approx(magnitude)


def test_convert_length_sazhen_to_metres_and_back():
    for magnitude in (0.001, 1.0, 1000.0):
        metres = convert_length(magnitude, "szh", "m")
        assert metres == pytest.approx(magnitude * 2.1336)
        assert convert_length(metres, "m", "szh") == pytest.approx(magnitude)


def test_convert_length_verst_to_metres_and_back():
    for magnitude in (0.001, 1.0, 1000.0):
        metres = convert_length(magnitude, "vst", "m")
        assert metres == pytest.approx(magnitude * 1066.8)
        assert convert_length(metres, "m", "vst") == pytest.approx(magnitude)


def test_convert_length_furlong_to_metres_and_back():
    for magnitude in (0.001, 1.0, 1000.0):
        metres = convert_length(magnitude, "fur", "m")
        assert metres == pytest.approx(magnitude * 201.168)
        assert convert_length(metres, "m", "fur") == pytest.approx(magnitude)


def test_convert_length_palm_to_metres_and_back():
    for magnitude in (0.001, 1.0, 1000.0):
        metres = convert_length(magnitude, "plm", "m")
        assert metres == pytest.approx(magnitude * 0.0762)
        assert convert_length(metres, "m", "plm") == pytest.approx(magnitude)


def test_convert_length_hand_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "hh", "mi")
        assert miles == pytest.approx(magnitude * 0.1016 / 1609.344)


def test_convert_length_cable_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "cbl", "mi")
        assert miles == pytest.approx(magnitude * 185.2 / 1609.344)


def test_convert_length_hank_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "hnk", "mi")
        assert miles == pytest.approx(magnitude * 768.1 / 1609.344)


def test_convert_length_nonpareil_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "non", "mi")
        assert miles == pytest.approx(magnitude * 0.00164 / 1609.344)


def test_convert_length_zeptometre_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "zm", "mi")
        assert miles == pytest.approx(magnitude * 1e-21 / 1609.344)


def test_convert_length_em_typographic_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "emu", "mi")
        assert miles == pytest.approx(magnitude * 0.0042333 / 1609.344)


def test_convert_length_em_typographic_full_name():
    for name in ("em (typographic)", "EM (Typographic)", "  em (typographic)  "):
        assert convert_length(1, name, "m") == pytest.approx(0.0042333)


def test_convert_length_vitasti_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "vit", "mi")
        assert miles == pytest.approx(magnitude * 0.2286 / 1609.344)


def test_convert_length_vitasti_full_name():
    for name in ("vitasti (Indian span)", "VITASTI (INDIAN SPAN)", "  vitasti (indian span)  "):
        assert convert_length(1, name, "m") == pytest.approx(0.2286)


def test_convert_length_pous_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "pous", "mi")
        assert miles == pytest.approx(magnitude * 0.308 / 1609.344)


def test_convert_length_pous_full_name():
    for name in ("pous (Greek foot)", "POUS (GREEK FOOT)", "  pous (greek foot)  "):
        assert convert_length(1, name, "m") == pytest.approx(0.308)


def test_convert_length_cicero_to_miles():
    for magnitude in (0.001, 1.0, 1000.0):
        miles = convert_length(magnitude, "cic", "mi")
        assert miles == pytest.approx(magnitude * 0.004513 / 1609.344)


def test_convert_length_cicero_full_name():
    for name in ("cicero", "CICERO", "  Cicero  "):
        assert convert_length(1, name, "m") == pytest.approx(0.004513)


def test_convert_length_hasta_to_inches():
    for magnitude in (0.001, 1.0, 1000.0):
        inches = convert_length(magnitude, "hst", "in")
        assert inches == pytest.approx(magnitude * 0.457 / 0.0254)


def test_convert_length_hasta_full_name():
    for name in ("hasta (Indian cubit)", "HASTA (INDIAN CUBIT)", "  hasta (indian cubit)  "):
        assert convert_length(1, name, "m") == pytest.approx(0.457)


def test_convert_length_actus_to_inches():
    for magnitude in (0.001, 1.0, 1000.0):
        inches = convert_length(magnitude, "act", "in")
        assert inches == pytest.approx(magnitude * 35.5 / 0.0254)


def test_convert_length_actus_full_name():
    for name in ("actus (Roman)", "ACTUS (ROMAN)", "  actus (roman)  "):
        assert convert_length(1, name, "m") == pytest.approx(35.5)


def test_convert_length_pulgada_to_inches():
    for magnitude in (0.001, 1.0, 1000.0):
        inches = convert_length(magnitude, "pul", "in")
        assert inches == pytest.approx(magnitude * 0.0232 / 0.0254)


def test_convert_length_pulgada_full_name():
    for name in ("pulgada (Spanish inch)", "PULGADA (SPANISH INCH)", "  pulgada (spanish inch)  "):
        assert convert_length(1, name, "m") == pytest.approx(0.0232)


def test_convert_length_fut_to_inches():
    for magnitude in (0.001, 1.0, 1000.0):
        inches = convert_length(magnitude, "fut", "in")
        assert inches == pytest.approx(magnitude * 0.3048 / 0.0254)


def test_convert_length_fut_full_name():
    for name in ("fut (Russian foot)", "FUT (RUSSIAN FOOT)", "  fut (russian foot)  "):
        assert convert_length(1, name, "m") == pytest.approx(0.3048)


def test_convert_length_voet_to_meters():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "voe", "m") == pytest.approx(magnitude * 0.2831)


def test_convert_length_meters_to_voet():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "m", "voe") == pytest.approx(magnitude / 0.2831)


def test_convert_length_light_minutes_to_meters():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "lmin", "m") == pytest.approx(
            magnitude * 17987547480.0
        )


def test_convert_length_meters_to_light_minutes():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "m", "lmin") == pytest.approx(
            magnitude / 17987547480.0
        )


def test_convert_length_dutch_ells_to_meters():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "eld", "m") == pytest.approx(magnitude * 0.687)


def test_convert_length_meters_to_dutch_ells():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "m", "eld") == pytest.approx(magnitude / 0.687)


def test_convert_length_dutch_ell_distinct_from_english_ell():
    assert convert_length(1, "eld", "m") == pytest.approx(0.687)
    assert convert_length(1, "ell", "m") == pytest.approx(1.143)


def test_convert_length_zettametres_to_meters():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "Zm", "m") == pytest.approx(magnitude * 1e21)


def test_convert_length_meters_to_zettametres():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "m", "Zm") == pytest.approx(magnitude / 1e21)


def test_convert_length_zettametre_distinct_from_zeptometre():
    assert convert_length(1, "Zm", "m") == pytest.approx(1e21)
    assert convert_length(1, "zm", "m") == pytest.approx(1e-21)


def test_convert_length_agates_to_meters():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "agt", "m") == pytest.approx(magnitude * 0.00181)


def test_convert_length_meters_to_agates():
    for magnitude in (0.001, 1.0, 1000.0):
        assert convert_length(magnitude, "m", "agt") == pytest.approx(magnitude / 0.00181)


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


def test_convert_mass_picul_to_kg_and_back():
    assert convert_mass(1, "pcl", "kg") == pytest.approx(60.478982)
    assert convert_mass(60.478982, "kg", "pcl") == pytest.approx(1.0)


def test_convert_mass_short_hundredweight_to_kg_and_back():
    assert convert_mass(1, "scwt", "kg") == pytest.approx(45.359237)
    assert convert_mass(45.359237, "kg", "scwt") == pytest.approx(1.0)


def test_convert_mass_tonne_to_kg_and_back():
    assert convert_mass(1, "t", "kg") == pytest.approx(1000.0)
    assert convert_mass(1000.0, "kg", "t") == pytest.approx(1.0)


def test_convert_mass_assay_ton_to_kg_and_back():
    assert convert_mass(1, "at", "kg") == pytest.approx(0.02916666)
    assert convert_mass(0.02916666, "kg", "at") == pytest.approx(1.0)


def test_convert_mass_tael_to_kg_and_back():
    assert convert_mass(1, "tl", "kg") == pytest.approx(0.037799364)
    assert convert_mass(0.037799364, "kg", "tl") == pytest.approx(1.0)


def test_convert_mass_candareen_to_kg_and_back():
    assert convert_mass(1, "cdr", "kg") == pytest.approx(0.00037799364)
    assert convert_mass(0.00037799364, "kg", "cdr") == pytest.approx(1.0)


def test_convert_mass_gamma_to_kg_and_back():
    assert convert_mass(1, "gam", "kg") == pytest.approx(1e-09)
    assert convert_mass(1e-09, "kg", "gam") == pytest.approx(1.0)


def test_convert_mass_grain_to_kg_and_back():
    assert convert_mass(1, "gr", "kg") == pytest.approx(6.479891e-05)
    assert convert_mass(6.479891e-05, "kg", "gr") == pytest.approx(1.0)


def test_convert_mass_short_ton_to_kg_and_back():
    assert convert_mass(1, "tn", "kg") == pytest.approx(907.18474)
    assert convert_mass(907.18474, "kg", "tn") == pytest.approx(1.0)


def test_convert_mass_jewellers_point_to_kg_and_back():
    assert convert_mass(1, "jpt", "kg") == pytest.approx(2e-06)
    assert convert_mass(2e-06, "kg", "jpt") == pytest.approx(1.0)


def test_convert_mass_centigram_to_kg_and_back():
    assert convert_mass(1, "cg", "kg") == pytest.approx(1e-05)
    assert convert_mass(1e-05, "kg", "cg") == pytest.approx(1.0)


def test_convert_mass_tola_to_kg_and_back():
    assert convert_mass(1, "tla", "kg") == pytest.approx(0.0116638038)
    assert convert_mass(0.0116638038, "kg", "tla") == pytest.approx(1.0)


def test_convert_mass_mark_to_kg_and_back():
    assert convert_mass(1, "mrk", "kg") == pytest.approx(0.2488278144)
    assert convert_mass(0.2488278144, "kg", "mrk") == pytest.approx(1.0)


def test_convert_mass_maund_to_kg_and_back():
    assert convert_mass(1, "mnd", "kg") == pytest.approx(37.3242)
    assert convert_mass(37.3242, "kg", "mnd") == pytest.approx(1.0)


def test_convert_mass_femtogram_to_kg_and_back():
    assert convert_mass(1, "fg", "kg") == pytest.approx(1e-18)
    assert convert_mass(1e-18, "kg", "fg") == pytest.approx(1.0)


def test_convert_mass_clove_to_kg_and_back():
    assert convert_mass(1, "clv", "kg") == pytest.approx(3.62874)
    assert convert_mass(3.62874, "kg", "clv") == pytest.approx(1.0)


def test_convert_mass_fun_to_kg_and_back():
    assert convert_mass(1, "fun", "kg") == pytest.approx(0.000375)
    assert convert_mass(0.000375, "kg", "fun") == pytest.approx(1.0)


def test_convert_mass_drachm_ottoman_to_kg_and_back():
    assert convert_mass(1, "drc", "kg") == pytest.approx(0.003207)
    assert convert_mass(0.003207, "kg", "drc") == pytest.approx(1.0)


def test_convert_mass_libra_castilian_to_kg_and_back():
    assert convert_mass(1, "lib", "kg") == pytest.approx(0.46)
    assert convert_mass(0.46, "kg", "lib") == pytest.approx(1.0)


def test_convert_mass_kan_japanese_to_kg_and_back():
    assert convert_mass(1, "kan", "kg") == pytest.approx(3.75)
    assert convert_mass(3.75, "kg", "kan") == pytest.approx(1.0)


def test_convert_mass_dalton_to_kg_and_back():
    assert convert_mass(1, "Da", "kg") == pytest.approx(1.6605390666e-27)
    assert convert_mass(1.6605390666e-27, "kg", "Da") == pytest.approx(1.0)


def test_convert_mass_long_hundredweight_to_kg_and_back():
    assert convert_mass(1, "cwt", "kg") == pytest.approx(50.80234544)
    assert convert_mass(50.80234544, "kg", "cwt") == pytest.approx(1.0)


def test_convert_mass_sack_wool_to_kg_and_back():
    assert convert_mass(1, "sck", "kg") == pytest.approx(165.10762)
    assert convert_mass(165.10762, "kg", "sck") == pytest.approx(1.0)


def test_convert_mass_troy_pound_to_kg_and_back():
    assert convert_mass(1, "lbt", "kg") == pytest.approx(0.3732417216)
    assert convert_mass(0.3732417216, "kg", "lbt") == pytest.approx(1.0)


def test_convert_mass_libra_portuguese_to_kg_and_back():
    assert convert_mass(1, "libp", "kg") == pytest.approx(0.459)
    assert convert_mass(0.459, "kg", "libp") == pytest.approx(1.0)


def test_convert_mass_megagram_to_kg_and_back():
    assert convert_mass(1, "Mg", "kg") == pytest.approx(1000.0)
    assert convert_mass(1000.0, "kg", "Mg") == pytest.approx(1.0)


def test_convert_mass_megagram_is_not_milligram():
    assert convert_mass(1, "Mg", "mg") == pytest.approx(1e09)


def test_convert_mass_petagram_to_g_is_exact():
    # 1e15 is under 2**53, so the conversion lands on the integer exactly.
    assert convert_mass(1, "Pg", "g") == 1e15
    assert convert_mass(1e15, "g", "Pg") == 1.0


def test_convert_mass_arroba_spanish_to_g_exact():
    assert convert_mass(1, "arb", "g") == 11502.9


def test_convert_mass_arroba_spanish_to_kg_and_back():
    assert convert_mass(1, "arb", "kg") == pytest.approx(11.5029)
    assert convert_mass(11.5029, "kg", "arb") == pytest.approx(1.0)


def test_convert_mass_candy_indian_to_g_exact():
    assert convert_mass(1, "cdy", "g") == 226500.0


def test_convert_mass_candy_indian_to_kg_and_back():
    assert convert_mass(1, "cdy", "kg") == pytest.approx(226.5)
    assert convert_mass(226.5, "kg", "cdy") == pytest.approx(1.0)


def test_convert_mass_quintal_portuguese_to_g_exact():
    assert convert_mass(1, "qpt", "g") == 58750.0


def test_convert_mass_seer_to_g_exact():
    assert convert_mass(1, "ser", "g") == 933.10


def test_convert_mass_stone_to_lb():
    assert convert_mass(1, "st", "lb") == pytest.approx(14.0)


def test_convert_mass_troy_pound_to_troy_ounce():
    assert convert_mass(1, "lbt", "ozt") == pytest.approx(12.0)


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

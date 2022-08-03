#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from functools import reduce
from random    import choice

from   hypothesis            import given
import hypothesis.strategies as st
import pytest

from cbdevtools import *


# ----------- #
# -- TOOLS -- #
# ----------- #

LAMBDA_DIGITS_2_NAT = lambda digits: reduce(
    lambda x, y: x*10 + y,
    digits
)

LAMBDA_BDIGITS_2_NAT = lambda bdigits, base: reduce(
    lambda x, y: x*base + y,
    bdigits
)


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.natural.nat2base import Nat2Base
# from unit.core       import build_removable


# -------------------------- #
# -- DIGITS / NUMERALS OF -- #
# -------------------------- #

@given(st.integers(max_value = -1))
def test_nat2base_numeralsof_negative_NOT_OK(bad):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*too small.*"
    ):
        Nat2Base().numeralsof(bad)


@given(st.integers(max_value = -1))
def test_nat2base_digitsof_negative_NOT_OK(bad):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*too small.*"
    ):
        Nat2Base().digitsof(bad)


@given(st.integers(min_value = 0))
def test_nat2base_numeralsof(nb):
    nb_numerals = Nat2Base().numeralsof(nb)

    assert str(nb) == ''.join(nb_numerals)


@given(st.integers(min_value = 0))
def test_nat2base_digitsof(nb):
    nb_digits = Nat2Base().digitsof(nb)

    assert nb == LAMBDA_DIGITS_2_NAT(nb_digits)


# ---------------------------- #
# -- FROM DIGITS / NUMERALS -- #
# ---------------------------- #

@given(st.integers(min_value = 0))
def test_nat2base_fromdigits_fromnumerals(nb):
    for chgethis, kind in [
        (int, "digits"),
        (str, "numerals")
    ]:
        method_fromXXX = Nat2Base().__getattribute__(f"from{kind}")
        datas          = [chgethis(c) for c in str(nb)]
        nbfound        = method_fromXXX(datas)

        assert nbfound == nb, (
                f"{nb      = }"
                 "\n\n"
                 f"fromXXX = from{kind}"
               )


# ---------------------------------------- #
# -- DECIMAL --> BASE DIGITS / NUMERALS -- #
# ---------------------------------------- #

@given(st.integers(max_value = 1))
def test_nat2base_nat2bdigits_negative_NOT_OK(bad_base):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*base.*too small.*"
    ):
        Nat2Base().nat2bdigits(
            nb   = 20220722, # This looks like a date...
            base = bad_base,
        )


@given(st.integers(min_value = 0),
       st.integers(min_value = 2))
def test_nat2base_nat2bdigits(nb, base):
    assert nb == LAMBDA_BDIGITS_2_NAT(
                Nat2Base().nat2bdigits(
                    nb   = nb,
                    base = base
                ),
                base
           ), (
                f"{nb   = }"
                 "\n\n"
                f"{base = }"
           )


@given(st.integers(min_value = 0),
       st.integers(min_value = 2, max_value=36))
def test_nat2base_nat2bnumerals_via_python_builtins(nb, base):
    assert nb == int(
           ''.join(
                Nat2Base().nat2bnumerals(
                    nb   = nb,
                    base = base
                )
           ),
           base = base
           ), (
                f"{nb   = }"
                 "\n\n"
                f"{base = }"
           )


# ------------------------------ #
# -- DECIMAL --> BASE NUMBERS -- #
# ------------------------------ #

@given(st.integers(min_value = 0),
       st.integers(min_value = 2))
def test_nat2base_nat2bnb(nb, base):
    assert Nat2Base().nat2bnb(
                nb   = nb,
                base = base
           ) == ''.join(
                Nat2Base().nat2bnumerals(
                    nb   = nb,
                    base = base
                )
           ), (
                f"{nb   = }"
                 "\n\n"
                f"{base = }"
           )


# -------------------------------------------------- #
# -- DIGITS / NUMERALS --> BASE DIGITS / NUMERALS -- #
# -------------------------------------------------- #


# --------------------------------------- #
# -- DIGITS / NUMERALS --> BASE NUMBER -- #
# --------------------------------------- #



# --------------------- #
# -- ... --> BASE 10 -- #
# --------------------- #


@given(st.integers(min_value = 0))
def test_nat2base_base_10_nat2bdigits_nat2bnumerals(nb):
    for kind in ["digits", "numerals"]:
        XXXof    = f"{kind}of"
        nat2bXXX = f"nat2b{kind}"

        assert Nat2Base().__getattribute__(XXXof)(nb) \
               == \
               Nat2Base().__getattribute__(nat2bXXX)(
                    nb   = nb,
                    base = 10
               ), (
                f"{nb       = }"
                 "\n\n"
                f"{XXXof    = }"
                 "\n\n"
                f"{nat2bXXX = }"
               )

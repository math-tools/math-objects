#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from functools import reduce

from   hypothesis            import given
import hypothesis.strategies as st
import pytest

from cbdevtools import *


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


# ---------------------- #
# -- DECIMAL NUMERALS -- #
# ---------------------- #

@given(st.integers(max_value = -1))
def test_nat2base_numerals_negative_NOT_OK(bad):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*too small.*"
    ):
        Nat2Base().numeralsof(bad)


@given(st.integers(min_value = 0))
def test_nat2base_numerals(nb):
    nb_numerals = Nat2Base().numeralsof(nb)

    assert str(nb) == ''.join(nb_numerals)


# -------------------- #
# -- DECIMAL DIGITS -- #
# -------------------- #

@given(st.integers(max_value = -1))
def test_nat2base_digits_negative_NOT_OK(bad):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*too small.*"
    ):
        Nat2Base().digitsof(bad)


@given(st.integers(min_value = 0))
def test_nat2base_digits(nb):
    nb_digits = Nat2Base().digitsof(nb)

    assert nb == reduce(
        lambda x, y: 10*x + y,
        nb_digits,
    )


# ---------------------- #
# -- DECIMAL --> BASE -- #
# ---------------------- #

@given(st.integers(max_value = 1))
def test_nat2base_digits_negative_NOT_OK(bad_base):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*base.*too small.*"
    ):
        Nat2Base().nat2bdigits(
            nb   = 20220722, # This looks like a date...
            base = bad_base,
        )

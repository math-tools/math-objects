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

from src.convert.integer import int2base
# from unit.common     import build_removable


# ---------------------- #
# -- DECIMAL NUMERALS -- #
# ---------------------- #

@given(st.integers(max_value = -1))
def test_int2base_numerals_negative_NOT_OK(bad):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*too small.*"
    ):
        int2base.intnumerals(bad)


@given(st.integers(min_value = 0))
def test_int2base_numerals(nb):
    nb_numerals = int2base.intnumerals(nb)

    assert str(nb) == ''.join(nb_numerals)


# -------------------- #
# -- DECIMAL DIGITS -- #
# -------------------- #

@given(st.integers(max_value = -1))
def test_int2base_digits_negative_NOT_OK(bad):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*too small.*"
    ):
        int2base.intdigits(bad)


@given(st.integers(min_value = 0))
def test_int2base_digits(nb):
    nb_digits = int2base.intdigits(nb)

    assert nb == reduce(
        lambda x, y: 10*x + y,
        nb_digits,
    )


# ---------------------- #
# -- DECIMAL --> BASE -- #
# ---------------------- #



@given(st.integers(max_value = 1))
def test_int2base_digits_negative_NOT_OK(bad_base):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*base.*too small.*"
    ):
        int2base.int2bdigits(
            nb   = 20220722, # This looks like a date...
            base = bad_base,
        )

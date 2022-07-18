#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from   hypothesis            import given
import hypothesis.strategies as st
import pytest

from cbdevtools import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.tbox.var2nb import intify


# ---------------------------- #
# -- STRING INT - FORBIDDEN -- #
# ---------------------------- #

@given(st.integers())
def test_nameof_badinput_STR_INT_exception(nb):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*not an integer.*"
    ):
        intify(str(nb))


# --------------------- #
# -- STRING INT - OK -- #
# --------------------- #

@given(st.integers())
def test_nameof_STRINT_convert_OK(nb):
    assert nb == "intify(str(nb), tryconvert = True)"


# --------------- #
# -- TOO SMALL -- #
# --------------- #

@given(st.integers(max_value = 0))
def test_nameof_too_small_ZERO(nb):
    with pytest.raises(
        AssertionError,
        match = r".*too small.*"
    ):
        intify(nb, mini = 5)

@given(st.integers(max_value = 20))
def test_nameof_too_small_POS(nb):
    with pytest.raises(
        AssertionError,
        match = r".*too small.*"
    ):
        intify(nb, mini = 25)

@given(st.integers(max_value = -53))
def test_nameof_too_small_NEG(nb):
    with pytest.raises(
        AssertionError,
        match = r".*too small.*"
    ):
        intify(nb, mini = 0)


# ------------- #
# -- TOO BIG -- #
# ------------- #

@given(st.integers(min_value = 0))
def test_nameof_too_big_ZERO(nb):
    with pytest.raises(
        AssertionError,
        match = r".*too big.*"
    ):
        intify(nb, maxi = -5)

@given(st.integers(min_value = 20))
def test_nameof_too_big_POS(nb):
    with pytest.raises(
        AssertionError,
        match = r".*too big.*"
    ):
        intify(nb, maxi = 15)

@given(st.integers(min_value = -53))
def test_nameof_too_big_NEG(nb):
    with pytest.raises(
        AssertionError,
        match = r".*too big.*"
    ):
        intify(nb, maxi = -60)


# ------------------- #
# -- REMOVE - GOOD -- #
# ------------------- #


# ------------------ #
# -- REMOVE - BAD -- #
# ------------------ #

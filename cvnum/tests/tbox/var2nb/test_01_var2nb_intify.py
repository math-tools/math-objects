#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import choice, randint

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

@given(st.text())
def test_nameof_badinput_name(text):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*XXXXXX.*"
    ):
        intify(text, name = "XXXXXX")


# ---------------------------- #
# -- STRING INT - FORBIDDEN -- #
# ---------------------------- #

@given(st.integers())
def test_nameof_badinput_str_int_NOT_OK(nb):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*not an integer.*"
    ):
        intify(str(nb))


# --------------------- #
# -- STRING INT - OK -- #
# --------------------- #

@given(st.integers())
def test_nameof_str_int_convert_OK(nb):
    assert nb == intify(str(nb), tryconvert = True)


# --------------- #
# -- TOO SMALL -- #
# --------------- #

# TODO UGGLY: too much copy and paste!
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

# TODO UGGLY: too much copy and paste!
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

# TODO Create a new strategy!
def build_removable(nb, toremove, atleastone = ""):
    nb          = str(nb)
    nb_polluted = ''

    for c in nb:
        if (
            nb_polluted
            and
            not nb_polluted[-1] in toremove
            and
            randint(0, 10) <= 7
        ):
            nb_polluted += choice(toremove)

        nb_polluted += c

    if(
        atleastone
        and
        not atleastone in nb_polluted
    ):
        nb_polluted = nb_polluted[:1] + atleastone + nb_polluted[1:]

    return nb_polluted


@given(st.integers(min_value = 1))
def test_nameof_remove_OK(nb):
    toremove = [' ', '_']

    assert intify(
        build_removable(nb, toremove),
        tryconvert = True,
        toremove   = toremove
    )


# ------------------ #
# -- REMOVE - BAD -- #
# ------------------ #

@given(st.integers(min_value = 10))
def test_nameof_remove_NOT_OK(nb):
    toremove = [' ', '_', '.']


    with pytest.raises(
        ValueError,
        match = r".*not an integer.*"
    ):
        intify(
            build_removable(
                nb         = nb,
                toremove   = toremove,
                atleastone = '.'
            ),
            tryconvert = True,
            # toremove   = toremove
        )

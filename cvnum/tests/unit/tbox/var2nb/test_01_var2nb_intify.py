#!/usr/bin/env python3

# from cbdevtools import *

# print(addfindsrc(
#     file    = __file__,
#     project = 'xx',
# ))

# from common import *
# exit()


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

_ = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.tbox.var2nb import intify


_ = addfindsrc(
    file    = __file__,
    project = 'tests',
)

from unit.common import build_removable


# ---------------------- #
# -- NOT A STRING INT -- #
# ---------------------- #

@given(st.text())
def test_intify_badinput_name(text):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*XXXXXX.*"
    ):
        intify(text, name = "XXXXXX")


# ---------------- #
# -- STRING INT -- #
# ---------------- #

@given(st.integers())
def test_intify_badinput_str_int_NOT_OK(nb):
    with pytest.raises(
        (AssertionError, ValueError),
        match = r".*not an integer.*"
    ):
        intify(str(nb))


@given(st.integers())
def test_intify_str_int_convert_OK(nb):
    assert nb == intify(str(nb), tryconvert = True)


# ------------------------- #
# -- TOO SMALL / TOO BIG -- #
# ------------------------- #

@st.composite
def st_badintminmax(draw, elements = st.integers()):
    nb   = draw(st.integers())
    mini = draw(st.integers(min_value = nb + 1))
    maxi = draw(st.integers(max_value = nb - 1))

    return (nb, mini, maxi)


@given(st_badintminmax())
def test_intify_too_small(nbminimaxi):
    nb, mini, _ = nbminimaxi

    with pytest.raises(
        AssertionError,
        match = r".*too small.*"
    ):
        intify(nb, mini = mini)


@given(st_badintminmax())
def test_intify_too_big(nbminimaxi):
    nb, _, maxi = nbminimaxi

    with pytest.raises(
        AssertionError,
        match = r".*too big.*"
    ):
        intify(nb, maxi = maxi)


# ------------ #
# -- REMOVE -- #
# ------------ #

@given(st.integers(min_value = 1))
def test_intify_remove_OK(nb):
    toremove = [' ', '_']

    assert intify(
        build_removable(nb, toremove),
        tryconvert = True,
        toremove   = toremove
    )


@given(st.integers(min_value = 10))
def test_intify_remove_NOT_OK(nb):
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

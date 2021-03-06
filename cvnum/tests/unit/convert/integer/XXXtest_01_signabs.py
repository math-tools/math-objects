#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from   hypothesis            import given
import hypothesis.strategies as st
# import pytest

from cbdevtools     import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)

from src.tbox.signabs import *


# --------------------- #
# -- POST CONDITIONS -- #
# --------------------- #

# Postconditions from the technical documentation.
#
#    let intnb = int(nb) ;
#    int(return[1]) = abs(intnb) ;
#    return[0] = '-' if intnb < 0 ;
#    return[0] in ['', '+'] if intnb >= 0
#
# warning::
#     The parameter ``nb`` is known to be a legal string representation of
#     an integer.

@given(st.integers())
def test_signabs_postcond(nb):
    valreturned = signabs(str(nb))

    assert (
        int(valreturned[1]) == abs(nb)
        and
        (
            (valreturned[0] == '-' and nb < 0)
            or
            (valreturned[0] in ['', '+'] and nb >= 0)
        )
    )


@given(st.integers(min_value = 0))
def test_signabs_postcond_plus_sign(nb):
    nb          = f"+{nb}"
    valreturned = signabs(nb)

    assert valreturned[0] == '+'


@given(st.integers(min_value = 0))
def test_signabs_postcond_no_plus_sign(nb):
    valreturned = signabs(str(nb))

    assert valreturned[0] == ''

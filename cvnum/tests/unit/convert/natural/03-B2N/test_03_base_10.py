#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from   hypothesis            import given
import hypothesis.strategies as st

from cbdevtools import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    'natural',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.natural.base2nat import Base2Nat

from natcore.constants import *


# --------------------- #
# -- BASE 10 --> ... -- #
# --------------------- #

@given(st.integers(min_value = 0))
def test_base2nat_bnb2nat_BASE_10_bnb2nat(nb):
    nb_found = Base2Nat().bnb2nat(
        bnb  = str(nb),
        base = 10
    )

    assert nb_found == nb


@given(st.integers(min_value = 0),
       st.sampled_from(OUTPUTS_NO_NB))
def test_base2nat_bnb2nat_BASE_10_bnb2XXX_vs_XXXof_by_hand(nb, XXX):
    bnb = str(nb)

    chgethis = KINDS_CHGETHIS[XXX]

    XXXof_byhand = [
        chgethis(c) for c in bnb
    ]

    XXXof_found = Base2Nat().__getattribute__(f"bnb2{XXX}")(
        bnb  = bnb,
        base = 10
    )

    assert XXXof_found == XXXof_byhand, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{XXX  = }"
             "\n"
           )

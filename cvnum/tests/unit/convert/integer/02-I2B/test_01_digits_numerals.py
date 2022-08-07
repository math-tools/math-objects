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
    'integer',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.integer import Int2Base
from src.convert.natural import Nat2Base

from intcore.constants import *


# -------------------------- #
# -- DIGITS / NUMERALS OF -- #
# -------------------------- #

@given(st.integers(),
       st.sampled_from(KINDS_ALL))
def test_int2base_XXXof_ignore_sign(nb, kind):
    XXXof = f"{kind}of"

    int_return = Int2Base().__getattribute__(XXXof)(nb)
    nat_return = Nat2Base().__getattribute__(XXXof)(abs(nb))

    assert nat_return == int_return[1:], \
           (
             "\n"
            f"{nb    = }"
             "\n"
            f"{XXXof = }"
             "\n"
           )


@given(st.integers(),
       st.sampled_from(KINDS_ALL))
def test_int2base_XXXof_just_sign(nb, kind):
    XXXof = f"{kind}of"

    int_return = Int2Base().__getattribute__(XXXof)(nb)

    sign_wanted = '-' if nb < 0 else '+'
    sign_wanted = KINDS_SIGNS[kind][sign_wanted]

    assert sign_wanted == int_return[0], \
           (
             "\n"
            f"{nb    = }"
             "\n"
            f"{XXXof = }"
             "\n"
           )


# ---------------------------- #
# -- FROM DIGITS / NUMERALS -- #
# ---------------------------- #

@given(st.integers(),
       st.sampled_from(KINDS_ALL))
def test_int2base_fromXXX(nb, kind):
    chgethis = KINDS_CHGETHIS[kind]

    fromXXX = f"from{kind}"

    sign_wanted = '-' if nb < 0 else '+'
    sign_wanted = KINDS_SIGNS[kind][sign_wanted]

    datas   = [sign_wanted] + [chgethis(c) for c in str(abs(nb))]

    nbfound = Int2Base().__getattribute__(fromXXX)(datas)

    assert nbfound == nb, \
           (
             "\n"
            f"{nb      = }"
             "\n"
             f"{fromXXX = }"
             "\n"
           )

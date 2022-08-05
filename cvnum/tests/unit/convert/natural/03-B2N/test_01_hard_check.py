#!/usr/bin/env python3

# --------------------- #
# -- SEVERAL IMPORTS -- #
# --------------------- #

from random import choice

from   hypothesis            import given
import hypothesis.strategies as st
# import pytest

from cbdevtools import *


# ------------------------------------------ #
# -- MODULE TESTED IMPORTED FROM SOURCES! -- #
# ------------------------------------------ #

for upfolder in [
    'cvnum',
    # 'natural',
    # 'tests',
]:
    _ = addfindsrc(
        file    = __file__,
        project = upfolder,
    )

from src.convert.natural.base2nat import Base2Nat
from src.convert.natural.nat2base import Nat2Base
# from unit.core       import build_removable

# from natcore.constants import *


# ------------------------- #
# -- VIA PYTHON BUILTINS -- #
# ------------------------- #

@given(st.integers(min_value = 36 + 1),
       st.integers(min_value = 2, max_value = 36))
def test_base2nat_nat2bnb_vs_python_builtins(nb, base):
    bnb =  Nat2Base().nat2bnb(
        nb   = nb,
        base = base
    )

    python_bnb2nat = int(bnb, base)

    bnb2nat_found = Base2Nat().bnb2nat(
        bnb  = bnb,
        base = base
    )

    assert bnb2nat_found == python_bnb2nat, \
           (
             "\n"
            f"{nb   = }"
             "\n"
            f"{base = }"
             "\n"
           )

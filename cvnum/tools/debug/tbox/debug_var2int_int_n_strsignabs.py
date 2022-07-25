#!/usr/bin/env python3

from cbdevtools import *


# ------------------------------------ #
# -- MODULES IMPORTED FROM SOURCES! -- #
# ------------------------------------ #

MODULE_DIR = addfindsrc(
    file    = __file__,
    project = 'cvnum',
)


# -------------- #
# -- TO DEBUG -- #
# -------------- #

from src.tbox.var2int import *

int_n_strsignabs = Var2Int(
    tryconvert = True,
    toremove   = [' ']
).int_n_strsignabs


# -------------- #
# -- LET'S GO -- #
# -------------- #

for n in [
    123,
    -123,
    "+ 60   000",
]:
    print()
    print('--- int_n_strsignabs ---')
    print(f"{              n = }")
    print(f"{        type(n) = }")
    print(f"{         str(n) = }")
    print(f"{int_n_strsignabs(n) = }")

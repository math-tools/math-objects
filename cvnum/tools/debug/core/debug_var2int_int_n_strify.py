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

from src.convert.core.var2int import *

int_n_strify = Var2Int(
    tryconvert = True,
    toremove   = [' ', '.']
).int_n_strify


# -------------- #
# -- LET'S GO -- #
# -------------- #

class fakeINT:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "  ".join(x for x in str(self.n))


for n in [
    123,
    -123,
    "60   000",
    "111_222_333 444_555_666",
    "111.222.333 444.555.666",
    fakeINT(54321),
]:
    print()
    print('--- int_n_strify ---')
    print(f"{              n = }")
    print(f"{        type(n) = }")
    print(f"{         str(n) = }")
    print(f"{int_n_strify(n) = }")

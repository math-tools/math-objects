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

from src.convert.natural import *

myn2b = Nat2Base()


# -------------- #
# -- LET'S GO -- #
# -------------- #

for n in [
    123456,
]:
    print()
    print('--- intdigits & intnumerals ---')
    print(f"{                   n = }")
    print(f'{  myn2b.digitsof(n) = }')
    print(f'{myn2b.numeralsof(n) = }')

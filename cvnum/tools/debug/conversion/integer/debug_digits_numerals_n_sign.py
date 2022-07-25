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

from src.convert.integer import *

myi2b = Int2Base(tryconvert = True)


# -------------- #
# -- LET'S GO -- #
# -------------- #

for n in [
    123456,
    "+123456",
    "-123456",
]:
    print()
    print('--- intdigits & intnumerals ---')
    print(f"{                   n = }")
    print(f'{  myi2b.intdigits(n) = }')
    print(f'{myi2b.intnumerals(n) = }')

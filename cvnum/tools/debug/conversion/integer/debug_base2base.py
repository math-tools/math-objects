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
# -- LET'S GO -- #
# -------------- #

from src.convert.integer import *

base2base = Base2Base()

for (x, f, b_1, b_2) in [
# SINGLE FUNC.
    (12**3 + 11*12 + 10, FORMAT_DIGITS, 10, 12),
    (12**3 + 11*12 + 10, FORMAT_NUMERALS, 10, 12),
    (['1', '0', 'B', 'A'], FORMAT_INT, 12, 10),
    ([1, 0, 11, 10], FORMAT_INT, 12, 10),
# COMPO. FUNC.
    ([1, 0, 11, 10], FORMAT_NUMERALS, 12, 10),
    ([1, 0, 11, 10], FORMAT_DIGITS, 12, 10),
    ([1, 0, 11, 10], FORMAT_INT, 12, 10),
# MISC.
    ([1, 0, 11, 10], FORMAT_NUMERALS, 12, 12),
]:
    base2base.changebases((b_1, b_2))

    y = base2base.convert(x, f)

    print('---')
    print(f'bases = ({b_1}, {b_2}))')
    print(f'convert({x}, {f}) = {y}')

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

base2base = Base2Base()


# -------------- #
# -- LET'S GO -- #
# -------------- #

print(
    base2base.bdigits2bnb(
        bdigits  = [1,0,4,8],
        base_in  = 10,
        base_out = 2
    )
)

print(
    base2base.bdigits2bdigits(
        bdigits  = [1,0,4,8],
        base_in  = 10,
        base_out = 2
    )
)

print(
    base2base.bdigits2bnumerals(
        bdigits  = [1,0,4,8],
        base_in  = 10,
        base_out = 2
    )
)

print(
    base2base.bnb2bnb(
        bnb      = "10000011000",
        base_in  = 2,
        base_out = 10,
    )
)

print(
    base2base.bnb2bdigits(
        bnb = base2base.bdigits2bnb(
            bdigits  = [1,2,3,4,5,6,7,8,9,0],
            base_in  = 10,
            base_out = 2
        ),
        base_in  = 2,
        base_out = 10
    )
)

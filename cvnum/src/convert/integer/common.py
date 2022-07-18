#!/usr/bin/env python3

###
# The module contains common tools only for conversions of integers.
###


from typing import *

from ...tbox.str2nb import intify


###
# prototype::
#     number     : any object that is printable as an integer
#                @ str(number) in str(ZZ)
#     tryconvert : to allow, or not, the use of the printed version of
#                  ``number`` such as to try to convert it to an integer
#
#     :return: a ¨python integer respecting greater than `1``
#            @ return in 2..+inf
###
def basify(
    number    : Any,
    tryconvert: bool  = False
) -> int:
    return intify(
        number     = number,
        mini       = 2,
        name       = "base",
        tryconvert = tryconvert
    )

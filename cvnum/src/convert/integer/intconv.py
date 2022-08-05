#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from lib2to3.pgen2.token import PLUS
from typing import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

MINUS_STR_SIGN = "-"
MINUS_INT_SIGN = -1

PLUS_STR_SIGN = ""
PLUS_INT_SIGN = 1

STR_SIGNS = [
    MINUS_STR_SIGN,
    PLUS_STR_SIGN,
]


# ----------------------------------------- #
# -- ??? -- #
# ----------------------------------------- #

###
# ???? This class is to be herited by the classes playing with base conversions of integers.
###
class IntConv:
###
# prototype::
#     errname : the name used in case of error message
###
    def __init__(
        self,
        errname : str = "number",
    ):
        self.errname = errname


###
# prototype::
#     ???
###
    def sign_n_abs_of(self, nb: int) -> Tuple[int]:
        if nb < 0:
            sign = MINUS_INT_SIGN
            nb   = -nb

        else:
            sign = PLUS_INT_SIGN

        return sign, nb


###
# prototype::
#     ???
###
    def strsign(self, sign: int) -> str:
        if sign == MINUS_INT_SIGN:
            return MINUS_STR_SIGN

        return PLUS_STR_SIGN


###
# prototype::
#     ???
###
    def intsign(self, strsign: str) -> int:
        if strsign == MINUS_STR_SIGN:
            return MINUS_INT_SIGN

        return PLUS_INT_SIGN

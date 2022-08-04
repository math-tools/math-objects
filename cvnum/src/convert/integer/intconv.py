#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *


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
    def sign_n_abs_ofnb(self, nb: int) -> List[int]:
        if nb < 0:
            sign = - 1
            nb   = - nb

        elif nb == 0:
            sign = 0

        else:
            sign = 1

        return sign, nb

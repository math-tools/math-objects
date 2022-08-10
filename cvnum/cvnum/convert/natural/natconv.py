#!/usr/bin/env python3

###
# This module proposes common tools for the classes playing with base
# conversions of naturals.
###


from typing import *


# ---------------- #
# -- BASE CLASS -- #
# ---------------- #

###
# This class is to be herited by the classes playing with base conversions
# of naturals.
###
class NatConv:
###
# prototype::
#     errname : the name used in case of error message
###
    def __init__(
        self,
        errname : str = "number",
    ) -> None:
        self.errname = errname

        self.max_singledigit = 36


###
# prototype::
#     nb      : a ¨python varoiable to be checked
#     mini    : a float number which is a minorant
#             @ mini in RR or mini in {-inf, +inf}
#     maxi    : a float number which is a majorant
#             @ maxi in RR or maxi in {-inf, +inf} ;
#               mini <= maxi
#     errname : :see: self.__init__
#
#     :canfail: if the postcondition is not respected, this method raises
#               an exception.
#
#     :postcond: nb in ZZ ;
#                mini <= nb <= maxi
###
    def checknatural(
        self,
        nb     : Any,
        mini   : float = 0,
        maxi   : float = float('inf'),
        errname: str   = '',
    ) -> None:
        if not errname:
            errname = self.errname

        assert isinstance(nb, int), \
               f"The {errname} ``{nb}`` is not an integer."

        assert mini <= maxi, \
               f"invalid mini and maxi: ``{mini = } > {maxi = }``."

        assert nb >= mini, \
               f"The {errname} ``{nb}`` is too small ({mini = })."

        assert nb <= maxi, \
               f"The {errname} ``{nb}`` is too big ({maxi = })."

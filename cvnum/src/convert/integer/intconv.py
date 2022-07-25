#!/usr/bin/env python3

###
# This module ????
###


from typing import *


from .var2int import Var2Int


# ------------------------------------------- #
# -- BASE CLASS FOR INTERGERS' CONVERSIONS -- #
# ------------------------------------------- #

###
# This class is to be herited by the classes playing with base conversions of integers.
###

class IntConv:
###
# prototype::
#     tryconvert : :see: ``tbox.var2int.Var2Int.__init__``
#     toremove   : :see: ``tbox.var2int.Var2Int.__init__``
###
    def __init__(
        self,
        tryconvert: bool      = False,
        toremove  : List[str] = [],
    ):
        self.tryconvert = tryconvert
        self.toremove   = toremove

        self.legalint = Var2Int(
            tryconvert = tryconvert,
            toremove   = toremove,
        )

        self.legalebase = Var2Int(
            mini       = 2,
            tryconvert = tryconvert,
            toremove   = toremove,
        )

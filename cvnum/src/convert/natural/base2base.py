#!/usr/bin/env python3

###
# This module proposes one class to convert integers between two bases.
###


from typing import *

from .natconv  import NatConv
from .nat2base import Nat2Base
from .base2nat import Base2Nat


# ------------------------------ #
# -- NATURAL: BASE <~~~> BASE -- #
# ------------------------------ #

###
# This class prposes an easy-to-use api to convert integers between two bases.
#
#
# warning::
#     If you only work with conversion from naturals to a base, just work
#     directly with the class ``nat2Base.Nat2Base``.
#     If you only work with conversion from one base to naturals, just work
#     directly with the class ``base2nat.Base2Nat``.
###
class Base2Base(NatConv):
    def XXX(self):
        ...


# -- METHODS "AUTO" - START -- #
# -- METHODS "AUTO" - END -- #

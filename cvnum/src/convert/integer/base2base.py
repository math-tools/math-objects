#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *

from .intconv import *

from ..natural.base2base import Base2Base


# -------------------------------- #
# -- DECIMAL ~~~> SPECIFIC BASE -- #
# -------------------------------- #

###
# ????
###
class Base2Base(IntConv):
###
# prototype::
#     :see: ``common.BaseConverter.__init__``
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base2base = Base2Base(self.errname)


# -- EXTRA METHODS "AUTO" - START -- #
# -- EXTRA METHODS "AUTO" - END -- #

#!/usr/bin/env python3

###
# This module proposes one class to convert integers between two bases.
###


from typing import *

from .intconv import *

from ..natural.base2base import Base2Base as NatBase2Base


# ------------------------------ #
# -- INTEGER: BASE <~~~> BASE -- #
# ------------------------------ #

###
# This class gives an easy-to-use ¨api to convert integers between two bases.
#
#
# warning::
#     If you only work with conversion from decimal writings to a base,
#     just work with the class ``int2Base.Int2Base``.
#     And if you only work with conversion from one base to decimal writings,
#     just work with the class ``base2int.Base2Int``.
###
class Base2Base(IntConv):
###
# prototype::
#     :see: IntConv.__init__
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base2base = NatBase2Base(self.errname)


# -- EXTRA METHODS "AUTO" - START -- #

# Lines automatically build by the following file.
#
#     + ``tools/factory/convert/integer/build_01_all_methods_I2B_B2I_B2B.py``

###
# prototype::
#     bdigits  : :see: integer.int2base.int2bdigits
#     base_in  : :see: integer.int2base.int2bnb
#     base_out : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bdigits
###
    @deco_callof(tocall = DECO_TAG_B2B,
                 params = [DECO_TAG_BDIGITS, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT])
    def bdigits2bdigits(
        self,
        bdigits : List[int],
        base_in : int,
        base_out: int,
    ) -> List[int]:
        ...


###
# prototype::
#     bdigits  : :see: integer.int2base.int2bdigits
#     base_in  : :see: integer.int2base.int2bnb
#     base_out : :see: integer.int2base.int2bnb
#     sep_out  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnb
###
    @deco_callof(tocall   = DECO_TAG_B2B,
                 params   = [DECO_TAG_BDIGITS, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT, DECO_TAG_SEP_OUT],
                 optional = [DECO_TAG_SEP_OUT])
    def bdigits2bnb(
        self,
        bdigits : List[int],
        base_in : int,
        base_out: int,
        sep_out : str = '',
    ) -> str:
        ...


###
# prototype::
#     bdigits  : :see: integer.int2base.int2bdigits
#     base_in  : :see: integer.int2base.int2bnb
#     base_out : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnumerals
###
    @deco_callof(tocall = DECO_TAG_B2B,
                 params = [DECO_TAG_BDIGITS, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT])
    def bdigits2bnumerals(
        self,
        bdigits : List[int],
        base_in : int,
        base_out: int,
    ) -> List[str]:
        ...


###
# prototype::
#     bnb      : :see: integer.int2base.int2bnb
#     base_in  : :see: integer.int2base.int2bnb
#     base_out : :see: integer.int2base.int2bnb
#     sep_in   : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bdigits
###
    @deco_callof(tocall   = DECO_TAG_B2B,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT, DECO_TAG_SEP_IN],
                 optional = [DECO_TAG_SEP_IN])
    def bnb2bdigits(
        self,
        bnb     : str,
        base_in : int,
        base_out: int,
        sep_in  : str = '',
    ) -> List[int]:
        ...


###
# prototype::
#     bnb      : :see: integer.int2base.int2bnb
#     base_in  : :see: integer.int2base.int2bnb
#     base_out : :see: integer.int2base.int2bnb
#     sep_in   : :see: integer.int2base.int2bnb
#     sep_out  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnb
###
    @deco_callof(tocall   = DECO_TAG_B2B,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT, DECO_TAG_SEP_IN, DECO_TAG_SEP_OUT],
                 optional = [DECO_TAG_SEP_IN, DECO_TAG_SEP_OUT])
    def bnb2bnb(
        self,
        bnb     : str,
        base_in : int,
        base_out: int,
        sep_in  : str = '',
        sep_out : str = '',
    ) -> str:
        ...


###
# prototype::
#     bnb      : :see: integer.int2base.int2bnb
#     base_in  : :see: integer.int2base.int2bnb
#     base_out : :see: integer.int2base.int2bnb
#     sep_in   : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnumerals
###
    @deco_callof(tocall   = DECO_TAG_B2B,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT, DECO_TAG_SEP_IN],
                 optional = [DECO_TAG_SEP_IN])
    def bnb2bnumerals(
        self,
        bnb     : str,
        base_in : int,
        base_out: int,
        sep_in  : str = '',
    ) -> List[str]:
        ...


###
# prototype::
#     bnumerals : :see: integer.int2base.int2bnumerals
#     base_in   : :see: integer.int2base.int2bnb
#     base_out  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bdigits
###
    @deco_callof(tocall = DECO_TAG_B2B,
                 params = [DECO_TAG_BNUMERALS, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT])
    def bnumerals2bdigits(
        self,
        bnumerals: List[str],
        base_in  : int,
        base_out : int,
    ) -> List[int]:
        ...


###
# prototype::
#     bnumerals : :see: integer.int2base.int2bnumerals
#     base_in   : :see: integer.int2base.int2bnb
#     base_out  : :see: integer.int2base.int2bnb
#     sep_out   : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnb
###
    @deco_callof(tocall   = DECO_TAG_B2B,
                 params   = [DECO_TAG_BNUMERALS, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT, DECO_TAG_SEP_OUT],
                 optional = [DECO_TAG_SEP_OUT])
    def bnumerals2bnb(
        self,
        bnumerals: List[str],
        base_in  : int,
        base_out : int,
        sep_out  : str = '',
    ) -> str:
        ...


###
# prototype::
#     bnumerals : :see: integer.int2base.int2bnumerals
#     base_in   : :see: integer.int2base.int2bnb
#     base_out  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnumerals
###
    @deco_callof(tocall = DECO_TAG_B2B,
                 params = [DECO_TAG_BNUMERALS, DECO_TAG_BASE_IN, DECO_TAG_BASE_OUT])
    def bnumerals2bnumerals(
        self,
        bnumerals: List[str],
        base_in  : int,
        base_out : int,
    ) -> List[str]:
        ...

# -- EXTRA METHODS "AUTO" - END -- #

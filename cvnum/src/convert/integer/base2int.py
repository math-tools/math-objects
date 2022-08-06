#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *

from .intconv import *

from ..natural.base2nat import Base2Nat


# -------------------------------- #
# -- DECIMAL ~~~> SPECIFIC BASE -- #
# -------------------------------- #

###
# ????
###
class Base2Int(IntConv):
###
# prototype::
#     :see: ``common.BaseConverter.__init__``
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base2nat = Base2Nat(self.errname)


###
# prototype::
#     bdigits : :see: integer.nat2base.int2bdigits
#     base    : :see: integer.nat2base.int2bnb
#
#     :return: ????
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_BDIGITS, DECO_TAG_BASE])
    def bdigits2nat(
        self,
        bdigits: List[int],
        base   : int,
    ) -> int:
        ...


# -- EXTRA METHODS "AUTO" - START -- #

# Lines automatically build by the following file.
#
#     + ``tools/factory/convert/integer/build_01_all_methods_I2B_B2I_B2B.py``

###
# prototype::
#     bdigits : :see: integer.nat2base.int2bdigits
#     base    : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.fromdigits
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BDIGITS, DECO_TAG_BASE])
    def bdigits2digits(
        self,
        bdigits: List[str],
        base   : int,
    ) -> List[int]:
        ...


###
# prototype::
#     bdigits : :see: integer.nat2base.int2bdigits
#     base    : :see: integer.nat2base.int2bnb
#
#     :return: :see: self.bdigits2nat
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BDIGITS, DECO_TAG_BASE])
    def bdigits2nat(
        self,
        bdigits: List[int],
        base   : int,
    ) -> int:
        ...


###
# prototype::
#     bdigits : :see: integer.nat2base.int2bdigits
#     base    : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.fromnumerals
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BDIGITS, DECO_TAG_BASE])
    def bdigits2numerals(
        self,
        bdigits: List[str],
        base   : int,
    ) -> List[str]:
        ...


###
# prototype::
#     bnb  : :see: integer.nat2base.int2bnb
#     base : :see: integer.nat2base.int2bnb
#     sep  : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.int2bdigits
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def bdigitsof(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[int]:
        ...


###
# prototype::
#     bnb  : :see: integer.nat2base.int2bnb
#     base : :see: integer.nat2base.int2bnb
#     sep  : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.fromdigits
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def bnb2digits(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[int]:
        ...


###
# prototype::
#     bnb  : :see: integer.nat2base.int2bnb
#     base : :see: integer.nat2base.int2bnb
#     sep  : :see: integer.nat2base.int2bnb
#
#     :return: :see: self.bdigits2nat
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def bnb2nat(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[str]:
        ...


###
# prototype::
#     bnb  : :see: integer.nat2base.int2bnb
#     base : :see: integer.nat2base.int2bnb
#     sep  : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.fromnumerals
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def bnb2numerals(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[str]:
        ...


###
# prototype::
#     bnumerals : :see: integer.nat2base.int2bnumerals
#     base      : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.fromdigits
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BNUMERALS, DECO_TAG_BASE])
    def bnumerals2digits(
        self,
        bnumerals: List[str],
        base     : int,
    ) -> List[int]:
        ...


###
# prototype::
#     bnumerals : :see: integer.nat2base.int2bnumerals
#     base      : :see: integer.nat2base.int2bnb
#
#     :return: :see: self.bdigits2nat
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BNUMERALS, DECO_TAG_BASE])
    def bnumerals2nat(
        self,
        bnumerals: List[str],
        base     : int,
    ) -> int:
        ...


###
# prototype::
#     bnumerals : :see: integer.nat2base.int2bnumerals
#     base      : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.fromnumerals
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BNUMERALS, DECO_TAG_BASE])
    def bnumerals2numerals(
        self,
        bnumerals: List[str],
        base     : int,
    ) -> List[str]:
        ...


###
# prototype::
#     bnb  : :see: integer.nat2base.int2bnb
#     base : :see: integer.nat2base.int2bnb
#     sep  : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.int2bnumerals
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def bnumeralsof(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[str]:
        ...


###
# prototype::
#     bdigits : :see: integer.nat2base.int2bdigits
#     base    : :see: integer.nat2base.int2bnb
#     sep     : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.int2bdigits
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BDIGITS, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def frombdigits(
        self,
        bdigits: List[str],
        base   : int,
        sep    : str = '',
    ) -> str:
        ...


###
# prototype::
#     bnumerals : :see: integer.nat2base.int2bnumerals
#     base      : :see: integer.nat2base.int2bnb
#     sep       : :see: integer.nat2base.int2bnb
#
#     :return: :see: integer.nat2base.int2bnumerals
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BNUMERALS, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def frombnumerals(
        self,
        bnumerals: List[str],
        base     : int,
        sep      : str = '',
    ) -> str:
        ...

# -- EXTRA METHODS "AUTO" - END -- #

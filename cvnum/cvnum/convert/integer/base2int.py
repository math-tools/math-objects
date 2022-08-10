#!/usr/bin/env python3

###
# This module converts integers given in different kinds of "base" writings
# into different kinds of decimal writings.
###


from typing import *

from .intconv import *

from ..natural.base2nat import Base2Nat


# -------------------------------- #
# -- DECIMAL ~~~> SPECIFIC BASE -- #
# -------------------------------- #

###
# This class can transform a "base" writting natural like ``"-7B"`` to a decimal
# one like ``-123`` (``"-7B"`` is the hexadecimal writing of ``-123``).
#
# The base must be ``int`` Python greater than ``1``, and , the input
# for conversion can be of the following kinds.
#
#     1) A ``str`` Python like ``"-7B"``.
#
#     1) A list of one ``int`` sign followed by ``int`` digits like
#        ``[-1, 7, 11]``.
#
#     1) A list of one ``str`` sign followed by ``str`` numerals like
#        ``["-", "7", "B"]``.
#
#
# The output for conversion can be of the following kinds.
#
#     1) An ``int`` Python like ``-123`` (``str`` version are not supported
#        by this module, and they won't be).
#
#     1) A list of one ``int`` sign followed by ``int`` digits like
#        ``[1, 2, 3]``.
#
#     1) A list of one ``str`` sign followed by ``str`` numerals like
#        ``["1", "2", "3"]``.
###
class Base2Int(IntConv):
###
# prototype::
#     :see: IntConv.__init__
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base2nat = Base2Nat(self.errname)


###
# prototype::
#     bdigits : :see: integer.int2base.int2bdigits
#     base    : :see: integer.int2base.int2bnb
#
#     :return: the integer obtained by taking care of the arguments
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BDIGITS, DECO_TAG_BASE])
    def bdigits2int(
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
#     bdigits : :see: integer.int2base.int2bdigits
#     base    : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.fromdigits
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
#     bdigits : :see: integer.int2base.int2bdigits
#     base    : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.fromnumerals
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
#     bnb  : :see: integer.int2base.int2bnb
#     base : :see: integer.int2base.int2bnb
#     sep  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bdigits
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
#     bnb  : :see: integer.int2base.int2bnb
#     base : :see: integer.int2base.int2bnb
#     sep  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.fromdigits
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
#     bnb  : :see: integer.int2base.int2bnb
#     base : :see: integer.int2base.int2bnb
#     sep  : :see: integer.int2base.int2bnb
#
#     :return: :see: self.bdigits2int
###
    @deco_callof(tocall   = DECO_TAG_B2N,
                 params   = [DECO_TAG_BNB, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def bnb2int(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[str]:
        ...


###
# prototype::
#     bnb  : :see: integer.int2base.int2bnb
#     base : :see: integer.int2base.int2bnb
#     sep  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.fromnumerals
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
#     bnumerals : :see: integer.int2base.int2bnumerals
#     base      : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.fromdigits
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
#     bnumerals : :see: integer.int2base.int2bnumerals
#     base      : :see: integer.int2base.int2bnb
#
#     :return: :see: self.bdigits2int
###
    @deco_callof(tocall = DECO_TAG_B2N,
                 params = [DECO_TAG_BNUMERALS, DECO_TAG_BASE])
    def bnumerals2int(
        self,
        bnumerals: List[str],
        base     : int,
    ) -> int:
        ...


###
# prototype::
#     bnumerals : :see: integer.int2base.int2bnumerals
#     base      : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.fromnumerals
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
#     bnb  : :see: integer.int2base.int2bnb
#     base : :see: integer.int2base.int2bnb
#     sep  : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnumerals
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
#     bdigits : :see: integer.int2base.int2bdigits
#     base    : :see: integer.int2base.int2bnb
#     sep     : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bdigits
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
#     bnumerals : :see: integer.int2base.int2bnumerals
#     base      : :see: integer.int2base.int2bnb
#     sep       : :see: integer.int2base.int2bnb
#
#     :return: :see: integer.int2base.int2bnumerals
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

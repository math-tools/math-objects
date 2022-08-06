#!/usr/bin/env python3

###
# This module converts different kinds of decimal writings of integers
# into different kinds of "base" writings.
###


from typing import *

from .intconv import *

from ..natural.nat2base import Nat2Base


# ----------------------------------------- #
# -- INTEGER: DECIMAL ~~~> SPECIFIC BASE -- #
# ----------------------------------------- #

###
# This class extends the capabilities of ``natural.Nat2Base`` to any integer.
# It can transform a decimal writting of an integer like ``-123`` into
# a "base" one like ``"-7B"`` (which is the hexadecimal writing of ``-123``).
#
# The input for conversions can be of the following kinds.
#
#     1) An ``int`` Python like ``-123`` (``str`` version are not supported
#        by this module, and they won't be).
#
#     1) A list of digits like ``[-1, 1, 2, 3]`` where the first value of
#        the list indicates the sign: ``-1`` is for a negative integer, and
#        ``1`` for a non-negative one.
#
#     1) A list of numerals like ``["-", "1", "2", "3"]`` where the first value
#        of the list indicates the sign: ``"-""`` is for a negative integer,
#        and ``""`` for a non-negative one.
#
#
# warning::
#     When working with strings, a plus sign is indicated with ``""``, and
#     not ``"+"``.
#
#
# The base must be an ``int`` Python greater than ``1``, and the output of
# one conversion can be of the following kinds.
#
#     1) A ``str`` Python like ``"-7B"``.
#
#     1) A list of one ``int`` sign followed by ``int`` digits like
#        ``[-1, 7, 11]``.
#
#     1) A list of one ``str`` sign followed by ``str`` numerals like
#        ``["-", "7", "B"]``.
###
class Int2Base(IntConv):
###
# prototype::
#     :see: IntConv.__init__
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nat2base = Nat2Base(self.errname)


###
# prototype::
#     nb : an integer ¨nb
#        @ nb in ZZ
#
#     :return: a list starting with a ``str`` sign followed by numerals
#              sorted from the biggest weight to the smallest one
#            @ if   nb < 0
#              then return[0] = "-"
#              else return[0] = "" ;
#              v in return[1:] ==> v in str(0..9)
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_NB])
    def numeralsof(self, nb: int) -> List[str]:
        ...


###
# prototype::
#     nb : :see: self.numeralsof
#
#     :return: a list starting with a ``int`` sign followed by digits
#              sorted from the biggest weight to the smallest one
#            @ if   nb < 0
#              then return[0] = -1
#              else return[0] = 1 ;
#              v in return[1:] ==> v in 0..9
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_NB])
    def digitsof(self, nb: int) -> List[int]:
        ...


###
# prototype::
#     numerals : a list starting with a ``str`` sign followed by numerals sorted
#                from the biggest weight to the smallest one
#              @ numerals[0] in ["-", ""] ;
#                d in numerals[1:] ==> d in str(0..9)
#
#     :return: the integer value corresponding to the sign and the numerals
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_NUMERALS])
    def fromnumerals(
        self,
        numerals: List[str],
    ) -> int:
        ...


###
# prototype::
#     digits : a list starting with a ``int`` sign followed by digits sorted
#              from the biggest weight to the smallest one
#            @ numerals[0] in [-1, 1] ;
#              d in numerals[1:] ==> d in 0..9
#
#     :return: the integer value corresponding to the sign and the digits
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_DIGITS])
    def fromdigits(
        self,
        digits: List[int],
    ) -> int:
        ...


###
# prototype::
#     nb   : :see: self.numeralsof
#     base : the base used to write a natural
#          @ base in 2 .. +inf
#     sep  : a text to separate the numerals.
#
#     :return: a string ``base`` number obtaining by taking care
#              of the arguments
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params   = [DECO_TAG_NB, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def int2bnb(
        self,
        nb  : int,
        base: int,
        sep : str = ''
    ) -> str:
        ...


###
# prototype::
#     nb   : :see: self.numeralsof
#     base : :see: self.int2bnb
#
#     :return: a list starting with a ``str`` sign followed by numerals of
#              the base ``base``, the numerals being sorted from the biggest
#              weight to the smallest one
#            @ if   nb < 0
#              then return[0] = "-"
#              else return[0] = ""
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_NB, DECO_TAG_BASE])
    def int2bnumerals(
        self,
        nb  : int,
        base: int
    ) -> List[str]:
        ...


###
# prototype::
#     nb   : :see: self.numeralsof
#     base : :see: self.int2bnb
#
#     :return: a list starting with a ``int`` sign followed by digits of
#              the base ``base``, the digits being sorted from the biggest
#              weight to the smallest one
#            @ if   nb < 0
#              then return[0] = -1
#              else return[0] = 1 ;
#              v in return[1:] ==> v in 0 .. (base-1)
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_NB, DECO_TAG_BASE])
    def int2bdigits(
        self,
        nb  : int,
        base: int
    ) -> List[int]:
        ...


# -- EXTRA METHODS "AUTO" - START -- #

# Lines automatically build by the following file.
#
#     + ``tools/factory/convert/integer/build_01_all_methods_I2B_B2I_B2B.py``

###
# prototype::
#     digits : :see: self.fromdigits
#     base   : :see: self.int2bnb
#
#     :return: :see: self.int2bdigits
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_DIGITS, DECO_TAG_BASE])
    def digits2bdigits(
        self,
        digits: List[int],
        base  : int,
    ) -> List[int]:
        ...


###
# prototype::
#     digits : :see: self.fromdigits
#     base   : :see: self.int2bnb
#     sep    : :see: self.int2bnb
#
#     :return: :see: self.int2bnb
###
    @deco_callof(tocall   = DECO_TAG_N2B,
                 params   = [DECO_TAG_DIGITS, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def digits2bnb(
        self,
        digits: List[int],
        base  : int,
        sep   : str = '',
    ) -> str:
        ...


###
# prototype::
#     digits : :see: self.fromdigits
#     base   : :see: self.int2bnb
#
#     :return: :see: self.int2bnumerals
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_DIGITS, DECO_TAG_BASE])
    def digits2bnumerals(
        self,
        digits: List[int],
        base  : int,
    ) -> List[str]:
        ...


###
# prototype::
#     numerals : :see: self.fromnumerals
#     base     : :see: self.int2bnb
#
#     :return: :see: self.int2bdigits
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_NUMERALS, DECO_TAG_BASE])
    def numerals2bdigits(
        self,
        numerals: List[str],
        base    : int,
    ) -> List[int]:
        ...


###
# prototype::
#     numerals : :see: self.fromnumerals
#     base     : :see: self.int2bnb
#     sep      : :see: self.int2bnb
#
#     :return: :see: self.int2bnb
###
    @deco_callof(tocall   = DECO_TAG_N2B,
                 params   = [DECO_TAG_NUMERALS, DECO_TAG_BASE, DECO_TAG_SEP],
                 optional = [DECO_TAG_SEP])
    def numerals2bnb(
        self,
        numerals: List[str],
        base    : int,
        sep     : str = '',
    ) -> str:
        ...


###
# prototype::
#     numerals : :see: self.fromnumerals
#     base     : :see: self.int2bnb
#
#     :return: :see: self.int2bnumerals
###
    @deco_callof(tocall = DECO_TAG_N2B,
                 params = [DECO_TAG_NUMERALS, DECO_TAG_BASE])
    def numerals2bnumerals(
        self,
        numerals: List[str],
        base    : int,
    ) -> List[str]:
        ...

# -- EXTRA METHODS "AUTO" - END -- #

#!/usr/bin/env python3

###
# This module converts naturals given in different kinds of "base" writings
# into different kinds of decimal writings.
###


from typing import *

from math import (
    ceil,
    log
)

from .natconv  import NatConv
from .nat2base import Nat2Base


# ----------------------------------------- #
# -- NATURAL: SPECIFIC BASE ~~~> DECIMAL -- #
# ----------------------------------------- #

###
# This class can transform a "base" writting natural like ``"7B"`` to a decimal
# one like ``123`` (``"7B"`` is the hexadecimal writing of ``123``).
#
# The base must be ``int`` Python greater than ``1``, and , the input
# for conversion can be of the following kinds.
#
#     1) A ``str`` Python like ``"7B"``.
#
#     1) A list of digits like ``[7, 11]``.
#
#     1) A list of numerals like ``["7", "11"]``.
#
#
# The output for conversion can be of the following kinds.
#
#     1) An ``int`` Python like ``123`` (``str`` version are not supported
#        by this module, and they won't be).
#
#     1) A list of digits like ``[1, 2, 3]``.
#
#     1) A list of numerals like ``["1", "2", "3"]``.
###
class Base2Nat(NatConv):
###
# prototype::
#     :see: NatConv.__init__
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nat2base = Nat2Base(
            errname = self.errname
        )


###
# prototype::
#     bnumerals     : a list of ``base`` textual numerals sorted from the biggest
#                     weight to the smallest one
#     base_numerals : the list of legal ``base`` textual numerals
#
#     :postcond: v in bnumerals ==> v in base_numerals
###
    def checkbnumerals(
        self,
        bnumerals    : List[str],
        base_numerals: List[str],
    ) -> None:
        for n in bnumerals:
            assert n in base_numerals, \
                   f"illegal numeral ``{n}`` found"


###
# prototype::
#     bdigits : a list of ``base`` digits from the biggest weight to
#               the smallest one
#     base    : :see: nat2base.Nat2Base.nat2bnb
#
#     :postcond: d in bdigits ==> d in 0..base-1
###
    def checkbdigits(
        self,
        bdigits: List[int],
        base   : int,
    ):
        for d in bdigits:
            self.checknatural(
                nb      = d,
                mini    = 0,
                maxi    = base - 1,
                errname = "digit"
            )


###
# prototype::
#     base : :see: nat2base.Nat2Base.nat2bnb
#
#     :return: a dictionary associating a ``base`` numerals to
#              its ``base``-digit integer value
###
    def basedigitize(self, base: int) -> Dict[str, int]:
# Don't trust the user!
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

# Let's work.
        numeralize = self.nat2base.numeralize(base)

        return {
            numeralize(i)[0]: i
            for i in range(base)
        }


###
# prototype::
#     bnb  : a string representation of a number in base ``base``
#     base : :see: self.checkbdigits
#     sep  : :see: nat2base.Nat2Base.nat2bnb
#
#     :return: the list of numerals of ``bnb``, the numerals beeing
#              sorted from the biggest weight to the smallest one
#            @ v in return ==> v in str(0 .. (base-1))
###
    def bnumeralsof(
        self,
        bnb : str,
        base: int,
        sep : str = ''
    ) -> List[str]:
# Don't trust the user!
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

# An non empty seperator used.
        if sep:
            bnumerals = bnb.split(sep)

# An empty seperator has been used.
#
# Nothing to do with small bases.
        elif base < 37:
            bnumerals = [x for x in bnb]

# Let's slice the input.
        else:
            bnumerals = []
            nbchars  = ceil(log(base) / log(36))
            sizenb   = len(bnb)

            for i in range(sizenb - nbchars, -1, -nbchars):
                bnumerals.append(bnb[i: i + nbchars])

            nbchars_isolated = sizenb % nbchars

            if nbchars_isolated != 0:
                bnumerals.append(bnb[:nbchars_isolated])

            bnumerals.reverse()

# Legal numerals?
        base_digits = self.basedigitize(base)

        self.checkbnumerals(bnumerals, base_digits)

# The job is finished.
        return bnumerals


###
# prototype::
#     bnb  : :see: self.bnumeralsof
#     base : :see: self.bnumeralsof
#     sep  : :see: self.bnumeralsof
#
#     :return: the list of decimal digits of ``bnb``, the digits beeing
#              sorted from the biggest weight to the smallest one
#            @ v in return ==> v in 0..base-1
###
    def bdigitsof(
        self,
        bnb : str,
        base: int,
        sep : str = ''
    ) -> List[int]:
        numerals2digits = self.basedigitize(base)

        return [
            numerals2digits[n]
            for n in self.bnumeralsof(bnb, base, sep)
        ]


###
# prototype::
#     bdigits : a list of integer ``base`` digits
#     base    : :see: self.bnumeralsof
#     sep     : :see: self.bnumeralsof
#
#     :return: the string ``base`` writing of ``bdigits``
###
    def frombdigits(
        self,
        bdigits: List[str],
        base   : int,
        sep    : str = ''
    ) -> str:
# Don't trust the user!
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        self.checkbdigits(
            bdigits = bdigits,
            base    = base,
        )

        numeralize = self.nat2base.numeralize(base)

        return sep.join(numeralize(i)[0] for i in bdigits)


###
# prototype::
#     bnumerals : :see: self.checkbnumerals
#     base      : :see: self.bnumeralsof
#     sep       : :see: self.bnumeralsof
#
#     :return: the string ``base`` writing of ``bnumerals``
###
    def frombnumerals(
        self,
        bnumerals: List[str],
        base     : int,
        sep      : str = ''
    ) -> str:
# Don't trust the user!
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        base_digits = self.basedigitize(base)

        self.checkbnumerals(
            bnumerals     = bnumerals,
            base_numerals = base_digits,
        )

        return sep.join(bnumerals)


###
# prototype::
#     bdigits : :see: self.checkbdigits
#     base    : :see: self.checkbdigits
#
#     :return: the integer value corresponding to the ``base`` digits
#
#     :see: bdigitize
#
#
# note::
#     The name ``bdigits2nat`` comes from "base digits to integer".
###
    def bdigits2nat(
        self,
        bdigits: List[int],
        base   : int,
    ) -> int:
# Don't trust the user!
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        self.checkbdigits(
            bdigits = bdigits,
            base    = base,
        )

        intval = 0
        bpower = 1

        for n in reversed(bdigits):
            intval += n*bpower
            bpower *= base

        return intval


###
# prototype::
#     bnumerals : :see: self.checkbnumerals
#     base      : :see: self.bnumeralsof
#
#     :return: the integer value from the biggest weight to the smallest one
#
#     :see: bdigitize
#
#
# note::
#     The name ``bnumerals2nat`` comes from "base numerals to integer".
###
    def bnumerals2nat(
        self,
        bnumerals: List[str],
        base     : int,
    ) -> int:
# Don't trust the user!
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        base_digits = self.basedigitize(base)

        self.checkbnumerals(
            bnumerals     = bnumerals,
            base_numerals = base_digits,
        )

        intval = 0
        bpower = 1

        for n in reversed(bnumerals):
            intval += base_digits[n]*bpower
            bpower *= base

        return intval


# -- EXTRA METHODS "AUTO" - START -- #

# Lines automatically build by the following file.
#
#     + ``tools/factory/convert/natural/build_01_xtra_methods_N2B_B2N.py``

###
# prototype::
#     bdigits : :see: self.frombdigits
#     base    : :see: self.frombdigits
#
#     :return: :see: self.bnb2digits
###
    def bdigits2digits(
        self,
        bdigits: List[str],
        base   : int,
    ) -> List[int]:
        return self.bnb2digits(
            bnb = self.frombdigits(
                bdigits = bdigits,
                base    = base,
            ),
            base = base,
        )


###
# prototype::
#     bdigits : :see: self.frombdigits
#     base    : :see: self.frombdigits
#
#     :return: :see: self.bnb2numerals
###
    def bdigits2numerals(
        self,
        bdigits: List[str],
        base   : int,
    ) -> List[str]:
        return self.bnb2numerals(
            bnb = self.frombdigits(
                bdigits = bdigits,
                base    = base,
            ),
            base = base,
        )


###
# prototype::
#     bnb  : :see: self.bnb2nat
#     base : :see: self.bnb2nat
#     sep  : :see: self.bnb2nat
#
#     :return: :see: self.nat2base.digitsof
###
    def bnb2digits(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[int]:
        return self.nat2base.digitsof(
            nb = self.bnb2nat(
                bnb  = bnb,
                base = base,
                sep  = sep,
            ),
        )


###
# prototype::
#     bnb  : :see: self.bnumeralsof
#     base : :see: self.bnumeralsof
#     sep  : :see: self.bnumeralsof
#
#     :return: :see: self.bnumeralsof
###
    def bnb2nat(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[str]:
        return self.bnumerals2nat(
            bnumerals = self.bnumeralsof(
                bnb  = bnb,
                base = base,
                sep  = sep,
            ),
            base = base,
        )


###
# prototype::
#     bnb  : :see: self.bnb2nat
#     base : :see: self.bnb2nat
#     sep  : :see: self.bnb2nat
#
#     :return: :see: self.nat2base.numeralsof
###
    def bnb2numerals(
        self,
        bnb : str,
        base: int,
        sep : str = '',
    ) -> List[str]:
        return self.nat2base.numeralsof(
            nb = self.bnb2nat(
                bnb  = bnb,
                base = base,
                sep  = sep,
            ),
        )


###
# prototype::
#     bnumerals : :see: self.frombnumerals
#     base      : :see: self.frombnumerals
#
#     :return: :see: self.bnb2digits
###
    def bnumerals2digits(
        self,
        bnumerals: List[str],
        base     : int,
    ) -> List[int]:
        return self.bnb2digits(
            bnb = self.frombnumerals(
                bnumerals = bnumerals,
                base      = base,
            ),
            base = base,
        )


###
# prototype::
#     bnumerals : :see: self.frombnumerals
#     base      : :see: self.frombnumerals
#
#     :return: :see: self.bnb2numerals
###
    def bnumerals2numerals(
        self,
        bnumerals: List[str],
        base     : int,
    ) -> List[str]:
        return self.bnb2numerals(
            bnb = self.frombnumerals(
                bnumerals = bnumerals,
                base      = base,
            ),
            base = base,
        )

# -- EXTRA METHODS "AUTO" - END -- #

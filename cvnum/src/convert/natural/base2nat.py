#!/usr/bin/env python3

###
# This module converts specific base writings to decimal writings.
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
# ???
###
class Base2Nat(NatConv):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nat2base = Nat2Base(
            safemode = self.safemode,
            errname  = self.errname
        )


###
# prototype::
#     base : :see: nat2base.Nat2Base.nat2bnb
#
#     :return: a dictionary associating ``base`` numerals to integer values
###
    def basedigitize(self, base: int) -> Dict[str, int]:# Safe mode used?
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        numeralize = self.nat2base.numeralize(base)

        return {
            numeralize(i)[0]: i
            for i in range(base)
        }


###
# prototype::
#     bnb  : a string represetation of a number in base ``base``
#     base : :see: nat2base.Nat2Base.nat2bnb
#     sep  : :see: nat2base.Nat2Base.nat2bnb
#
#     :return: the list of textual numerals of ``bnb``, the numerals beeing
#              sorted from the biggest weight to the smallest one
#            @ v in return ==> v in str(0..10)
###
    def bnumeralsof(
        self,
        bnb : str,
        base: int,
        sep : str = ''
    ) -> List[str]:
# Safe mode used?
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        base_numerals = list(self.basedigitize(base))

# An non empty seperator used.
        if sep:
            numerals = bnb.split(sep)

# ???
        elif base < 37:
            numerals = [x for x in bnb]

# An empty seperator has been used.
        else:
            numerals = []
            nbchars  = ceil(log(base) / log(36))
            sizenb   = len(bnb)

            for i in range(sizenb - nbchars, -1, -nbchars):
                numerals.append(bnb[i: i + nbchars])

            nbchars_isolated = sizenb % nbchars

            if nbchars_isolated != 0:
                numerals.append(bnb[:nbchars_isolated])

            numerals.reverse()

# Legal numerals?
        for n in numerals:
            assert n in base_numerals, \
                   f"illegal numeral << {n} >> found"

# The job is finished.
        return numerals


###
# prototype::
#     bnb  : a number writing into the base ``base``
#     base : :see: ``bdigitize``
#     sep  : the text used to separate the integer numerals
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
#     bdigits : a list of ``base`` digits from the biggest weight to
#               the smallest one
#             @ d in bdigits ==> d in 0..base-1
#     base    : :see: ``bdigitize``
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
# Safe mode used?
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        intval = 0
        bpower = 1

        for n in reversed(bdigits):
# Safe mode used?
            self.checknatural(
                nb      = n,
                mini    = 0,
                maxi    = base - 1,
                errname = "digit"
            )

            intval += n*bpower
            bpower *= base

        return intval


###
# prototype::
#     bnumerals : a list of ``base`` textual numerals sorted from the biggest
#                 weight to the smallest one
#     base      : :see: ``bdigitize``
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
# Safe mode used?
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        base_digits = self.basedigitize(base)

        intval = 0
        bpower = 1

        for n in reversed(bnumerals):
            assert n in base_digits, \
                   'unknown numeral << {0} >>.'.format(n)

            intval += base_digits[n]*bpower
            bpower *= base

        return intval


###
# prototype::
#     bnb  : a number written into the base ``base``
#     base : :see: ``bdigitize``
#     sep  : the text used to separate the textual numerals
#
#     :return: the integer value of ``number``
#
#     :see: basenumerals ,
#           bnumerals2nat
#
#
# note::
#     The name ``bnb2int`` comes from "base number to integer".
###
    def bnb2nat(
        self,
        bnb : str,
        base: int,
        sep : str = ''
    ) -> int:
        return self.bnumerals2nat(
            bnumerals = self.bnumeralsof(
                bnb  = bnb,
                base = base,
                sep  = sep
            ),
            base = base
        )


###
# prototype:: cohérence de l'API!
#     bdigits : a list of ``base`` digits from the biggest weight to
#               the smallest one
#             @ d in bdigits ==> d in 0..9
#
#     :return: the integer value corresponding to the ``base`` digits
#
#     :see: bdigitize
#
#
# note::
#     The name ``bdigits2nat`` comes from "base digits to integer".
###
    def bnb2digits(
        self,
        bnb : str,
        base: int,
        sep : str = ''
    ) -> List[int]:
        return self.nat2base.digitsof(
            self.bnb2nat(
                bnb  = bnb,
                base = base,
                sep  = sep
            )
        )


###
# prototype:: cohérence de l'API!
#     bdigits : a list of ``base`` digits from the biggest weight to
#               the smallest one
#             @ d in bdigits ==> d in 0..9
#
#     :return: the integer value corresponding to the ``base`` digits
#
#     :see: bdigitize
#
#
# note::
#     The name ``bdigits2nat`` comes from "base digits to integer".
###
    def bnb2numerals(
        self,
        bnb : str,
        base: int,
        sep : str = ''
    ) -> List[int]:
        return self.nat2base.numeralsof(
            self.bnb2nat(
                bnb  = bnb,
                base = base,
                sep  = sep
            )
        )

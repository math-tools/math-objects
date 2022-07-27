#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *

from string import digits as STR_DIGITS
from .natconv import NatConv

from math import (
    ceil,
    log
)


# ----------------------------------------- #
# -- NATURAL: DECIMAL ~~~> SPECIFIC BASE -- #
# ----------------------------------------- #

DIGITS = tuple(range(10))

###
# ???
###
class Nat2Base(NatConv):
###
# prototype::
#     nb : a natural ¨nb
#        @ nb in NN
#
#     :return: the sign, and the list of textual decimal digits of ``nb``
#              from the biggest weight to the smallest one
#            @ v in return ==> v in str(0 .. 9)
###
    def numeralsof(self, nb: int) -> List[str]:
# Safe mode used?
        self.checknatural(nb)

# Let's work.
        return [d for d in str(nb)]


###
# prototype::
#     nb : a natural ¨nb
#        @ nb in NN
#
#     :return: the list of decimal digits of ``nb``, the digits
#              beeing sorted from the biggest weight to the smallest one
#            @ v in return ==> v in 0..10
###
    def digitsof(self, nb: int) -> List[int]:
# Safe mode used?
        self.checknatural(nb)

# We can do the conversion.
        return [int(d) for d in str(nb)]



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
    def digits2nat(
        self,
        digits: List[int],
    ) -> int:
        intval = 0
        power  = 1

        for n in reversed(digits):
            assert n in DIGITS, \
                   'unknown digit ``{0}``.'.format(n)

            intval += n*power
            power  *= 10

        return intval


###
# prototype::  cohérence de l'API!
#     numerals : a list of ``base`` textual numerals sorted from the biggest
#                 weight to the smallest one
#
#     :return: the integer value from the biggest weight to the smallest one
#
#     :see: bdigitize
#
#
# note::
#     The name ``numerals2nat`` comes from "base numerals to integer".
###
    def numerals2nat(
        self,
        numerals: List[str],
    ) -> int:
        for n in reversed(numerals):
            assert n in STR_DIGITS, \
                   'unknown numeral ``{0}``.'.format(n)

        return int(''.join(numerals))

###
# prototype::
#     base : :see: self.nat2bdigits
#
#     :return: a function that converts a ``base`` integer digit into
#              a textual numeral.
#
#
# warning::
#     This method is an internal one even if we let it public. No check is done on
#     the type and the value of ``base``!
###
    def numeralize(self, base: int) -> Callable[[int], str]:
# Number of characters needed to code one single digit.
        if base > self.max_singledigit:
            nbchars = ceil(log(base) / log(self.max_singledigit))

        else:
            nbchars = 1

# Internal functions
        def alphanum_single(
            x      : int,
            padding: bool = True
        ) -> str:
# We need more than one character.
            if x >= self.max_singledigit:
                result = "".join(
                    alphanum_single(
                        x       = d,
                        padding = False
                    )
                    for d in self.nat2bdigits(
                        nb   = x,
                        base = self.max_singledigit,
                    )
                )

# One single decimal numeral.
            elif x < 10:
                result = str(x)

# One single upper case letter.
            else:
# 65 - 10 = 55
                result = chr(55 + x)

# Padding or not padding? That is the question...
            if padding:
                result = result.rjust(nbchars, '0')

            return result


        def alphanum(nb: int) -> str:
            coding = tuple(
                map(
                    alphanum_single,
                    self.nat2bdigits(
                        nb   = nb,
                        base = base,
                    )
                )
            )

            return coding

# We return the coding function.
        return alphanum


###
# prototype::
#     nb   : a natural ¨nb
#          @ nb in NN
#     base : the base used to write a natural integer
#          @ base in 2 .. +inf  {not checked}
#
#     :return: the list of integer digits of ``nb`` converted
#              into the base ``base``, the digits beeing sorted from
#              the biggest weight to the smallest one
#            @ v in return ==> v in 0 .. (base-1)
#
#
# note::
#     The name ``nat2bdigits`` comes from "integer to base digits".
###
    def nat2bdigits(
        self,
        nb  : int,
        base: int,
    ) -> List[int]:
# Special case of ``base = 10``.
        if base == 10:
            return self.digitsof(nb)

# Safe mode used?
        self.checknatural(nb)
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

# Let's go.
        bdigits = []

        if nb == 0:
            bdigits = [0]

        else:
            while(nb):
                bdigits.append(nb % base)
                nb = nb // base

            bdigits.reverse()

        return bdigits


###
# prototype::
#     nb   : :see: self.nat2bdigits
#     base : :see: self.nat2bdigits
#
#     :return: the list of textual numerals of ``nb`` converted
#              into the base ``base``, the numerals beeing sorted from
#              the biggest weight to the smallest one
#
#     :see: self.numeralize
#
#
# note::
#     The name ``nat2bdigits`` comes from "integer to base numerals".
###
    def nat2bnumerals(
        self,
        nb  : int,
        base: int,
    ) -> List[int]:
# Special case of ``base = 10``.
        if base == 10:
            return self.numeralsof(nb)

# Safe mode used?
        self.checknatural(nb)
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

        return self.numeralize(base)(nb)


###
# prototype::
#     nb   : :see: self.nat2bdigits
#     base : :see: self.nat2bdigits
#     sep  : the text that will be used only if it is needed to separate numerals
#            using at least two digits (that is the case when the base
#            is bigger than 36). An empty separator can be used.
#
#     :return: an easy-to-read string version of ``nb`` converted into
#              the base ``base``
#
#     :see: nat2bnumerals ,
#           ./dec2base.bnb2int
#
#
# note::
#     The name ``nat2bnb`` comes from "integer to base number".
###
    def nat2bnb(
        self,
        nb  : int,
        base: int,
        sep : str = ''
    ) -> str:
# Safe mode used?
        self.checknatural(nb)
        self.checknatural(
            nb      = base,
            mini    = 2,
            errname = 'base'
        )

# ???
        numerals = self.nat2bnumerals(
            nb   = nb,
            base = base,
        )

        return sep.join(numerals)

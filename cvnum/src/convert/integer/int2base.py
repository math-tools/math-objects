#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *

from math import (
    ceil,
    log
)

from .common import (
    basify,
    intify
)


# ---------------------- #
# -- DECIMAL WRITINGS -- #
# ---------------------- #

###
# prototype::
#     nb : the integer to convert into digits in base ``base``
#        @ nb >= 0
#
#     :return: the list of textual numerals of ``nb``, the numerals beeing
#              sorted from the biggest weight to the smallest one
#            @ v in return ==> v in str(0..10)
###
def intnumerals(nb: int) -> List[str]:
# Is ``nb`` a natural ?
    nb = intify(nb)

# We can do the conversion.
    return [d for d in str(nb)]


###
# prototype::
#     nb : the integer to convert into digits in base ``base``
#        @ nb >= 0
#
#     :return: the list of decimal digits of ``nb``, the digits beeing
#              sorted from the biggest weight to the smallest one
#            @ v in return ==> v in 0..10
###
def intdigits(nb: int) -> List[int]:
# Is ``nb`` a natural ?
    nb = intify(nb)

# We can do the conversion.
    return [int(d) for d in str(nb)]


# -------------------------------- #
# -- DECIMAL ~~~> SPECIFIC BASE -- #
# -------------------------------- #

###
# prototype::
#     nb   : the integer to convert into digits in base ``base``
#          @ nb >= 0
#     base : an integer that represents a base
#          @ base > 1
#
#     :return: the list of digits of ``nb`` converted into the base
#              ``base``, the digits beeing sorted from the biggest weight
#              to the smallest one
#            @ v in return ==> v in NN
#
#
# note::
#     The name ``int2bdigits`` comes from "integer to base digits".
###
def int2bdigits(
    nb  : int,
    base: int,
) -> List[int]:
# Is ``nb`` a natural ?
    nb = intify(nb)

# Is ``base`` a natural greater than one ?
    base = basify(base)

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
#     base : the base used to write a natural integer
#          @ base > 1
#
#     :return: a function that converts a ``base`` digit into a textual numeral.
#
#
# warning::
#     This function is an internal one even if we let it public.
###
def numeralize(base: int) -> Callable[[int], str]:
# Number of characters needed to code one single digit.
    max_singledigit = 36

    if base > max_singledigit:
        nbchars = ceil(log(base) / log(max_singledigit))

    else:
        nbchars = 1

# Internal functions
    def alphanum_single(
        x      : int,
        padding: bool = True
    ) -> str:
# We need more than one character.
        if x >= max_singledigit:
            result = "".join(
                alphanum_single(
                    x       = d,
                    padding = False
                )
                for d in int2bdigits(
                    nb   = x,
                    base = max_singledigit,
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
        coding = list(
            map(
                alphanum_single,
                int2bdigits(
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
#     nb   : the integer to convert into digits in base ``base``
#          @ nb >= 0
#     base : an integer that represents a base
#          @ base > 1
#
#     :return: the list of textual numerals of ``nb`` converted into
#              the base ``base``, the numerals beeing sorted from the biggest
#              weight to the smallest one
#
#     :see: numeralize
#
#
# note::
#     The name ``int2bdigits`` comes from "integer to base numerals".
###
def int2bnumerals(
    nb  : int,
    base: int,
) -> List[int]:
    nb   = intify(nb)
    base = basify(base)

    return numeralize(base)(nb)


###
# prototype::
#     nb   : the integer to convert into digits in base ``base``
#          @ nb >= 0
#     base : an integer that represents a base
#          @ base > 1
#     sep  : the text that will be used if needed to separate numerals
#            using at least two digits (that is the case when base > 36)
#
#     :return: an easy-to-read string version of ``nb`` converted into
#              the base ``base``
#
#     :see: int2bnumerals ,
#           ./dec2base.bnb2int
#
#
# note::
#     The name ``int2bnb`` comes from "integer to base number".
###
def int2bnb(
    nb  : int,
    base: int,
    sep : str = "."
) -> str:
    nb   = intify(nb)
    base = basify(base)

    if base < 37:
        sep = ""

    return sep.join(
        int2bnumerals(
            nb   = nb,
            base = base,
        )
    )

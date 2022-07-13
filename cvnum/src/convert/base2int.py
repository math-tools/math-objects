#!/usr/bin/env python3

###
# This module converts specific base writings to decimal writings.
###


from typing import *

from math import (
    ceil,
    log
)

from .int2base import (
    intnonneg,
    intbase,
    int2bnb
)


# ---------------------------- #
# -- SPECIFIC BASE WRITINGS -- #
# ---------------------------- #

###
# prototype::
#     base : an integer that represents a base
#          @ base > 1
#
#     :return: a dictionary associating ``base`` numerals to integer values
###
def bdigitize(base: int) -> Dict[str, int]:
    return {
        int2bnb(i, base): i
        for i in range(base)
    }


###
# prototype::
#     bnb  : a number writing into the base ``base``
#     base : an integer that represents a base
#          @ base > 1
#     sep  : the text used to separate the textual numerals
#
#     :return: the list of textual numerals of ``bnb``, the numerals beeing
#              sorted from the biggest weight to the smallest one
#            @ v in return ==> v in str(0..10)
###
def basenumerals(
    bnb : str,
    base: int,
    sep : str = "."
) -> List[str]:
    base          = intbase(base)
    base_numerals = list(bdigitize(base))

# No need to use a separator.
    if base <= 36:
        numerals = [x for x in bnb]

# An non empty seperator used.
    elif sep:
        numerals = bnb.split(sep)

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
#     base : an integer that represents a base
#          @ base > 1
#     sep  : the text used to separate the textual numerals
#
#     :return: the list of decimal digits of ``bnb``, the digits beeing
#              sorted from the biggest weight to the smallest one
#            @ v in return ==> v in 0..base-1
###
def basedigits(
    bnb : str,
    base: int,
    sep : str = "."
) -> List[int]:
    numerals2digits = bdigitize(base)

    return [
        numerals2digits[n]
        for n in basenumerals(bnb, base, sep)
    ]


# -------------------------------- #
# -- SPECIFIC BASE ~~~> DECIMAL -- #
# -------------------------------- #

###
# prototype::
#     bdigits : a list of ``base`` digits from the biggest weight to
#               the smallest one
#             @ d in bdigits ==> d in 0..base-1
#     base    : an integer that represents a base
#             @ base > 1
#
#     :return: the integer value corresponding to the ``base`` digits
#
#     :see: bdigitize
#
#
# note::
#     The name ``bdigits2int`` comes from "base digits to integer".
###
def bdigits2int(
    bdigits: List[int],
    base   : int,
) -> int:
    base   = intbase(base)
    intval = 0
    bpower = 1

    for n in reversed(bdigits):
        n = intnonneg(n, "digit")

        assert n < base, \
               f"digit << {n} >> is bigger than the base << {base} >>."

        intval += n*bpower
        bpower *= base

    return intval


###
# prototype::
#     bnumerals : a list of ``base`` textual numerals sorted from the biggest
#                 weight to the smallest one
#     base      : an integer that represents a base
#               @ base > 1
#
#     :return: the integer value from the biggest weight to the smallest one
#
#     :see: bdigitize
#
#
# note::
#     The name ``bnumerals2int`` comes from "base numerals to integer".
###
def bnumerals2int(
    bnumerals: List[str],
    base     : int,
) -> int:
    base_digits = bdigitize(base)

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
#     bnb  : a string version of ``number`` written into the base ``base``
#     base : an integer that represents a base
#          @ base > 1
#     sep  : the text used to separate the textual numerals
#
#     :return: the integer value of ``number``
#
#     :see: bnumerals2int ,
#           bnb2bnumerals
#
#
# note::
#     The name ``bnb2int`` comes from "base number to integer".
###
def bnb2int(
    bnb : str,
    base: int,
    sep : str = "."
) -> int:
    return bnumerals2int(
        bnumerals = basenumerals(
            bnb  = bnb,
            base = base,
            sep  = sep
        ),
        base = base
    )

#!/usr/bin/env python3

###
# This module converts positive integers in [1 , 4999] into roman ones
# and vice versa.
###


from typing import *

import re

from ...config.digit import ROMAN_2_NUMERAL
from ...tbox.str2nb  import intify


# ---------------------- #
# -- A ROMAN NUMBER ? -- #
# ---------------------- #

# The following pattern comes from the book "Dive into Python".

PATTERN_ROMAN_NUMERAL = re.compile(
    '''
    ^                   # beginning of string
    M{0,4}              # thousands: 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds: 900 (CM),
                        #           400 (CD),
                        #           0-300 (0 to 3 C's) or
                        #           500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens: 90 (XC), 40 (XL),
                        #       0-30 (0 to 3 X's) or
                        #       50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones: 9 (IX), 4 (IV),
                        #       0-3 (0 to 3 I's) or
                        #       5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    ''' ,
    re.VERBOSE
)


###
# prototype::
#     rnb : a string that should be a roman number.
#
#     :return: ``True`` if ``nb`` is a valid roman nb, or
#              ``False`` otherwise.
###
def isroman(rnb: str) -> bool:
    return (
         rnb.isupper()
         and
         bool(PATTERN_ROMAN_NUMERAL.search(rnb))
    )


# --------------------------------- #
# -- POSITIVE INTEGER ~~~> ROMAN -- #
# --------------------------------- #

###
# prototype::
#     nb : an integer to convert
#        @ nb in 1..4999
#
#     :return: the roman writing of ``nb``.
###
def int2roman(nb: int) -> str:
# ``nb`` must be a natural integer.
    nb = intify(nb)

# We must have ``1 <= nb <= 4999``.
    assert 0 < nb < 5000, \
           'the natural integer ``nb`` must go from 1 to 4999.'

# We first build the upper version of the roman nb by adding the biggest
# roman numerals first (here, we use the fact that ``ROMAN_2_NUMERAL`` is
# an ordered dictionnary).
    result = ""

    for numerals, integer in ROMAN_2_NUMERAL.items():
        while nb >= integer:
            result += numerals
            nb     -= integer

# All the job has been done.
    return result


# --------------------------------- #
# -- ROMAN ~~~> POSITIVE INTEGER -- #
# --------------------------------- #

###
# prototype::
#     rnb : a roman number to convert.
#
#     :return: the decimal version of the roman number ``rnb``
#            @ return in 1..4999
###
def roman2int(rnb: str) -> int:
# ``nb`` must be a legal roman nb.
    assert isroman(rnb), \
           f"<< {rnb} >> is not a legal roman nb."

# Just eat the upper roman digits from left to right by taking care of
# couple of roman digits like IX (9), IV (4) and CM (900) for example.
    imax   = len(rnb)
    i      = 0
    result = 0

    while(i < imax):
# We look first for couples of roman digits that are numerals.
        intval = ROMAN_2_NUMERAL.get(rnb[i: i+2], -1)

# KO !
        if intval == - 1:
            intval = ROMAN_2_NUMERAL[rnb[i]]
            i     += 1

# OK !
        else:
            i += 2

        result += intval

    return result

#!/usr/bin/env python3

###
# The module tests and converts objects that represent numbers.
###


from typing import *


###
# prototype::
#     number     : any object that is printable as an integer
#                @ str(number) in str(ZZ)
#     mini       : the minimum value for the integer representation of number
#                @ mini in RR
#     maxi       : the maximum value for the integer representation of number
#                @ maxi in RR
#     tryconvert : to allow, or not, the use of the printed version of
#                  ``number`` such as to try to convert it to an integer
#     toremove   : a list of string to remove (like space, or digital seprator
#                  for example)
#                @ len(toremove) >= 0
#     name       : the name used in case of error message
#
#     :return: a ¨python integer respecting the boundary constraints
#            @ return in ZZ ;
#              mini <= return <= maxi
###
def intify(
    number    : Any,
    mini      : float     = float('-inf'),
    maxi      : float     = float('inf'),
    tryconvert: bool      = False,
    toremove  : List[str] = [],
    name      : str       = "number",
) -> int:
    if not isinstance(number, int):
        assert tryconvert, \
               (
                f"``The {name} {str(number) = }`` is not an integer. "
                f"Info: no try to convert, and {repr(number) = }"
               )

        strnumber = str(number)

# Remove spaces and decimal separators.
        for xtra in toremove:
            strnumber = strnumber.replace(xtra, '')

        try:
            strnumber = str(int(strnumber))

        except Exception:
            raise ValueError(
                f"``The {name} {str(number) = }`` is not an integer. "
                f"Info: {repr(number) = }"
            )

        number = int(strnumber)

    assert number >= mini, \
           f"``The {name} {number}`` is too small ({mini = })."

    assert number <= maxi, \
           f"``The {name} {number}`` is too big ({maxi = })."

    return number

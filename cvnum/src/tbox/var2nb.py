#!/usr/bin/env python3

###
# The module tests and converts objects that represent numbers.
###


from typing import *


###
# prototype::
#     nb         : any object that is printable as an integer
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
#            @ mini <= return <= maxi
###
def intify(
    nb        : Any,
    mini      : float     = float('-inf'),
    maxi      : float     = float('inf'),
    tryconvert: bool      = False,
    toremove  : List[str] = [],
    name      : str       = "number",
) -> int:
    if not isinstance(nb, int):
        assert tryconvert, \
               (
                f"``The {name} {str(nb) = }`` is not an integer. "
                f"Info: no try to convert, and {repr(nb) = }."
               )

        strnumber = str(nb)

# Remove spaces and decimal separators.
        for xtra in toremove:
            strnumber = strnumber.replace(xtra, '')

        try:
            strnumber = str(int(strnumber))

        except Exception:
            raise ValueError(
                f"``The {name} {str(nb) = }`` is not an integer. "
                f"Infos: {repr(nb) = } and {toremove = }."
            )

        nb = int(strnumber)

    assert nb >= mini, \
           f"``The {name} {nb}`` is too small ({mini = })."

    assert nb <= maxi, \
           f"``The {name} {nb}`` is too big ({maxi = })."

    return nb


###
# prototype::
#     nb         : any object that is printable as an integer
#                @ str(nb) in str(ZZ)
#     tryconvert : to allow, or not, the use of the printed version of
#                  ``nb`` such as to try to convert it to an integer
#     name       : the name used in case of error message
#
#     :return: a ¨python integer greater than `1``
#            @ return in 2..+inf
###
def basify(
    nb        : Any,
    tryconvert: bool = False,
    name      : str  = "base"
) -> int:
    return intify(
        nb         = nb,
        mini       = 2,
        tryconvert = tryconvert,
        name       = name
    )


###
# prototype::
#     nb         : any object that is printable as an integer
#                @ str(nb) in str(ZZ)
#     tryconvert : to allow, or not, the use of the printed version of
#                  ``nb`` such as to try to convert it to an integer
#     name       : the name used in case of error message
#
#     :return: a ¨python non-negative integer
#            @ return in 0..+inf
###
def intify_notneg(
    nb        : Any,
    tryconvert: bool = False,
    name      : str  = "number"
) -> int:
    return intify(
        nb         = nb,
        mini       = 0,
        tryconvert = tryconvert,
        name       = name
    )

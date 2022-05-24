#!/usr/bin/env python3

###
# The module tests and converts objects that represent numbers.
###


from typing import *


###
# prototype::
#     number     : any object that represents an integer
#     name       : the name used in case of error message
#     tryconvert : to allow or not to use, if needed, the printed version
#                  of ``number`` such as to try to convert it to an integer
#
#     :return: a ¨python non negative integer
#            @ return >= 0
###
def intnonneg(
    number    : Any,
    name      : str = "number",
    tryconvert: bool = False
) -> int:
    if not isinstance(number, int):
        if not tryconvert:
            raise ValueError(
                f"``{name} = {repr(number)}`` is not an integer."
            )

        strnumber = str(number)

        if not strnumber.isdigit():
            raise ValueError(
                f"``{name} = {repr(number)}`` is not printed as an integer."
            )

        number = int(strnumber)

    if number < 0:
        raise ValueError(
            f"``{name} = {number}`` is not a natural integer."
        )

    return number


###
# prototype::
#     base       : any object that represents an integer
#     name       : the name used in case of error message
#     tryconvert : to allow or not to use, if needed, the printed version
#                  of ``base`` such as to try to convert it to an integer
#
#     :return: a ¨python integer greater than `1`
#            @ return >= 2
###
def intbase(
    base      : Any,
    name      : str = "base",
    tryconvert: bool = False
) -> int:
    base = intnonneg(base, name, tryconvert)

    if base in [0, 1]:
        raise ValueError(
            f"``{name} = {base}`` is not greater than one."
        )

    return base

#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from lib2to3.pgen2.token import PLUS
from typing import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

MINUS_STR_SIGN = "-"
MINUS_INT_SIGN = -1

PLUS_STR_SIGN = ""
PLUS_INT_SIGN = 1

STR_SIGNS = [
    MINUS_STR_SIGN,
    PLUS_STR_SIGN,
]

PARAM_TAG_NB       = 'nb'
PARAM_TAG_NUMERALS = 'numerals'
PARAM_TAG_DIGITS   = 'digits'
PARAM_TAG_BASE     = 'base'
PARAM_TAG_SEP      = 'sep'

# ----------------------------------------- #
# -- ??? -- #
# ----------------------------------------- #

###
# prototype::
#     ???
###
def self_n_kwargs(
    method_name,
    params,
    optionals,
    args,
    kwargs,
):
# Isolation of the ``self`` argument.
    self, *args = args

# We populate ``kwargs`` by using ``args``.
    _kwargs   = kwargs.copy()

    i_params  = -1
    nb_params = len(params)

    for i, val in enumerate(args):
        i_params += 1

        if params[i_params] in _kwargs:
            i_params += 1

        assert i_params < nb_params

        _kwargs[params[i_params]] = val

# Only optional parameters can miss!
    missing = set(params) - set(_kwargs)

    assert missing <= optionals, \
           (
             f"Int2Base.{method_name}() needs "
            + ("one" if len (missing) == 1 else "some")
            + " mandatory parameter"
            + ("" if len(missing) == 1 else "s")
            + " that "
            + ("is" if len (missing) == 1 else "are")
            + " missing: "
            + ", ".join(sorted(list(missing)))
            + "."
           )

# Nothing looks bad... For the moment!
    return self, _kwargs


# ----------------------------------------- #
# -- ??? -- #
# ----------------------------------------- #

###
# ???? This class is to be herited by the classes playing with base conversions of integers.
###
class IntConv:
###
# prototype::
#     errname : the name used in case of error message
###
    def __init__(
        self,
        errname : str = "number",
    ):
        self.errname = errname


###
# prototype::
#     ???
###
    def sign_n_abs_of(self, nb: int) -> Tuple[int]:
        if nb < 0:
            sign = MINUS_INT_SIGN
            nb   = -nb

        else:
            sign = PLUS_INT_SIGN

        return sign, nb


###
# prototype::
#     ???
###
    def strsign(self, sign: int) -> str:
        if sign == MINUS_INT_SIGN:
            return MINUS_STR_SIGN

        return PLUS_STR_SIGN


###
# prototype::
#     ???
###
    def intsign(self, strsign: str) -> int:
        if strsign == MINUS_STR_SIGN:
            return MINUS_INT_SIGN

        return PLUS_INT_SIGN

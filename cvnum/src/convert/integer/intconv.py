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

INT_SIGNS = [
    MINUS_INT_SIGN,
    PLUS_INT_SIGN,
]

DECO_TAG_N2B = 'nat2base'
DECO_TAG_B2N = 'base2nat'
DECO_TAG_B2B = 'base2base'

DECO_TAG_NB = 'nb'

DECO_TAG_BNB  = 'bnb'
DECO_TAG_BASE = 'base'
DECO_TAG_SEP  = 'sep'

DECO_TAG_NUMERALS = 'numerals'
DECO_TAG_DIGITS   = 'digits'

DECO_TAG_BNUMERALS = 'bnumerals'
DECO_TAG_BDIGITS   = 'bdigits'


# ------------------------------------- #
# -- DECORATORS FOR THE LAZZY CODERS -- #
# ------------------------------------- #

###
# prototype::
#     ???
###
def self_n_kwargs(
    method_name,
    params,
    optional,
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
    missing = set(params) - set(_kwargs) - optional

    assert missing == set(), \
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


###
# prototype::
#     ???
###
def deco_callof(tocall, params, optional = []):
    def _deco_callof_(method):
        method_name     = method.__name__
        nat_method_name = method_name.replace('int', 'nat')

        def method_wrapped(*args, **kwargs):
            self, params_found = self_n_kwargs(
                method_name = method_name,
                params      = params,
                optional    = set(optional),
                args        = args,
                kwargs      = kwargs,
            )

# Let's take care of signs!
            if DECO_TAG_NB in params_found:
                sign, params_found[DECO_TAG_NB] = self.intsign_n_abs_of(
                    params_found[DECO_TAG_NB]
                )

            elif DECO_TAG_BNB in params_found:
                sign, params_found[DECO_TAG_BNB] = self.strsign_n_abs_of(
                    params_found[DECO_TAG_BNB]
                )

            else:
                for tag in [
                    DECO_TAG_DIGITS,
                    DECO_TAG_NUMERALS,
                    DECO_TAG_BDIGITS,
                    DECO_TAG_BNUMERALS,
                ]:
                    if tag in params_found:
                        sign, *input_absnb = params_found[tag]
                        params_found[tag]  = input_absnb
                        break

            absreturn = self.__getattribute__(
                tocall
            ).__getattribute__(
                nat_method_name
            )(
                **params_found
            )

            if isinstance(absreturn, list):
                if isinstance(absreturn[0], str):
                    sign = self.strsign(sign)

                elif isinstance(sign, str):
                    sign = self.intsign(sign)

                absreturn.insert(0, sign)

            elif isinstance(absreturn, int):
                if sign in STR_SIGNS:
                    sign = self.intsign(sign)

                absreturn = sign * absreturn

            else:
                if not sign in STR_SIGNS:
                    sign = self.strsign(sign)

                absreturn = f"{sign}{absreturn}"

            return absreturn

        return method_wrapped

    return _deco_callof_




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
    def intsign_n_abs_of(self, nb: int) -> Tuple[int]:
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
    def strsign_n_abs_of(self, bnb: str) -> Tuple[str]:
        if bnb[0] == MINUS_STR_SIGN:
            sign = MINUS_STR_SIGN
            bnb  = bnb[1:]

        else:
            sign = PLUS_STR_SIGN

        return sign, bnb


###
# prototype::
#     ???
###
    def strsign(self, sign: int) -> str:
        if sign in STR_SIGNS:
            return sign

        if sign == MINUS_INT_SIGN:
            return MINUS_STR_SIGN

        return PLUS_STR_SIGN


###
# prototype::
#     ???
###
    def intsign(self, sign: str) -> int:
        if sign in STR_SIGNS:
            return sign

        if sign == MINUS_STR_SIGN:
            return MINUS_INT_SIGN

        return PLUS_INT_SIGN

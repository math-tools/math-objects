#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *

from .intconv import *

from ..natural.nat2base import Nat2Base


# ------------------------------------- #
# -- DECORATORS FOR THE LAZZY CODERS -- #
# ------------------------------------- #

def decotest(params, optionals = []):
    def _decotest_(method):
        method_name     = method.__name__
        nat_method_name = method_name.replace('int', 'nat')

        def method_wrapped(*args, **kwargs):
            self, params_found = self_n_kwargs(
                method_name = method_name,
                params      = params,
                optionals   = set(optionals),
                args        = args,
                kwargs      = kwargs,
            )

# Let's take care of signs!
            if PARAM_TAG_NB in params_found:
                sign, params_found[PARAM_TAG_NB] = self.sign_n_abs_of(
                    params_found[PARAM_TAG_NB]
                )

            else:
                for tag in [
                    PARAM_TAG_DIGITS,
                    PARAM_TAG_NUMERALS,
                ]:
                    if tag in params_found:
                        sign, *input_absnb = params_found[tag]
                        params_found[tag]  = input_absnb
                        break

            abseturn = self.nat2base.__getattribute__(nat_method_name)(
                **params_found
            )

            if isinstance(abseturn, list):
                if isinstance(abseturn[0], str):
                    sign = self.strsign(sign)

                abseturn.insert(0, sign)

            elif isinstance(abseturn, int):
                if sign in STR_SIGNS:
                    sign = self.intsign(sign)

                abseturn = sign*abseturn

            else:
                if not sign in STR_SIGNS:
                    sign = self.strsign(sign)

                abseturn = sign+abseturn

            return abseturn

        return method_wrapped

    return _decotest_


# -------------------------------- #
# -- DECIMAL ~~~> SPECIFIC BASE -- #
# -------------------------------- #

###
# ????
###
class Int2Base(IntConv):
###
# prototype::
#     :see: ``common.BaseConverter.__init__``
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nat2base = Nat2Base(self.errname)


###
# prototype::
#     nb : a integer ¨nb
#        @ nb in ZZ
#
#     ??? :return: the list of textual decimal digits of ``nb`` sorted from
#              the biggest weight to the smallest one
#            @ return[0] = 1  if v >= 0 ;
#              return[0] = -1 if v < 0 ;
#              v in return[1:] ==> v in str(0..9)
#
#
#     :see: deco_XXXof_via_NAT
###
    @decotest(params = [PARAM_TAG_NB])
    def numeralsof(self, nb: int) -> List[str]:
        ...


###
# prototype::
#     nb : :see: self.numeralsof
#
#     :return: ???? the list of decimal digits of ``nb``, the digits sorted from
#              the biggest weight to the smallest one
#            @ v in return ==> v in 0..9
#
#
#     :see: deco_XXXof_via_NAT
###
    @decotest(params = [PARAM_TAG_NB])
    def digitsof(self, nb: int) -> List[int]:
        ...


###
# prototype::
#     ??? digits : a list of digits sorted from the biggest weight to
#              the smallest one
#             @ d in digits ==> d in 0..9
#
#     :return: the decorator gives ????
#              the natural value corresponding to the digits
#
#
#     :see: deco_fromXXX_via_NAT
###
    @decotest(params = [PARAM_TAG_NUMERALS])
    def fromnumerals(
        self,
        numerals: List[str],
    ) -> int:
        ...


###
# prototype::
#     ??? digits : a list of digits sorted from the biggest weight to
#              the smallest one
#             @ d in digits ==> d in 0..9
#
#     :return: the decorator gives ????
#              the natural value corresponding to the digits
#
#
#     :see: deco_fromXXX_via_NAT
###
    @decotest(params = [PARAM_TAG_DIGITS])
    def fromdigits(
        self,
        digits: List[int],
    ) -> int:
        ...


###
# prototype::
#     nb   : :see: self.numeralsof
#     base : the base used to write a natural natural
#          @ base in 2 .. +inf
#     sep  : a text to use to separate numerals only if they use at least
#            two characters (that is the case when the base is bigger than 36).
#            An empty separator can be used.
#
#     :return: a string version of ``nb`` when it is converted into the base
#              ``base``
#
#
# note::
#     The name ``nat2bnb`` comes from "natural to base number".
###
    @decotest(params    = [PARAM_TAG_NB, PARAM_TAG_BASE, PARAM_TAG_SEP],
              optionals = [PARAM_TAG_SEP])
    def int2bnb(
        self,
        nb  : int,
        base: int,
        sep : str = ''
    ) -> str:
        ...


# -- EXTRA METHODS "AUTO" - START -- #

    @decotest(params    = [PARAM_TAG_DIGITS, PARAM_TAG_BASE])
    def digits2bdigits(
        self,
        digits: List[int],
        base  : int,
    ) -> List[int]:
        ...

# -- EXTRA METHODS "AUTO" - END -- #

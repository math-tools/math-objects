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

def _self_n_single_input(
    arg_name,
    args,
    kwargs,
    error_message,
):
    self, *args = args

    if len(args) > 1:
        raise TypeError(error_message)

    if len(args) == 1:
        input = args[0]

    else:
        if set(kwargs.keys()) != set([arg_name]):
            raise TypeError(error_message)

        for input in kwargs.values():
            ... # Prettyr hack... Or not!

    return self, input


def deco_fromXXX_via_NAT(method):
    method_name = method.__name__
    arg_name    = method_name.replace("from", '')

    error_message = f"{method_name}() requires only 1 argument {arg_name}."

    def method_wrapped(*args, **kwargs):
        self, input = _self_n_single_input(
            arg_name      = arg_name,
            args          = args,
            kwargs        = kwargs,
            error_message = error_message,
        )

        sign, *input_absnb = input

        absnb = self.nat2base.__getattribute__(method_name)(
            input_absnb
        )

        if sign in STR_SIGNS:
            sign = self.intsign(sign)

        return sign*absnb

    return method_wrapped


def deco_XXXof_via_NAT(method):
    method_name = method.__name__
    arg_name    = 'nb'

    error_message = f"{method_name}() requires only 1 argument {arg_name}."

    def method_wrapped(*args, **kwargs):
        self, input = _self_n_single_input(
            arg_name      = arg_name,
            args          = args,
            kwargs        = kwargs,
            error_message = error_message,
        )

        sign, absnb = self.sign_n_abs_of(input)

        XXXof_absnb = self.nat2base.__getattribute__(method_name)(absnb)

        if isinstance(XXXof_absnb[0], str):
            sign = self.strsign(sign)

        XXXof_absnb.insert(0, sign)

        return XXXof_absnb

    return method_wrapped


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
    @deco_XXXof_via_NAT
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
    @deco_XXXof_via_NAT
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
    @deco_fromXXX_via_NAT
    def fromnumerals(
        self,
        numerals: List[int],
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
    @deco_fromXXX_via_NAT
    def fromdigits(
        self,
        digits: List[int],
    ) -> int:
        ...

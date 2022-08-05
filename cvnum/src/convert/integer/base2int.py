#!/usr/bin/env python3

###
# This module converts decimal writings into specific base writings.
###


from typing import *

from .intconv import *

from ..natural.base2nat import Base2Nat


# -------------------------------- #
# -- DECIMAL ~~~> SPECIFIC BASE -- #
# -------------------------------- #

###
# ????
###
class Base2Int(IntConv):
###
# prototype::
#     :see: ``common.BaseConverter.__init__``
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base2nat = Base2Nat(self.errname)


# ###
# # prototype::
# #     nb : a integer ¨nb
# #        @ nb in ZZ
# #
# #     ??? :return: the list of textual decimal digits of ``nb`` sorted from
# #              the biggest weight to the smallest one
# #            @ return[0] = 1  if v >= 0 ;
# #              return[0] = -1 if v < 0 ;
# #              v in return[1:] ==> v in str(0..9)
# #
# #
# #     :see: deco_XXXof_via_NAT
# ###
#     @deco_callof_nat(params = [PARAM_TAG_NB])
#     def numeralsof(self, nb: int) -> List[str]:
#         ...


# ###
# # prototype::
# #     nb : :see: self.numeralsof
# #
# #     :return: ???? the list of decimal digits of ``nb``, the digits sorted from
# #              the biggest weight to the smallest one
# #            @ v in return ==> v in 0..9
# #
# #
# #     :see: deco_XXXof_via_NAT
# ###
#     @deco_callof_nat(params = [PARAM_TAG_NB])
#     def digitsof(self, nb: int) -> List[int]:
#         ...


# ###
# # prototype::
# #     ??? numerals : a list of digits sorted from the biggest weight to
# #              the smallest one
# #             @ d in digits ==> d in 0..9
# #
# #     :return: the decorator gives ????
# #              the natural value corresponding to the digits
# #
# #
# #     :see: deco_fromXXX_via_NAT
# ###
#     @deco_callof_nat(params = [PARAM_TAG_NUMERALS])
#     def fromnumerals(
#         self,
#         numerals: List[str],
#     ) -> int:
#         ...


# ###
# # prototype::
# #     ??? digits : a list of digits sorted from the biggest weight to
# #              the smallest one
# #             @ d in digits ==> d in 0..9
# #
# #     :return: the decorator gives ????
# #              the natural value corresponding to the digits
# #
# #
# #     :see: deco_fromXXX_via_NAT
# ###
#     @deco_callof_nat(params = [PARAM_TAG_DIGITS])
#     def fromdigits(
#         self,
#         digits: List[int],
#     ) -> int:
#         ...


# ###
# # prototype::
# #     nb   : :see: self.numeralsof
# #     base : the base used to write a natural natural
# #          @ base in 2 .. +inf
# #     sep  : a text to use to separate numerals only if they use at least
# #            two characters (that is the case when the base is bigger than 36).
# #            An empty separator can be used.
# #
# #     :return: a string version of ``nb`` when it is converted into the base
# #              ``base``
# ###
#     @deco_callof_nat(params   = [PARAM_TAG_NB, PARAM_TAG_BASE, PARAM_TAG_SEP],
#                      optional = [PARAM_TAG_SEP])
#     def int2bnb(
#         self,
#         nb  : int,
#         base: int,
#         sep : str = ''
#     ) -> str:
#         ...


# ###
# # prototype::
# #     nb   : :see: self.numeralsof
# #     base : :see: self.int2bnb
# #
# #     :return: ????
# ###
#     @deco_callof_nat(params = [PARAM_TAG_NB, PARAM_TAG_BASE])
#     def int2bnumerals(
#         self,
#         nb  : int,
#         base: int
#     ) -> str:
#         ...


# ###
# # prototype::
# #     nb   : :see: self.numeralsof
# #     base : :see: self.int2bnb
# #
# #     :return: ????
# ###
#     @deco_callof_nat(params = [PARAM_TAG_NB, PARAM_TAG_BASE])
#     def int2bdigits(
#         self,
#         nb  : int,
#         base: int
#     ) -> str:
#         ...


# # -- EXTRA METHODS "AUTO" - START -- #
# # -- EXTRA METHODS "AUTO" - END -- #

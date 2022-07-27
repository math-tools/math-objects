#!/usr/bin/env python3

###
# This module proposes one class to convert integers between two bases.
###


from typing import *

from .natconv  import NatConv
from .nat2base import Nat2Base
from .base2nat import Base2Nat


# ------------------------------ #
# -- NATURAL: BASE <~~~> BASE -- #
# ------------------------------ #

# -- FORMATS ALLOWED "AUTO" - START -- #

# Lines automatically build by the following file.
#
#     + ``tools/factory/convert/natural/build_01_format_b2b.py``

# To avoid mistypings of formats.

FORMAT_BDIGITS_OF   = 'bdigitsof'
FORMAT_NAT          = 'nat'
FORMAT_BNUMERALS_OF = 'bnumeralsof'
FORMAT_BDIGITS      = 'bdigits'
FORMAT_BNB          = 'bnb'
FORMAT_BNUMERALS    = 'bnumerals'

# To test "hard" typing strings of formats.

ALL_FORMATS = {
    FORMAT_BDIGITS_OF,
    FORMAT_NAT,
    FORMAT_BNUMERALS_OF,
    FORMAT_BDIGITS,
    FORMAT_BNB,
    FORMAT_BNUMERALS,
}

# -- FORMATS ALLOWED "AUTO" - END -- #


###
# This class simplifies conversions of integers between two bases.
#
#
# warning::
#     If you only work with conversion from naturals to a base, just work directly
#     with the class ``nat2Base.Nat2Base``.
#     If you only work with conversion from one base to naturals, just work directly
#     with the class ``base2nat.Base2Nat``.
###
class Base2Base(NatConv):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.nat2base = Nat2Base(
            safemode = self.safemode,
            errname  = self.errname
        )

        self.base2nat = Base2Nat(
            safemode = self.safemode,
            errname  = self.errname
        )











# # --------------- #
# # -- CONSTANTS -- #
# # --------------- #

# FORMAT_BASE_NB  = "nb"
# FORMAT_DIGITS   = "digits"
# FORMAT_INT      = "int"
# FORMAT_NUMERALS = "numerals"

# FORMAT_ALLOWED = [
#     FORMAT_BASE_NB ,
#     FORMAT_DIGITS  ,
#     FORMAT_INT     ,
#     FORMAT_NUMERALS
# ]


# # --------------------- #
# # --  -- #
# # --------------------- #


# class Base2Base(NatConv):
# # The list of functions that can be use directly.
#     CONVERT_FUNCS = {
# # --     name_of_func  : (func         , needs_seps)      -- #
#         'bnb2nat'      : (bnb2nat      , True),
#         'bnumerals2nat': (bnumerals2nat, False),
#         'bdigits2nat'  : (bdigits2nat  , False),
#         'nat2bnb'      : (nat2bnb      , True),
#         'nat2bnumerals': (nat2bnumerals, False),
#         'nat2bdigits'  : (nat2bdigits  , False),
#     }



# ###
# # prototype::
# #     x      : into the base ``self.bases[0]`` system, ``x`` can be either
# #              an integer, or
# #              a list of digits, or
# #              a list of textual numerals
# #     format : the formatted expected into the base ``self.bases[1]`` system
# #            @ format in FORMAT_ALLOWED
# #
# #     :return: regarding to the formatting expected, we obtain either
# #              an integer, or
# #              a list of digits, or
# #              a list of textual numerals
# #
# #     :see: ./base2dec ,
# #           ./dec2base
# ###
#     def convert(
#         self,
#         x     : Union[int, List[int], List[str]],
#         format: str
#     ) -> Union[int, List[int], List[str]]:
# # Legal format?
#         assert format in FORMAT_ALLOWED, f'invalid << format = {format} >>'

#         assert format != FORMAT_INT or self.bases[1] == 10, \
#                (
#                 f" format << {FORMAT_INT} >> used with "
#                 f"<< base_2 = {self.bases[1]} >> , use << base_2 = 10 >>"
#                )

# # Legal value?
#         assert bool(x), f'invalid << x = {repr(x)} >>'

#         if isinstance(x, list):
#             if isinstance(x[0], int):
#                 fromkind = FORMAT_DIGITS
#             else:
#                 fromkind = FORMAT_NUMERALS

#         elif isinstance(x, int):
#             assert self.bases[0] == 10, \
#                    (
#                     f" integer << {x} >> used with "
#                     f"<< base_1 = {self.bases[0]} != 10 >>"
#                    )

#             fromkind = FORMAT_INT

#         else:
#             fromkind = FORMAT_BASE_NB

# # Function to call.
#         if self.bases[0] == 10 and fromkind == FORMAT_INT:
#             prefix_1 = ''

#         else:
#             prefix_1 = 'b'

#         if format == FORMAT_INT:
#             prefix_2 = ''
#             base     = self.bases[0]
#             sep      = self.seps[0]

#         else:
#             prefix_2 = 'b'
#             base     = self.bases[1]
#             sep      = self.seps[1]

# # A ready-to-use function?
#         funcname = f'{prefix_1}{fromkind}2{prefix_2}{format}'

#         if funcname in self.CONVERT_FUNCS:
#             return self.__applyfunc(
#                 funcname,
#                 x,
#                 base,
#                 sep
#             )

# # We need to compose two functions.
#         funcname_nat2xxx = f'b{fromkind}2nat'
#         funcname_xxx2nat = f'nat2b{format}'

#         val = self.__applyfunc(
#             funcname_nat2xxx,
#             x,
#             self.bases[0],
#             self.seps[0]
#         )

#         return self.__applyfunc(
#             funcname_xxx2nat,
#             val,
#             self.bases[1],
#             self.seps[1]
#         )


# ###
# # prototype::
# #     funcname : the name of one function to apply
# #              @ funcname in self.CONVERT_FUNCS
# #     x        : an integer, or
# #                a list of digits, or
# #                a list of textual numerals
# #     base     : the base to use
# #              @ base > 1
# #     sep      : the text used to separate numerals (if needed)
# #
# #     :return: the value returned by the function called.
# ###
#     def __applyfunc(
#         self,
#         funcname: str,
#         x       : Union[int, List[int], List[str]],
#         base    : int,
#         sep     : str
#     ):
#         func, hassep = self.CONVERT_FUNCS[funcname]

#         if hassep:
#             return func(x, base, sep)

#         return func(x, base)

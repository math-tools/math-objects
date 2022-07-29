# #!/usr/bin/env python3

###
# This module proposes one class to convert integers between two bases.
###


from typing import *

# from .natconv  import NatConv
# from .nat2base import Nat2Base
# from .base2nat import Base2Nat


# # ------------------------------ #
# # -- NATURAL: BASE <~~~> BASE -- #
# # ------------------------------ #

# # -- FORMATS ALLOWED "AUTO" - START -- #

# # Lines automatically build by the following file.
# #
# #     + ``tools/factory/convert/natural/build_01_format_b2b.py``

# # To avoid mistypings of formats.

# FORMAT_BDIGITS   = 'bdigits'
# FORMAT_BNB       = 'bnb'
# FORMAT_NAT       = 'nat'
# FORMAT_BNUMERALS = 'bnumerals'

# # To test "hard" typing strings of formats.

# ALL_FORMATS = {FORMAT_BDIGITS, FORMAT_BNB, FORMAT_NAT, FORMAT_BNUMERALS}

# # -- FORMATS ALLOWED "AUTO" - END -- #


# ###
# # This class simplifies conversions of integers between two bases.
# #
# #
# # warning::
# #     If you only work with conversion from naturals to a base, just work directly
# #     with the class ``nat2Base.Nat2Base``.
# #     If you only work with conversion from one base to naturals, just work directly
# #     with the class ``base2nat.Base2Nat``.
# ###
# class Base2Base(NatConv):
#     TYPE_INT      = 'int'
#     TYPE_STR      = 'str'
#     TYPE_LIST_INT = 'List[int]'
#     TYPE_LIST_STR = 'List[str]'


# ###
# # prototype::
# #     :see: NatConv.__init__
# ###
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.nat2base = Nat2Base(
#             errname  = self.errname
#         )

#         self.base2nat = Base2Nat(
#             errname = self.errname
#         )


# ###
# # prototype::
# #     :action: ???
# ###
#     def checkcvargs(self) -> None:
# # Good sizes?
#         for k, v in [
#             ("formats", self.formats),
#             ("bases"  , self.bases),
#             ("seps"   , self.seps),
#         ]:
# # Good sizes?
#             assert len(v) == 2, \
#                    (
#                     f'``len({k}) != 2``.'
#                     '\n'
#                     f'Infos: {k} = {v}'
#                    )

# # Legal formats?
#         for f in self.formats:
#             assert f in ALL_FORMATS, \
#                 (
#                     f'invalid format ``{f = }``.'
#                     '\n'
#                     f'Infos: {self.formats = }'
#                 )

# # Legal bases?
#         for i, b in enumerate(self.bases):
#             self.checknatural(
#                 nb      = b,
#                 mini    = 2,
#                 errname = f'bases[{i}]'
#             )

# # Legal type of ``input`` regarding to ``formats[0]``?
#         typeofinput = self._typeofinput()

#         assert (
#                 (
#                         typeofinput == self.TYPE_INT
#                     and self.formats[0] == FORMAT_NAT
#                 )
#                 or
#                 (
#                         typeofinput == self.TYPE_STR
#                     and self.formats[0] == FORMAT_BNB
#                 )
#                 or
#                 (
#                         typeofinput == self.TYPE_LIST_INT
#                     and self.formats[0] == FORMAT_BDIGITS
#                 )
#                 or
#                 (
#                         typeofinput == self.TYPE_LIST_STR
#                     and self.formats[0] == FORMAT_BNUMERALS
#                 )
#                ), (
#                 f"incompatible type ``{typeofinput}`` of ``input`` with "
#                 f"the format ``{self.formats[0] = }``."
#                )



# # It is always possible to convert the input to a natural number, whatever
# # is the 2nd base used (which is totally ignored in that special situation).
#         assert (
#                 self.formats[0] != FORMAT_NAT
#                 or
#                 self.bases[0] == 10
#                ), (
#                 f"format ``{FORMAT_NAT = }`` used with "
#                 f"``bases[0] = {self.bases[0]}`` . "
#                  "Use ``bases[0] = 10``"
#                )


# ###
# # prototype::
# #     :action: ???
# ###
#     def _typeofinput(self):
# # Look for a legal type.
#         typefound = None

#         if isinstance(self.input, int):
#             typefound = self.TYPE_INT

#         elif isinstance(self.input, str):
#             typefound = self.TYPE_STR

#         elif isinstance(self.input[0], (int, str)):
#             typefound = type(self.input[0])

#             for i in self.input[1:]:
#                 if not isinstance(i, typefound):
#                     typefound = None
#                     break

#             if typefound == int:
#                 typefound = self.TYPE_LIST_INT

#             elif typefound == str:
#                 typefound = self.TYPE_LIST_STR

# # No legal type found.
#         if typefound is None:
#             raise TypeError(
#                   'illegal type for ``input``. You must use '
#                  f'``{self.TYPE_INT}``, ``{self.TYPE_STR}``, '
#                  f'``{self.TYPE_LIST_INT}``, or ``{self.TYPE_LIST_STR}``.'
#                   '\n'
#                  f'Infos: input = {self.input}'
#             )

# # Legal type used for the input. Let's continue to work...
#         return typefound


# ###
# # prototype::
# #     input  : into the base ``self.bases[0]`` system, ``x`` can be either
# #              an integer, or
# #              a list of digits, or
# #              a list of textual numerals
# #     bases   :
# #     formats : the formatted expected into the base ``self.bases[1]`` system
# #            @ format in FORMAT_ALLOWED
# #     seps    :
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
#         input  : Union[int, str, List[int], List[str]],
#         bases  : List[int],
#         formats: List[str],
#         seps   : List[str] = ['', '']
#     ) -> Union[int, str, List[int], List[str]]:
# # POO needs some attributs...
#         self.input   = input
#         self.bases   = bases
#         self.formats = formats
#         self.seps    = seps

# # Safe mode.
#         self.checkcvargs()

# # Call the good method(s) with the good arguments.
#         return self.buildoutput()


# ###
# # prototype::
# #     :action: ???
# #
# #
# # note::
# #     Except with the base `10`, we always work from the base ``self.bases[0]``
# #     to a natural, and the from the natural found to the base ``self.bases[1]``.
# ###
#     def buildoutput(self):
# # A little of abstraction is so useful!
#         methods = []
#         kwargs  = [] # << WARNING! >> Here we use a list of dictionaries!


# # methods_nat2base = {'numeralsof', 'digitsof', 'nat2bdigits', 'nat2bnumerals', 'numerals2nat', 'nat2bnb', 'digits2nat'}
# # methods_base2nat = {'bdigitsof', 'bdigits2nat', 'bnumeralsof', 'bnumerals2nat', 'bnb2nat'}
# #
# # ``FORMAT_1 = FORMAT_NAT``: in that special case, we ignore the 2nd base that
# # is been forced to be equal to `10`.



# # First mandatory method.

# # Second optional method.

# # Let's apply the methods with the corresponding keywords arguments.

# # Nothing more left to do.
#         return

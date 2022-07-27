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

FORMAT_BDIGITS   = 'bdigits'
FORMAT_BNB       = 'bnb'
FORMAT_NAT       = 'nat'
FORMAT_BNUMERALS = 'bnumerals'

# To test "hard" typing strings of formats.

ALL_FORMATS = {FORMAT_BDIGITS, FORMAT_BNB, FORMAT_NAT, FORMAT_BNUMERALS}

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


###
# prototype::
#     input  : into the base ``self.bases[0]`` system, ``x`` can be either
#              an integer, or
#              a list of digits, or
#              a list of textual numerals
#     bases   :
#     formats : the formatted expected into the base ``self.bases[1]`` system
#            @ format in FORMAT_ALLOWED
#     seps    :
#
#     :return: regarding to the formatting expected, we obtain either
#              an integer, or
#              a list of digits, or
#              a list of textual numerals
#
#     :see: ./base2dec ,
#           ./dec2base
###
    def convert(
        self,
        input  : Union[int, str, List[int], List[str]],
        bases  : List[int],
        formats: List[str],
        seps   : List[str] = ['', '']
    ) -> Union[int, str, List[int], List[str]]:
# Safe mode used.
        if self.safemode:
# Good sizes?
            for k, v in [
                ("formats", formats),
                ("bases"  , bases),
                ("seps"   , seps),
            ]:
                assert len(v) == 2, \
                       (
                        f'``len({k}) != 2``.'
                        '\n'
                        f'Infos: {k} = {v}'
                       )

# Legal formats?
            for f in formats:
                assert f in ALL_FORMATS, \
                    (
                        f'invalid format ``{f = }``.'
                        '\n'
                        f'Infos: {formats = }'
                    )

# It is always possible to convert the input to a natural number, whatever
# is the 2nd base used (which is totally ignored in that special situation).
            assert (
                    formats[0] != FORMAT_NAT
                    or
                    bases[0] == 10
                   ), (
                    f" format ``{FORMAT_NAT = }`` used with "
                    f"``bases[0] = {bases[0]}`` . Use ``bases[0] = 10``"
                   )

# Legal bases?
            for i, b in enumerate(bases):
                self.checknatural(
                    nb      = b,
                    mini    = 2,
                    errname = f'bases[{i}]'
                )

# Let's call the good methods (that will take care of errors).
#
# ``FORMAT_1 = FORMAT_NAT`` : in that sppecial case, we ignore the 2nd base!
        if formats[1] == FORMAT_NAT:
            ...

# Standard usecase: the two bases are used.
        ...

# The job as been done. What a miracle!


###
# prototype:: ????
###
    def __typeof(self, input):
# Look for a legal type.
        typefound = None

        if isinstance(input, int):
            typefound = int

        elif isinstance(input, str):
            typefound = str

        elif isinstance(input[0], (int, str)):
            typefound = type(input[0])

            for i in input[1:]:
                if not isinstance(i, typefound):
                    typefound = None
                    break

# No legal type found.
        if typefound is None:
            raise TypeError(
                 'illegal type for ``input``. You must use '
                 'a ``int``, a``str``, '
                 'a list of ``int``, or a list of ``str``.'
                 '\n'
                f'Infos: {input = }'
            )

# Legal type used for the input. Let's continue to work...
        return typefound

#!/usr/bin/env python3

###
# This module proposes one class to convert integers between different bases.
###


from typing import *

from .base2int import (
    bnb2int,
    bnumerals2int,
    bdigits2int
)

from .int2base import (
    int2bnb,
    int2bnumerals,
    int2bdigits,
    intbase
)


# --------------- #
# -- CONSTANTS -- #
# --------------- #

FORMAT_BASE_NB  = "nb"
FORMAT_DIGITS   = "digits"
FORMAT_INT      = "int"
FORMAT_NUMERALS = "numerals"

FORMAT_ALLOWED = [
    FORMAT_BASE_NB ,
    FORMAT_DIGITS  ,
    FORMAT_INT     ,
    FORMAT_NUMERALS
]


# --------------------- #
# -- BASE <~~~> BASE -- #
# --------------------- #

###
# This class simplifies conversions of integers between two bases.
#
#
# warning::
#     If you must do the same kind of conversion a lot, you should work
#     directly with the functions of the modules ``dec2base`` and ``base2dec``.
###
class Base2Base:
# The list of functions that can be use directly.
    CONVERT_FUNCS = {
# --     name_of_func  : (func         , needs_seps)      -- #
        'bnb2int'      : (bnb2int      , True),
        'bnumerals2int': (bnumerals2int, False),
        'bdigits2int'  : (bdigits2int  , False),
        'int2bnb'      : (int2bnb      , True),
        'int2bnumerals': (int2bnumerals, False),
        'int2bdigits'  : (int2bdigits  , False),
    }


###
# prototype::
#     bases : a couple of two integers
#           @ b in bases ==> b > 1
#     seps  : a couple of texts used to separate numerals
###
    def __init__(
        self,
        bases: Tuple[int, int] = (10, 16),
        seps : Tuple[str, str] = (".", ".")
    ) -> None:
        self.bases = bases
        self.seps  = seps


###
# We have to verify the bases when they are setted.
###
    @property
    def bases(self) -> Tuple[int, int]:
        return self._bases

    @bases.setter
    def bases(self, bases: Tuple[int, int]) -> None:
        self._bases = (
            intbase(bases[0]),
            intbase(bases[1]),
        )


###
# prototype::
#     b     : either an integer, or a couple of two integers
#           @ type(bases) = tuple ==> b in bases ==> b > 1
#           @ type(bases) = int   ==> bases > 1
#     which : an integer code to indicate what have to be updated.
#             ``1`` is to just update the first base.
#             ``2`` is to just update the second base.
#             ``-1`` is to update the both bases.
#           @ which in {-1 , 1, 2}
#
#     :action: update of the value of ``self.bases``
#
#     :see: self.__change_tuple_attr
###
    def changebases(
        self,
        b    : Union[int, Tuple[int, int]],
        which: int  = -1
    ) -> None:
        self.__change_tuple_attr(
            name  = "bases",
            val   = b,
            which = which
        )


###
# prototype::
#     s     : a couple of texts used to separate numerals
#     which : an integer code to indicate what have to be updated.
#             ``1`` is to just update the first separator.
#             ``2`` is to just update the second separator.
#             ``-1`` is to update the both separators.
#           @ which in {-1 , 1, 2}
#
#     :action: update of the value of ``self.seps``
#
#     :see: self.__change_tuple_attr
###
    def changeseps(
        self,
        s    : Union[str, Tuple[str, str]],
        which: int  = -1
    ) -> None:
        self.__change_tuple_attr(
            name  = "seps",
            val   = s,
            which = which
        )


###
# prototype::
#     name  : the name of the attribut to update to a couple of two primitive
#             ¨python values
#     val   : one primitive ¨python value, or a couple a couple of
#             two primitive ¨python values
#     which : an integer code to indicate what have to be updated.
#             ``1`` is to just update the first separator.
#             ``2`` is to just update the second separator.
#             ``-1`` is to update the both separators.
#           @ which in {-1 , 1, 2}
#
#     :action: the attribut named ``name`` with a tuple value is updated
#              regarding the values of the arguments above.
###
    def __change_tuple_attr(
        self,
        name : str,
        val  : Any,
        which: int
    ) -> None:
        if which == 1:
            setattr(self, name, (val, getattr(self, name)[1]))

        elif which == 2:
            setattr(self, name, (getattr(self, name)[0], val))

        elif which == -1:
            setattr(self, name, val)

        else:
            raise ValueError(f"illegal use of << which = {which} >>")


###
# prototype::
#     x      : into the base ``self.bases[0]`` system, ``x`` can be either
#              an integer, or
#              a list of digits, or
#              a list of textual numerals
#     format : the formatted expected into the base ``self.bases[1]`` system
#            @ format in FORMAT_ALLOWED
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
        x     : Union[int, List[int], List[str]],
        format: str
    ) -> Union[int, List[int], List[str]]:
# Legal format?
        assert format in FORMAT_ALLOWED, f'invalid << format = {format} >>'

        assert format != FORMAT_INT or self.bases[1] == 10, \
               (
                f" format << {FORMAT_INT} >> used with "
                f"<< base_2 = {self.bases[1]} >> , use << base_2 = 10 >>"
               )

# Legal value?
        assert bool(x), f'invalid << x = {repr(x)} >>'

        if isinstance(x, list):
            if isinstance(x[0], int):
                fromkind = FORMAT_DIGITS
            else:
                fromkind = FORMAT_NUMERALS

        elif isinstance(x, int):
            assert self.bases[0] == 10, \
                   (
                    f" integer << {x} >> used with "
                    f"<< base_1 = {self.bases[0]} != 10 >>"
                   )

            fromkind = FORMAT_INT

        else:
            fromkind = FORMAT_BASE_NB

# Function to call.
        if self.bases[0] == 10 and fromkind == FORMAT_INT:
            prefix_1 = ''

        else:
            prefix_1 = 'b'

        if format == FORMAT_INT:
            prefix_2 = ''
            base     = self.bases[0]
            sep      = self.seps[0]

        else:
            prefix_2 = 'b'
            base     = self.bases[1]
            sep      = self.seps[1]

# A ready-to-use function?
        funcname = f'{prefix_1}{fromkind}2{prefix_2}{format}'

        if funcname in self.CONVERT_FUNCS:
            return self.__applyfunc(
                funcname,
                x,
                base,
                sep
            )

# We need to compose two functions.
        funcname_int2xxx = f'b{fromkind}2int'
        funcname_xxx2int = f'int2b{format}'

        val = self.__applyfunc(
            funcname_int2xxx,
            x,
            self.bases[0],
            self.seps[0]
        )

        return self.__applyfunc(
            funcname_xxx2int,
            val,
            self.bases[1],
            self.seps[1]
        )


###
# prototype::
#     funcname : the name of one function to apply
#              @ funcname in self.CONVERT_FUNCS
#     x        : an integer, or
#                a list of digits, or
#                a list of textual numerals
#     base     : the base to use
#              @ base > 1
#     sep      : the text used to separate numerals (if needed)
#
#     :return: the value returned by the function called.
###
    def __applyfunc(
        self,
        funcname: str,
        x       : Union[int, List[int], List[str]],
        base    : int,
        sep     : str
    ):
        func, hassep = self.CONVERT_FUNCS[funcname]

        if hassep:
            return func(x, base, sep)

        return func(x, base)

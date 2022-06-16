#!/usr/bin/env python3

###
# This module proposes one class to name integers in several languages.
###

from typing import *

from .automata import *


# --------------------- #
# -- NAMING INTEGERS -- #
# --------------------- #

###
# This class can name integers in different languages.
###
class IntName(BaseAutomata):
###
# prototype::
#     nb : an integer to name
#
#     :return: the name of ``nb`` in the language ``self.lang``
#
#     :see: self.name_big
###
    def nameof(self, nb: Union[str, int]) -> str:
# Name of the sign and absolute value of the integer in string format.
        sign, str_absnb = self.sign_n_abs(nb)

# Do big numbers are allowed?
        if (
            not self._very_big_allowed
            and
            len(str_absnb) > 2*self._small_big_max_expo
        ):
            raise ValueError(
                 "number too big to be named. "
                 "The maximal number of digits is "
                f"{2*self._small_big_max_expo}"
                 " < "
                f"{len(str_absnb)}."
            )

# Let's go!
        name = self.name_big(str_absnb)

# The "complete" name.
        if sign:
            name = f"{sign} {name}"

# Patch?
        for old, new in self._patch.items():
            name = name.replace(old, new)

# Nothing more to do.
        return name


###
# prototype::
#     nb : an integer to name
#        @ real(nb) in ¨Z
#
#     :return: the name of the sign, and just the string version of
#              the absolute value of ``nb``
###
    def sign_n_abs(self, nb: Union[str, int]) -> Tuple[str, str]:
# Normalization and sign of the number.
        sign = ""

        if isinstance(nb, int):
            if nb < 0:
                sign = "-"
                nb   = -nb

            nb = str(nb)

        elif isinstance(nb, str):
            if nb[0] in "-+":
                sign = nb[0]
                nb   = nb[1:]

            if not nb.isdigit():
                raise ValueError(
                    f'``{nb} = "{sign}{nb}"`` is not an integer'
                )

        else:
            raise ValueError(
                "``nb`` must be an integer or a string"
            )


# Name of the sign
        if sign:
            if self._sign_name[sign] is None:
                raise ValueError(
                    f"the sign ``{sign}`` can't be used "
                    f"with the language {self.lang}"
                )

            sign = self._sign_name[sign]

# Nothing more to do.
        return sign, nb


###
# prototype::
#     XXX :???
#
#     :return: ??
###
    def name_big(self, str_absnb, suffix = ''):
        D_VAR = str_absnb[:-self._small_big_max_expo]
        R_VAR = str_absnb[-self._small_big_max_expo:]

        print("BIG:", R_VAR, D_VAR, suffix)

        suffix = self.next_big_suffix(suffix)

        if D_VAR:
           self.name_big(D_VAR, suffix)




###
# prototype::
#     XXX :???
#
#     :return: ??
###
    def next_big_suffix(self, suffix):
        if suffix:
            suffix = suffix.replace('...', self._very_big_suffix)

        else:
            suffix = self._very_big_suffix


        return suffix




###
# prototype::
#     XXX :???
#
#     :return: ??
###
    def name_small_big(self, str_absnb):
        ...

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
# This class names integers in different languages.
###
class IntName(BaseAutomata):
###
# prototype::
#     nb : an integer to name
#        @ str(nb) in str(ZZ)
#
#     :return: the name of ``nb`` in the language ``self.lang``
#
#     :see: self.name_big ,
#           self.name_small_big ,
#           self.name_small_slice
###
    def nameof(self, nb: Union[str, int]) -> str:
# For error messages.
        self._initial_nb = nb

# Name of the sign, and the string version of the absolute value of the integer.
        sign, str_absnb = self.sign_n_abs(nb)

# Do big numbers are allowed?
        if (
            not self._very_big_allowed
            and
            len(str_absnb) > 2*self._small_big_expo_max
        ):
            raise ValueError(
                 "number too big to be named. The maximal number of digits is "
                f"{2*self._small_big_expo_max}"
                 " < "
                f"{len(str_absnb)}."
            )

# Let's go!
#
# warning::
#     Zero is a very special case (thinks about slice with zero value).
        if str_absnb == '0':
            name = self.name_small_slice(str_absnb)

        else:
            name = self.name_big(str_absnb)

# The "complete" name.
        if sign:
            name = f"{sign} {name}"

# Patches to apply?
        for old, new in self._patch.items():
            name = name.replace(old, new)

# Nothing left to do.
        return name


###
# prototype::
#     nb : an integer to name
#        @ str(nb) in str(ZZ)
#
#     :return: the name of the sign, and just the string version of
#              the absolute numerical value of ``nb``
#            @ abs(return[1]) = abs(real(nb))
###
    def sign_n_abs(self, nb: Union[str, int]) -> Tuple[str, str]:
# Normalization and sign of the number.
        sign = ""

        if isinstance(nb, int):
            if nb < 0:
                sign = "-"
                nb   = -nb

        elif isinstance(nb, str):
            if nb[0] in "-+":
                sign = nb[0]
                nb   = nb[1:]

            if not nb.isdigit():
                raise ValueError(
                    f'``nb = "{sign}{nb}"`` is not an integer'
                )

            nb = int(nb)

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
        return sign, str(nb)





###
# prototype::
#     very_bigslice : a positive integer that can be named whatever
#                     is its size
#                   @ very_bigslice in str(NN) - {0}
#     suffix        : a suffix to use fo very big integers (it is used
#                     and build for recursive calls)
#
#     :return: the name of ``very_bigslice`` in the language ``self.lang``
#
#     :see: self.name_small_big ,
#           self.name_small_slice
###
    def name_big(self, very_bigslice: str, suffix: str = '') -> None:
        D_VAR = very_bigslice[:-self._small_big_expo_max]
        R_VAR = very_bigslice[-self._small_big_expo_max:]

        if D_VAR:
            print("BIG:", R_VAR, ' Before:', D_VAR, f' >>> {suffix}' if suffix else '')
        else:
            print("BIG:", R_VAR)

        R_NAME = self.name_small_big(R_VAR)

        suffix = self.next_big_suffix(suffix)

        if D_VAR:
           D_NAME = self.name_big(D_VAR, suffix)


###
# prototype::
#     suffix : a suffix to use fo very big integers used for recursive calls
#
#     :return: the suffix for the next very big slice
###
    def next_big_suffix(self, suffix: str) -> str:
        if suffix:
            suffix = suffix.replace('...', self._very_big_suffix)

        else:
            suffix = self._very_big_suffix

        return suffix


###
# prototype::
#     bigslice : a positive integer that can be named using only the rules
#                for groups in the dictionnary ``INT_2_NAME[DSL_SPECS_GROUP]``
#              @ bigslice in str(NN)
#
#     :return: the name of ``bigslice`` in the language ``self.lang``
#
#     :see: self.name_small_slice,
#           INT_2_NAME
###
    def name_small_big(self, bigslice: str) -> str:
        i_right = 0

        for i_left in self._small_big_expos:
            smallslice = bigslice[i_right: i_left]
            i_right    = i_left

            if not smallslice:
                break

            if int(smallslice) != 0:
                print("SMALL BIG >", smallslice)#, ":", self.name_small_slice(smallslice))



###
# prototype::
#     smallslice : a positive integer that can be named using only the rules
#                  for small in the dictionnary ``INT_2_NAME[DSL_SPECS_SMALL]``
#                @ smallslice in str(NN)
#
#     :return: the name of ``smallslice`` in the language ``self.lang``
#
#     :see: INT_2_NAME
###
    def name_small_slice(self, smallslice: str) -> str:
# As it.
        if smallslice in self._small_asit:
            actions = self._small_asit[smallslice]

# Matching.
        else:
            actions = None

            for i, matchings in self._small_matching.items():
                nb_digits = len(smallslice)

                if i < nb_digits:
                    continue

                if i > nb_digits:
                    smallslice = '0'*(nb_digits - i) + smallslice

                for pattern, pattern_actions in matchings.items():
                    if pattern.search(smallslice):
                        actions = pattern_actions
                        break

                if not actions is None:
                    break

            if actions is None:
                raise Exception(
                       'BUG: no matching found.'
                    f'\n    + lang = {self.lang}'
                    f'\n    + nb   = {self._initial_nb}'
                     '\nReport the message above to the developper'
                )

# Let's work!
        return self.apply(smallslice, actions).strip()

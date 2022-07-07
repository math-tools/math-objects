#!/usr/bin/env python3

###
# This module proposes one class to name integers in several languages.
###

from typing import *

from re import findall

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
#     nb : an object having a string representation equal to an integer
#        @ str(nb) in str(ZZ)
#
#     :return: the name of ``nb`` in the language ``self.lang``
#
#     :see: self.name_big ,
#           self.name_small
###
    def nameof(self, nb: Any) -> str:
# For error messages.
        self._initial_nb = nb

# Name of the sign, and the string version of the absolute value of the integer.
        sign, str_absnb = self.sign_n_abs(nb)
        nb_digits       = len(str_absnb)

# Do big numbers are allowed?
        if (
            not self._very_big_allowed
            and
            nb_digits > self._small_big_max_len
        ):
            raise ValueError(
                 "number too big to be named. The maximal number of digits is "
                f"{self._small_big_max_len}  < {nb_digits}."
            )

# Let's go!
#
# warning::
#     Zero is a very special case (thinks about d_var with zero value).
        if str_absnb == '0':
            name = self.name_small(str_absnb)

        else:
            name = self.name_big(str_absnb)

# Suffixes for very big integers.
            if nb_digits > self._small_big_max_len:
                name = self.build_suffixes(name)

# TODO Remove the following ugly hack!
            name = name.replace('--', '-')

            while('  ' in name):
                name = name.replace('  ', ' ')

            name = name.strip()

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
#     nb : an object having a string representation equal to an integer
#        @ str(nb) in str(ZZ)
#
#     :return: the name of the sign,
#              and just the string version of the absolute numerical value
#              of ``nb``
#            @ let rnb = real(nb) ;
#              abs(return[1]) = abs(rnb) ;
#              return[0] = '-' if rnb < 0 ;
#              return[0] in ['', '+'] if rnb >= 0
###
    def sign_n_abs(self, nb: Any) -> Tuple[str, str]:
# String version of the object ``nb``.
        nb = str(nb)

# Remove spaces and decimal separators.
        for toremove in [' ', self._groups_sep]:
            nb = nb.replace(toremove, '')

# Normalization and sign of the number.
        if nb[0] in "-+":
            sign = nb[0]
            nb   = nb[1:]

        else:
            sign = ""

        nb = nb.strip()

        if not nb.isdigit():
            raise ValueError(
                f'``nb = "{sign}{nb}"`` is not an integer'
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
#     bigslice : a positive integer that can be named whatever is its size
#              @ bigslice in str(NN) - {0}
#
#     :return: the name of ``bigslice`` in the language ``self.lang`` **without
#              applying the suffixes for very big integers**
#
#     :see: self.name_small,
#           self.build_DnR_vars
###
    def name_big(self, bigslice: str,) -> str:

# The big slice is not zero.
        nbdigits = len(bigslice)

# A small number.
#
# warning::
#     We have to transform ``"005"`` into ``"5"``.
        if nbdigits <= self._small_big_min_len:
            bigslice = str(int(bigslice))

            return self.name_small(bigslice)

# The special variables ``d`` and ``r``.
        d_var, r_var, grppower = self.build_DnR_vars(bigslice)

# We must take care of "small" final groups that are equal to zero!
        # print(f"{d_var    = }")
        # print(f"{r_var    = }")
        # print(f"{grppower = }")

        if (
            grppower < self._small_big_expo_max
            and
            d_var == '0'
            and
            int(r_var) == 0
        ):
            return ''

# We have something to name.
        return self.apply(
            actions = self._small_big[grppower],
            d_var   = d_var,
            r_var   = r_var
        )


###
# prototype::
#     bigslice : a positive integer that can be named whatever is its size
#              @ bigslice in str(NN) - {0}
#
#     :return: the string representation of the special variable ``d``,
#              the string representation of the special variable ``r``
#              and the power of the group to be named
###
    def build_DnR_vars(self, bigslice: str,) -> Tuple[str, str, int]:
        bigslice  = str((bigslice))
        nb_digits = len(bigslice)

# A "real" big number?
        nb_digits_left = nb_digits % self._small_big_expo_max

        if nb_digits_left == 0:
            if nb_digits <= self._small_big_expo_max:
                d_var = bigslice
                r_var = ""

            else:
                d_var = bigslice[:self._small_big_expo_max]
                r_var = bigslice[self._small_big_expo_max:]

        else:
            d_var = bigslice[:nb_digits_left]
            r_var = bigslice[nb_digits_left:]

# A "small" big number?
        if r_var:
            grppower = self._small_big_expo_max

        else:
            grppower = 0

            for power in self._small_big:
                if power >= nb_digits:
                    break

                grppower = power

            d_var = bigslice[:-grppower]
            r_var = bigslice[-grppower:]

# We must always remove useless zero in ``d_var``.
#
# This is not true for ``r_var``. Think about 10*27 for example.
        d_var = str(int(d_var))

# Nothing left to do...
        return d_var, r_var, grppower


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
    def name_small(self, smallslice: str) -> str:
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
                       f'BUG: no matching found for ``{smallslice}``.'
                    f'\n    + lang     = {self.lang}'
                    f'\n    + nb       = {self._initial_nb}'
                    f'\n    + type(nb) = {type(self._initial_nb)}'
                     '\nReport the message above to the developper'
                )

# Let's work!
        return self.apply(
            actions = actions,
            d_var   = smallslice,
        )


###
# prototype::
#     name : the name built by ``self.name_big`` without applying the suffixes
#            for very big integers
#
#     :return: the name of a very big integer obtained by **applying the
#              suffixes for very big integers**
#
#     :see: self.name_big
###
    def build_suffixes(self, name: str) -> str:
# We must look for consecutive zeros for big groups that will not be in
# the final name.
#
# TODO Remove the following ugly strip!
        zerobigname = self.apply(
            actions = self._small_big[self._small_big_expo_max],
            d_var   = '0',
            r_var   = '0'*self._small_big_expo_max
        ).strip()

# Let's look for the groups that will stay in the name.
        grpnames = []
        end      = 0

        for _ in findall(zerobigname, name):
            start = name.index(zerobigname, end)

            grpnames += list(
                findall(
                    self._very_big_matching,
                    name[end: start]
                )
            )

            grpnames.append(zerobigname)

            end = start + len(zerobigname)

# The suffixes (we have to take care of the direction used).
        suffix   = ''
        suffixes = []

        for _ in range(len(grpnames)):
            if suffixes:
                if suffix:
                    suffix = suffix.replace('...', self._very_big_suffix)

                else:
                    suffix = self._very_big_suffix

            suffixes.append(suffix)

        if self._very_big_dir == DSL_DIR_L2R:
            suffixes.reverse()

# Let's apply the suffixes.
        newname = []
        end  = 0

        for i, onegrpname in enumerate(grpnames):
            start = name.index(onegrpname, end)

            newname.append(name[end: start])

            end = start + len(onegrpname)

            if onegrpname == zerobigname:
                continue

            suffix = suffixes[i]

            if suffix:
                onegrpname = suffix.replace('...', onegrpname)

            newname.append(onegrpname)

        newname.append(name[end:])

# Job finished. That's great!
        return ''.join(newname)

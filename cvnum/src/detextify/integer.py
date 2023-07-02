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
class IntName(BaseAutomaton):
###
# prototype::
#     :see: automata.BaseAutomata.__init__
###
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# TODO UGGLY: Remove the following ugly strip! It's a shame...
        if self._very_big_allowed:
            self._zerobigname = self.apply(
                actions = self._big_rules[self._big_expo_max],
                d_var   = '1',
                r_var   = '0'*self._big_expo_max
            ).strip()

            self._zerobigname = ' ' + self._zerobigname.replace(
                self.name_small('1'),
                self.name_small('0')
            )

        else:
            self._zerobigname = None

# ! -- DEBUGGING -- ! #
        # print(f"{self._very_big_allowed = }")
        # print(f"{self._zerobigname      = }")
        # exit()
# ! -- DEBUGGING -- ! #


###
# prototype::
#     nb : any object that is printable as a "legal" integer (spaces and separators
#          for digits can be used)
#
#     :return: the name of ``nb`` in the language ``self.lang``
#
#     :see: self.name_big ,
#           self.name_small
###
    def nameof(self, varnb: Any) -> str:
# For error messages.
        self._initial_nb = varnb

# Name of the sign, and the string version of the absolute value of the integer.
        _, sign, absnb = self.int_n_strsignabs(varnb = varnb)

# Can we use a sign?
        if sign:
            assert not self._sign_name[sign] is None, \
                (
                    f"the sign ``{sign}`` can't be used "
                    f"with the language {self.lang}"
                )

# Do big numbers are allowed?
        nb_digits = len(absnb)

        assert (
                self._very_big_allowed
                or
                nb_digits <= self._big_len_max
               ), (
                 "number too big to be named. "
                 "The maximal number of digits is "
                f"{self._big_len_max} < {nb_digits}."
               )

# Let's go!
#
# warning::
#     Zero is a very special case (we will work with ``d_var`` made of
#     several zero).
        if absnb == '0':
            name = self.name_small(absnb)

        else:
            name = self.name_big(absnb)

# Suffixes for very big integers.
# ! -- DEBUGGING -- ! #
            # print(">>> Before self.build_suffixes <<<")
            # print(f"{name = }")
# ! -- DEBUGGING -- ! #

            if nb_digits > self._big_len_max:
                name = self.build_suffixes(name)

# TODO UGGLY: Remove the following ugly hacks! It's a shame...
            name = name.replace('--', '-')

            while('  ' in name):
                name = name.replace('  ', ' ')

            name = name.strip()

# The "complete" name with a sign.
        if sign:
            name = self._sign_name[sign].replace(ELLIPSIS, name)

# Patches to apply?
        for old, new in self._patch.items():
            name = name.replace(old, new)

# Nothing left to do.
        return name


###
# prototype::
#     bigslice : an integer that can be named whatever is its size
#              @ bigslice in str(NN) - {"0"}
#
#     :return: the name of ``bigslice`` in the language ``self.lang``
#              **without applying the suffixes for very big integers**
#
#     :see: self.name_small,
#           self.build_DnR_vars
###
    def name_big(self, bigslice: str) -> str:
# ! -- DEBUGGING -- ! #
        # print()
        # print(">>> name_big <<<")
        # print(f"{bigslice = }")
        # print(f"{self._big_len_min = }")
# ! -- DEBUGGING -- ! #

# A small number.
#
# warning::
#     We have to transform ``"005"`` into ``"5"``.
        if len(bigslice) <= self._big_len_min:
            bigslice = str(int(bigslice))

            return self.name_small(bigslice)

# The special variables ``d`` and ``r``.
        d_var, r_var, grppower = self.build_DnR_vars(bigslice)

# We have something to name.
# ! -- DEBUGGING -- ! #
        # print("self.apply used")
# ! -- DEBUGGING -- ! #

# A null intermediate group.
#
# We must take care of a biggest null group.
        if d_var == '0':
            name = ''

            if grppower == self._big_expo_max:
                name += self._zerobigname

            name += self.name_big(r_var)

# A not null intermediate group.
        else:
            name = self.apply(
                actions = self._big_rules[grppower],
                d_var   = d_var,
                r_var   = r_var
            )

# For very by numbers, we must take care of "small" final groups
# that are equal to zero!
        if self._very_big_allowed:
# ! -- DEBUGGING -- ! #
            # print(f"{d_var    = }")
            # print(f"{r_var    = }")
            # print(f"{grppower = }")
# ! -- DEBUGGING -- ! #

            nb_r_digits = len(r_var)

            if (
                int(r_var) == 0
                and
                nb_r_digits >= self._big_expo_max
            ):
                name += self._zerobigname*(
                    nb_r_digits // self._big_expo_max - 1
                )

# Nothing left to do.
        return name


###
# prototype::
#     bigslice : :see: self.name_big
#
#     :return: the string representation of the special variable ``d``,
#              the string representation of the special variable ``r``
#              and the power of the group to be named (in this order)
###
    def build_DnR_vars(self, bigslice: str,) -> Tuple[str, str, int]:
        bigslice  = str((bigslice))
        nb_digits = len(bigslice)

# A "real" big number?
        nb_digits_left = nb_digits % self._big_expo_max

        if nb_digits_left == 0:
            if nb_digits <= self._big_expo_max:
                d_var = bigslice
                r_var = ""

            else:
                d_var = bigslice[:self._big_expo_max]
                r_var = bigslice[self._big_expo_max:]

        else:
            d_var = bigslice[:nb_digits_left]
            r_var = bigslice[nb_digits_left:]

# A "small" big number?
        if r_var:
            grppower = self._big_expo_max

        else:
            grppower = 0

            for power in self._big_rules:
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
#                  for small in the ¨dict ``INT_2_NAME[DSL_SPECS_SMALL]``
#                @ smallslice in str(NN);
#                  len(smallslice) <= self._big_len_min
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

            assert not actions is None, \
                   (
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
#     name : the name built by ``self.name_big`` using ``self._zerobigname``
#
#     :return: the name of a very big integer obtained by **applying the
#              suffixes for very big integers**
#
#     :see: self.name_big
###
    def build_suffixes(self, name: str) -> str:
# ! -- DEBUGGING -- ! #
        # print(">>> build_suffixes <<<")
        # print(f"{name = }")
# ! -- DEBUGGING -- ! #

# We must look for consecutive zeros for big groups that will not be in
# the final name.
# ! -- DEBUGGING -- ! #
        # print(f"{self._zerobigname = }")
# ! -- DEBUGGING -- ! #

# Let's look for the groups that will stay in the name.
        grpnames = []
        end      = 0

        for _ in findall(self._zerobigname, name):
            start = name.index(self._zerobigname, end)

            grpnames += list(
                findall(
                    self._very_big_matching,
                    name[end: start]
                )
            )

            grpnames.append(self._zerobigname)

            end = start + len(self._zerobigname)

        grpnames += list(
            findall(
                self._very_big_matching,
                name[end: ]
            )
        )

# ! -- DEBUGGING -- ! #
        # print(f"{grpnames = }")
# ! -- DEBUGGING -- ! #

# The suffixes (we have to take care of the direction used).
        suffix   = ''
        suffixes = []

        for _ in range(len(grpnames)):
            if suffixes:
                if suffix:
                    suffix = suffix.replace(ELLIPSIS, self._very_big_suffix)

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

            if onegrpname == self._zerobigname:
                continue

            suffix = suffixes[i]

            if suffix:
                onegrpname = suffix.replace(ELLIPSIS, onegrpname)

            newname.append(onegrpname)

        newname.append(name[end:])

# Job finished. That's great!
        return ''.join(newname)

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
#     :see: automata.BaseAutomata.name_small_big
###
    def name_big(
        self,
        very_bigslice: str,
        suffix       : str = ''
    ) -> None:
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
#     :see: automata.BaseAutomata.name_small_big
###
    def name_small_big(self, bigslice: str) -> str:
# We name the first "none zero" biggest group.
#
# The remaining digits will be managed recursively via ``self.nameit_group``
# that will call ``self.name_small_big``.
        nbdigits = len(bigslice)
        maxpower = 0

        for power in self._small_big_expos:
            if power > nbdigits:
                break

            maxpower = power

        power_pos = self._small_big_expos.index(maxpower)

        if power_pos == 0:
            d_var = bigslice
            r_var = ""

        else:
            prev_maxpower = self._small_big_expos[power_pos - 1]

            d_var = bigslice[-maxpower: -prev_maxpower]
            r_var = bigslice[-prev_maxpower:]

        if r_var:
            from pprint import pprint;pprint(self._small_big[prev_maxpower])
            return self.apply(
                actions = self._small_big[prev_maxpower],
                d_var   = d_var,
                r_var   = r_var
            )

        return self.name_small_slice(d_var)


###
# prototype::
#     :see: automata.BaseAutomata.name_small_slice
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
                       f'BUG: no matching found for ``{smallslice}``.'
                    f'\n    + lang     = {self.lang}'
                    f'\n    + nb       = {self._initial_nb}'
                    f'\n    + type(nb) = {type(self._initial_nb)}'
                     '\nReport the message above to the developper'
                )

# Let's work!
#
# TODO: remove strip when :space: will be available in the DSL.
        return self.apply(
            actions = actions,
            d_var   = smallslice,
        ).strip()

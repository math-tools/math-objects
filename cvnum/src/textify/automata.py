#!/usr/bin/env python3

from typing import *

from ..config.detextify import *


class IntNameAutomata:
###
# prototype::
#     lang : the language used to name integers
#          @ lang in ALL_LANGS
###
    def __init__(self, lang: str) -> None:
        self.lang = lang

        self._DIRECT_ACTIONS = {
            DSL_ACTION_EXTRACT_NUMBER_OF: self.extractnbof,
            DSL_ACTION_IF_ELSE          : self.ifelse,
            DSL_ACTION_NAME_IT          : self.namethis,
            DSL_ACTION_VERBATIM         : self.verbatim,
        }


###
# We have to verify the language wanted when it is setted and also to update
# internal variables used for one language.
###
    @property
    def lang(self) -> str:
        return self._lang

    @lang.setter
    def lang(self, lang: str) -> None:
        assert lang in ALL_LANGS

        self._lang = lang
        self.update_internals()

###
# prototype::
#     :action: update of the values of private attributes used to name integers.
###
    def update_internals(self) -> None:
        rulestouse = INT_2_NAME[self.lang]

# Signs
        self._sign_name = {
            '+': rulestouse[DSL_SPECS_SIGN][DSL_TAG_SIGN_PLUS],
            '-': rulestouse[DSL_SPECS_SIGN][DSL_TAG_SIGN_MINUS],
        }

# General
        self._gene_sep = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_SEP]
        self._gene_big = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG]

# Groups
        self._groups           = rulestouse[DSL_SPECS_GROUP]
        self._groups_slices    = list(self._groups)
        self._groups_nb_slices = len(self._groups_slices)

# Small
        self._small_asit = rulestouse[DSL_SPECS_SMALL][
            DSL_ACTION_ASIT
        ]

        self._small_matching = rulestouse[DSL_SPECS_SMALL][
            DSL_ACTION_MATCHING
        ]

# Patch
        self._patch = rulestouse[DSL_SPECS_PATCH]


###
# prototype::
#     strnb : the string decimal representation of a small natural integer
#             (small means a slice for one language)
#           @ strnb in str(NN)
#
#     :return: the name of the slice
###
    def nameofsmall(self, strnb: str) -> str:
# As it.
        if strnb in self._small_asit:
            actions = self._small_asit[strnb]

# Matching.
        else:
            actions     = None
            nb_digits = len(strnb)

            for i, matchings in self._small_matching.items():
                if i < nb_digits:
                    continue

                if i > nb_digits:
                    strnb = f'0{strnb}'

                for pattern, action in matchings.items():
                    if pattern.search(strnb):
                        actions = action
                        break

                if not actions is None:
                    break

            if actions is None:
                raise Exception(
                    'BUG: no matching found.\n'
                    f'    + lang = {self.lang}\n'
                    f'    + nb   = {self._nb}\n'
                    'Report the message above to the developper'
                )

# Let's work!
        return self.apply(strnb, actions).strip()


###
# prototype::
#     strnb   : the string decimal representation of a natural integer
#             @ strnb in str(NN)
#     actions : a list of actions to use to name ``strnb``
#
#     :return: the name of ``strnb``
###
    def apply(
        self,
        strnb  : str,
        actions: Any
    ) -> str:
        name = ""

        for code, subactions in actions:
# Direct action
            if code in self._DIRECT_ACTIONS:
                name += self._DIRECT_ACTIONS[code](
                    strnb,
                    subactions,
                )

#! -- BUG? -- !#
            else:
                raise Exception(
                    f'BUG: unsupported code for actions ``{code}``.'
                     '\n'
                     'Report the message above to the developper'
                )

        return name


###
# prototype::
#     strnb    : the string decimal representation of a natural integer
#                (not used here)
#     verbtext : just a text
#
#     :return: the value of ``verbtext``
###
    def verbatim(
        self,
        strnb   : str,
        verbtext: str
    ) -> str:
        return verbtext


###
# prototype::
#     strnb     : the string decimal representation of a natural integer
#               @ strnb in str(NN)
#     start_end : a couple of two integers ``(start, end)``
#
#     :return: the string representatin of the numbers obtain by extracting
#              consecutive digits ``strnb`` from the position ``start`` to
#              the position ``end``.
###
    def extractnbof(
        self,
        strnb    : str,
        start_end: Tuple[int, int]
    ) -> str:
        digits    = [d for d in strnb[::-1]]
        nb_digits = len(digits)

        start, end = start_end

        if start >= nb_digits:
            return '0'

        end = min(end + 1, nb_digits)

# We have to remove unuseful zero on the left.
        strnb = int("".join(digits[start: end]))
        strnb = str(strnb)

        return strnb


###
# prototype::
#     strnb     : the string decimal representation of a natural integer
#               @ strnb in str(NN)
#     actions   : a list of actions to construct the name of ``strnb``, or
#                 a new integer (cf. tests used to name slices)
#     justnewnb : ``True`` asks to returns a string decimal representation, but
#                 ``False`` asks to return a name.
#
#     :return: the name of natural slice, or the string decimal representation
#              of natural integer build using some actions
###
    def namethis(
        self,
        strnb    : str,
        actions  : Any,
        justnewnb: bool = False
    ) -> str:
        newnb = ''

        for code, subactions in actions:
            newnb += self._DIRECT_ACTIONS[code](
                strnb,
                subactions
            )

# We must remove unuseful zeros!
        newnb = str(int(newnb))

        if justnewnb:
            return newnb

        return self.nameofsmall(newnb)


###
# prototype::
#     strnb  : the string decimal representation of a natural integer
#            @ strnb in str(NN)
#     actions: the actions that define an ``if-else`` alternative
#
#     :return: the result of the ``if-else`` alternative
###
    def ifelse(
        self,
        strnb  : str,
        actions: Any
    ) -> str:
        totest, winactions, looseactions = actions

        if self.testok(strnb, totest):
            return self.apply(strnb, winactions)

        return self.apply(strnb, looseactions)


###
# prototype::
#     strnb  : the string decimal representation of a natural integer
#            @ strnb in str(NN)
#     actions: the actions that define an ``if-else`` alternative
#
#     :return: the result of the ``if-else`` alternative
###
    def testok(
        self,
        strnb : str,
        totest: Any
    ) -> bool:
        compopes, args = totest

        for i, onecompo in enumerate(compopes):
            a = int(
                self.namethis(
                    strnb,
                    args[i],
                    justnewnb = True
                )
            )

            b = int(
                self.namethis(
                    strnb,
                    args[i+1],
                    justnewnb = True
                )
            )

            if onecompo == DSL_COMPOPE_EQ:
                result = (a == b)

            elif onecompo == DSL_COMPOPE_NOT_EQ:
                result = (a != b)

            elif onecompo == DSL_COMPOPE_GREATER:
                result = (a > b)

            elif onecompo == DSL_COMPOPE_GREATER_EQ:
                result = (a >= b)

            elif onecompo == DSL_COMPOPE_LOWER:
                result = (a < b)

            elif onecompo == DSL_COMPOPE_LOWER_EQ:
                result = (a <= b)

# We want that all tests succed.
            if not result:
                return result

        return result

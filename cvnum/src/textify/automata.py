#!/usr/bin/env python3

from typing import *

from ..config.detextify import *


# ------------------------- #
# -- BASE AUTOMATA CLASS -- #
# ------------------------- #

###
# This class gives the common methods to apply automata rules.
###
class BaseAutomata:
# Special variables ``d`` and ``r``, the last one being used only for groups.
    D_VAR = 0
    R_VAR = 1

###
# prototype::
#     lang : the language used to name integers
#          @ lang in ALL_LANGS
###
    def __init__(self, lang: str = "en_GB") -> None:
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
        self._update_internals()


###
# prototype::
#     :action: update of the values of private attributes used to name integers.
###
    def _update_internals(self) -> None:
        rulestouse = INT_2_NAME[self.lang]

# Signs
        self._sign_name = {
            '+': rulestouse[DSL_SPECS_SIGN][DSL_TAG_SIGN_PLUS],
            '-': rulestouse[DSL_SPECS_SIGN][DSL_TAG_SIGN_MINUS],
        }

# General
        self._groups_sep = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_SEP]

        self._very_big_allowed   = bool(rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG])
        self._very_big_matching, \
        self._very_big_suffix    = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG]

# Groups
        self._small_big          = rulestouse[DSL_SPECS_GROUP]
        self._small_big_expo_max = max(self._small_big)
        self._small_big_expos    = list(self._small_big)

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
#     slice   : the string decimal representation of a natural integer
#             @ slice in str(NN)
#     actions : a list of actions to use to name ``slice``
#
#     :return: the name of ``slice``
###
    def apply(
        self,
        slice  : str,
        actions: Any,
        spevars: Dict[str, str]
    ) -> str:
        name = ""

        for code, subactions in actions:
# Direct action
            if code in self._DIRECT_ACTIONS:
                name += self._DIRECT_ACTIONS[code](
                    slice,
                    subactions,
                )

#! -- BUG? -- !#
            else:
                dsl_spevar_name = ''
                fixed_globals   = globals().copy()

                for varname, varcode in fixed_globals.items():
                    if (
                        varname.startswith('DSL_ACTION_')
                        and
                        varcode == code
                    ):
                        dsl_spevar_name = varname
                        break

                if dsl_spevar_name:
                    message = f'unsupported action: ``{message}``'

                else:
                    message = f'unknown code for actions: ``{code}``'

                raise Exception(
                    f'BUG: {message}.'
                    '\n'
                    'Report the message above to the developper'
                )

# The job has been done.
        return name


###
# prototype::
#     slice    : the string decimal representation of a natural integer
#                (not used here)
#     verbtext : just a text
#
#     :return: the value of ``verbtext``
###
    def verbatim(
        self,
        slice   : str,
        verbtext: str
    ) -> str:
        return verbtext


###
# prototype::
#     slice     : the string decimal representation of a natural integer
#               @ slice in str(NN)
#     start_end : a couple of two integers ``(start, end)``
#
#     :return: the string representatin of the numbers obtain by extracting
#              consecutive digits ``slice`` from the position ``start`` to
#              the position ``end``.
###
    def extractnbof(
        self,
        slice    : str,
        start_end: Tuple[int, int]
    ) -> str:
        digits    = [d for d in slice[::-1]]
        nb_digits = len(digits)

        start, end = start_end

        if start >= nb_digits:
            return '0'

        end = min(end + 1, nb_digits)

# We have to remove unuseful zero on the left.
        slice = int("".join(digits[start: end]))
        slice = str(slice)

        return slice


###
# prototype::
#     slice     : the string decimal representation of a natural integer
#               @ slice in str(NN)
#     actions   : a list of actions to construct the name of ``slice``,
#                 or a new integer (cf. tests used to name slices)
#     justnewnb : ``True`` asks to returns a string decimal representation, but
#                 ``False`` asks to return a name.
#
#     :return: the name of natural slice, or the string decimal representation
#              of natural integer build using some actions
###
    def namethis(
        self,
        slice    : str,
        actions  : Any,
        justnewnb: bool = False
    ) -> str:
        newnb = ''

        for code, subactions in actions:
            newnb += self._DIRECT_ACTIONS[code](
                slice,
                subactions
            )

# We must remove unuseful zeros!
        newnb = str(int(newnb))

        if justnewnb:
            return newnb

        return self.nameofsmall(newnb)


###
# prototype::
#     slice  : the string decimal representation of a natural integer
#            @ slice in str(NN)
#     actions: the actions that define an ``if-else`` alternative
#
#     :return: the result of the ``if-else`` alternative
###
    def ifelse(
        self,
        slice  : str,
        actions: Any
    ) -> str:
        totest, winactions, looseactions = actions

        if self.testok(slice, totest):
            return self.apply(slice, winactions)

        return self.apply(slice, looseactions)


###
# prototype::
#     slice  : the string decimal representation of a natural integer
#            @ slice in str(NN)
#     actions: the actions that define an ``if-else`` alternative
#
#     :return: the result of the ``if-else`` alternative
###
    def testok(
        self,
        slice : str,
        totest: Any
    ) -> bool:
        compopes, args = totest

        for i, onecompo in enumerate(compopes):
            a = int(
                self.namethis(
                    slice,
                    args[i],
                    justnewnb = True
                )
            )

            b = int(
                self.namethis(
                    slice,
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

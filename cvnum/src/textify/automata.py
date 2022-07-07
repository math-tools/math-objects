#!/usr/bin/env python3

from typing import *

from ..config.detextify import *


# ------------------------- #
# -- BASE AUTOMATA CLASS -- #
# ------------------------- #

### TODO  revoir tous les prototypes!!!
# This class gives the common methods to apply automata rules.
#
#
# note::
#     We prefer to implement the main logic of building names in a dedicated
#     class. This motivates the choice to propose this unimplemented method.
###
class BaseAutomata:
###
# prototype::
#     lang : the language used to name integers
#          @ lang in ALL_LANGS
###
    def __init__(self, lang: str = "en_GB") -> None:
        self.lang = lang

        self.ACTIONS_IMPLEMENTED = {
            DSL_ACTION_SPEVAR           : self.spevar,
            DSL_ACTION_EXTRACT_NUMBER_OF: self.extractnbof,
            DSL_ACTION_IF_ELSE          : self.ifelse,
            DSL_ACTION_NAME_IT          : self.nameit,
            DSL_ACTION_NAME_IT_GROUP    : self.nameit_group,
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

        self._very_big_dir = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_DIR]

        self._very_big_allowed = bool(
            rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG]
        )

        self._very_big_matching, \
        self._very_big_suffix    = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG]

# Groups
        self._small_big          = rulestouse[DSL_SPECS_GROUP]
        self._small_big_expo_max = max(self._small_big)
        self._small_big_max_len  = 2*self._small_big_expo_max
        self._small_big_min_len  = min(self._small_big)

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
#     :return: a text given fine ¨infos for debugging messages
###
    def _error_about(self) -> str:
        return (
            f'\n    + lang     = {self.lang}'
            f'\n    + nb       = {self._initial_nb}'
            f'\n    + type(nb) = {type(self._initial_nb)}'
             '\nReport the message above to the developper.'
        )


###
# prototype::
#     :return: a text given ¨infos for debugging messages about unknown
#              codes of action
###
    def _errorcode_message(self, code) -> str:
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
            message = f'unsupported action: ``{dsl_spevar_name}``'

        else:
            message = f'unknown code for actions: ``{code}``'

        raise Exception(
            f'BUG: {message}.' + self._error_about()
        )


###
# prototype::
#     d_var   : the string decimal representation of a natural integer
#             @ d_var in str(NN)
#     actions : a list of actions to use to name ``d_var``
#
#     :return: the name of ``d_var``
###
    def apply(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str = '',
    ) -> str:
        name = ""

        for code, subactions in actions:
# Direct action
            if code in self.ACTIONS_IMPLEMENTED:
                name += self.ACTIONS_IMPLEMENTED[code](
                    actions = subactions,
                    d_var   = d_var,
                    r_var   = r_var,
                )

#! -- BUG? -- !#
            else:
                self._errorcode_message(code)

# The job has been done.
        return name


###
# prototype::
#     d_var    : the string decimal representation of a natural integer
#                (not used here)
#     verbtext : just a text
#
#     :return: the value of ``verbtext``
###
    def verbatim(
        self,
        actions: str,
        d_var  : str,
        r_var  : str,
    ) -> str:
        return actions


    def spevar(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
    ) -> str:
        if actions == DSL_SPEVAR_NUMBER_OF:
            return d_var

        if actions == DSL_SPEVAR_REMAINING:
            return r_var

        raise Exception(
            f'BUG: unknown code ``{actions}`` for a special var.'
            +
            self._error_about()
        )

###
# prototype::
#     d_var     : the string decimal representation of a natural integer
#               @ d_var in str(NN)
#     start_end : a couple of two integers ``(start, end)``
#
#     :return: the string representatin of the numbers obtain by extracting
#              consecutive digits ``d_var`` from the position ``start`` to
#              the position ``end``.
###
    def extractnbof(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
    ) -> str:
        digits    = [d for d in d_var[::-1]]
        nb_digits = len(digits)

        start, end = actions

        if start >= nb_digits:
            return '0'

        end = min(end + 1, nb_digits)

# We have to remove unuseful zero on the left.
        d_var = int("".join(digits[start: end]))
        d_var = str(d_var)

        return d_var


###
# prototype::
#     d_var     : the string decimal representation of a natural integer
#               @ d_var in str(NN)
#     actions   : a list of actions to construct the name of ``d_var``,
#                 or a new integer (cf. tests used to name d_vars)
#     justnewnb : ``True`` asks to returns a string decimal representation, but
#                 ``False`` asks to return a name.
#
#     :return: the name of natural d_var, or the string decimal representation
#              of natural integer build using some actions
###
    def nameit_group(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
    ) -> str:
        _, var_to_name = actions[0]

        if var_to_name == DSL_SPEVAR_NUMBER_OF:
            return self.name_big(d_var)

        return self.name_big(r_var)


###
# prototype::
#     d_var     : the string decimal representation of a natural integer
#               @ d_var in str(NN)
#     actions   : a list of actions to construct the name of ``d_var``,
#                 or a new integer (cf. tests used to name d_vars)
#     justnewnb : ``True`` asks to returns a string decimal representation, but
#                 ``False`` asks to return a name.
#
#     :return: the name of natural d_var, or the string decimal representation
#              of natural integer build using some actions
###
    def nameit(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
        justnewnb: bool = False
    ) -> str:
        newnb = ''

        for code, subactions in actions:
            if not code in self.ACTIONS_IMPLEMENTED:
                self._errorcode_message(code)

            newnb += self.ACTIONS_IMPLEMENTED[code](
                actions = subactions,
                d_var   = d_var,
                r_var   = r_var,
            )

# We must remove unuseful zeros!
        newnb = str(int(newnb))

        if justnewnb:
            return newnb

        return self.name_small(newnb)


###
# prototype::
#     d_var  : the string decimal representation of a natural integer
#            @ d_var in str(NN)
#     actions: the actions that define an ``if-else`` alternative
#
#     :return: the result of the ``if-else`` alternative
###
    def ifelse(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
    ) -> str:
        totest, winactions, looseactions = actions

        if self.testok(
            actions = totest,
            d_var   = d_var,
            r_var   = r_var,
        ):
            return self.apply(
                actions = winactions,
                d_var   = d_var,
                r_var   = r_var,
            )

        return self.apply(
            actions = looseactions,
            d_var   = d_var,
            r_var   = r_var,
        )


###
# prototype::
#     d_var  : the string decimal representation of a natural integer
#            @ d_var in str(NN)
#     actions: the actions that define an ``if-else`` alternative
#
#     :return: the result of the ``if-else`` alternative
###
    def testok(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
    ) -> bool:
        compopes, args = actions

        for i, onecompo in enumerate(compopes):
            a = int(
                self.nameit(
                    actions = args[i],
                    d_var   = d_var,
                    r_var   = r_var,
                    justnewnb = True
                )
            )

            b = int(
                self.nameit(
                    actions = args[i+1],
                    d_var   = d_var,
                    r_var   = r_var,
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

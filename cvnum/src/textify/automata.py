#!/usr/bin/env python3

###
# This module defines a class which implements the automaton (but not
# the whole analyzer of numbers).
###


from typing import *

from ..config.textify import *

from ..core.var2int import Var2Int


# -------------------------- #
# -- BASE AUTOMATON CLASS -- #
# -------------------------- #

###
# This class defines the methods to apply the automaton's rules.
#
#
# note::
#     We prefer to implement the main logic of building names in a dedicated
#     class. This motivates the choice to propose an interface like class.
###
class BaseAutomaton:
###
# prototype::
#     lang : the language used to name integers
#          @ lang in ALL_LANGS
#
#     :action: this method builds the ¨dict ``self.ACTIONS_IMPLEMENTED``
#              that associates each ¨DSL tag to an effective method.
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
        assert lang in ALL_LANGS, \
               f"illegal lang ``{lang}``"

        self._lang = lang
        self._update_internals()


###
# prototype::
#     :action: update of the values of private attributes used to name
#              integers.
#
#     :see: self.var2int.Var2Int
###
    def _update_internals(self) -> None:
# Rules
        rulestouse = INT_2_NAME[self.lang]

# Patch
        self._patch = rulestouse[DSL_SPECS_PATCH]

# Signs
        self._sign_name = {
            '+': rulestouse[DSL_SPECS_SIGN][DSL_TAG_SIGN_PLUS],
            '-': rulestouse[DSL_SPECS_SIGN][DSL_TAG_SIGN_MINUS],
        }

# Small
        self._small_asit = rulestouse[DSL_SPECS_SMALL][
            DSL_ACTION_ASIT
        ]

        self._small_matching = rulestouse[DSL_SPECS_SMALL][
            DSL_ACTION_MATCHING
        ]

# Groups
        self._big_rules    = rulestouse[DSL_SPECS_GROUP]
        self._big_expo_max = max(self._big_rules)
        self._big_len_max  = 2*self._big_expo_max
        self._big_len_min  = min(self._big_rules)

# ! -- DEBUGGING -- ! #
        # print(f"{self._big_expo_max = }")
# ! -- DEBUGGING -- ! #

# Big groups
        self._groups_sep = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_SEP]

        if rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG] is None:
            self._very_big_allowed  = False
            self._very_big_dir      = None
            self._very_big_matching = None
            self._very_big_suffix   = None

        else:
            self._very_big_allowed = True

            self._very_big_dir = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_DIR]

            self._very_big_matching,   \
            self._very_big_suffix    = \
            rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG]

# Sign and absolute value
        self.int_n_strsignabs = Var2Int(
            tryconvert = True,
            toremove   = [' ', self._groups_sep]
        ).int_n_strsignabs


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
#     actions : a list of actions to use to name ``d_var``
#     d_var   : the string decimal representation of a natural integer
#               smallest than the biggest group
#             @ d_var in str(NN) ;
#               len(d_var) <= self._big_expo_max
#     r_var   : the string decimal representation of the remaining digits
#               of a group, or an empty string if such digits don't exist
#             @    r_var in str(NN)
#               or r_var = ''
#
#     :return: the name obtained by applying the actions of the list
#              ``actions`` by using the values of ``d_var`` and ``r_var``
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
#     actions : just a text
#     d_var   : :see: self.apply
#     r_var   : :see: self.apply
#
#     :return: the value of ``verbtext``
#
# note::
#     The variables ``d_var`` and ``r_var`` are useless here.
###
    def verbatim(
        self,
        actions: str,
        d_var  : str,
        r_var  : str,
    ) -> str:
        return actions


###
# prototype::
#     actions : a tag to select the good kind of special variable
#             @ actions in [DSL_SPEVAR_NUMBER_OF, DSL_SPEVAR_REMAINING]
#     d_var   : :see: self.apply
#     r_var   : the string decimal representation of the remaining digits
#               of a group (here the value can't be empty)
#             @ r_var in str(NN)
#     :return: the string value of either ``d_var``, or ``r_var``
#            @ if   actions == DSL_SPEVAR_NUMBER_OF
#              then return = d_var
#              else return = r_var
###
    def spevar(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
    ) -> str:
        if actions == DSL_SPEVAR_NUMBER_OF:
            return d_var

        return r_var


###
# prototype::
#     actions : a couple of integers ``(start, end)``
#             @ actions in [NN, NN]
#     d_var   : :see: self.apply
#     r_var   : :see: self.apply
#
#     :return: the string representatin of the numbers obtained by extracting
#              consecutive digits of ``d_var`` from the position ``start``
#              to the position ``end`` (the case of a too big end is managed).
#
# note::
#     The variable ``r_var`` is useless here.
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
#     actions : a couple of variables to indicate which "big" integers
#               bewtween ``d_var`` and ``r_var``  must be named
#             @ actions[0] = DSL_ACTION_SPEVAR ;
#               actions[1] in [DSL_SPEVAR_NUMBER_OF, DSL_SPEVAR_REMAINING]
#     d_var   : :see: self.apply
#     r_var   : the string decimal representation of the remaining digits
#               of a group (here the value can't be empty)
#             @ r_var in str(NN)
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
# ! -- DEBUGGING -- ! #
        # print(">>> nameit_group <<<")
        # print(f"{actions = }")
        # print(f"{d_var   = }")
        # print(f"{r_var   = }")
# ! -- DEBUGGING -- ! #

        _, var_to_name = actions[0]

        if var_to_name == DSL_SPEVAR_NUMBER_OF:
            return self.name_big(d_var)

# Do we have remaining none zero digits?
        if int(r_var) == 0:
            return ''

        return self.name_big(r_var)


###
# prototype::
#     actions   : :see: self.apply
#     d_var     : :see: self.apply
#     r_var     : :see: self.apply
#     justnewnb : ``True`` asks to returns a string decimal representation,
#                 whereas ``False`` is to obtain a name.
#
#     :return: the name of the natural ``d_var``, or its string decimal
#              representation
###
    def nameit(
        self,
        actions  : Any,
        d_var    : str,
        r_var    : str,
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
#     actions : the actions that define an ``if-else`` alternative
#     d_var   : :see: self.apply
#     r_var   : :see: self.apply
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
#     actions : the actions that define a boolean test to do
#     d_var   : :see: self.apply
#     r_var   : :see: self.apply
#
#     :return: the boolean result of the test
###
    def testok(
        self,
        actions: Any,
        d_var  : str,
        r_var  : str,
    ) -> bool:
        compopes, args = actions

# We work on AND tests on several comparison operators.
        for i, onecompo in enumerate(compopes):
# We need to have the integer values of the variables.
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

# We can do the test expected.
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

# We want that all tests succed. No need to do more job.
            if not result:
                return result

# All the tests have been passed.
        return True

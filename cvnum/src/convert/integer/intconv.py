#!/usr/bin/env python3

###
# This module proposes common tools for the classes playing with base
# conversions of integers.
###


from typing import *


# --------------- #
# -- CONSTANTS -- #
# --------------- #

###
# Some constants are used to manage the different kinds of signs.
###
MINUS_STR_SIGN = "-"
MINUS_INT_SIGN = -1

PLUS_STR_SIGN      = ""
PLUS_STR_SIGN_LONG = "+"
PLUS_INT_SIGN      = 1

STR_SIGNS = [
    MINUS_STR_SIGN,
    PLUS_STR_SIGN,
]

INT_SIGNS = [
    MINUS_INT_SIGN,
    PLUS_INT_SIGN,
]


###
# To avoid typos, some tags are given to work with the decorator ``deco_callof``.
###
DECO_TAG_N2B = 'nat2base'
DECO_TAG_B2N = 'base2nat'
DECO_TAG_B2B = 'base2base'

DECO_TAG_NB = 'nb'

DECO_TAG_BNB      = 'bnb'
DECO_TAG_BASE     = 'base'
DECO_TAG_BASE_IN  = 'base_in'
DECO_TAG_BASE_OUT = 'base_out'
DECO_TAG_SEP      = 'sep'
DECO_TAG_SEP_IN   = 'sep_in'
DECO_TAG_SEP_OUT  = 'sep_out'

DECO_TAG_NUMERALS = 'numerals'
DECO_TAG_DIGITS   = 'digits'

DECO_TAG_BNUMERALS = 'bnumerals'
DECO_TAG_BDIGITS   = 'bdigits'


# ------------------------------------ #
# -- DECORATOR FOR THE LAZZY CODERS -- #
# ------------------------------------ #

###
# prototype::
#     method_name : the name of a method (only used in case of problems)
#     params      : a list of names of parameters sorted as in the signature
#                   of the method
#     optional    : the list of optional parameters (the ones with a default
#                   value in the signature of the method)
#     args        : a list of values for parameters not named when calling
#                   the method (the traditional ``*args`` of ¨python)
#     kwargs      : a dictionary associated the name of a parameter to
#                   its values when calling the method (the traditional
#                   ``**kwargs`` of ¨python)
#
#     :return: the pointer to the object ``self`` of the method, and a full
#              ``kwargs`` argument ready-to-use
###
def self_n_kwargs(
    method_name: str,
    params     : List[str],
    optional   : List[str],
    args       : List[Any],
    kwargs     : Dict[str, Any],
) -> Tuple[Any, Dict[str, Any]]:
# Isolation of the ``self`` argument.
    self, *args = args

# We populate ``kwargs`` by using ``args``.
    _kwargs   = kwargs.copy()

    i_params  = -1
    nb_params = len(params)

    for i, val in enumerate(args):
        i_params += 1

        if params[i_params] in _kwargs:
            i_params += 1

        assert i_params < nb_params

        _kwargs[params[i_params]] = val

# Only optional parameters can miss!
    missing = set(params) - set(_kwargs) - optional

    assert missing == set(), \
           (
             f"Int2Base.{method_name}() needs "
            + ("one" if len (missing) == 1 else "some")
            + " mandatory parameter"
            + ("" if len(missing) == 1 else "s")
            + " that "
            + ("is" if len (missing) == 1 else "are")
            + " missing: "
            + ", ".join(sorted(list(missing)))
            + "."
           )

# Nothing looks bad... For the moment!
    return self, _kwargs


###
# prototype::
#     tocall   : the name of a sub-method to call such as to build the ouput
#                of the decorated method
#     params   : the list of the parameters of the method to decorate
#     optional : the list of the optional parameters of the method to decorate
#
#     :return: a decorated version of the method producing the expected value
###
def deco_callof(
    tocall  : str,
    params  : List[str],
    optional: List[str] = []
) -> Callable:
###
# prototype::
#     method :
#
#     :return:
###
    def _deco_callof_(method: Callable) -> Callable:
        method_name     = method.__name__
        nat_method_name = method_name.replace('int', 'nat')

###
# ????
###
        def method_wrapped(
            *args   : List[Any],
            **kwargs: Dict[str, Any]
        ) -> Any:
            self, params_found = self_n_kwargs(
                method_name = method_name,
                params      = params,
                optional    = set(optional),
                args        = args,
                kwargs      = kwargs,
            )

# Let's take care of of the initial sign.
            if DECO_TAG_NB in params_found:
                sign, params_found[DECO_TAG_NB] = self.intsign_n_abs_of(
                    params_found[DECO_TAG_NB]
                )

            elif DECO_TAG_BNB in params_found:
                sign, params_found[DECO_TAG_BNB] = self.strsign_n_abs_of(
                    params_found[DECO_TAG_BNB]
                )

            else:
                for tag in [
                    DECO_TAG_DIGITS,
                    DECO_TAG_NUMERALS,
                    DECO_TAG_BDIGITS,
                    DECO_TAG_BNUMERALS,
                ]:
                    if tag in params_found:
                        sign, *input_absnb = params_found[tag]
                        params_found[tag]  = input_absnb
                        break

# Let's work with a naturaL
            absreturn = self.__getattribute__(
                tocall
            ).__getattribute__(
                nat_method_name
            )(
                **params_found
            )

# Let the initial sign come back.
            if isinstance(absreturn, list):
                if isinstance(absreturn[0], str):
                    sign = self.strsign(sign)

                elif isinstance(sign, str):
                    sign = self.intsign(sign)

                absreturn.insert(0, sign)

            elif isinstance(absreturn, int):
                if sign in STR_SIGNS:
                    sign = self.intsign(sign)

                absreturn = sign * absreturn

            else:
                if not sign in STR_SIGNS:
                    sign = self.strsign(sign)

                absreturn = f"{sign}{absreturn}"

            return absreturn

# Our wrapped method is functional (at least, we hope it).
        return method_wrapped

# Our parametrized decorator can be used.
    return _deco_callof_


# ---------------- #
# -- BASE CLASS -- #
# ---------------- #

###
# This class is to be herited by the classes playing with base conversions
# of integers.
###
class IntConv:
###
# prototype::
#     errname : the name used in case of error message
###
    def __init__(
        self,
        errname : str = "number",
    ) -> None:
        self.errname = errname


###
# prototype::
#     nb : an integer
#        @ nb in ZZ
#
#     :return: the sign of ``nb`` coded by ``(-1)`` if nb > 0, and
#              ``1`` either, followed by the absolute value of ``nb``.
#            @ if   nb < 0
#              then return[0] = -1
#              else return[0] = 1 ;
#              return[1] = abs(nb)
#
#
# warning::
#     The type of the variable ``nb`` is not tested!
###
    def intsign_n_abs_of(self, nb: int) -> Tuple[int, int]:
        if nb < 0:
            sign = MINUS_INT_SIGN
            nb   = -nb

        else:
            sign = PLUS_INT_SIGN

        return sign, nb


###
# prototype::
#     bnb : a string number writing in any base that can start by the sign
#           ``-`` or ``+`` (this last one being optional to indicate a positive
#           base number)
#
#     :return: the sign of ``nb`` coded by ``"-"`` if nb > 0, and
#              an empty string either, followed by the string ``bnb`` not starting
#              by the sign found.
#            @ if   bnb[0] = "-"
#              then return[0] = "-" and return[1] = bnb[1:] ;
#              elif bnb[0] = "+"
#              then return[0] = "" and return[1] = bnb[1:] ;
#              else return[0] = "" and return[1] = bnb
#
#
# warning::
#     The validity of base number ``bnb`` is not tested!
###
    def strsign_n_abs_of(self, bnb: str) -> Tuple[str, str]:
# ``bnb`` is negative.
        if bnb[0] == MINUS_STR_SIGN:
            sign = MINUS_STR_SIGN
            bnb  = bnb[1:]

# ``bnb`` is non-negative.
        else:
            sign = PLUS_STR_SIGN

# ``bnb`` starts with a ``+``.
            if bnb[0] == PLUS_STR_SIGN:
                bnb  = bnb[1:]

        return sign, bnb


###
# prototype::
#     sign : a sign indicated via either a string, or an integer
#            (the conventions used by the package ``convert.integer``
#            must be respected).
#          @ sign in INT_SIGNS or sign in STR_SIGNS
#
#     :return: the string version of the sign
#            @ if   sign in ["-", -1]
#              then return = "-"
#              else return = ""
#
#     :see: self._XXXsign
###
    def strsign(self, sign: Union[int, str]) -> str:
        return self._XXXsign(
            sign          = sign,
            signs_wanted  = STR_SIGNS,
            minus_allowed = MINUS_INT_SIGN,
            minus_wanted  = MINUS_STR_SIGN,
            plus_allowed  = [PLUS_INT_SIGN],
            plus_wanted   = PLUS_STR_SIGN,
        )


###
# prototype::
#     sign : :see: self.strsign
#
#     :return: the integer version of the sign
#            @ if   sign in ["-", -1]
#              then return = -1
#              else return = 1
#
#     :see: _XXXsign
###
    def intsign(self, sign: Union[int, str]) -> int:
        return self._XXXsign(
            sign          = sign,
            signs_wanted  = INT_SIGNS,
            minus_allowed = MINUS_STR_SIGN,
            minus_wanted  = MINUS_INT_SIGN,
            plus_allowed  = [PLUS_STR_SIGN, PLUS_STR_SIGN_LONG],
            plus_wanted   = PLUS_INT_SIGN,
        )


###
# prototype::
#     sign          : a sign indicated via either a string, or an integer
#                   @ sign in signs_wanted
#     signs_wanted  : a list of the signs wanted to be used
#     minus_allowed : the minus version allowed to be used
#     minus_wanted  : the minus version wanted for the remaining operations
#     plus_allowed  : the list of plus versions allowed to be used (we need
#                     to use a list because a ``+`` sign can be omitted in
#                     the string representation of an integer)
#     plus_wanted   : the plus version wanted for the remaining operations
#
#     :return: the wanted version of the sign indicated via ``sign``
#            @ if   sign in [minus_allowed, minus_wanted]
#              then return = minus_wanted
#              else return = plus_wanted
#
#
# note::
#     This method factorizes the behavior of the methods ``self.strsign``
#     and ``self.intsign``.
###
    def _XXXsign(
        self,
        sign         : Union[int, str],
        signs_wanted : Union[List[int], List[str]],
        minus_allowed: Union[int, str],
        minus_wanted : Union[int, str],
        plus_allowed : Union[List[int], List[str]],
        plus_wanted  : Union[int, str],
    ) -> Union[int, str]:
        if sign in signs_wanted:
            return sign

        if sign == minus_allowed:
            return minus_wanted

        if sign in plus_allowed:
            return plus_wanted

        raise ValueError(f"invalid sign: {sign = }")

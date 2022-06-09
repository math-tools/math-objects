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
class IntName:
###
# prototype::
#     lang : the language used to name integers
#          @ lang in ALL_LANGS
###
    def __init__(self, lang: str) -> None:
        self.lang = lang

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
        self._groups_sep    = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_SEP]
        self._groups_big    = rulestouse[DSL_SPECS_GENE][DSL_TAG_GENE_BIG]
        self._groups_big_OK = bool(self._groups_big)

# Groups
        self._groups           = rulestouse[DSL_SPECS_GROUP]
        self._groups_slices    = list(self._groups)
        self._groups_max_power = self._groups_slices[-1]

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
#     nb : an integer to name
#        @ type(nb) = int ==> nb >= 0
#
#     :return: the name of ``nb`` in the language ``self.lang``
#
#     :see: self._build_reverse_slicesint,
#           self._build_name_from_slices
###
    def nameof(self, nb: Union[str, int]) -> str:
# Name of the sign and absolute value of the integer in string format.
        sign, absnb = self.sign_n_abs(nb)

# A little big or a real big number?
        if self._groups_big_OK:
# The naming will use a specilaized recursive method.
            name = self.name_very_big(absnb)

        else:
# We must have a little big number.
            if len(str(absnb)) > 2*self._groups_max_power:
                raise ValueError(
                     "number too big to be named ."
                     "The maximal number of digits is "
                    f"{2*self._groups_max_power}"
                     " < "
                    f"{len(str(absnb))}."
                )

            name = self.name_little_big(absnb)

# The "complete" name.
        if sign:
            name = f"{sign} {name}"

# Patch?
        for old, new in self._patch.items():
            name.replace(old, new)

# Nothing more to do.
        return name








###
# prototype::
#     nb : an integer to name
#        @ type(nb) = int ==> nb >= 0
#
#     :return: the name of the sign, and the absolute value of ``nb``
###
    def sign_n_abs(self, nb: Union[str, int]) -> Tuple[str, int]:
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
                    f'``{nb} = "{sign}{nb}"`` is not an integer'
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
        return sign, nb





###
# prototype::
#     ?? : ???
#
#     :return: ??
###
    def name_very_big(self, absnb):
        print("DU GROS")


###
# prototype::
#     ?? : ???
#
#     :return: ??
###
    def name_little_big(self, absnb):
        print("PAS DU GROS")

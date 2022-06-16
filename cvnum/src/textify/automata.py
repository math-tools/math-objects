#!/usr/bin/env python3

from typing import *

from ..config.detextify import *


# ------------------------------------------ #
# -- ???? -- #
# ------------------------------------------ #

###
# This class ????
###
class BaseAutomata:
###
# prototype::
#     lang : the language used to name integers
#          @ lang in ALL_LANGS
###
    def __init__(self, lang: str = "en_GB") -> None:
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
        self._small_big_slices   = list(self._small_big)
        self._small_big_max_expo = self._small_big_slices[-1]

# Small
        self._small_asit = rulestouse[DSL_SPECS_SMALL][
            DSL_ACTION_ASIT
        ]

        self._small_matching = rulestouse[DSL_SPECS_SMALL][
            DSL_ACTION_MATCHING
        ]

# Patch
        self._patch = rulestouse[DSL_SPECS_PATCH]

#!/usr/bin/env python3

from http.client import OK
from orpyste.data import RecuOrderedDict

from .parsers   import *
from .pythonify import *


# ---------------- #
# -- MAIN CLASS -- #
# ---------------- #

class Parser(BaseParser):
    def __init__(
        self,
        treedict,
        shortpathfile
    ):
        super().__init__(shortpathfile)

        self.treedict = treedict


    def stddict_patch(self, onevar):
        if isinstance(onevar, RecuOrderedDict):
            result = OrderedDict()

            for k, v in onevar.items():
                result[k] = self.stddict_patch(v)

            return result

        if isinstance(onevar, tuple):
            return onevar

        del onevar['sep']

        return onevar


    def build(self):
        infos    = self.stddict_patch(self.treedict)
        allrules = OrderedDict()

        for kind, rules in infos.items():
            if kind == DSL_SPECS_THIS:
                allrules[kind] = rules

            else:
                subparser = PARSERS[kind](
                    rules,
                    self.shortpathfile
                )
                subparser.build()

                allrules[kind] = subparser.specs

        if DSL_SPECS_SIGN not in allrules:
            allrules[DSL_SPECS_SIGN] = {
                DSL_TAG_SIGN_MINUS: None,
                DSL_TAG_SIGN_PLUS : None
            }

        return allrules

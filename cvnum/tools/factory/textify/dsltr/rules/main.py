#!/usr/bin/env python3

from .configpeuf import *

from .calctrans  import *
from .keymatch   import *


# -------------------------------- #
# -- PARSER FOR ``GROUP`` BLOCK -- #
# -------------------------------- #

class BaseParserRules(BaseParser):
    def __init__(
        self,
        rules,
        shortpathfile
    ):
        super().__init__(shortpathfile)

        self.rules = rules
        self.specs = OrderedDict()


# -- LINE BY LINE -- #
    def extractlinebyline(self):
        for key, onerule in self.rules.items():
            self.nbline = onerule[TAG_NBLINE]

            yield key, onerule[TAG_VALUE]


# -- LEGAL INTEGER -- #
    def build_int(
        self,
        onevar,
        error_message,
    ):
        if not onevar.isdigit():
            self.stopall(error_message)

        onevar = int(onevar)

        if onevar < 0:
            self.stopall(error_message)

        return onevar


# -- BUILD IGNORE SPECS -- #
    def build_ignore(self, keys_specs):
        self.specs = []

# Keys are just integers ( cf. groups).
        if TYPE_INT in keys_specs:
            keymapper = self.build_int
            keykind   = "an integer"

# Keys are DSL rules (cf. small).
        elif TYPE_DSL in keys_specs:
            keymapper = self.build_onedslkey
            keykind   = "a good DSL rule"

# Unsupported feature.
        else:
            self.shortpathfile = "tools/factory/de-textify/dsl/config.py"
            self.nbline        = 0

            self.stopall(
                f"BUG - illegal internal specs:"
                 "\n"
               f"{keys_specs}"
            )

# Let's work!
        for key in self.rules:
            self.nbline = key[TAG_NBLINE]
            key         = key[TAG_VALUE]

            if key:
                key = keymapper(
                    key,
                    f"the key  << {key} >> is not {keykind}."
                )

                self.specs.append(key)


# -- BUILD "STANDARD" RULES FOR KEY/VAL -- #
    def build_keyvals(self, keys_specs):
        self.specs = OrderedDict()

# Keys are just integers (cf. groups).
        if TYPE_INT in keys_specs:
            self.size_1_keys_specs(
                keys_specs,
                "only one integer key spec allowed"
            )

            self.buildfor_intkeys(keys_specs)

# Keys are DSL rules (cf. small).
        elif TYPE_DSL in keys_specs:
            if len(keys_specs) != 1:
                self.size_1_keys_specs(
                    keys_specs,
                    "only one DSL key spec allowed"
                )

            self.buildfor_dslkeys(keys_specs)

# Fixed keys.
        else:
            self.buildfor_fixedkeys(keys_specs)


# -- SIZE 1 FOR KEYS SPECS -- #
    def size_1_keys_specs(
        self,
        keys_specs,
        error_message
    ):
        if len(keys_specs) != 1:
            self.nbline        = 0
            self.shortpathfile = (
                "tools/factory/de-textify/dsl/rules/configpeuf.py"
            )

            self.stopall(
                f"BUG - illegal internal specs ({error_message}):"
                 "\n"
               f"{keys_specs}"
            )


# -- LEGAL KEY? -- #
    def iskeylegal(
        self,
        key,
        keys_allowed,
        error_message,
    ):
        if not key in keys_allowed:
            self.stopall(error_message)


# -- BUILD "STANDARD" RULES FOR KEY/VAL - FIXED KEYS -- #
    def buildfor_fixedkeys(self, keys_specs):
        for key, onerule in self.extractlinebyline():
# Legal key?
            self.iskeylegal(
                key,
                keys_specs,
                f"unknown key << {key} >>.",
            )

# Do we have what we want?
            type_val, about_val = keys_specs[key]

# Good type for the value.
            if type_val == TYPE_INT:
                onerule = self.build_int(
                    onerule,
                    f"illegal value << {onerule} >> for the key << {key} >>. ",
                )

            elif type_val == TYPE_YES_NO:
                if onerule not in YES_NO:
                    self.stopall(
                        f"illegal {TYPE_YES_NO} value << {onerule} >> "
                        f"for the key << {key} >>. "
                    )

                onerule = bool(onerule == YES)

# No problem found.
            self.specs[key] = onerule

# Add missing keys.
        for key in keys_specs:
            if key in self.specs:
                continue

            type_val, about_val = keys_specs[key]

            if about_val == TAG_MANDATORY:
                self.stopall(
                    f"missing {TAG_MANDATORY} key << {key} >>. "
                )

            self.specs[key] = about_val


# -- BUILD "STANDARD" RULES FOR KEY/VAL - INT KEYS -- #
    def buildfor_intkeys(self, keys_specs):
        self.buildfor_spekeys(
            self.build_int,
            "an integer",
            forgroup = True
        )


# -- BUILD "STANDARD" RULES FOR KEY/VAL - DSL KEYS -- #
    def buildfor_dslkeys(self, keys_specs):
        self.buildfor_spekeys(
            self.build_onedslkey,
            "a good DSL rule",
            forgroup = False
        )


# -- BUILD "SPE" RULES - DSL KEYS -- #
    def buildfor_spekeys(
        self,
        keymapper,
        keykind,
        forgroup
    ):
        for key, onerule in self.extractlinebyline():
# DSL key?
            key = keymapper(
                key,
                f"the key  << {key} >> is not {keykind}."
            )

# Building rules.
#
# We have to take care the use of ``... => ...`` for groups.
            if forgroup and onerule[0] == TAG_SHORTCUT_FOR_D_R:
                onerule = onerule[1:].lstrip()
                onerule = f"[{DSL_SPEVAR_NUMBER_OF}] {onerule} [{DSL_SPEVAR_REMAINING}]"

            self.specs[key] = self.build_onedslval(
                onerule,
                f"illegal rules for the value of the key << {key} >> :"
                 "\n"
                f"{onerule}"
            )


# -- "STANDARD" RULES FOR KEY/VAL - "PARSING INTEGERS" -- #
    def build_onedslkey(
        self,
        onerule,
        error_message,
    ):
# Empty key are not allowed.
        if not onerule:
            self.stopall(
                "key can't be empty."
            )

# Let's analyze!
        try:
            ismatching, onerule = matchpatt(onerule)

        except Exception as e:
            self.stopall(
                f"{error_message}"
                 "\n\n"
                f"Exception raised by matchpatt: {e}"
            )

        context = DSL_ACTION_MATCHING if ismatching else DSL_ACTION_ASIT

        return (context, onerule)


# -- "STANDARD" RULES FOR KEY/VAL - "TEXTIFY" -- #
    def build_onedslval(
        self,
        onerule,
        error_message,
    ):
# Empty values are allowed (cf. Shadok's numbers and co).
        if not onerule:
            return onerule

# Let's build the rules for our automaton!
        try:
            automaton_rules = calctrans(onerule)

        except Exception as e:
            self.stopall(
                f"{error_message}"
                 "\n\n"
                f"Exception raised by calctrans: {e}"
            )

        return automaton_rules

#!/usr/bin/env python3

from .rules import *


# ---------------- #
# -- ``EXTEND`` -- #
# ---------------- #

class ParserExtend(BaseParserRules):
    def build(self):
        super().build_keyvals(KEYS_EXTEND)

# ! -- DEBUGGING -- ! #
        # print('--- EXTEND ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


# ----------------- #
# -- ``GENERAL`` -- #
# ----------------- #

class ParserGene(BaseParserRules):
    def build(self):
        super().build_keyvals(KEYS_GENE)

# Preparing regex rules for very big names.
        if self.specs[DSL_TAG_GENE_BIG]:
            bigname, sep, verybigname = self.specs[
                DSL_TAG_GENE_BIG
            ].partition(REPLACE_WITH)

            if not sep:
                raise Exception(
                    f"missing ``{REPLACE_WITH}`` in the value of ``big`` "
                     "(see the block ``gene``)."
                )

            bigname     = bigname.strip()
            verybigname = verybigname.strip()

            if not bigname or not verybigname:
                raise Exception(
                    f"empty string can't be used in ``... {REPLACE_WITH} ...`` "
                     "(see the key ``big`` of the block ``gene``)."
                )

            bigname = bigname.replace(ELLIPSIS, '\S+')
            bigname = f"(?P<bname>{bigname})"

            self.specs[DSL_TAG_GENE_BIG] = {bigname: verybigname}

# ! -- DEBUGGING -- ! #
        # print('--- GENE ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


# --------------- #
# -- ``GROUP`` -- #
# --------------- #

class ParserGroup(BaseParserRules):
    def build(self):
        super().build_keyvals(KEYS_GROUP)

# ! -- DEBUGGING -- ! #
        # print('--- GROUP ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


# ---------------------- #
# -- ``IGNORE GROUP`` -- #
# ---------------------- #

class ParserIgnoreGroup(BaseParserRules):
    def build(self):
        super().build_ignore(KEYS_IGNORE_GROUP)

# ! -- DEBUGGING -- ! #
        # print('--- IGNORE GROUP ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


# ---------------------- #
# -- ``IGNORE SMALL`` -- #
# ---------------------- #

class ParserIgnoreSmall(BaseParserRules):
    def build(self):
        super().build_ignore(KEYS_IGNORE_SMALL)

# ! -- DEBUGGING -- ! #
        # print('--- IGNORE SMALL ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


# --------------- #
# -- ``PATCH`` -- #
# --------------- #

class ParserPatch(BaseParserRules):
    def build(self):
# Just texts to find and replace...
        self.specs = {
            f: r
            for f, r in self.extractlinebyline()
        }

# ! -- DEBUGGING -- ! #
        # print('--- PATCH ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


# -------------- #
# -- ``SIGN`` -- #
# -------------- #

class ParserSign(BaseParserRules):
    def build(self):
        super().build_keyvals(KEYS_SIGN)

# ! -- DEBUGGING -- ! #
        # print('--- SIGN ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


# --------------- #
# -- ``SMALL`` -- #
# --------------- #

class ParserSmall(BaseParserRules):
    def build(self):
        super().build_keyvals(KEYS_SMALL)

# The special variable ``r`` is not allowed!
        self.__no_spevar_r()

# ! -- DEBUGGING -- ! #
        # print('--- SMALL ---')
        # from pprint import pprint
        # pprint(self.specs)
        # exit()
# ! -- DEBUGGING -- ! #


    def __no_spevar_r(self):
        for matching, actions in self.specs.items():
            dsl_expanded_matching = matching[1]
            dsl_expanded_matching = dsl_expanded_matching.replace('.', '*')

            self.__recu_no_spevar_r(
                actions,
                 "the (expanded matching) key rule "
                f"<< {dsl_expanded_matching} >>."
            )


    def __recu_no_spevar_r(
        self,
        actions,
        error_message
    ):
        # print("__recu_no_spevar_r", actions)
        for (kind, subactions) in actions:
            if kind in [
                DSL_ACTION_VERBATIM,
                DSL_ACTION_EXTRACT_NUMBER_OF,
            ]:
                continue

            if kind == DSL_ACTION_EXTRACT_REMAIN:
                raise Exception(
                    f"illegal use of << {kind} >>. See {error_message}."
                )

            if (kind, subactions) == (DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING):
                raise Exception(
                    f"illegal use of << r >>. See {error_message}."
                )

            if kind == DSL_ACTION_IF_ELSE:
                (_, lbr_actions), winrules, looserules = subactions

# We can't use ``lbr_actions += [winrules, looserules]`` because
# ``lbr_actions`` is one ref variable!
                for lbr_win_loose in list(lbr_actions) + [winrules, looserules]:
                    self.__recu_no_spevar_r(
                        lbr_win_loose,
                        f'{error_message} inside a "... :if: ... :else: ..."'
                    )

            elif kind == DSL_ACTION_NAME_IT:
                self.__recu_no_spevar_r(
                    subactions,
                    error_message
                )

            else:
                self.__recu_no_spevar_r(
                    subactions,
                    error_message
                )


# ----------------- #
# -- ALL PARSERS -- #
# ----------------- #

PARSERS = {
    DSL_SPECS_EXTEND      : ParserExtend,
    DSL_SPECS_GENE        : ParserGene,
    DSL_SPECS_GROUP       : ParserGroup,
    DSL_SPECS_IGNORE_GROUP: ParserIgnoreGroup,
    DSL_SPECS_IGNORE_SMALL: ParserIgnoreSmall,
    DSL_SPECS_PATCH       : ParserPatch,
    DSL_SPECS_SIGN        : ParserSign,
    DSL_SPECS_SMALL       : ParserSmall,
}

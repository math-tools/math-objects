#!/usr/bin/env python3

from ..rules import *

# ! -- DEBUGGING -- ! #
# from pprint import pprint
# ! -- DEBUGGING -- ! #


# -------------------- #
# --  EXTENDED LANG -- #
# -------------------- #

_KINDS_TO_KEEP = set(DSL_ALL_FINAL_SPECS) - set([
    DSL_SPECS_EXTEND,
    DSL_SPECS_IGNORE_GROUP,
    DSL_SPECS_IGNORE_SMALL,
])

_REMAINING_KINDS_TO_KEEP = _KINDS_TO_KEEP - set([
    DSL_SPECS_GROUP,
    DSL_SPECS_SMALL,
])


def manage_extend(alltrans):
    pyspecs_alltrans = {}

    for lang, specs in alltrans.items():
        pyspecs_onelang = {}

# Illegal use of IGNORE blocks.
        if (
            not DSL_SPECS_EXTEND in specs
            and
            (
                DSL_SPECS_IGNORE_GROUP in specs
                or
                DSL_SPECS_IGNORE_SMALL in specs
            )
        ):
            raise Exception(
                 'use of an "ignore block" without using '
                f'the "extend block". See the translation "{lang}".'
            )

# Not an extension.
        if not DSL_SPECS_EXTEND in specs:
            for kind in _KINDS_TO_KEEP:
                pyspecs_onelang[kind] = specs.get(kind, {})

# An extension.
        else:
            ignored_keys = {
                DSL_SPECS_GROUP: specs.get(DSL_SPECS_IGNORE_GROUP, []),
                DSL_SPECS_SMALL: specs.get(DSL_SPECS_IGNORE_SMALL, []),
            }

            lang_ext = specs[DSL_SPECS_EXTEND][DSL_TAG_LANG]

            for kind in [DSL_SPECS_GROUP, DSL_SPECS_SMALL]:
                ignoreme = ignored_keys[kind]
                all_rules = OrderedDict()

# We copy the rules wuanted from the initial lang.
                for k, v in alltrans[lang_ext][kind].items():
                    if k in ignoreme:
                        continue

                    all_rules[k] = v

# We add the rules for the extended lang.
                for k, v in specs.get(kind, {}).items():
                    all_rules[k] = v

# We store all the rules.
                pyspecs_onelang[kind] = all_rules

# Let's copy block from the initial lang.
            for kind in _REMAINING_KINDS_TO_KEEP:
                pyspecs_onelang[kind] = alltrans[lang_ext].get(kind, {})

# Take care of changes in the block ``general``.
            for k, v in alltrans[lang].get(DSL_SPECS_GENE, {}).items():
                pyspecs_onelang[DSL_SPECS_GENE][k] = v

# Nothing more to do.
        pyspecs_alltrans[lang] = pyspecs_onelang

# Job hase been done.
    return pyspecs_alltrans

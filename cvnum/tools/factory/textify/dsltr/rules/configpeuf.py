#!/usr/bin/env python3

from collections import OrderedDict


# ---------------- #
# -- PEUF FILES -- #
# ---------------- #

TAG_USECASES = "usecases"

TAG_NBLINE = 'nbline'
TAG_VALUE  = 'value'

ELLIPSIS     = "..."
REPLACE_WITH = "->"

NO     = "no"
YES    = "yes"
YES_NO = [YES, NO]

TAG_MANDATORY = "mandatory"

TYPE_DSL    = "DSL rules"
TYPE_INT    = "integer"
TYPE_STR    = "string"
TYPE_YES_NO = "yes/no"


DSL_SPECS_THIS = "this"


DSL_SPECS_EXTEND = "extend"
DSL_TAG_LANG     = "lang"
KEYS_EXTEND      = {
    DSL_TAG_LANG: (TYPE_STR, TAG_MANDATORY),
}


DSL_DIR_L2R = "l2r"
DSL_DIR_R2L = "r2l"

DSL_SPECS_GENE    = "general"
DSL_TAG_GENE_BIG  = "big"
DSL_TAG_GENE_DIR  = "dir"
DSL_TAG_GENE_SEP  = "sep"
KEYS_GENE         = {
    DSL_TAG_GENE_BIG: (TYPE_STR, ''),
    DSL_TAG_GENE_DIR: (TYPE_STR, ''),
    DSL_TAG_GENE_SEP: (TYPE_STR, ''),
}


DSL_SPECS_GROUP = "group"
KEYS_GROUP      = {
    TYPE_INT: (TYPE_DSL, ''),
}


DSL_SPECS_IGNORE_GROUP = "ignore-group"
KEYS_IGNORE_GROUP      = KEYS_GROUP


DSL_SPECS_PATCH = "patch"
KEYS_PATCH      = {
    TYPE_DSL: (TYPE_DSL, ''),
}

DSL_SPECS_SIGN     = "sign"
DSL_TAG_SIGN_PLUS  = "+"
DSL_TAG_SIGN_MINUS = "-"
KEYS_SIGN          = {
    DSL_TAG_SIGN_PLUS : (TYPE_STR, TAG_MANDATORY),
    DSL_TAG_SIGN_MINUS: (TYPE_STR, TAG_MANDATORY),
}


DSL_SPECS_SMALL = "small"
KEYS_SMALL      = {
    TYPE_DSL: (TYPE_DSL, ''),
}


DSL_SPECS_IGNORE_SMALL = "ignore-small"
KEYS_IGNORE_SMALL      = KEYS_SMALL


DSL_ALL_FINAL_SPECS = [
    DSL_SPECS_GENE,
    DSL_SPECS_GROUP,
    DSL_SPECS_PATCH,
    DSL_SPECS_SMALL,
    DSL_SPECS_SIGN,
]


MODE_TRANS = {
    "keyval:: =": [
        DSL_SPECS_EXTEND,
        DSL_SPECS_GENE, DSL_SPECS_GROUP,
        DSL_SPECS_PATCH,
        DSL_SPECS_SIGN, DSL_SPECS_SMALL,
        DSL_SPECS_THIS,
    ],
    "verbatim": [
        DSL_SPECS_IGNORE_SMALL,
        DSL_SPECS_IGNORE_GROUP,
    ]
}


# ---------------- #
# -- BASE CLASS -- #
# ---------------- #

class BaseParser:
    def __init__(
        self,
        shortpathfile
    ):
        self.shortpathfile = shortpathfile

# -- STOP THE PROCESS -- #
    def stopall(
        self,
        error_message,
    ):
        stopall(
            error_message,
            self.shortpathfile,
            nbline = self.nbline
        )

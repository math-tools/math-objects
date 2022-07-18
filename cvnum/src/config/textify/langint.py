#!/usr/bin/env python3

# -------------------------------------------------------------------------- #
# --  This code was automatically build by the following file.            -- #
# --                                                                      -- #
# --      + ``tools/factory/textify/build_01_int2txt_automaton_rules.py`` -- #
# -------------------------------------------------------------------------- #

from collections import OrderedDict
from re          import compile as __re_compile


# -------------------------------------------- #
# -- JUST AN ELLIPSIS BEFORE A SERIOUS TALK -- #
# -------------------------------------------- #

ELLIPSIS = "..."


# -------------------- #
# -- TAGS FOR LANGS -- #
# -------------------- #

# Names of integers in academic German.
de_DE = "de_DE"

# Names of integers in academic British English.
en_GB = "en_GB"

# Names of integers in academic American English.
en_US = "en_US"

# Names of integers in academic Spanish.
es_ES = "es_ES"

# Names of integers in academic Belgian.
fr_BE = "fr_BE"

# Names of integers in academic French.
fr_FR = "fr_FR"

# Names of very large integers in French using the short Chuquet's rules
# (without using "milliard").
fr_FR_chuquet_1 = "fr_FR_chuquet_1"

# Names of very large integers in French using the full Chuquet's rules
# (using "milliard").
fr_FR_chuquet_2 = "fr_FR_chuquet_2"

# Names of very large integers in French using the Rowlett's rules.
fr_FR_rowlett = "fr_FR_rowlett"

# Names of integers in academic French using the "hyphens everywhere"
# convention.
fr_FR_tiret = "fr_FR_tiret"

# Names of integers in academic Italian.
it_IT = "it_IT"


# ---------------- #
# -- DIRECTIONS -- #
# ---------------- #

DSL_DIR_L2R = "l2r"
DSL_DIR_R2L = "r2l"


# ------------ #
# -- ACTION -- #
# ------------ #

DSL_ACTION_ASIT              = 0  # --> 'asit'
DSL_ACTION_EXTRACT_NUMBER_OF = 1  # --> 'd(m..n)'
DSL_ACTION_IF_ELSE           = 2  # --> 'if-else'
DSL_ACTION_MATCHING          = 3  # --> 'matching'
DSL_ACTION_NAME_IT           = 4  # --> 'name-it'
DSL_ACTION_NAME_IT_GROUP     = 5  # --> 'name-it-group'
DSL_ACTION_SPEVAR            = 6  # --> 'special-var'
DSL_ACTION_VERBATIM          = 7  # --> 'verbatim'


# ------------- #
# -- COMPOPE -- #
# ------------- #

DSL_COMPOPE_EQ         = 8   # --> '='
DSL_COMPOPE_GREATER    = 9   # --> '>'
DSL_COMPOPE_GREATER_EQ = 10  # --> '>='
DSL_COMPOPE_LOWER      = 11  # --> '<'
DSL_COMPOPE_LOWER_EQ   = 12  # --> '<='
DSL_COMPOPE_NOT_EQ     = 13  # --> '!='


# ----------- #
# -- SPECS -- #
# ----------- #

DSL_SPECS_GENE  = 14  # --> 'general'
DSL_SPECS_GROUP = 15  # --> 'group'
DSL_SPECS_PATCH = 16  # --> 'patch'
DSL_SPECS_SIGN  = 17  # --> 'sign'
DSL_SPECS_SMALL = 18  # --> 'small'


# ------------ #
# -- SPEVAR -- #
# ------------ #

DSL_SPEVAR_NUMBER_OF = 19  # --> 'd'
DSL_SPEVAR_REMAINING = 20  # --> 'r'


# --------- #
# -- TAG -- #
# --------- #

DSL_TAG_GENE_BIG   = 21  # --> 'big'
DSL_TAG_GENE_DIR   = 22  # --> 'dir'
DSL_TAG_GENE_SEP   = 23  # --> 'sep'

DSL_TAG_SIGN_MINUS = 24  # --> '-'
DSL_TAG_SIGN_PLUS  = 25  # --> '+'


# ---------------------- #
# -- INTEGER --> NAME -- #
# ---------------------- #

INT_2_NAME = {}


INT_2_NAME[de_DE] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: (__re_compile("Milliarde[^\\s-]*"), "... von Milliarden"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, "tausend"),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " Million"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "en"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " Milliarde"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "n"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"einsund": "einund", "eins M": "eine M"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "minus ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "null"),),
            "1": ((DSL_ACTION_VERBATIM, "eins"),),
            "2": ((DSL_ACTION_VERBATIM, "zwei"),),
            "3": ((DSL_ACTION_VERBATIM, "drei"),),
            "4": ((DSL_ACTION_VERBATIM, "vier"),),
            "5": ((DSL_ACTION_VERBATIM, "fünf"),),
            "6": ((DSL_ACTION_VERBATIM, "sechs"),),
            "7": ((DSL_ACTION_VERBATIM, "sieben"),),
            "8": ((DSL_ACTION_VERBATIM, "acht"),),
            "9": ((DSL_ACTION_VERBATIM, "neun"),),
            "10": ((DSL_ACTION_VERBATIM, "zehn"),),
            "11": ((DSL_ACTION_VERBATIM, "elf"),),
            "12": ((DSL_ACTION_VERBATIM, "zwölf"),),
            "16": ((DSL_ACTION_VERBATIM, "sechzehn"),),
            "17": ((DSL_ACTION_VERBATIM, "siebzehn"),),
            "20": ((DSL_ACTION_VERBATIM, "zwanzig"),),
            "30": ((DSL_ACTION_VERBATIM, "dreißig"),),
            "60": ((DSL_ACTION_VERBATIM, "sechzig"),),
            "70": ((DSL_ACTION_VERBATIM, "siebzig"),),
            "100": ((DSL_ACTION_VERBATIM, "hundert"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("1."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                            (DSL_ACTION_VERBATIM, "zehn"),
                        ),
                    ),
                    (
                        __re_compile(".0"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),),
                            ),
                            (DSL_ACTION_VERBATIM, "zig"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                            (DSL_ACTION_VERBATIM, "und"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, "hundert"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),
                                    (DSL_ACTION_VERBATIM, "00"),
                                ),
                            ),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[en_GB] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ",",
        DSL_TAG_GENE_BIG: (__re_compile("billion"), "... of billion"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " thousand "),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_LOWER, DSL_COMPOPE_LOWER),
                        (
                            ((DSL_ACTION_VERBATIM, "0"),),
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),),
                            ((DSL_ACTION_VERBATIM, "100"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "and"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " billion "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "minus ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zero"),),
            "1": ((DSL_ACTION_VERBATIM, "one"),),
            "2": ((DSL_ACTION_VERBATIM, "two"),),
            "3": ((DSL_ACTION_VERBATIM, "three"),),
            "4": ((DSL_ACTION_VERBATIM, "four"),),
            "5": ((DSL_ACTION_VERBATIM, "five"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "seven"),),
            "8": ((DSL_ACTION_VERBATIM, "eight"),),
            "9": ((DSL_ACTION_VERBATIM, "nine"),),
            "10": ((DSL_ACTION_VERBATIM, "ten"),),
            "11": ((DSL_ACTION_VERBATIM, "eleven"),),
            "12": ((DSL_ACTION_VERBATIM, "twelve"),),
            "13": ((DSL_ACTION_VERBATIM, "thirteen"),),
            "15": ((DSL_ACTION_VERBATIM, "fifteen"),),
            "18": ((DSL_ACTION_VERBATIM, "eighteen"),),
            "20": ((DSL_ACTION_VERBATIM, "twenty"),),
            "30": ((DSL_ACTION_VERBATIM, "thirty"),),
            "40": ((DSL_ACTION_VERBATIM, "forty"),),
            "50": ((DSL_ACTION_VERBATIM, "fifty"),),
            "80": ((DSL_ACTION_VERBATIM, "eighty"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("1."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                            (DSL_ACTION_VERBATIM, "teen"),
                        ),
                    ),
                    (
                        __re_compile(".0"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),),
                            ),
                            (DSL_ACTION_VERBATIM, "ty"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " hundred"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " hundred and "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[en_US] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ",",
        DSL_TAG_GENE_BIG: (__re_compile("billion"), "... of billion"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " thousand "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " billion "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "minus ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zero"),),
            "1": ((DSL_ACTION_VERBATIM, "one"),),
            "2": ((DSL_ACTION_VERBATIM, "two"),),
            "3": ((DSL_ACTION_VERBATIM, "three"),),
            "4": ((DSL_ACTION_VERBATIM, "four"),),
            "5": ((DSL_ACTION_VERBATIM, "five"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "seven"),),
            "8": ((DSL_ACTION_VERBATIM, "eight"),),
            "9": ((DSL_ACTION_VERBATIM, "nine"),),
            "10": ((DSL_ACTION_VERBATIM, "ten"),),
            "11": ((DSL_ACTION_VERBATIM, "eleven"),),
            "12": ((DSL_ACTION_VERBATIM, "twelve"),),
            "13": ((DSL_ACTION_VERBATIM, "thirteen"),),
            "15": ((DSL_ACTION_VERBATIM, "fifteen"),),
            "18": ((DSL_ACTION_VERBATIM, "eighteen"),),
            "20": ((DSL_ACTION_VERBATIM, "twenty"),),
            "30": ((DSL_ACTION_VERBATIM, "thirty"),),
            "40": ((DSL_ACTION_VERBATIM, "forty"),),
            "50": ((DSL_ACTION_VERBATIM, "fifty"),),
            "80": ((DSL_ACTION_VERBATIM, "eighty"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("1."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                            (DSL_ACTION_VERBATIM, "teen"),
                        ),
                    ),
                    (
                        __re_compile(".0"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),),
                            ),
                            (DSL_ACTION_VERBATIM, "ty"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " hundred"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " hundred "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[es_ES] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: (__re_compile("mill[^\\s-]*"), "... de millones"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mil "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "un"),),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mill"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "ones"),),
                    ((DSL_ACTION_VERBATIM, "ón"),),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "más ...", DSL_TAG_SIGN_MINUS: "menos ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "cero"),),
            "1": ((DSL_ACTION_VERBATIM, "uno"),),
            "2": ((DSL_ACTION_VERBATIM, "dos"),),
            "3": ((DSL_ACTION_VERBATIM, "tres"),),
            "4": ((DSL_ACTION_VERBATIM, "cuatro"),),
            "5": ((DSL_ACTION_VERBATIM, "cinco"),),
            "6": ((DSL_ACTION_VERBATIM, "seis"),),
            "7": ((DSL_ACTION_VERBATIM, "siete"),),
            "8": ((DSL_ACTION_VERBATIM, "ocho"),),
            "9": ((DSL_ACTION_VERBATIM, "nueve"),),
            "10": ((DSL_ACTION_VERBATIM, "diez"),),
            "11": ((DSL_ACTION_VERBATIM, "once"),),
            "12": ((DSL_ACTION_VERBATIM, "doce"),),
            "13": ((DSL_ACTION_VERBATIM, "trece"),),
            "14": ((DSL_ACTION_VERBATIM, "catorce"),),
            "15": ((DSL_ACTION_VERBATIM, "quince"),),
            "16": ((DSL_ACTION_VERBATIM, "dieciséis"),),
            "20": ((DSL_ACTION_VERBATIM, "veinte"),),
            "21": ((DSL_ACTION_VERBATIM, "veintiuno"),),
            "22": ((DSL_ACTION_VERBATIM, "veintidós"),),
            "23": ((DSL_ACTION_VERBATIM, "veintitrés"),),
            "26": ((DSL_ACTION_VERBATIM, "veintiséis"),),
            "30": ((DSL_ACTION_VERBATIM, "treinta"),),
            "40": ((DSL_ACTION_VERBATIM, "cuarenta"),),
            "50": ((DSL_ACTION_VERBATIM, "cincuenta"),),
            "60": ((DSL_ACTION_VERBATIM, "sesenta"),),
            "70": ((DSL_ACTION_VERBATIM, "setenta"),),
            "80": ((DSL_ACTION_VERBATIM, "ochenta"),),
            "90": ((DSL_ACTION_VERBATIM, "noventa"),),
            "100": ((DSL_ACTION_VERBATIM, "ciento"),),
            "500": ((DSL_ACTION_VERBATIM, "quinientos"),),
            "700": ((DSL_ACTION_VERBATIM, "setecientos"),),
            "900": ((DSL_ACTION_VERBATIM, "novecientos"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("1."),
                        (
                            (DSL_ACTION_VERBATIM, "dieci"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                    (
                        __re_compile("2."),
                        (
                            (DSL_ACTION_VERBATIM, "veinti"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, " y "),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, "cientos"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),
                                    (DSL_ACTION_VERBATIM, "00"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, " "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[fr_BE] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: (__re_compile("milliard[^\\s-]*"), "... de milliards"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " "),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 5)),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "de"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " milliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "moins ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zéro"),),
            "1": ((DSL_ACTION_VERBATIM, "un"),),
            "2": ((DSL_ACTION_VERBATIM, "deux"),),
            "3": ((DSL_ACTION_VERBATIM, "trois"),),
            "4": ((DSL_ACTION_VERBATIM, "quatre"),),
            "5": ((DSL_ACTION_VERBATIM, "cinq"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "sept"),),
            "8": ((DSL_ACTION_VERBATIM, "huit"),),
            "9": ((DSL_ACTION_VERBATIM, "neuf"),),
            "10": ((DSL_ACTION_VERBATIM, "dix"),),
            "11": ((DSL_ACTION_VERBATIM, "onze"),),
            "12": ((DSL_ACTION_VERBATIM, "douze"),),
            "13": ((DSL_ACTION_VERBATIM, "treize"),),
            "14": ((DSL_ACTION_VERBATIM, "quatorze"),),
            "15": ((DSL_ACTION_VERBATIM, "quinze"),),
            "16": ((DSL_ACTION_VERBATIM, "seize"),),
            "20": ((DSL_ACTION_VERBATIM, "vingt"),),
            "30": ((DSL_ACTION_VERBATIM, "trente"),),
            "40": ((DSL_ACTION_VERBATIM, "quarante"),),
            "50": ((DSL_ACTION_VERBATIM, "cinquante"),),
            "60": ((DSL_ACTION_VERBATIM, "soixante"),),
            "100": ((DSL_ACTION_VERBATIM, "cent"),),
            "70": ((DSL_ACTION_VERBATIM, "septante"),),
            "80": ((DSL_ACTION_VERBATIM, "octante"),),
            "90": ((DSL_ACTION_VERBATIM, "nonante"),),
        },
        DSL_ACTION_MATCHING: {
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " cents"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_IF_ELSE,
                                (
                                    (
                                        (DSL_COMPOPE_GREATER,),
                                        (
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                            ((DSL_ACTION_VERBATIM, "1"),),
                                        ),
                                    ),
                                    (
                                        (
                                            DSL_ACTION_NAME_IT,
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                        ),
                                    ),
                                    (),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, " cent "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
            2: OrderedDict(
                [
                    (
                        __re_compile(".1"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-et-un"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[fr_FR] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: (__re_compile("milliard[^\\s-]*"), "... de milliards"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " "),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 5)),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "de"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " milliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "moins ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zéro"),),
            "1": ((DSL_ACTION_VERBATIM, "un"),),
            "2": ((DSL_ACTION_VERBATIM, "deux"),),
            "3": ((DSL_ACTION_VERBATIM, "trois"),),
            "4": ((DSL_ACTION_VERBATIM, "quatre"),),
            "5": ((DSL_ACTION_VERBATIM, "cinq"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "sept"),),
            "8": ((DSL_ACTION_VERBATIM, "huit"),),
            "9": ((DSL_ACTION_VERBATIM, "neuf"),),
            "10": ((DSL_ACTION_VERBATIM, "dix"),),
            "11": ((DSL_ACTION_VERBATIM, "onze"),),
            "12": ((DSL_ACTION_VERBATIM, "douze"),),
            "13": ((DSL_ACTION_VERBATIM, "treize"),),
            "14": ((DSL_ACTION_VERBATIM, "quatorze"),),
            "15": ((DSL_ACTION_VERBATIM, "quinze"),),
            "16": ((DSL_ACTION_VERBATIM, "seize"),),
            "20": ((DSL_ACTION_VERBATIM, "vingt"),),
            "30": ((DSL_ACTION_VERBATIM, "trente"),),
            "40": ((DSL_ACTION_VERBATIM, "quarante"),),
            "50": ((DSL_ACTION_VERBATIM, "cinquante"),),
            "60": ((DSL_ACTION_VERBATIM, "soixante"),),
            "80": ((DSL_ACTION_VERBATIM, "quatre-vingts"),),
            "71": ((DSL_ACTION_VERBATIM, "soixante-et-onze"),),
            "100": ((DSL_ACTION_VERBATIM, "cent"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("8."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                    (
                        __re_compile("7."),
                        (
                            (DSL_ACTION_VERBATIM, "soixante-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile("9."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile(".1"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-et-un"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " cents"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_IF_ELSE,
                                (
                                    (
                                        (DSL_COMPOPE_GREATER,),
                                        (
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                            ((DSL_ACTION_VERBATIM, "1"),),
                                        ),
                                    ),
                                    (
                                        (
                                            DSL_ACTION_NAME_IT,
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                        ),
                                    ),
                                    (),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, " cent "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[fr_FR_chuquet_1] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: None,
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        12: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " billion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        18: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " trillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        24: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " quadrillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        30: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " quintillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        36: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " sextillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        42: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " septillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        48: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " octillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        54: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " nonillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        60: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " decillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "moins ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zéro"),),
            "1": ((DSL_ACTION_VERBATIM, "un"),),
            "2": ((DSL_ACTION_VERBATIM, "deux"),),
            "3": ((DSL_ACTION_VERBATIM, "trois"),),
            "4": ((DSL_ACTION_VERBATIM, "quatre"),),
            "5": ((DSL_ACTION_VERBATIM, "cinq"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "sept"),),
            "8": ((DSL_ACTION_VERBATIM, "huit"),),
            "9": ((DSL_ACTION_VERBATIM, "neuf"),),
            "10": ((DSL_ACTION_VERBATIM, "dix"),),
            "11": ((DSL_ACTION_VERBATIM, "onze"),),
            "12": ((DSL_ACTION_VERBATIM, "douze"),),
            "13": ((DSL_ACTION_VERBATIM, "treize"),),
            "14": ((DSL_ACTION_VERBATIM, "quatorze"),),
            "15": ((DSL_ACTION_VERBATIM, "quinze"),),
            "16": ((DSL_ACTION_VERBATIM, "seize"),),
            "20": ((DSL_ACTION_VERBATIM, "vingt"),),
            "30": ((DSL_ACTION_VERBATIM, "trente"),),
            "40": ((DSL_ACTION_VERBATIM, "quarante"),),
            "50": ((DSL_ACTION_VERBATIM, "cinquante"),),
            "60": ((DSL_ACTION_VERBATIM, "soixante"),),
            "80": ((DSL_ACTION_VERBATIM, "quatre-vingts"),),
            "71": ((DSL_ACTION_VERBATIM, "soixante-et-onze"),),
            "100": ((DSL_ACTION_VERBATIM, "cent"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("8."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                    (
                        __re_compile("7."),
                        (
                            (DSL_ACTION_VERBATIM, "soixante-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile("9."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile(".1"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-et-un"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " cents"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_IF_ELSE,
                                (
                                    (
                                        (DSL_COMPOPE_GREATER,),
                                        (
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                            ((DSL_ACTION_VERBATIM, "1"),),
                                        ),
                                    ),
                                    (
                                        (
                                            DSL_ACTION_NAME_IT,
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                        ),
                                    ),
                                    (),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, " cent "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[fr_FR_chuquet_2] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: None,
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " "),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 5)),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "de"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " milliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        12: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " billion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        15: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " billiard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        18: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " trillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        21: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " trilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        24: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " quadrillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        27: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " quadrilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        30: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " quintillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        33: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " quintilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        36: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " sextillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        39: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " sextilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        42: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " septillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        45: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " septilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        48: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " octillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        51: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " octilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        54: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " nonillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        57: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " nonilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        60: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " decillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        63: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " decilliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "moins ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zéro"),),
            "1": ((DSL_ACTION_VERBATIM, "un"),),
            "2": ((DSL_ACTION_VERBATIM, "deux"),),
            "3": ((DSL_ACTION_VERBATIM, "trois"),),
            "4": ((DSL_ACTION_VERBATIM, "quatre"),),
            "5": ((DSL_ACTION_VERBATIM, "cinq"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "sept"),),
            "8": ((DSL_ACTION_VERBATIM, "huit"),),
            "9": ((DSL_ACTION_VERBATIM, "neuf"),),
            "10": ((DSL_ACTION_VERBATIM, "dix"),),
            "11": ((DSL_ACTION_VERBATIM, "onze"),),
            "12": ((DSL_ACTION_VERBATIM, "douze"),),
            "13": ((DSL_ACTION_VERBATIM, "treize"),),
            "14": ((DSL_ACTION_VERBATIM, "quatorze"),),
            "15": ((DSL_ACTION_VERBATIM, "quinze"),),
            "16": ((DSL_ACTION_VERBATIM, "seize"),),
            "20": ((DSL_ACTION_VERBATIM, "vingt"),),
            "30": ((DSL_ACTION_VERBATIM, "trente"),),
            "40": ((DSL_ACTION_VERBATIM, "quarante"),),
            "50": ((DSL_ACTION_VERBATIM, "cinquante"),),
            "60": ((DSL_ACTION_VERBATIM, "soixante"),),
            "80": ((DSL_ACTION_VERBATIM, "quatre-vingts"),),
            "71": ((DSL_ACTION_VERBATIM, "soixante-et-onze"),),
            "100": ((DSL_ACTION_VERBATIM, "cent"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("8."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                    (
                        __re_compile("7."),
                        (
                            (DSL_ACTION_VERBATIM, "soixante-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile("9."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile(".1"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-et-un"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " cents"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_IF_ELSE,
                                (
                                    (
                                        (DSL_COMPOPE_GREATER,),
                                        (
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                            ((DSL_ACTION_VERBATIM, "1"),),
                                        ),
                                    ),
                                    (
                                        (
                                            DSL_ACTION_NAME_IT,
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                        ),
                                    ),
                                    (),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, " cent "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[fr_FR_rowlett] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: None,
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " "),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 5)),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "de"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " milliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        12: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " tetrillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        15: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " pentillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        18: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " hexillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        21: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " eptillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        24: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " oktillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        27: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " ennillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        30: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " dekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        33: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " hendekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        36: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " dodekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        39: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " trisdekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        42: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " tetradekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        45: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " pentadekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        48: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " hexadekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        51: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " heptadekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        54: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " oktadekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        57: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " enneadekillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        60: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        63: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosihenillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        66: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosidillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        69: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icositrillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        72: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icositetrillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        75: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosipentillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        78: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosihexillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        81: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosiheptillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        84: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosioktillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        87: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " icosiennillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        90: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " triacontillion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus ...", DSL_TAG_SIGN_MINUS: "moins ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zéro"),),
            "1": ((DSL_ACTION_VERBATIM, "un"),),
            "2": ((DSL_ACTION_VERBATIM, "deux"),),
            "3": ((DSL_ACTION_VERBATIM, "trois"),),
            "4": ((DSL_ACTION_VERBATIM, "quatre"),),
            "5": ((DSL_ACTION_VERBATIM, "cinq"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "sept"),),
            "8": ((DSL_ACTION_VERBATIM, "huit"),),
            "9": ((DSL_ACTION_VERBATIM, "neuf"),),
            "10": ((DSL_ACTION_VERBATIM, "dix"),),
            "11": ((DSL_ACTION_VERBATIM, "onze"),),
            "12": ((DSL_ACTION_VERBATIM, "douze"),),
            "13": ((DSL_ACTION_VERBATIM, "treize"),),
            "14": ((DSL_ACTION_VERBATIM, "quatorze"),),
            "15": ((DSL_ACTION_VERBATIM, "quinze"),),
            "16": ((DSL_ACTION_VERBATIM, "seize"),),
            "20": ((DSL_ACTION_VERBATIM, "vingt"),),
            "30": ((DSL_ACTION_VERBATIM, "trente"),),
            "40": ((DSL_ACTION_VERBATIM, "quarante"),),
            "50": ((DSL_ACTION_VERBATIM, "cinquante"),),
            "60": ((DSL_ACTION_VERBATIM, "soixante"),),
            "80": ((DSL_ACTION_VERBATIM, "quatre-vingts"),),
            "71": ((DSL_ACTION_VERBATIM, "soixante-et-onze"),),
            "100": ((DSL_ACTION_VERBATIM, "cent"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("8."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                    (
                        __re_compile("7."),
                        (
                            (DSL_ACTION_VERBATIM, "soixante-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile("9."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile(".1"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-et-un"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, " cents"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_IF_ELSE,
                                (
                                    (
                                        (DSL_COMPOPE_GREATER,),
                                        (
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                            ((DSL_ACTION_VERBATIM, "1"),),
                                        ),
                                    ),
                                    (
                                        (
                                            DSL_ACTION_NAME_IT,
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                        ),
                                    ),
                                    (),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, " cent "),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[fr_FR_tiret] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: (__re_compile("milliard[^\\s-]*"), "...-de-milliards"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                        (DSL_ACTION_VERBATIM, "-"),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, "mille"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    (
                        (DSL_ACTION_VERBATIM, "-"),
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),),
                        ),
                    ),
                    (),
                ),
            ),
        ),
        6: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                        (DSL_ACTION_VERBATIM, "-"),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, "million"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    (
                        (DSL_ACTION_VERBATIM, "-"),
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),),
                        ),
                    ),
                    (),
                ),
            ),
        ),
        9: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                        (DSL_ACTION_VERBATIM, "-"),
                    ),
                    (),
                ),
            ),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 5)),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "de-"),),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, "milliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "s"),),
                    (),
                ),
            ),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),),
                            ((DSL_ACTION_VERBATIM, "0"),),
                        ),
                    ),
                    (
                        (DSL_ACTION_VERBATIM, "-"),
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),),
                        ),
                    ),
                    (),
                ),
            ),
        ),
    },
    DSL_SPECS_PATCH: {"cents-mille": "cent-mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus-...", DSL_TAG_SIGN_MINUS: "moins-..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zéro"),),
            "1": ((DSL_ACTION_VERBATIM, "un"),),
            "2": ((DSL_ACTION_VERBATIM, "deux"),),
            "3": ((DSL_ACTION_VERBATIM, "trois"),),
            "4": ((DSL_ACTION_VERBATIM, "quatre"),),
            "5": ((DSL_ACTION_VERBATIM, "cinq"),),
            "6": ((DSL_ACTION_VERBATIM, "six"),),
            "7": ((DSL_ACTION_VERBATIM, "sept"),),
            "8": ((DSL_ACTION_VERBATIM, "huit"),),
            "9": ((DSL_ACTION_VERBATIM, "neuf"),),
            "10": ((DSL_ACTION_VERBATIM, "dix"),),
            "11": ((DSL_ACTION_VERBATIM, "onze"),),
            "12": ((DSL_ACTION_VERBATIM, "douze"),),
            "13": ((DSL_ACTION_VERBATIM, "treize"),),
            "14": ((DSL_ACTION_VERBATIM, "quatorze"),),
            "15": ((DSL_ACTION_VERBATIM, "quinze"),),
            "16": ((DSL_ACTION_VERBATIM, "seize"),),
            "20": ((DSL_ACTION_VERBATIM, "vingt"),),
            "30": ((DSL_ACTION_VERBATIM, "trente"),),
            "40": ((DSL_ACTION_VERBATIM, "quarante"),),
            "50": ((DSL_ACTION_VERBATIM, "cinquante"),),
            "60": ((DSL_ACTION_VERBATIM, "soixante"),),
            "80": ((DSL_ACTION_VERBATIM, "quatre-vingts"),),
            "71": ((DSL_ACTION_VERBATIM, "soixante-et-onze"),),
            "100": ((DSL_ACTION_VERBATIM, "cent"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile("8."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                    (
                        __re_compile("7."),
                        (
                            (DSL_ACTION_VERBATIM, "soixante-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile("9."),
                        (
                            (DSL_ACTION_VERBATIM, "quatre-vingt-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_VERBATIM, "1"),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                    (
                        __re_compile(".1"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-et-un"),
                        ),
                    ),
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "-"),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    ),
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, "-cents"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_IF_ELSE,
                                (
                                    (
                                        (DSL_COMPOPE_GREATER,),
                                        (
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                            ((DSL_ACTION_VERBATIM, "1"),),
                                        ),
                                    ),
                                    (
                                        (
                                            DSL_ACTION_NAME_IT,
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                        ),
                                        (DSL_ACTION_VERBATIM, "-"),
                                    ),
                                    (),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "cent-"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


INT_2_NAME[it_IT] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: (__re_compile("miliard[^\\s-]*"), "... di miliardi"),
        DSL_TAG_GENE_DIR: DSL_DIR_L2R,
    },
    DSL_SPECS_GROUP: {
        3: (
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    (
                        (
                            DSL_ACTION_NAME_IT_GROUP,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, "mil"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_GREATER,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "a"),),
                    ((DSL_ACTION_VERBATIM, "le"),),
                ),
            ),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " milion"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "e"),),
                    ((DSL_ACTION_VERBATIM, "i"),),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " miliard"),
            (
                DSL_ACTION_IF_ELSE,
                (
                    (
                        (DSL_COMPOPE_EQ,),
                        (
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                            ((DSL_ACTION_VERBATIM, "1"),),
                        ),
                    ),
                    ((DSL_ACTION_VERBATIM, "o"),),
                    ((DSL_ACTION_VERBATIM, "i"),),
                ),
            ),
            (DSL_ACTION_VERBATIM, " "),
            (DSL_ACTION_NAME_IT_GROUP, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {
        "auno": "uno",
        "iuno": "uno",
        "atre": "atré",
        "itre": "itré",
        "aott": "ott",
        "iott": "ott",
        "oott": "ott",
    },
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "più ...", DSL_TAG_SIGN_MINUS: "meno ..."},
    DSL_SPECS_SMALL: {
        DSL_ACTION_ASIT: {
            "0": ((DSL_ACTION_VERBATIM, "zero"),),
            "1": ((DSL_ACTION_VERBATIM, "uno"),),
            "2": ((DSL_ACTION_VERBATIM, "due"),),
            "3": ((DSL_ACTION_VERBATIM, "tre"),),
            "4": ((DSL_ACTION_VERBATIM, "quattro"),),
            "5": ((DSL_ACTION_VERBATIM, "cinque"),),
            "6": ((DSL_ACTION_VERBATIM, "sei"),),
            "7": ((DSL_ACTION_VERBATIM, "sette"),),
            "8": ((DSL_ACTION_VERBATIM, "otto"),),
            "9": ((DSL_ACTION_VERBATIM, "nove"),),
            "10": ((DSL_ACTION_VERBATIM, "dieci"),),
            "11": ((DSL_ACTION_VERBATIM, "undici"),),
            "12": ((DSL_ACTION_VERBATIM, "dodici"),),
            "13": ((DSL_ACTION_VERBATIM, "tredici"),),
            "14": ((DSL_ACTION_VERBATIM, "quattordici"),),
            "15": ((DSL_ACTION_VERBATIM, "quindici"),),
            "16": ((DSL_ACTION_VERBATIM, "sedici"),),
            "17": ((DSL_ACTION_VERBATIM, "diciassette"),),
            "18": ((DSL_ACTION_VERBATIM, "diciotto"),),
            "19": ((DSL_ACTION_VERBATIM, "diciannove"),),
            "20": ((DSL_ACTION_VERBATIM, "venti"),),
            "30": ((DSL_ACTION_VERBATIM, "trenta"),),
            "40": ((DSL_ACTION_VERBATIM, "quaranta"),),
            "50": ((DSL_ACTION_VERBATIM, "cinquanta"),),
            "60": ((DSL_ACTION_VERBATIM, "sessanta"),),
            "70": ((DSL_ACTION_VERBATIM, "settanta"),),
            "80": ((DSL_ACTION_VERBATIM, "ottanta"),),
            "90": ((DSL_ACTION_VERBATIM, "novanta"),),
        },
        DSL_ACTION_MATCHING: {
            2: OrderedDict(
                [
                    (
                        __re_compile(".."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
                            (
                                DSL_ACTION_NAME_IT,
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),),
                            ),
                        ),
                    )
                ]
            ),
            3: OrderedDict(
                [
                    (
                        __re_compile(".00"),
                        (
                            (
                                DSL_ACTION_IF_ELSE,
                                (
                                    (
                                        (DSL_COMPOPE_GREATER,),
                                        (
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                            ((DSL_ACTION_VERBATIM, "1"),),
                                        ),
                                    ),
                                    (
                                        (
                                            DSL_ACTION_NAME_IT,
                                            ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                                        ),
                                    ),
                                    (),
                                ),
                            ),
                            (DSL_ACTION_VERBATIM, "cento"),
                        ),
                    ),
                    (
                        __re_compile("..."),
                        (
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),
                                    (DSL_ACTION_VERBATIM, "00"),
                                ),
                            ),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    ),
                ]
            ),
        },
    },
}


# --------------------------------- #
# -- LIST OF ALL LANGS SUPPORTED -- #
# --------------------------------- #

ALL_LANGS = list(INT_2_NAME)
#!/usr/bin/env python3

# ---------------------------------------------------------------- #
# --  This code was automatically build by the following file.  -- #
# --                                                            -- #
# --      + ``tools/factory/de-textify/build_tr.py``            -- #
# --                                                            -- #
# --  See the repository of the project ``cvnum`` for more      -- #
# --  informations.                                             -- #
# --                                                            -- #
# --      + https://github.com/math-objects/cvnum               -- #
# ---------------------------------------------------------------- #

from collections import OrderedDict
from re          import compile as __re_compile


# ------------- #
# -- PATTERN -- #
# ------------- #

DSL_PATTERN_ELLIPSIS = __re_compile("(?P<bname>\.\.\.)")


# ------------ #
# -- ACTION -- #
# ------------ #

DSL_ACTION_ASIT              = 0  # --> 'asit'
DSL_ACTION_EXTRACT_NUMBER_OF = 1  # --> 'd(m..n)'
DSL_ACTION_IF_ELSE           = 2  # --> 'if-else'
DSL_ACTION_MATCHING          = 3  # --> 'matching'
DSL_ACTION_NAME_IT           = 4  # --> 'name-it'
DSL_ACTION_SPEVAR            = 5  # --> 'special-var'
DSL_ACTION_VERBATIM          = 6  # --> 'verbatim'


# ------------- #
# -- COMPOPE -- #
# ------------- #

DSL_COMPOPE_EQ         = 0  # --> '='
DSL_COMPOPE_GREATER    = 1  # --> '>'
DSL_COMPOPE_GREATER_EQ = 2  # --> '>='
DSL_COMPOPE_LOWER      = 3  # --> '<'
DSL_COMPOPE_LOWER_EQ   = 4  # --> '<='
DSL_COMPOPE_NOT_EQ     = 5  # --> '!='


# ----------- #
# -- SPECS -- #
# ----------- #

DSL_SPECS_GENE  = 0  # --> 'general'
DSL_SPECS_GROUP = 1  # --> 'group'
DSL_SPECS_PATCH = 2  # --> 'patch'
DSL_SPECS_SIGN  = 3  # --> 'sign'
DSL_SPECS_SMALL = 4  # --> 'small'


# ------------ #
# -- SPEVAR -- #
# ------------ #

DSL_SPEVAR_NUMBER_OF = 0  # --> 'd'
DSL_SPEVAR_REMAINING = 1  # --> 'r'


# --------- #
# -- TAG -- #
# --------- #

DSL_TAG_GENE_BIG   = 0  # --> 'big'
DSL_TAG_GENE_SEP   = 1  # --> 'sep'

DSL_TAG_SIGN_MINUS = 2  # --> '-'
DSL_TAG_SIGN_PLUS  = 3  # --> '+'


# ---------------------- #
# -- INTEGER --> NAME -- #
# ---------------------- #

INT_2_NAME = {}


INT_2_NAME["en_GB"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ",",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>billion)"): "... of billion"},
    },
    DSL_SPECS_GROUP: {
        3: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " billion "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "minus"},
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
            "14": ((DSL_ACTION_VERBATIM, "forteen"),),
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


INT_2_NAME["en_US"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ",",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>billion)"): "... of billion"},
    },
    DSL_SPECS_GROUP: {
        3: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " thousand "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " million "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
            (DSL_ACTION_VERBATIM, " billion "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "minus"},
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
            "14": ((DSL_ACTION_VERBATIM, "forteen"),),
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


INT_2_NAME["es_ES"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>mill\\S+)"): "... de millones"},
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
                            DSL_ACTION_NAME_IT,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mil "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
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
                            DSL_ACTION_NAME_IT,
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "más", DSL_TAG_SIGN_MINUS: "menos"},
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


INT_2_NAME["fr_BE"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>milliard\\S+)"): "... de milliards"},
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
                            DSL_ACTION_NAME_IT,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "moins"},
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


INT_2_NAME["fr_FR"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>milliard\\S+)"): "... de milliards"},
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
                            DSL_ACTION_NAME_IT,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "moins"},
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


INT_2_NAME["fr_FR[chuquet-1]"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>milliard\\S+)"): "... de milliards"},
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
                            DSL_ACTION_NAME_IT,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        12: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        18: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        24: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        30: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        36: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        42: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        48: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        54: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        60: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "moins"},
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


INT_2_NAME["fr_FR[chuquet-2]"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>milliard\\S+)"): "... de milliards"},
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
                            DSL_ACTION_NAME_IT,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        12: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        15: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        18: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        21: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        24: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        27: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        30: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        33: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        36: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        39: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        42: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        45: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        48: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        51: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        54: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        57: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        60: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        63: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "moins"},
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


INT_2_NAME["fr_FR[rowlett]"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>milliard\\S+)"): "... de milliards"},
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
                            DSL_ACTION_NAME_IT,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, " mille "),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        12: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        15: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        18: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        21: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        24: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        27: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        30: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        33: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        36: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        39: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        42: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        45: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        48: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        51: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        54: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        57: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        60: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        63: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        66: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        69: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        72: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        75: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        78: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        81: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        84: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        87: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        90: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {"cents mille": "cent mille"},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "moins"},
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


INT_2_NAME["ge_GE"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {
            __re_compile("(?P<bname>Milliarde\\S+)"): "... von Milliarden"
        },
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
                            DSL_ACTION_NAME_IT,
                            ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),),
                        ),
                    ),
                    (),
                ),
            ),
            (DSL_ACTION_VERBATIM, "tausend"),
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "plus", DSL_TAG_SIGN_MINUS: "minus"},
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
                        __re_compile(".1"),
                        (
                            (DSL_ACTION_VERBATIM, "einsund"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_VERBATIM, "0"),
                                ),
                            ),
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
                                ((DSL_ACTION_EXTRACT_NUMBER_OF, (2, 2)),),
                            ),
                            (DSL_ACTION_VERBATIM, "hundert"),
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


INT_2_NAME["it_IT"] = {
    DSL_SPECS_GENE: {
        DSL_TAG_GENE_SEP: ".",
        DSL_TAG_GENE_BIG: {__re_compile("(?P<bname>miliard\\S+)"): "... di miliardi"},
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
                            DSL_ACTION_NAME_IT,
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        6: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
        9: (
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_NUMBER_OF),)),
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
            (DSL_ACTION_NAME_IT, ((DSL_ACTION_SPEVAR, DSL_SPEVAR_REMAINING),)),
        ),
    },
    DSL_SPECS_PATCH: {},
    DSL_SPECS_SIGN: {DSL_TAG_SIGN_PLUS: "più", DSL_TAG_SIGN_MINUS: "meno"},
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
            "100": ((DSL_ACTION_VERBATIM, "cento"),),
        },
        DSL_ACTION_MATCHING: {
            3: OrderedDict(
                [
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
                            (DSL_ACTION_VERBATIM, "cento"),
                            (
                                DSL_ACTION_NAME_IT,
                                (
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (1, 1)),
                                    (DSL_ACTION_EXTRACT_NUMBER_OF, (0, 0)),
                                ),
                            ),
                        ),
                    )
                ]
            )
        },
    },
}


# --------------------------------- #
# -- LIST OF ALL LANGS SUPPORTED -- #
# --------------------------------- #

ALL_LANGS = list(INT_2_NAME.keys())

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


INT_2_NAME[de_DE] = {14: {23: '.', 21: (__re_compile('Milliarde[^\\s-]*'), '... von Milliarden'), 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, 'tausend'), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' Million'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 'en'),), ())), (7, ' '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' Milliarde'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 'n'),), ())), (7, ' '), (5, ((6, 20),)))}, 16: {'einsund': 'einund', 'eins M': 'eine M'}, 17: {25: 'plus ...', 24: 'minus ...'}, 18: {0: {'0': ((7, 'null'),), '1': ((7, 'eins'),), '2': ((7, 'zwei'),), '3': ((7, 'drei'),), '4': ((7, 'vier'),), '5': ((7, 'fünf'),), '6': ((7, 'sechs'),), '7': ((7, 'sieben'),), '8': ((7, 'acht'),), '9': ((7, 'neun'),), '10': ((7, 'zehn'),), '11': ((7, 'elf'),), '12': ((7, 'zwölf'),), '16': ((7, 'sechzehn'),), '17': ((7, 'siebzehn'),), '20': ((7, 'zwanzig'),), '30': ((7, 'dreißig'),), '60': ((7, 'sechzig'),), '70': ((7, 'siebzig'),), '100': ((7, 'hundert'),)}, 3: {2: OrderedDict([(__re_compile('1.'), ((4, ((1, (0, 0)),)), (7, 'zehn'))), (__re_compile('.0'), ((4, ((1, (1, 1)),)), (7, 'zig'))), (__re_compile('..'), ((4, ((1, (0, 0)),)), (7, 'und'), (4, ((1, (1, 1)), (7, '0')))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, 'hundert'))), (__re_compile('...'), ((4, ((1, (2, 2)), (7, '00'))), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[en_GB] = {14: {23: ',', 21: (__re_compile('billion'), '... of billion'), 22: "l2r"}, 15: {3: ((5, ((6, 19),)), (7, ' thousand '), (2, (((11, 11), (((7, '0'),), ((6, 20),), ((7, '100'),))), ((7, 'and'),), ())), (7, ' '), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' million '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' billion '), (5, ((6, 20),)))}, 16: {}, 17: {25: 'plus ...', 24: 'minus ...'}, 18: {0: {'0': ((7, 'zero'),), '1': ((7, 'one'),), '2': ((7, 'two'),), '3': ((7, 'three'),), '4': ((7, 'four'),), '5': ((7, 'five'),), '6': ((7, 'six'),), '7': ((7, 'seven'),), '8': ((7, 'eight'),), '9': ((7, 'nine'),), '10': ((7, 'ten'),), '11': ((7, 'eleven'),), '12': ((7, 'twelve'),), '13': ((7, 'thirteen'),), '14': ((7, 'forteen'),), '15': ((7, 'fifteen'),), '18': ((7, 'eighteen'),), '20': ((7, 'twenty'),), '30': ((7, 'thirty'),), '40': ((7, 'forty'),), '50': ((7, 'fifty'),), '80': ((7, 'eighty'),)}, 3: {2: OrderedDict([(__re_compile('1.'), ((4, ((1, (0, 0)),)), (7, 'teen'))), (__re_compile('.0'), ((4, ((1, (1, 1)),)), (7, 'ty'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, ' hundred'))), (__re_compile('...'), ((4, ((1, (2, 2)),)), (7, ' hundred and '), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[en_US] = {14: {23: ',', 21: (__re_compile('billion'), '... of billion'), 22: "l2r"}, 15: {3: ((5, ((6, 19),)), (7, ' thousand '), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' million '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' billion '), (5, ((6, 20),)))}, 16: {}, 17: {25: 'plus ...', 24: 'minus ...'}, 18: {0: {'0': ((7, 'zero'),), '1': ((7, 'one'),), '2': ((7, 'two'),), '3': ((7, 'three'),), '4': ((7, 'four'),), '5': ((7, 'five'),), '6': ((7, 'six'),), '7': ((7, 'seven'),), '8': ((7, 'eight'),), '9': ((7, 'nine'),), '10': ((7, 'ten'),), '11': ((7, 'eleven'),), '12': ((7, 'twelve'),), '13': ((7, 'thirteen'),), '14': ((7, 'forteen'),), '15': ((7, 'fifteen'),), '18': ((7, 'eighteen'),), '20': ((7, 'twenty'),), '30': ((7, 'thirty'),), '40': ((7, 'forty'),), '50': ((7, 'fifty'),), '80': ((7, 'eighty'),)}, 3: {2: OrderedDict([(__re_compile('1.'), ((4, ((1, (0, 0)),)), (7, 'teen'))), (__re_compile('.0'), ((4, ((1, (1, 1)),)), (7, 'ty'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('...'), ((4, ((1, (2, 2)),)), (7, ' hundred '), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[es_ES] = {14: {23: '.', 21: (__re_compile('mill[^\\s-]*'), '... de millones'), 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, ' mil '), (5, ((6, 20),))), 6: ((2, (((8,), (((6, 19),), ((7, '1'),))), ((7, 'un'),), ((5, ((6, 19),)),))), (7, ' mill'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 'ones'),), ((7, 'ón'),))), (7, ' '), (5, ((6, 20),)))}, 16: {}, 17: {25: 'más ...', 24: 'menos ...'}, 18: {0: {'0': ((7, 'cero'),), '1': ((7, 'uno'),), '2': ((7, 'dos'),), '3': ((7, 'tres'),), '4': ((7, 'cuatro'),), '5': ((7, 'cinco'),), '6': ((7, 'seis'),), '7': ((7, 'siete'),), '8': ((7, 'ocho'),), '9': ((7, 'nueve'),), '10': ((7, 'diez'),), '11': ((7, 'once'),), '12': ((7, 'doce'),), '13': ((7, 'trece'),), '14': ((7, 'catorce'),), '15': ((7, 'quince'),), '16': ((7, 'dieciséis'),), '20': ((7, 'veinte'),), '21': ((7, 'veintiuno'),), '22': ((7, 'veintidós'),), '23': ((7, 'veintitrés'),), '30': ((7, 'treinta'),), '40': ((7, 'cuarenta'),), '50': ((7, 'cincuenta'),), '60': ((7, 'sesenta'),), '70': ((7, 'setenta'),), '80': ((7, 'ochenta'),), '90': ((7, 'noventa'),), '100': ((7, 'ciento'),), '500': ((7, 'quinientos'),), '700': ((7, 'setecientos'),), '900': ((7, 'novecientos'),)}, 3: {2: OrderedDict([(__re_compile('1.'), ((7, 'dieci'), (4, ((1, (0, 0)),)))), (__re_compile('2.'), ((7, 'veinti'), (4, ((1, (0, 0)),)))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, ' y '), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, 'cientos'))), (__re_compile('...'), ((4, ((1, (2, 2)), (7, '00'))), (7, ' '), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[fr_BE] = {14: {23: '.', 21: (__re_compile('milliard[^\\s-]*'), '... de milliards'), 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, ' mille '), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' million'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' '), (2, (((8,), (((1, (0, 5)),), ((7, '0'),))), ((7, 'de'),), ())), (7, ' milliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),)))}, 16: {'cents mille': 'cent mille'}, 17: {25: 'plus ...', 24: 'moins ...'}, 18: {0: {'0': ((7, 'zéro'),), '1': ((7, 'un'),), '2': ((7, 'deux'),), '3': ((7, 'trois'),), '4': ((7, 'quatre'),), '5': ((7, 'cinq'),), '6': ((7, 'six'),), '7': ((7, 'sept'),), '8': ((7, 'huit'),), '9': ((7, 'neuf'),), '10': ((7, 'dix'),), '11': ((7, 'onze'),), '12': ((7, 'douze'),), '13': ((7, 'treize'),), '14': ((7, 'quatorze'),), '15': ((7, 'quinze'),), '16': ((7, 'seize'),), '20': ((7, 'vingt'),), '30': ((7, 'trente'),), '40': ((7, 'quarante'),), '50': ((7, 'cinquante'),), '60': ((7, 'soixante'),), '100': ((7, 'cent'),), '70': ((7, 'septante'),), '80': ((7, 'octante'),), '90': ((7, 'nonante'),)}, 3: {3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, ' cents'))), (__re_compile('...'), ((2, (((9,), (((1, (2, 2)),), ((7, '1'),))), ((4, ((1, (2, 2)),)),), ())), (7, ' cent '), (4, ((1, (1, 1)), (1, (0, 0))))))]), 2: OrderedDict([(__re_compile('.1'), ((4, ((1, (1, 1)), (7, '0'))), (7, '-et-un'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))])}}}
            

INT_2_NAME[fr_FR] = {14: {23: '.', 21: (__re_compile('milliard[^\\s-]*'), '... de milliards'), 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, ' mille '), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' million'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' '), (2, (((8,), (((1, (0, 5)),), ((7, '0'),))), ((7, 'de'),), ())), (7, ' milliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),)))}, 16: {'cents mille': 'cent mille'}, 17: {25: 'plus ...', 24: 'moins ...'}, 18: {0: {'0': ((7, 'zéro'),), '1': ((7, 'un'),), '2': ((7, 'deux'),), '3': ((7, 'trois'),), '4': ((7, 'quatre'),), '5': ((7, 'cinq'),), '6': ((7, 'six'),), '7': ((7, 'sept'),), '8': ((7, 'huit'),), '9': ((7, 'neuf'),), '10': ((7, 'dix'),), '11': ((7, 'onze'),), '12': ((7, 'douze'),), '13': ((7, 'treize'),), '14': ((7, 'quatorze'),), '15': ((7, 'quinze'),), '16': ((7, 'seize'),), '20': ((7, 'vingt'),), '30': ((7, 'trente'),), '40': ((7, 'quarante'),), '50': ((7, 'cinquante'),), '60': ((7, 'soixante'),), '80': ((7, 'quatre-vingts'),), '71': ((7, 'soixante-et-onze'),), '100': ((7, 'cent'),)}, 3: {2: OrderedDict([(__re_compile('8.'), ((7, 'quatre-vingt-'), (4, ((1, (0, 0)),)))), (__re_compile('7.'), ((7, 'soixante-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('9.'), ((7, 'quatre-vingt-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('.1'), ((4, ((1, (1, 1)), (7, '0'))), (7, '-et-un'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, ' cents'))), (__re_compile('...'), ((2, (((9,), (((1, (2, 2)),), ((7, '1'),))), ((4, ((1, (2, 2)),)),), ())), (7, ' cent '), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[fr_FR_chuquet_1] = {14: {23: '.', 21: None, 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, ' mille '), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' million'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 12: ((5, ((6, 19),)), (7, ' billion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 18: ((5, ((6, 19),)), (7, ' trillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 24: ((5, ((6, 19),)), (7, ' quadrillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 30: ((5, ((6, 19),)), (7, ' quintillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 36: ((5, ((6, 19),)), (7, ' sextillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 42: ((5, ((6, 19),)), (7, ' septillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 48: ((5, ((6, 19),)), (7, ' octillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 54: ((5, ((6, 19),)), (7, ' nonillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 60: ((5, ((6, 19),)), (7, ' decillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),)))}, 16: {'cents mille': 'cent mille'}, 17: {25: 'plus ...', 24: 'moins ...'}, 18: {0: {'0': ((7, 'zéro'),), '1': ((7, 'un'),), '2': ((7, 'deux'),), '3': ((7, 'trois'),), '4': ((7, 'quatre'),), '5': ((7, 'cinq'),), '6': ((7, 'six'),), '7': ((7, 'sept'),), '8': ((7, 'huit'),), '9': ((7, 'neuf'),), '10': ((7, 'dix'),), '11': ((7, 'onze'),), '12': ((7, 'douze'),), '13': ((7, 'treize'),), '14': ((7, 'quatorze'),), '15': ((7, 'quinze'),), '16': ((7, 'seize'),), '20': ((7, 'vingt'),), '30': ((7, 'trente'),), '40': ((7, 'quarante'),), '50': ((7, 'cinquante'),), '60': ((7, 'soixante'),), '80': ((7, 'quatre-vingts'),), '71': ((7, 'soixante-et-onze'),), '100': ((7, 'cent'),)}, 3: {2: OrderedDict([(__re_compile('8.'), ((7, 'quatre-vingt-'), (4, ((1, (0, 0)),)))), (__re_compile('7.'), ((7, 'soixante-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('9.'), ((7, 'quatre-vingt-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('.1'), ((4, ((1, (1, 1)), (7, '0'))), (7, '-et-un'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, ' cents'))), (__re_compile('...'), ((2, (((9,), (((1, (2, 2)),), ((7, '1'),))), ((4, ((1, (2, 2)),)),), ())), (7, ' cent '), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[fr_FR_chuquet_2] = {14: {23: '.', 21: None, 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, ' mille '), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' million'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' '), (2, (((8,), (((1, (0, 5)),), ((7, '0'),))), ((7, 'de'),), ())), (7, ' milliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 12: ((5, ((6, 19),)), (7, ' billion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 15: ((5, ((6, 19),)), (7, ' billiard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 18: ((5, ((6, 19),)), (7, ' trillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 21: ((5, ((6, 19),)), (7, ' trilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 24: ((5, ((6, 19),)), (7, ' quadrillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 27: ((5, ((6, 19),)), (7, ' quadrilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 30: ((5, ((6, 19),)), (7, ' quintillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 33: ((5, ((6, 19),)), (7, ' quintilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 36: ((5, ((6, 19),)), (7, ' sextillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 39: ((5, ((6, 19),)), (7, ' sextilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 42: ((5, ((6, 19),)), (7, ' septillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 45: ((5, ((6, 19),)), (7, ' septilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 48: ((5, ((6, 19),)), (7, ' octillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 51: ((5, ((6, 19),)), (7, ' octilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 54: ((5, ((6, 19),)), (7, ' nonillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 57: ((5, ((6, 19),)), (7, ' nonilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 60: ((5, ((6, 19),)), (7, ' decillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 63: ((5, ((6, 19),)), (7, ' decilliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),)))}, 16: {'cents mille': 'cent mille'}, 17: {25: 'plus ...', 24: 'moins ...'}, 18: {0: {'0': ((7, 'zéro'),), '1': ((7, 'un'),), '2': ((7, 'deux'),), '3': ((7, 'trois'),), '4': ((7, 'quatre'),), '5': ((7, 'cinq'),), '6': ((7, 'six'),), '7': ((7, 'sept'),), '8': ((7, 'huit'),), '9': ((7, 'neuf'),), '10': ((7, 'dix'),), '11': ((7, 'onze'),), '12': ((7, 'douze'),), '13': ((7, 'treize'),), '14': ((7, 'quatorze'),), '15': ((7, 'quinze'),), '16': ((7, 'seize'),), '20': ((7, 'vingt'),), '30': ((7, 'trente'),), '40': ((7, 'quarante'),), '50': ((7, 'cinquante'),), '60': ((7, 'soixante'),), '80': ((7, 'quatre-vingts'),), '71': ((7, 'soixante-et-onze'),), '100': ((7, 'cent'),)}, 3: {2: OrderedDict([(__re_compile('8.'), ((7, 'quatre-vingt-'), (4, ((1, (0, 0)),)))), (__re_compile('7.'), ((7, 'soixante-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('9.'), ((7, 'quatre-vingt-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('.1'), ((4, ((1, (1, 1)), (7, '0'))), (7, '-et-un'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, ' cents'))), (__re_compile('...'), ((2, (((9,), (((1, (2, 2)),), ((7, '1'),))), ((4, ((1, (2, 2)),)),), ())), (7, ' cent '), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[fr_FR_rowlett] = {14: {23: '.', 21: None, 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, ' mille '), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' million'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' '), (2, (((8,), (((1, (0, 5)),), ((7, '0'),))), ((7, 'de'),), ())), (7, ' milliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 12: ((5, ((6, 19),)), (7, ' tetrillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 15: ((5, ((6, 19),)), (7, ' pentillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 18: ((5, ((6, 19),)), (7, ' hexillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 21: ((5, ((6, 19),)), (7, ' eptillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 24: ((5, ((6, 19),)), (7, ' oktillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 27: ((5, ((6, 19),)), (7, ' ennillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 30: ((5, ((6, 19),)), (7, ' dekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 33: ((5, ((6, 19),)), (7, ' hendekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 36: ((5, ((6, 19),)), (7, ' dodekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 39: ((5, ((6, 19),)), (7, ' trisdekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 42: ((5, ((6, 19),)), (7, ' tetradekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 45: ((5, ((6, 19),)), (7, ' pentadekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 48: ((5, ((6, 19),)), (7, ' hexadekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 51: ((5, ((6, 19),)), (7, ' heptadekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 54: ((5, ((6, 19),)), (7, ' oktadekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 57: ((5, ((6, 19),)), (7, ' enneadekillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 60: ((5, ((6, 19),)), (7, ' icosillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 63: ((5, ((6, 19),)), (7, ' icosihenillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 66: ((5, ((6, 19),)), (7, ' icosidillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 69: ((5, ((6, 19),)), (7, ' icositrillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 72: ((5, ((6, 19),)), (7, ' icositetrillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 75: ((5, ((6, 19),)), (7, ' icosipentillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 78: ((5, ((6, 19),)), (7, ' icosihexillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 81: ((5, ((6, 19),)), (7, ' icosiheptillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 84: ((5, ((6, 19),)), (7, ' icosioktillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 87: ((5, ((6, 19),)), (7, ' icosiennillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),))), 90: ((5, ((6, 19),)), (7, ' triacontillion'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (7, ' '), (5, ((6, 20),)))}, 16: {'cents mille': 'cent mille'}, 17: {25: 'plus ...', 24: 'moins ...'}, 18: {0: {'0': ((7, 'zéro'),), '1': ((7, 'un'),), '2': ((7, 'deux'),), '3': ((7, 'trois'),), '4': ((7, 'quatre'),), '5': ((7, 'cinq'),), '6': ((7, 'six'),), '7': ((7, 'sept'),), '8': ((7, 'huit'),), '9': ((7, 'neuf'),), '10': ((7, 'dix'),), '11': ((7, 'onze'),), '12': ((7, 'douze'),), '13': ((7, 'treize'),), '14': ((7, 'quatorze'),), '15': ((7, 'quinze'),), '16': ((7, 'seize'),), '20': ((7, 'vingt'),), '30': ((7, 'trente'),), '40': ((7, 'quarante'),), '50': ((7, 'cinquante'),), '60': ((7, 'soixante'),), '80': ((7, 'quatre-vingts'),), '71': ((7, 'soixante-et-onze'),), '100': ((7, 'cent'),)}, 3: {2: OrderedDict([(__re_compile('8.'), ((7, 'quatre-vingt-'), (4, ((1, (0, 0)),)))), (__re_compile('7.'), ((7, 'soixante-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('9.'), ((7, 'quatre-vingt-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('.1'), ((4, ((1, (1, 1)), (7, '0'))), (7, '-et-un'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, ' cents'))), (__re_compile('...'), ((2, (((9,), (((1, (2, 2)),), ((7, '1'),))), ((4, ((1, (2, 2)),)),), ())), (7, ' cent '), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[fr_FR_tiret] = {14: {23: '.', 21: (__re_compile('milliard[^\\s-]*'), '...-de-milliards'), 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)), (7, "-")), ())), (7, 'mille'), (2, (((9,), (((6, 20),), ((7, '0'),))), ((7, "-"), (5, ((6, 20),))), ()))), 6: ((2, (((9,), (((6, 19),), ((7, '0'),))), ((5, ((6, 19),)), (7, "-")), ())), (7, 'million'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (2, (((9,), (((6, 20),), ((7, '0'),))), ((7, "-"), (5, ((6, 20),))), ()))), 9: ((2, (((9,), (((6, 19),), ((7, '0'),))), ((5, ((6, 19),)), (7, "-")), ())), (2, (((8,), (((1, (0, 5)),), ((7, '0'),))), ((7, 'de-'),), ())), (7, 'milliard'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 's'),), ())), (2, (((9,), (((6, 20),), ((7, '0'),))), ((7, "-"), (5, ((6, 20),))), ())))}, 16: {'cents-mille': 'cent-mille'}, 17: {25: 'plus-...', 24: 'moins-...'}, 18: {0: {'0': ((7, 'zéro'),), '1': ((7, 'un'),), '2': ((7, 'deux'),), '3': ((7, 'trois'),), '4': ((7, 'quatre'),), '5': ((7, 'cinq'),), '6': ((7, 'six'),), '7': ((7, 'sept'),), '8': ((7, 'huit'),), '9': ((7, 'neuf'),), '10': ((7, 'dix'),), '11': ((7, 'onze'),), '12': ((7, 'douze'),), '13': ((7, 'treize'),), '14': ((7, 'quatorze'),), '15': ((7, 'quinze'),), '16': ((7, 'seize'),), '20': ((7, 'vingt'),), '30': ((7, 'trente'),), '40': ((7, 'quarante'),), '50': ((7, 'cinquante'),), '60': ((7, 'soixante'),), '80': ((7, 'quatre-vingts'),), '71': ((7, 'soixante-et-onze'),), '100': ((7, 'cent'),)}, 3: {2: OrderedDict([(__re_compile('8.'), ((7, 'quatre-vingt-'), (4, ((1, (0, 0)),)))), (__re_compile('7.'), ((7, 'soixante-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('9.'), ((7, 'quatre-vingt-'), (4, ((7, '1'), (1, (0, 0)))))), (__re_compile('.1'), ((4, ((1, (1, 1)), (7, '0'))), (7, '-et-un'))), (__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (7, "-"), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((4, ((1, (2, 2)),)), (7, '-cents'))), (__re_compile('...'), ((2, (((9,), (((1, (2, 2)),), ((7, '1'),))), ((4, ((1, (2, 2)),)), (7, "-")), ())), (7, 'cent-'), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}
            

INT_2_NAME[it_IT] = {14: {23: '.', 21: (__re_compile('miliard[^\\s-]*'), '... di miliardi'), 22: "l2r"}, 15: {3: ((2, (((9,), (((6, 19),), ((7, '1'),))), ((5, ((6, 19),)),), ())), (7, 'mil'), (2, (((9,), (((6, 19),), ((7, '1'),))), ((7, 'a'),), ((7, 'le'),))), (5, ((6, 20),))), 6: ((5, ((6, 19),)), (7, ' milion'), (2, (((8,), (((6, 19),), ((7, '1'),))), ((7, 'e'),), ((7, 'i'),))), (7, ' '), (5, ((6, 20),))), 9: ((5, ((6, 19),)), (7, ' miliard'), (2, (((8,), (((6, 19),), ((7, '1'),))), ((7, 'o'),), ((7, 'i'),))), (7, ' '), (5, ((6, 20),)))}, 16: {'auno': 'uno', 'iuno': 'uno', 'atre': 'atré', 'itre': 'itré', 'aott': 'ott', 'iott': 'ott', 'oott': 'ott'}, 17: {25: 'più ...', 24: 'meno ...'}, 18: {0: {'0': ((7, 'zero'),), '1': ((7, 'uno'),), '2': ((7, 'due'),), '3': ((7, 'tre'),), '4': ((7, 'quattro'),), '5': ((7, 'cinque'),), '6': ((7, 'sei'),), '7': ((7, 'sette'),), '8': ((7, 'otto'),), '9': ((7, 'nove'),), '10': ((7, 'dieci'),), '11': ((7, 'undici'),), '12': ((7, 'dodici'),), '13': ((7, 'tredici'),), '14': ((7, 'quattordici'),), '15': ((7, 'quindici'),), '16': ((7, 'sedici'),), '17': ((7, 'diciassette'),), '18': ((7, 'diciotto'),), '19': ((7, 'diciannove'),), '20': ((7, 'venti'),), '30': ((7, 'trenta'),), '40': ((7, 'quaranta'),), '50': ((7, 'cinquanta'),), '60': ((7, 'sessanta'),), '70': ((7, 'settanta'),), '80': ((7, 'ottanta'),), '90': ((7, 'novanta'),)}, 3: {2: OrderedDict([(__re_compile('..'), ((4, ((1, (1, 1)), (7, '0'))), (4, ((1, (0, 0)),))))]), 3: OrderedDict([(__re_compile('.00'), ((2, (((9,), (((1, (2, 2)),), ((7, '1'),))), ((4, ((1, (2, 2)),)),), ())), (7, 'cento'))), (__re_compile('...'), ((4, ((1, (2, 2)), (7, '00'))), (4, ((1, (1, 1)), (1, (0, 0))))))])}}}


# --------------------------------- #
# -- LIST OF ALL LANGS SUPPORTED -- #
# --------------------------------- #

ALL_LANGS = list(INT_2_NAME)

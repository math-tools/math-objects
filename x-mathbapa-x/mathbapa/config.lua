--------------------
-- CONFIGURATIONS --
--------------------

-- +/- math.huge can't be used!

-- "Volatile" codes
CODE_SPACE  = -90
CODE_LETTER = -91
CODE_DIGIT  = -92

-- Groups use codes that are opposite to indicate opening and closing character.
CODE_OPEN_PAR  = 1
CODE_CLOSE_PAR = -1

CODE_OPEN_BRACE  = 2
CODE_CLOSE_BRACE = -2

-- The priority are indicated using the value of CODE // 10 (euclidean quotient).
--
--     1) If CODE // 10 == 1, we know that we have just a variable like thing.
--     2) The first things to evaluate corresponds to the smallest code.

CATEGOS_2_NAMES = {}

-- GROUPS
NAME_CATEGO_GROUP             = 'group'
CATEGO_GROUP                  = 0
CATEGOS_2_NAMES[CATEGO_GROUP] = NAME_CATEGO_GROUP

-- SYMBOLS "LIKE"
NAME_CATEGO_SYMBOL             = 'symbol'
CODE_SYMB_INT                  = 10
CODE_SYMB_VAR                  = 11
CODE_SYMB_EMPTY                = 12 -- For the +/- sign and not ope.
CATEGO_SYMBOL                  = CODE_SYMB_INT // 10
CATEGOS_2_NAMES[CATEGO_SYMBOL] = NAME_CATEGO_SYMBOL

NAME_SIGN_MINUS   = 'sign-minus'
NAME_SIGN_PLUS    = 'sign-plus'
EMPTY_CHAR        = "@"
CONT_N_CODE_EMPTY = {
    content = EMPTY_CHAR,
    code    = CODE_SYMB_EMPTY
}

-- OPERATORS
NAME_CATEGO_OPE       = 'operator'
MIN_NB_CATEGO_FOR_OPE = CATEGO_SYMBOL + 1

NAME_CATEGO_POWER                     = 'power'
CODE_OPE_POWER                        = 20
CATEGOS_2_NAMES[CODE_OPE_POWER // 10] = NAME_CATEGO_POWER

-- FUNCTIONS "LIKE" (always with a single variable from a syntaxical point of view)
NAME_CATEGO_FUNC             = 'function'
CODE_FUNC_SIGN_MINUS         = 30
CODE_FUNC_SIGN_PLUS          = 31
CATEGO_FUNC                  = CODE_FUNC_SIGN_PLUS // 10
CATEGOS_2_NAMES[CATEGO_FUNC] = NAME_CATEGO_FUNC

NAME_CATEGO_FRAC                     = 'fraction'
CODE_OPE_FRAC                        = 70
CATEGOS_2_NAMES[CODE_OPE_FRAC // 10] = NAME_CATEGO_FRAC

NAME_CATEGO_PROD                     = 'product'
TXT_IMPLICIT_MULT                    = ''
CODE_OPE_IMPLICIT_MULT               = 80
CODE_OPE_MULT                        = 81
CATEGOS_2_NAMES[CODE_OPE_MULT // 10] = NAME_CATEGO_PROD

CONT_N_CODE_IMPLICIT_MULT = {
    content = TXT_IMPLICIT_MULT,
    code    = CODE_OPE_IMPLICIT_MULT
}

NAME_CATEGO_SUM              = 'addition'
CODE_OPE_PLUS                = 90
CODE_OPE_MINUS               = 91
CATEGO_SUM                   = CODE_OPE_PLUS // 10
CATEGOS_2_NAMES[CATEGO_SUM ] = NAME_CATEGO_SUM

-- CODE OF A CHAR.
CHARS_2_CODES = {
    -- Groups
    ['('] = CODE_OPEN_PAR,
    [')'] = CODE_CLOSE_PAR,
    ['{'] = CODE_OPEN_BRACE,
    ['}'] = CODE_CLOSE_BRACE,
    -- Add. & co.
    ['+'] = CODE_OPE_PLUS,
    ['-'] = CODE_OPE_MINUS,
    -- Prod.
    [' ']               = CODE_SPACE, -- Spaces are legal characters
    ['*']               = CODE_OPE_MULT,
    [TXT_IMPLICIT_MULT] = CODE_OPE_IMPLICIT_MULT,
    -- Fraction
    ['/'] = CODE_OPE_FRAC,
    -- Prower
    ['^'] = CODE_OPE_POWER,
}

CODES_2_CHARS = {}

for key, val in pairs(CHARS_2_CODES) do
    CODES_2_CHARS[val] = key
end

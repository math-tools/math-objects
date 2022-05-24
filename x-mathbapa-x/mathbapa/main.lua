--------------
-- SETTINGS --
--------------

require 'config'


----------------------
-- HOME MADE ERRORS --
----------------------

function throwerror(message)
    error(message)
end


-----------------
-- IDENTIFY IT --
-----------------

function isgroup(code)
    return math.abs(code) // 10 == CATEGO_GROUP
end

function issymbol(code)
    return code // 10 == CATEGO_SYMBOL
end

-- function isfunc(code)
--      return code // 10 == CATEGO_FUNC
-- end

function isope(code)
    return code // 10 >= MIN_NB_CATEGO_FOR_OPE
end

function issign(before, after, sign)
    if after == nil then
        throwerror("A single " .. sign .. " has been found.")
    end

    return before == nil or before.code == CODE_SPACE
end


---------------------
-- PARTIAL PARSING --
---------------------

function charncode(char)
-- Fixed char?
    local code = CHARS_2_CODES[char]

-- One letter? One digit?
    if code == nil then
        local byte = string.byte(char)

        if (byte >= 65 and byte <= 90)
        or (byte >= 97 and byte <= 122) then
            code = CODE_LETTER

        elseif (byte >= 48 and byte <=57) then
            code = CODE_DIGIT
        end
    end

-- Let's return our job.
    if code == nil then -- An unknonw character...
        return nil
    else
        return {content = char, code = code}
    end
end

function split_to_charncode(str)
    local chars_n_codes = {}

    for i = 1, #str do
        local char            = string.sub(str, i, i)
        local charncode_found = charncode(char)

        if charncode_found == nil then
            throwerror("Illegal character used: " .. char)
        end

        table.insert(chars_n_codes, charncode_found)
    end

    return chars_n_codes
end

function gatherchars(partial_tree, chars, code)
    if #chars ~= 0 then
        table.insert(
            partial_tree,
            {
                content = table.concat(chars),
                code    = code
            }
        )
    end

    return partial_tree
end

function findgroup(i, code, chars_n_codes)
    local nbopen       = 1
    local groupcontent = {}

    while i < #chars_n_codes and nbopen ~= 0 do
        i = i + 1

        if chars_n_codes[i].code == code then
            nbopen = nbopen + 1
        elseif chars_n_codes[i].code == -code then
            nbopen = nbopen - 1
        end

        if nbopen ~= 0 then
            groupcontent[#groupcontent + 1] = chars_n_codes[i]
        end
    end

    if nbopen ~= 0 then
        throwerror(
            "Opening group "
            .. CODES_2_CHARS[code] ..
            " used without its corresponding closing group "
            .. CODES_2_CHARS[-code] .. "."
        )
    end

    return i, partial_parser(groupcontent)
end

function partial_parser(chars_n_codes)
    local partial_tree = {}

    local last_letters = {}
    local last_digits  = {}

-- Let's go!
    local i = 0

-- Remove leading spaces...
    local starting_spaces = true

    while starting_spaces and i < #chars_n_codes do
        i          = i + 1
        local code = chars_n_codes[i].code

        starting_spaces = (code == CODE_SPACE)
    end

-- For the +/- sign and not ope.
    if chars_n_codes[i].code == CODE_OPE_PLUS
    or chars_n_codes[i].code == CODE_OPE_MINUS then
        partial_tree = {CONT_N_CODE_EMPTY}
    end

-- Let's continue...
    while i <= #chars_n_codes do
        local code = chars_n_codes[i].code

-- We gather letters to make a symbol (only var names are supported for the moment).
        if code == CODE_LETTER then
            partial_tree = gatherchars(
                partial_tree,
                last_digits,
                CODE_SYMB_INT
            )
            last_digits = {}

            table.insert(last_letters, chars_n_codes[i].content)

-- We gather digits to make a natural number (only integers are supported for the moment).
        elseif code == CODE_DIGIT then
            partial_tree = gatherchars(
                partial_tree,
                last_letters,
                CODE_SYMB_VAR
            )
            last_letters = {}

            table.insert(last_digits, chars_n_codes[i].content)

-- We don't have neither a letter, nor a digit.
        else
-- Before we can have one symbol (x)or an integer.
            partial_tree  = gatherchars(
                partial_tree,
                last_digits,
                CODE_SYMB_INT
            )
            last_digits = {}

            partial_tree = gatherchars(
                partial_tree,
                last_letters,
                CODE_SYMB_VAR
            )
            last_letters = {}

-- We ignore spaces.
            if code ~= CODE_SPACE then
-- Groups are treated recursively.
                if isgroup(code) then
-- A negative grouping code indicate an isolated closing groups !
                    if code < 0 then
                        throwerror(
                            "Closing group "
                            .. CODES_2_CHARS[code] ..
                            " used without its corresponding opening group "
                            .. CODES_2_CHARS[-code] .. "."
                        )

                    else
-- Searching for the end of the group...
                        i, groupcontent = findgroup(i, code, chars_n_codes)

                        table.insert(
                            partial_tree,
                            {content = groupcontent, code = code}
                        )
                    end

-- An operator
                else
-- One operator can't be preceded by another one !
                    if i ~= 1 and isope(chars_n_codes[i-1].code) then
                        throwerror(
                            "Two following operators " ..
                            chars_n_codes[i-1].content ..
                            chars_n_codes[i].content ..
                            " have been found."
                        )
                    end

                    table.insert(partial_tree, chars_n_codes[i])
                end
            end
        end

-- Goto the next char...
        i = i + 1
    end

-- The formula can finish with one symbol (x)or an integer.
    partial_tree  = gatherchars(
        partial_tree,
        last_digits,
        CODE_SYMB_INT
    )
    last_digits = {}

    partial_tree = gatherchars(
        partial_tree,
        last_letters,
        CODE_SYMB_VAR
    )
    last_letters = {}

-- The job is finished...
    return partial_tree
end


----------------------
-- COMPLETE PARSING --
----------------------

function addimplicitmult(i, lastcode)
    return i ~= 1 and (not isope(lastcode)) --and (not isfunc(lastcode))
end

function complete_tree_main_category(partial_tree)
    local tree = {}

    local lastcode      = - math.huge
    local main_category = - math.huge

    local implicit_category = CODE_OPE_IMPLICIT_MULT // 10

    local i = 0

    while i < #partial_tree do
        i = i + 1

        local code    = partial_tree[i].code
        local content = partial_tree[i].content

-- We have an operator.
        if isope(code) then
-- A +/- sign?
            if issign(
                partial_tree[i - 1],
                partial_tree[i + 1],
                content
            ) then
                if content == "+" then
                    code = CODE_FUNC_SIGN_PLUS
                else
                    code = CODE_FUNC_SIGN_MINUS
                end

                partial_tree[i].code = code
            end

            current_category = code // 10

            if main_category < current_category then
                main_category = current_category
            end

-- We have a group, a function, a variable or an integer after an implicit product.
        elseif addimplicitmult(i, lastcode) then
            table.insert(tree, CONT_N_CODE_IMPLICIT_MULT)

            if main_category < implicit_category then
                main_category = implicit_category
            end
        end

-- A group.
        if isgroup(code) then
            _, partial_tree[i].content = complete_tree_main_category(
                partial_tree[i].content
            )
        end

-- Insert the current (changed?) piece.
        table.insert(tree, partial_tree[i])

-- New last code...
        lastcode = code
    end

-- The job has been done.
    if main_category == - math.huge then
        main_category = CATEGO_SYMBOL
    end

    return main_category, tree
end

function find_main_catego(partial_tree)
    local main_code = - math.huge
    local i = 0
    local code

    while i < #partial_tree do
        i = i + 1

        code = partial_tree[i].code

        if main_code < code then
            main_code = code
        end
    end

    if main_code < 10 then
        main_code = 10
    end

    return main_code // 10
end

function parser(main_category, tree)
-- One symbol or one group.
    if main_category <= CATEGO_SYMBOL then  -- BUG de find_main_catego
        if isgroup(tree[1].code) then
            return {
                catego = CATEGO_GROUP,
                type   = tree[1].code,
                group  = parser(
                    find_main_catego(tree[1].content),
                    tree[1].content
                )
            }

        else
            return {
                catego = CATEGO_SYMBOL,
                type   = tree[1].code,
                symbol = tree[1].content
            }
        end
    end

-- One function.
    -- if main_category == CATEGO_FUNC then
    --     return {
    --         catego = CATEGO_FUNC,
    --         type   = tree[1].code,
    --         arg    = parser(CATEGO_SYMBOL, {tree[2]})
    --     }
    -- end

-- At least one operator is used, we have to find ist arguments.
    local tags        = {}
    local args        = {}
    local current_arg = {}

    local main_catego_current_arg = - math.huge

    for i = 1, #tree do
        category = tree[i].code // 10

        if category == main_category then
            table.insert(tags, CODES_2_CHARS[tree[i].code])
            table.insert(
                args,
                parser(main_catego_current_arg, current_arg)
            )

            current_arg             = {}
            main_catego_current_arg = - math.huge

        else
            if main_catego_current_arg < category then
                main_catego_current_arg = category
            end

            table.insert(current_arg, tree[i])
        end
    end

    if current_arg ~= {} then
        table.insert(
            args,
            parser(main_catego_current_arg, current_arg)
        )
    end

-- We have to take care of the +/- sign and not ope.
    if main_category == CATEGO_SUM
    and args[1].catego == CATEGO_SYMBOL
    and args[1].type == CODE_SYMB_EMPTY then
        local funcname

        if tags[1] == "+" then
            funcname = NAME_SIGN_PLUS
        else
            funcname = NAME_SIGN_MINUS
        end

        local newfirsttarg = {
            catego   = CATEGO_FUNC,
            funcname = funcname,
            arg      = args[2]
        }

-- Just a single argument with a sign before.
        if #args == 2 then
            return newfirsttarg
        end

-- The sign eats the first argument.
        args[1] = newfirsttarg

        for i = 2, #args - 1 do
            args[i] = args[i + 1]
        end

        args[#args] = nil

        for i = 1, #tags - 1 do
            tags[i] = tags[i + 1]
        end

        tags[#tags] = nil
    end

    return {
        catego   = main_category,
        opename  = CATEGOS_2_NAMES[main_category],
        tags     = tags,
        args     = args
    }
end


--------------------
-- MAIN FUNCTIONS --
--------------------

function calctree(formula)
    local chars_n_codes                 = split_to_charncode(formula)
    local partial_tree                  = partial_parser(chars_n_codes)
    local main_category, completed_tree = complete_tree_main_category(partial_tree)
    local tree                          = parser(main_category, completed_tree)

    return tree
end

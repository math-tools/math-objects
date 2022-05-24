-----------------------
-- IMPORT THE MODULE --
-----------------------

-- See: https://stackoverflow.com/a/46390210/4589608
package.path =  "../mathbapa/?.lua;" .. package.path

require 'main'


-----------------
-- DEBUG TOOLS --
-----------------

function debugprint_partial_tree(partial_tree)
    for i = 1, #partial_tree do
        if isgroup(partial_tree[i].code) then
            print('>> OPEN GROUP : ' .. partial_tree[i].code)
            debugprint_partial_tree(partial_tree[i].content)
            print('<< CLOSE GROUP: ' .. partial_tree[i].code)

        else
            if partial_tree[i].code // 10 >= MIN_NB_CATEGO_FOR_OPE then
                extra = " <--> " .. CODES_2_CHARS[partial_tree[i].code]
            else
                extra = ""
            end

            print(
                tostring(partial_tree[i].content),
                " --> ",
                partial_tree[i].code .. extra
            )
        end
    end
end

function debugprint_tree(tree)
    if tree.catego == CATEGO_SYMBOL then
        print('LEAF', tree.symbol .. "   [" .. tree.type .. "]")

    elseif tree.catego == CATEGO_GROUP then
        print('GROUP  [' .. tree.type .. "]")
        debugprint_tree(tree.group)

    elseif tree.catego == CATEGO_FUNC then
        print('FUNC  [' .. tree.funcname .. "]")
        debugprint_tree(tree.arg)

    else
        print('OPE-NAME  [' .. tree.opename .. ']')
        print('OPE-NAME  [' .. tree.opename .. ']  -  Tags : | '
           .. table.concat(tree.tags, " | ") .. ' |')

        for i = 1, #tree.args do
            print('OPE-NAME  [' .. tree.opename .. ']  -  ARG.' .. i)
            debugprint_tree(tree.args[i])
        end
    end
end

function debug(formula)
    print('')
    print('##################')
    print('## PARTIAL TREE ##')
    print('##################')
    print('')
    --
    local chars_n_codes = split_to_charncode(formula)
    local partial_tree  = partial_parser(chars_n_codes)
    --
    debugprint_partial_tree(partial_tree)

    print('')
    print('####################')
    print('## COMPLETED TREE ##')
    print('####################')
    print('')
    --
    local main_category, completed_tree = complete_tree_main_category(partial_tree)
    --
    print('MAIN CATEGORY = ' .. main_category .. " : " .. CATEGOS_2_NAMES[main_category])
    print('')
    debugprint_partial_tree(completed_tree)

    print('')
    print('##########')
    print('## TREE ##')
    print('##########')
    print('')
    --
    local tree = parser(main_category, completed_tree)
    --
    debugprint_tree(tree)
end


-------------
-- NEW PB! --
-------------

-- ????


----------------
-- HAND TESTS --
----------------

-- debug("a")
-- debug("-a")

-- debug("2a")
-- debug("2*a")
-- debug("-2a")
-- debug("2^a")
-- debug("-2^a")
-- debug("2 + a")
-- debug("-2 + a")

-- debug("2 + a+b")
debug("2a+b")
-- debug("-2a+b-c")
-- debug("2a  +   b  ^2")
-- debug("2a + b*c^2  - d")
-- debug("-2a + b*c^2  - d")

-- debug("(a)")
-- debug("(-a)")
-- debug("(a+b)")
-- debug("(a^b)")
-- debug("(a*b)")
-- debug("(2a)")
-- debug("((b))")
-- debug("(((b)))")
-- debug("((a*b))")

-- debug("2+(a)")
-- debug("2(a+b)^2")
-- debug("(b + {c})")
-- debug("(b + {-c})")
-- debug("(b + {c+v})")
-- debug("(a + {-2 + b})")
-- debug("2(a + {-2 + b})")
-- debug("2(a + {  -2 + b}) + 4/5")
-- debug("abcd( b   + { 1 + c})123r/2")
-- debug("abcd( b   + {-1 + c})+123r/2")
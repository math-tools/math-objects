-----------------------
-- IMPORT THE MODULE --
-----------------------

-- See: https://stackoverflow.com/a/46390210/4589608
package.path =  "../?.lua;" .. package.path
main         = require 'main'


-------------------
-- ASCII PRINTER --
-------------------

function asciiformula(formula)
    local tree = main.calctree(formula)

    return _asciiformula_rec(tree, 0)
end


function _asciiformula_rec(tree)
    if tree.symbol then
        return tree.symbol
    end

    if tree.group then
        return table.concat({
            CODES_2_CHARS[tree.type],
            _asciiformula_rec(tree.group),
            CODES_2_CHARS[-tree.type],
        })
    end

    if tree.funcname then
        local funcname

        if tree.funcname == NAME_SIGN_MINUS then
            funcname = '-'
        else
            funcname = tree.funcname .. " "
        end

        return table.concat({
            funcname,
            _asciiformula_rec(tree.arg),
        })
    end

    local txt = {}
    local ope = nil

    for i = 1, #tree.args do
        table.insert(txt, _asciiformula_rec(tree.args[i]))

        if i <= #tree.tags then
            if tree.tags[i] == TXT_IMPLICIT_MULT then
                ope = {" "}

            elseif tree.tags[i] == "+" or tree.tags[i] == "-" then
                ope = {" ", tree.tags[i], " "}

            else
                ope = {tree.tags[i]}
            end

            ope = table.concat(ope)
            table.insert(txt, ope)
        end
    end

    return table.concat(txt)
end

function asciitree(formula)
    local tree = main.calctree(formula)

    _asciitree_rec(tree, 0)
end

function _asciitree_rec(tree, level)
    local tab    = string.rep(" ", level*4)
    local subtab = table.concat({tab, "    "})

    if tree.symbol then
        print(tab .. tree.symbol)

    elseif tree.group then
        print(tab .. CODES_2_CHARS[tree.type] .. '..' .. CODES_2_CHARS[-tree.type])
        _asciitree_rec(tree.group, level + 1)

    elseif tree.funcname then
        print(tab .. tree.funcname .. '(..)')
        _asciitree_rec(tree.arg, level + 1)

    else
        print(tab .. tree.opename)

        for i = 1, #tree.args do
            _asciitree_rec(tree.args[i], level + 1)

            if i <= #tree.tags then
                print(subtab .. "[" .. tree.tags[i] .. "]")
            end
        end
    end
end

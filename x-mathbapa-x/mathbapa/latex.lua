-----------------------
-- IMPORT THE MODULE --
-----------------------

-- See: https://stackoverflow.com/a/46390210/4589608
package.path =  "../?.lua;" .. package.path
main         = require 'main'


--------------------------
-- LATEX/FOREST PRINTER --
--------------------------

function latexformula(formula)
    error("NOT IMPLEMENTED")
    local tree = main.calctree(formula)

    return _latex_rec(tree, 0)
end

function _latex_rec(tree)
    if tree.symbol then
        return tree.symbol
    end

    if tree.group then
        return table.concat({
            CODES_2_CHARS[tree.type],
            _latex_rec(tree.group),
            CODES_2_CHARS[-tree.type],
        })
    end

    if tree.funcname then
        return table.concat({
            tree.funcname,
            _latex_rec(tree.arg),
        })
    end

    local txt = {}
    local ope = nil

    for i = 1, #tree.args do
        table.insert(txt, _latex_rec(tree.args[i]))

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

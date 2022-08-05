#!/usr/bin/env python3

# ------------------- #
# -- FOR TEMPLATES -- #
# ------------------- #

TABU_PROTO  = '\n# ' + ' '*4
TABU_METH_2 = '\n'   + ' '*8
TABU_METH_3 = '\n'   + ' '*12
TABU_METH_4 = '\n'   + ' '*16
TABU_DECO   = '\n'   + ' '*(4 + len("@deco_callof_nat("))

TEMP_PROTOTYPE = """
###
# prototype::
#     {see_params}
#
#     :return: {see_return}
###
""".strip()

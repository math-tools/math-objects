#!/usr/bin/env python3

from ..rules import *

from .extend    import *
from .normalize import *
from .pyfile    import *

from pprint import pformat

# ! -- DEBUGGING -- ! #
# from pprint import pprint
# ! -- DEBUGGING -- ! #



# -------------------------------------- #
# --  BUILD OF THE CONGIG PYTHON FILE -- #
# -------------------------------------- #

def pythonify(
    debug_coding,
    alltrans,
    srcdir_file
):
# ! -- DEBUGGING -- ! #
    # pprint(alltrans['debug_DEBUG']);exit()
# ! -- DEBUGGING -- ! #

    alltrans = manage_extend(alltrans)
    alltrans = normalize_rules(alltrans)

    code = pycode(debug_coding, alltrans)

    srcdir_file.create("file")

    with srcdir_file.open(
        encoding = 'utf-8',
        mode     = 'w',
    ) as f:
        f.write(
            f"""
#!/usr/bin/env python3

# ---------------------------------------------------------------- #
# --  This code was automatically build by the following file.  -- #
# --                                                            -- #
# --      + ``tools/factory/de-textify/build_tr.py``            -- #
# --                                                            -- #
# --  See the project ``cvnum`` in the mono repository          -- #
# --  ``math-objects`` for more informations.                   -- #
# --                                                            -- #
# --      + https://github.com/math-tools/math-objects          -- #
# ---------------------------------------------------------------- #

from collections import OrderedDict
from re          import compile as __re_compile


{code}
            """.strip()
            +
            '\n'
        )

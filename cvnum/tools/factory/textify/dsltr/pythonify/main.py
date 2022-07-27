#!/usr/bin/env python3

from ..rules import *

from .desc    import *
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
    srcdir_file,
    buildfile_relpath
):
    # ! -- DEBUGGING -- ! #
    # pprint(alltrans['debug_DEBUG']);exit()
    # ! -- DEBUGGING -- ! #

    alldescs = extracts_desc(alltrans)

    # ! -- DEBUGGING -- ! #
    # pprint(alltrans['en_US']['small'].keys());exit()
    # ! -- DEBUGGING -- ! #

    alltrans = manage_extend(alltrans)

    # ! -- DEBUGGING -- ! #
    # pprint(alltrans['en_US']['small'].keys());exit()
    # ! -- DEBUGGING -- ! #

    alltrans = normalize_rules(alltrans)

    # ! -- DEBUGGING -- ! #
    # for v in alltrans.values():
    #     pprint(v.get('extend', None))
    # exit()
    # ! -- DEBUGGING -- ! #

    code = pycode(debug_coding, alltrans, alldescs)

    srcdir_file.create("file")

    with srcdir_file.open(
        encoding = 'utf-8',
        mode     = 'w',
    ) as f:
        f.write(
            f"""
#!/usr/bin/env python3

# This code was automatically build by the following file.
#
#     + ``{buildfile_relpath}``

from collections import OrderedDict
from re          import compile as __re_compile


{code}
            """.strip()
            +
            '\n'
        )

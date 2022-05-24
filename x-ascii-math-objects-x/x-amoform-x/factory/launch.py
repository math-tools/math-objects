#!/usr/bin/env python3

# ----------------- #
# -- EXTRA TOOLS -- #
# ----------------- #

from mistool.os_use import (
    cd,
    PPath,
    runthis
)


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_FILE = PPath(__file__)
THIS_DIR  = THIS_FILE.parent


# -------------------------------------- #
# -- LAUNCHING ALL THE BUILDING TOOLS -- #
# -------------------------------------- #

for onepath in THIS_DIR.walk("file::**build_*.py"):
    with cd(THIS_DIR):
        print('+ Launching "{0}"'.format(onepath.name))

        runthis(
            cmd        = 'python "{0}"'.format(onepath),
            showoutput = True
        )

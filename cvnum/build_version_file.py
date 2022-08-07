#!/usr/bin/env python3

import re

from mistool.os_use import PPath

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath(__file__).parent

CHGES_DIR    = THIS_DIR / "changes"
VERSION_FILE = THIS_DIR / "VERSION.txt"


# ----------- #
# -- TOOLS -- #
# ----------- #

PATTERN_TITLE = re.compile("\n==\n(\d+.*)\n==\n")

MEANING = ['major', 'minor', 'patch', 'extra']

def easyversion(version, infos):
    version = version.strip()
    parts   = version.split('.')

    assert len(parts) == 3, \
           (
            f'invalid version number ``{version}``: '
             '3 dots must be used.'
             '\n' + infos
           )

    about = {
        'full': version
    }

    for i, p in enumerate(parts):
        if i == 4:
            ...

        else:
            assert p.isdigit(), \
                   (
                    f'invalid {MEANING[i]} number: {p}.'
                    '\n' + infos
                   )

        about[MEANING[i]] = p

    if not MEANING[-1] in about:
        about[MEANING[-1]] = ''

    return about


# --------------------- #
# -- FIND VERSION NB -- #
# --------------------- #

print(f"   * Looking for the version nb. in the change log.")

versions_found = {}

chge_files = [
    f
    for f in CHGES_DIR.walk('file::**')
    if(f.stem.isdigit())
]

chge_files.sort()
chge_files.reverse()

for path in chge_files:
    with path.open(
        encoding = 'utf-8',
        mode     = 'r',
    ) as f:
        content = f.read()

    year  = path.parent.name
    month = path.stem

    titles = re.findall(
        PATTERN_TITLE,
        content
    )

    if titles is None:
        continue

    for t in titles:
        t = t.strip()

        infos = (
            f'See the title ``{t}`` in the file '
            f'changes/{year}/{month}.txt'
        )

        if not '(' in t:
            continue

        assert t[-1] == ')', \
               (
                 'missing ``)`` at the end.'
                 '\n' + infos
               )

        day, *version = t.split('(')

        assert len(version) == 1, \
               (
                 'invalid number of ``(``.'
                 '\n' + infos
               )

        version = version[0]
        version = version[:-1].strip()

        aboutversion = easyversion(
            version = version,
            infos   = infos
        )

        day  = day.strip()
        date = f"{year}-{month}-{day}"

        assert date not in versions_found, \
               (
                 'date ``{date}`` already used.'
                 '\n'
                f'See the title ``{t}`` in the file '
                f'changes/{year}/{month}.txt'
               )

        versions_found[date] = aboutversion


# ! -- DEBUGGING -- ! #
from pprint import pprint
pprint(versions_found)
# ! -- DEBUGGING -- ! #

#!/usr/bin/env python3

from json import dumps
import re

from semantic_version import Version

from mistool.os_use import PPath

# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #


# --------------- #
# -- CONSTANTS -- #
# --------------- #

SRC_DIR = PPath(__file__)

while SRC_DIR.name != "cvnum":
    SRC_DIR = SRC_DIR.parent

CHGES_DIR    = SRC_DIR / "changes"
VERSION_FILE = SRC_DIR / "VERSION.json"


# ----------- #
# -- TOOLS -- #
# ----------- #

PATTERN_TITLE = re.compile("\n==\n(\d+.*)\n==\n")

MEANING_VERSION_PARTS = ['major', 'minor', 'patch', 'prerelease']
MEANING_DATE          = ['year', 'month', 'date']


# ---------------------- #
# -- CHANGE LOG FILES -- #
# ---------------------- #

print(f"   * Looking for the version NB. in the change log.")

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
        version = Version(version)

        day  = day.strip()
        date = (year, month, day)

        assert date not in versions_found, \
               (
                 'date ``{date}`` already used.'
                 '\n'
                f'See the title ``{t}`` in the file '
                f'changes/{year}/{month}.txt'
               )

        versions_found[date] = {
            m: version.__getattribute__(m)
            for m in MEANING_VERSION_PARTS
        }

        versions_found[date]['full'] = str(version)


# ! -- DEBUGGING -- ! #
# from pprint import pprint
# pprint(versions_found)
# exit()
# ! -- DEBUGGING -- ! #


# --------------------- #
# -- LAST VERSION NB -- #
# --------------------- #

print(f"   * Update of the file ``VERSION.json``.")

if not versions_found:
    about_version = {}

else:
    for date, infos in versions_found.items():
        about_version = infos

        about_version['date'] = {
            m: date[i]
            for i, m in enumerate(MEANING_DATE)
        }


        break

content = dumps(about_version)

with VERSION_FILE.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(content)


if about_version:
    what = "last"
    xtra = f": {about_version['full']}"

else:
    what = "no"
    xtra = ''

print(f"   * {what.title()} version NB. found{xtra}.")

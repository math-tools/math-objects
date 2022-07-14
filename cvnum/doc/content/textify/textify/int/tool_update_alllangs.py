#!/usr/bin/env python3

from mistool.os_use     import PPath
from mistool.string_use import between


# ! -- DEBUGGING -- ! #
# Clear the terminal.
print("\033c", end="")
# ! -- DEBUGGING -- ! #

print(f"   * Updating the list of langs in the doc.")


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR      = PPath(__file__).parent
LANG_DOC_FILE = THIS_DIR / "lang.txt"

LANG_CONFIG_FILE = THIS_DIR

while(LANG_CONFIG_FILE.name != "cvnum"):
    LANG_CONFIG_FILE = LANG_CONFIG_FILE.parent

LANG_CONFIG_FILE = \
LANG_CONFIG_FILE / "src" / "config" / "textify" / "langint.py"


# ----------------------- #
# -- CODES FOR THE DOC -- #
# ----------------------- #

with LANG_CONFIG_FILE.open(
    mode     = "r",
    encoding = "utf-8",
) as f:
    pycontent = f.read()

_, codefromconfig, _ = between(
    text = pycontent,
    seps = [
        "# -- TAGS FOR LANGS -- #",
        "# -- ",
    ],
)

langsfordoc = []

for oneline in codefromconfig.splitlines():
    if '--' in oneline:
        continue

    langsfordoc.append(oneline)

langsfordoc = "\n    ".join(langsfordoc)
langsfordoc = langsfordoc.strip()


filepathfordoc = PPath()

while(LANG_CONFIG_FILE.name != "src"):
    filepathfordoc   = LANG_CONFIG_FILE.name / filepathfordoc
    LANG_CONFIG_FILE = LANG_CONFIG_FILE.parent


codefordoc = f"""
python::
    ---
    file    = {filepathfordoc}
    extract = yes
    ---

    {langsfordoc}
"""


# -------------------- #
# -- UPDATE THE DOC -- #
# -------------------- #

with LANG_DOC_FILE.open(
    mode     = "r",
    encoding = "utf-8",
) as f:
    txtcontent = f.read()

# print(txtcontent)

before, _, after = between(
    text = txtcontent,
    seps = [
        "// -- ALL LANGS - START -- //",
        "// -- ALL LANGS - END -- //",
    ],
    keepseps = True,
)

txtcontent = f"""
{before}
{codefordoc}
{after}
""".strip() + "\n"

with LANG_DOC_FILE.open(
    mode     = "w",
    encoding = "utf-8",
) as f:
    f.write(txtcontent)

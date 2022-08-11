#!/usr/bin/env python3

from json import load

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


VERSION_FILE = SRC_DIR / "VERSION.json"

README_FILE = SRC_DIR / "readme" / "last.md"
POETRY_FILE = SRC_DIR / "pyproject.toml"
INIT_FILE   = SRC_DIR / "src" / "__init__.py"


# ---------------------- #
# -- LAST NB. VERSION -- #
# ---------------------- #

print(f"   * Loading last version NB. found.")

with VERSION_FILE.open(
    encoding = "utf-8",
    mode     = "r",
) as f:
    about_version = load(f)


version_nb_found = bool(about_version)

if version_nb_found:
    version_full = about_version['full']


if version_nb_found:
    what = "last"
    xtra = f": {version_full}"

else:
    what = "no"
    xtra = ''

print(f"   * {what.title()} version NB. found{xtra}.")


# ------------------- #
# -- UPDATE README -- #
# ------------------- #

print(f"   * Update of the README file.")

TEMPLATE_NO_NB = """
Last version
------------

For the moment, there is no version number.
""".strip() + "\n"


TEMPLATE_WITH_NB = """
Last version: {version}
--------------{decotitle}

This version **{version}** was made on **{date}** .
""".strip() + "\n"


if version_nb_found:
    decotitle = '-'*len(version_full)
    date      = '-'.join(about_version['date'].values())

    content = TEMPLATE_WITH_NB.format(
        version   = version_full,
        decotitle = decotitle,
        date      = date,
    )

else:
    content = TEMPLATE_NO_NB


with README_FILE.open(
    encoding = "utf-8",
    mode     = "w",
) as f:
    f.write(content)


# ----------------------------- #
# -- UPDATE POETRY, SRC INIT -- #
# ----------------------------- #

for param, info, path in [
    (
        'version',
        "Update of the POETRY TOML file.",
        POETRY_FILE
    ),
    (
        '__version__',
        "Update of the __init__.py in the source folder.",
        INIT_FILE
    ),
]:
    print(f"   * {info}.")


    with path.open(
        encoding = "utf-8",
        mode     = "r",
    ) as f:
        content = f.read()

    if version_nb_found:
        new_content = []

        for line in content.split('\n'):
            for pref in ['', '#']:
                if line.startswith(f'{pref}{param}'):
                    if pref:
                        line = line[1:]

                    version_txt, _, version_nb = line.partition('=')

                    line = f'{version_txt}= "{version_full}"'

            new_content.append(line)

        new_content = '\n'.join(new_content)

    else:
        new_content = content.replace(
            f'\n{param}',
            f'\n#{param}'
        )


    with path.open(
        encoding = "utf-8",
        mode     = "w",
    ) as f:
        f.write(new_content)

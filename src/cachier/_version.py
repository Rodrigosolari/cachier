# This file is part of Cachier.
# https://github.com/python-cachier/cachier

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2024, Jirka Borovec <***@gmail.com>

import os
from version import VERSION

_RELEASING_PROCESS = os.getenv("RELEASING_PROCESS", "0") == "1"

__version__ = VERSION


def _get_git_sha() -> str:
    from subprocess import DEVNULL, check_output

    out = check_output(["git", "rev-parse", "--short", "HEAD"], stderr=DEVNULL)  # noqa: S603, S607
    return out.decode("utf-8").strip()


if not _RELEASING_PROCESS:
    try:
        sha_short = _get_git_sha()
        # print(f"Version enriched with git commit hash: {__version__}.")
    except Exception:
        # print("Failed to get the git commit hash,"
        #       f" falling back to base version {__version__}.")
        sha_short = ""
    __version__ += f".dev+{sha_short}" if sha_short else ".dev"


__all__ = ["__version__"]

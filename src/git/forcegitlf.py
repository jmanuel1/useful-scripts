# NOTE Dependencies: Python 3.5+, Git

import subprocess
import os

from typing import Iterable, cast


def git(*args: str) -> Iterable[str]:
    process: subprocess.CompletedProcess = subprocess.run(
        ['git'] + list(args),
        stdout=subprocess.PIPE,
        encoding='utf8'
    )
    return cast(str, process.stdout).split('\n')


def delete_all_tracked_files() -> None:
    for file in git('ls-tree', '-r', 'HEAD', '--name-only'):
        os.remove(file)


git('config', 'core.eol', 'LF')
git('config', 'core.autocrlf', 'input')

delete_all_tracked_files()

os.remove('.git/index')
git('reset')
git('checkout-index', '--force', '--all')

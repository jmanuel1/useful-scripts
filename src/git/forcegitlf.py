import subprocess
import os


def git(*args):
    process = subprocess.run(['git'] + list(args),
                             stdout=subprocess.PIPE, encoding='utf8')
    return process.stdout.split('\n')


def delete_all_tracked_files():
    for file in git('ls-tree', '-r', 'HEAD', '--name-only'):
        os.remove(file)


git('config', 'core.eol', 'LF')
git('config', 'core.autocrlf', 'input')

delete_all_tracked_files()

os.remove('.git/index')
git('reset')
git('checkout-index', '--force', '--all')

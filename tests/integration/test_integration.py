import subprocess

import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
ROOT_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, '../..'))


def test_cli_prints_reduced_list():
    result = subprocess.run(
        ['bin/find_failure.py', 'bin/dependency_failer_cli.py 2', '1', '2', '3', '4', '5', '6', '7'],
        cwd=ROOT_DIR,
        capture_output=True,
        encoding='utf-8',
    )
    assert result.returncode == 0
    assert result.stdout.strip().split('\n')[-1] == '[\'2\', \'7\']'

#!/usr/bin/env python3
import argparse
import shlex
import subprocess
from typing import List

# dumb hack for pythonpath
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, '..')))

from failure_finder import reduce_to_smallest_failing_list


class CLIRunner:
    def __init__(self, command: str, tests: List[str]):
        self.command = command
        self.tests = tests

    def test_fn(self, items: List[str]) -> bool:
        process = subprocess.run(shlex.split(self.command) + items, cwd=os.getcwd())
        return process.returncode == 0

    def run(self):
        reduced_list = reduce_to_smallest_failing_list(self.test_fn, self.tests)
        print(reduced_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        help='Command to run tests to which the list of files will be appended',
    )
    parser.add_argument(
        'tests',
        help='The list of test files producing an error, in order, with the failing test last',
        nargs=argparse.REMAINDER,
    )
    args = parser.parse_args()
    runner = CLIRunner(command=args.command, tests=args.tests)
    runner.run()

#!/usr/bin/env python3

import argparse
# dumb hack for pythonpath
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, '..')))

from tests.utils import DependencyFailer

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'problem_id',
        help='file that causes the problem',
    )
    parser.add_argument(
        'tests',
        help='files to test',
        nargs=argparse.REMAINDER,
    )
    args = parser.parse_args()
    failer = DependencyFailer(args.tests[-1], args.problem_id)
    if not failer(args.tests):
        raise Exception('it failed!')
    print('passed!')

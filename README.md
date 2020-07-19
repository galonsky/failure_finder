# failure_finder [![circle](https://circleci.com/gh/galonsky/failure_finder.svg?style=svg)](https://circleci.com/gh/galonsky/failure_finder)
narrows down failures in dependent test failures

## Example usage

Say you have a failure in a certain test when run with a bunch of other tests: `test123.py` fails when run after these other tests: `docker-compose run --rm tests pytest test456.py testfoo.py testbar.py test123.py`

In order to narrow down the offending test, you can run:

    ./bin/find_failure.py "docker-compose run --rm tests pytest" test456.py testfoo.py testbar.py test123.py
    
This will divide and conquer the tests until it narrows down to two files, which it will print.

Note that the program assumes the last test in the list is the failing test you're targeting.

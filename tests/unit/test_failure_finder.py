from failure_finder import reduce_to_smallest_failing_list
from tests.utils import DependencyFailer


class TestReduceToSmallestFailingList:
    def test_when_two_items_returns_two_items(self):
        assert reduce_to_smallest_failing_list(lambda l: False, [1, 2]) == [1, 2]

    def test_three_items_last_two_are_problem(self):
        items = [1, 2, 3]
        tester = DependencyFailer(3, 2)
        assert reduce_to_smallest_failing_list(tester, items) == [2, 3]

    def test_three_items_first_and_last_are_problem(self):
        items = [1, 2, 3]
        tester = DependencyFailer(3, 1)
        assert reduce_to_smallest_failing_list(tester, items) == [1, 3]

    def test_lots_of_items_last_two_are_problems(self):
        items = [8] * 60 + [1, 3]
        tester = DependencyFailer(3, 1)
        assert reduce_to_smallest_failing_list(tester, items) == [1, 3]

    def test_lots_of_items_first_and_last_are_problems(self):
        items = [1] + [8] * 60 + [3]
        tester = DependencyFailer(3, 1)
        assert reduce_to_smallest_failing_list(tester, items) == [1, 3]

    def test_lots_of_items_problem_in_middle(self):
        items = [8] * 60 + [1] + [9] * 60 + [3]
        tester = DependencyFailer(3, 1)
        assert reduce_to_smallest_failing_list(tester, items) == [1, 3]
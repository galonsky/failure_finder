from typing import TypeVar, Callable, List

T = TypeVar('T')


def reduce_to_smallest_failing_list(test_fn: Callable[[List[T]], bool], failing_list: List[T]) -> List[T]:
    """
    Given a list of items in order that produce a failure, reduce the list to the smallest possible failing list (size 2)
    :param test_fn: function that takes in a list of items and returns true or false
    :param failing_list: list of items with the target test at the end
    :return: reduced list of items
    """
    if len(failing_list) <= 2:
        return failing_list
    # half it
    cutoff_index = len(failing_list) // 2
    second_half = failing_list[cutoff_index:]
    result = test_fn(second_half)

    if result:
        # everything in second_half can be eliminated besides the target
        first_half_plus_target = failing_list[:cutoff_index] + [second_half[-1]]
        return reduce_to_smallest_failing_list(test_fn, first_half_plus_target)
    else:
        return reduce_to_smallest_failing_list(test_fn, second_half)

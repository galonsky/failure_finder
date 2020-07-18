from typing import List


class DependencyFailer:
    def __init__(self, target_id, problem_id):
        self.target_id = target_id
        self.problem_id = problem_id

    def __call__(self, items: List) -> bool:
        target_index = items.index(self.target_id)
        try:
            problem_index = items.index(self.problem_id)
            return target_index < problem_index
        except ValueError:
            return True

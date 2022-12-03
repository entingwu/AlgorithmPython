from typing import (
    List,
)

class CombinationSum:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
             we will sort your return value in output
    """
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        results = []
        candidates = sorted(list(set(candidates)))
        self.dfs(candidates, target, 0, [], results)
        return results

    def dfs(self, candidates, target, index, combination, results):
        if target == 0:
            results.append(combination[:])
            return
        if target < 0:
            return

        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, results)
            combination.pop()
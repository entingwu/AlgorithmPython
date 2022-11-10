from typing import (
    List,
)

class Permutations:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
             we will sort your return value in output
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None:
            return [[]]
        permutations = []
        visited = set({})
        self.dfs(nums, visited, [], permutations)
        return permutations

    def dfs(self, nums, visited, temp, permutations):
        if len(visited) == len(nums):
            permutations.append(list(temp))
            return

        for num in nums:
            if num in visited:
                continue

            temp.append(num)  # list append
            visited.add(num)  # set add
            self.dfs(nums, visited, temp, permutations)
            visited.remove(num)
            temp.pop() # list pop last one
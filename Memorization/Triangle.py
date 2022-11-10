from typing import List

class Triangle:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        return self.dfs(triangle, 0, 0, {})

    def dfs(self, triangle, i, j, memo):
        if i == len(triangle):
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        left = self.dfs(triangle, i + 1, j, memo)
        right = self.dfs(triangle, i + 1, j + 1, memo)

        memo[(i, j)] = min(left, right) + triangle[i][j]
        return memo[(i, j)]
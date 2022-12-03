from typing import List

class Triangle:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimum_total(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n= len(triangle)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[n - 1])


    def minimum_total1(self, triangle: List[List[int]]) -> int:
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
from typing import List
class CountSquareSubmatricsWithAllOnes:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        # state
        dp = [[0] * m for _ in range(n)]
        left = [[0] * m for _ in range(n)]
        up = [[0] * m for _ in range(n)]

        # initialize
        for j in range(m):
            dp[0][j] = left[0][j] = up[0][j] = matrix[0][j]
        for i in range(n):
            dp[i][0] = left[i][0] = up[i][0] = matrix[i][0]

        # function
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    continue
                left[i][j] = left[i][j - 1] + 1
                up[i][j] = up[i - 1][j] + 1
                dp[i][j] = min(left[i][j - 1], up[i - 1][j], dp[i - 1][j - 1]) + 1
        print(dp)
        # answer
        sum = 0
        for i in range(n):
            for j in range(m):
                sum += dp[i][j]
        return sum
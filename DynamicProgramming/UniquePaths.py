class UniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        # state
        dp = [[0] * n for _ in range(m)]
        # initiate
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
        # function
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        # answer
        return dp[m - 1][n - 1]
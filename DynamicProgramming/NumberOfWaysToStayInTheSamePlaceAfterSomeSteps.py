class NumberOfWaysToStayInTheSamePlaceAfterSomeSteps:
    """
    @param steps: steps you can move
    @param arr_len: the length of the array
    @return: Number of Ways to Stay in the Same Place After Some Steps
    """
    MOD = 10 ** 9 + 7
    def num_ways(self, steps: int, arr_len: int) -> int:
        if arr_len == 1:
            return 1
        # 计算可以走到的最远index
        n = min(steps // 2 + 1, arr_len)
        # state
        dp = [[0] * n for _ in range(2)]
        print(dp)
        # initialize: 一开始站在index=0
        dp[0][0] = 1
        # function
        for i in range(1, steps + 1): # step
            dp[i % 2][0] = (dp[(i - 1) % 2][0] + dp[(i - 1) % 2][1]) % self.MOD
            dp[i % 2][n - 1] = (dp[(i - 1) % 2][n - 1] + dp[(i - 1) % 2][n - 2]) % self.MOD
            for j in range(1, n - 1): # location
                dp[i % 2][j] = (dp[(i - 1) % 2][j - 1] + dp[(i - 1) % 2][j] + dp[(i - 1) % 2][j + 1]) % self.MOD
        print(dp)
        # answer
        return dp[steps % 2][0]

    def num_ways1(self, steps: int, arr_len: int) -> int:
        if arr_len == 1:
            return 1
        # 计算可以走到的最远index
        n = min(steps // 2 + 1, arr_len)
        # state
        dp = [[0] * n for _ in range(steps + 1)]
        print(dp)
        # initialize: 一开始站在index=0
        dp[0][0] = 1
        # function
        for i in range(1, steps + 1): # step
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % self.MOD
            dp[i][n - 1] = (dp[i - 1][n - 1] + dp[i - 1][n - 2]) % self.MOD
            for j in range(1, n - 1): # location
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) % self.MOD
        print(dp)
        # answer
        return dp[steps][0]
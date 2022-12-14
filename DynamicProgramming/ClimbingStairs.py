class ClimbingStairs:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        # state
        dp = [0] * (n + 1)
        # initiate
        dp[0], dp[1] = 1, 1
        # function
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        # answer
        return dp[n]
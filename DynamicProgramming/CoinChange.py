from typing import List
class CoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state
        dp = [float('inf')] * (amount + 1)
        # initialize
        dp[0] = 0
        # function
        for i in range(amount + 1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        # answer
        return -1 if dp[amount] == float('inf') else dp[amount]
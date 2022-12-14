from typing import List
class PaintHouse:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]:
            return 0
        n, m = len(costs), 3
        # state
        dp = [[0] * m for _ in range(2)]
        # initiate
        for j in range(m):
            dp[0][j] = costs[0][j]
        # function
        for i in range(1, n):
            dp[i % 2][0] = min(dp[(i - 1) % 2][1], dp[(i - 1) % 2][2]) + costs[i][0]
            dp[i % 2][1] = min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][2]) + costs[i][1]
            dp[i % 2][2] = min(dp[(i - 1) % 2][0], dp[(i - 1) % 2][1]) + costs[i][2]
        # answer
        print(dp)
        return min(dp[(n - 1) % 2])

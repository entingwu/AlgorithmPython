from typing import (
    List,
)

class Backpack:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a: List[int]) -> int:
        n = len(a)
        # 从前i个中选出若干个数组成j的和,使得j最接近m
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        # initialize
        dp[0][0] = True

        for i in range(1, n + 1):
            dp[i][0] = True
            for j in range(1, m + 1):
                item = a[i - 1]
                if j >= item:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - item]
                else:
                    dp[i][j] = dp[i - 1][j]

        for v in range(m, 0, -1):
            if dp[n][v]:
                return v
        return -1
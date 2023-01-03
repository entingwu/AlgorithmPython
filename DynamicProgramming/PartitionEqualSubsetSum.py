from typing import (
    List,
)

class PartitionEqualSubsetSum:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def can_partition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        # state
        dp = [[False] * (target + 1) for _ in range(n)]
        # initialize
        dp[0][0] = True

        # function
        # 前i个物品能否装满刚好j的空间
        for i in range(1, n):
            dp[i][0] = True
            for j in range(1, target + 1):
                item = nums[i]
                if j >= item:
                    dp[i][j] = dp[i - 1][j - item] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        # answer
        return dp[n - 1][target]


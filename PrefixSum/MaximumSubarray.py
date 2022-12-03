import sys
from typing import (
    List,
)

class MaximumSubarray:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def max_sub_array(self, nums: List[int]) -> int:
        # prefix_sum记录前i个数的和，max_Sum记录全局最大值，min_Sum记录前i个数中0-k的最小值
        prefix_sum = 0
        min_sum, max_sum = 0, -sys.maxsize
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(prefix_sum, min_sum) # not include current
        return max_sum
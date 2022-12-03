import sys
from typing import (
    List,
)

class SubarraySumEqualsToK:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the minimum length of continuous subarrays whose sum equals to k
    """
    def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
        prefix_sum = self.get_prefix_sum(nums)
        min_len = float('inf')
        sumToIndex = {0: 0}
        # prefix_sum[j+1] - prefix[i] = k means i-j=k
        for j in range(len(nums)):
            start_value = prefix_sum[j + 1] - k
            if start_value in sumToIndex:
                min_len = min(min_len, j + 1 - sumToIndex[start_value])
            sumToIndex[prefix_sum[j + 1]] = j + 1
        return min_len if min_len != float('inf') else -1

    def get_prefix_sum(self, nums):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = self.get_prefix_sum(nums)
        count = 0
        sumToTimes = {0: 1}
        for j in range(len(nums)):
            start_value = prefix_sum[j + 1] - k
            if start_value in sumToTimes:
                count += sumToTimes[start_value]
            sumToTimes[prefix_sum[j + 1]] = sumToTimes.get(prefix_sum[j + 1], 0) + 1
        return count

    # def subarray_sum_equals_k_i_i(self, nums: List[int], k: int) -> int:
    #     prefix_sum = self.get_prefix_sum(nums)
    #     print(prefix_sum)
    #     min_len = sys.maxsize
    #     for i in range(len(prefix_sum)):
    #         for j in range(i, len(prefix_sum) - 1):
    #             sum = prefix_sum[j + 1] - prefix_sum[i]
    #             if sum == k:
    #                 min_len = min(min_len, j + 1 - i)
    #     return min_len


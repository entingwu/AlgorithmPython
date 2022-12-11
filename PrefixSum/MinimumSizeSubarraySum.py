from typing import (
    List,
)

class MinimumSizeSubarraySum:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimum_size(self, nums: List[int], s: int) -> int:
        if not nums:
            return -1
        j, sum = 0, 0
        min_length = float('inf')
        for i in range(len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                min_length = min(j - i, min_length)
            sum -= nums[i]
        return min_length if min_length != float('inf') else -1


    def minimum_size2(self, nums: List[int], s: int) -> int:
        presum = self.get_prefix_sum(nums)
        min_size = float('inf')
        for start in range(len(nums)):
            end = self.get_end_of_subarray(presum, start, s)
            if presum[end + 1] - presum[start] >= s:
                min_size = min(end - start + 1, min_size)
        return min_size if min_size != float('inf') else -1

    def get_end_of_subarray(self, presum, start, sum):
        left, right = start, len(presum) - 2
        while left + 1 < right:
            mid = (left + right) // 2
            if presum[mid + 1] - presum[start] >= sum:
                right = mid
            else:
                left = mid
        if presum[left + 1] - presum[start] >= sum:
            return left
        return right


    def get_prefix_sum(self, nums):
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)
        return presum

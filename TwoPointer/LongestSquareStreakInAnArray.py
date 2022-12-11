from typing import List
import math
class LongestSquareStreakInAnArray:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        square = {}
        for num in nums:
            if math.sqrt(num) in nums:
                square[num] = square[math.sqrt(num)] + 1
            else:
                square[num] = 1
        cnt = max(square.values())
        return cnt if cnt > 1 else -1

    # def longestSquareStreak(self, nums: List[int]) -> int:
    #     nums.sort()
    #     square_len = -1
    #     for i in range(len(nums)):
    #         square = [nums[i]]
    #         target = nums[i] * nums[i]
    #         j = i
    #         while j < len(nums) and nums[j] <= target:
    #             if nums[j] == target:
    #                 square.append(nums[j])
    #                 target = nums[j] * nums[j]
    #             j += 1
    #         if len(square) > 1:
    #             square_len = max(len(square), square_len)
    #     return square_len
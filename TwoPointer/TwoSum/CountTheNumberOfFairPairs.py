from typing import List

class CountTheNumberOfFairPairs:

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            right = self.findRightBound(nums, nums[i], i, upper)
            left = self.findLeftBound(nums, nums[i], i, lower)
            result += right - left
        return result

    def findRightBound(self, nums, curr, index, upper):
        start, end = index + 1, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > upper - curr:
                end = mid
            else:
                start = mid + 1
        return start

    def findLeftBound(self, nums, curr, index, lower):
        start, end = index + 1, len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] < lower - curr:
                start = mid + 1
            else:
                end = mid
        return start

    def findRightBound1(self, nums, curr, index, target):
        start, end = index + 1, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target - curr:
                start = mid
            else:
                end = mid
        if nums[end] <= target - curr:
            return end
        return start

    def findLeftBound1(self, nums, curr, index, target):
        start, end = index + 1, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target - curr:
                end = mid
            else:
                start = mid
        if nums[start] >= target - curr:
            return start
        return end


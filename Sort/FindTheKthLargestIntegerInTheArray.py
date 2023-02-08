from typing import List

class FindTheKthLargestIntegerInTheArray:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numbers = list(map(int, nums))
        n = len(numbers)
        self.divide(numbers, 0, n - 1, k)
        return str(numbers[n - k])

    def divide(self, nums, left, right, k):
        n = len(nums)
        if left >= right:
            return
        pivot_pos = self.partition(nums, left, right)
        if pivot_pos == n - k:
            return nums[pivot_pos]
        elif pivot_pos < n - k:
            return self.divide(nums, pivot_pos + 1, right, k)
        else:
            return self.divide(nums, left, pivot_pos - 1, k)

    def partition(self, nums, left, right):
        pivot = nums[right]
        wall = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[wall] = nums[wall], nums[i]
                wall += 1
        nums[wall], nums[right] = nums[right], nums[wall]
        return wall
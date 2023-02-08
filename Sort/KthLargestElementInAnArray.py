from typing import List

class KthLargestElementInAnArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.divide(nums, 0, len(nums) - 1, k)
        return nums[len(nums) - k]


    def divide(self, nums, left, right, k):
        n = len(nums)
        if left >= right:
            return
        pivot_pos = self.partition(nums, 0, n - 1)
        if pivot_pos == n - k: # 6-2
            return nums[pivot_pos]
        elif pivot_pos < n - k:
            return self.divide(nums, pivot_pos + 1, right, k)
        else:
            return self.divide(nums, left, pivot_pos - 1, k)


    #  0  1  2  3  4  5
    # [3, 2, 1, 5, 6, 4]
    # 基本思路是吧最右边当做pivot，然后左边比pivot小的放在墙左边，
    # 然后把墙和pivot互换位置，pivot就在正确的排序位置上
    def partition(self, nums, left, right):
        pivot = nums[right]
        wall = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[wall] = nums[wall], nums[i]
                wall += 1
        nums[wall], nums[right] = nums[right], nums[wall]
        return wall

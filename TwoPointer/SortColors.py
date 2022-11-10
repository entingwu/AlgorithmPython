from typing import (
    List,
)

class SortColors:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        if not colors:
            return
        self.quick_sort(colors, 1, k, 0, len(colors) - 1)

    def quick_sort(self, colors, color_from, color_to, idx_from, idx_to):
        if color_from == color_to:
            return
        mid_color = (color_from + color_to) // 2
        left, right = idx_from, idx_to
        left, right = self.partition(colors, mid_color, left, right)

        self.quick_sort(colors, color_from, mid_color, idx_from, right)
        self.quick_sort(colors, mid_color + 1, color_to, left, idx_to)

    # 相向双指针
    def partition(self, nums, k, left, right):
        while left <= right:
            while left <= right and nums[left] <= k:
                left += 1
            while left <= right and nums[right] > k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left, right

    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing, O(N)
    """
    def sort_colors(self, nums: List[int]):
        if not nums:
            return []
        self.partition1(nums, 1)
        self.partition1(nums, 2)

    # 同向双指针
    def partition1(self, nums, k):
        last_small_ptr = -1
        for i in range(len(nums)):
            if nums[i] < k:
                last_small_ptr += 1
                nums[last_small_ptr], nums[i] = nums[i], nums[last_small_ptr]
        return last_small_ptr + 1


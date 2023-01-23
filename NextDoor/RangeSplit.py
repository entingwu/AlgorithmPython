# Q: given an array of integers, split them into a two dimensionals array by delimiter 0. Example could be:
# [1, 0, 1] => [[1], [1]]
#  0 1 2 3 4 5 6 7 8
# [1,2,0,4,6,7,0,9,0] => [[1,2], [4,6,7], [9]]
import collections
from typing import List

class RangeSplit:
    def split_range(self, nums: List[int])->List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        result, temp = [], []

        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
            if nums[i] == 0 or i == len(nums) - 1:
                result.append(list(temp))
                temp = []
        return result

    # Follow up: given an array of integers, and an index k, return the Range contains kth indexed number. If kth number if 0, return None
    #  0 1 2 3 4 5 6 7 8
    # [1,2,0,4,6,7,0,9,0] => [[1,2], [4,6,7], [9]]
    # index 7 -> [9]
    # index 1 -> [1,2]
    # index 4 -> [4,7]
    def find_range(self, nums: List[int], k: int):
        if not nums or nums[k] == 0:
            return None
        ranges = self.split_range(nums)
        print("@", ranges)
        start, end = 0, len(ranges) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if ranges[mid][0] <= nums[k] <= ranges[mid][-1]:
                return ranges[mid]
            elif nums[k] < ranges[mid][0]:
                end = mid
            else:
                start = mid

        if ranges[start][0] <= nums[k] <= ranges[start][-1]:
            return ranges[start]
        if ranges[end][0] <= nums[k] <= ranges[end][-1]:
            return ranges[end]
        return None

    #  0, 1, 2, 3, 4, 5
    # [1, 0, 2, 3, 0, 4]
    # [[1], [2,3], [4]]
    def split_index_to_range(self, nums: List[int]) -> dict[int, List[int]]:
        if not nums or len(nums) == 0:
            return {}
        range_map = collections.defaultdict(list)
        for i, num in enumerate(nums):
            if num != 0:
                range_map[i] = self.find_range(nums, i)
        return range_map


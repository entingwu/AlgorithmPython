from typing import (
    List,
)

class TwoSum:
    """
    HashTable
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        # hash用于建立数值到下标的映射
        hash = {}
        # 循环nums数值，并添加映射
        for i in range(len(numbers)):
            num = target - numbers[i]
            if num in hash:
                return [[num], i]
            hash[numbers[i]] = i
        # 无解的情况
        return [-1, -1]

    def two_sum_1(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        nums = [
            (number, index) for index, number in enumerate(numbers)
        ]
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                return sorted([nums[left][1], nums[right][1]])
        return [-1, -1]

from typing import (List)

class ThreeSum:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """

    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        numbers = sorted(numbers)
        results = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.findTwoSum(numbers, i + 1, len(numbers) - 1, -numbers[i], results)
        return results


    def findTwoSum(self, numbers, left, right, target, results):
        last_pair = None # dedup
        while left < right:
            if numbers[left] + numbers[right] == target:
                if (numbers[left], numbers[right]) != last_pair:
                    results.append([-target, numbers[left], numbers[right]])
                last_pair = (numbers[left], numbers[right])
                right -= 1
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

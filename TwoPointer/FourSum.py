from typing import (List)

class FourSum:
    """
        @param numbers: Give an array
        @param target: An integer
        @return: Find all unique quadruplets in the array which gives the sum of zero
                 we will sort your return value in output
        """

    def four_sum(self, numbers: List[int], target: int) -> List[List[int]]:
        numbers = sorted(numbers)
        results = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            for j in range(i + 1, len(numbers)):
                two_sum = target - numbers[i] - numbers[j]
                self.find_two_sum(numbers, two_sum, i, j, i + 2, len(numbers) - 1, results)
        return results


    def find_two_sum(self, numbers, target, i, j, left, right, results):
        last_pair = None
        while left < right:
            if numbers[left] + numbers[right] == target:
                if (numbers[i], numbers[j], numbers[left], numbers[right]) != last_pair:
                    results.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                last_pair = (numbers[i], numbers[j], numbers[left], numbers[right])
                left += 1
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

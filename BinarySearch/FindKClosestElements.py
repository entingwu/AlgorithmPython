from typing import (
    List,
)

class FindKClosestElements:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        if not a:
            return []
        index = self.find_upper_closest(a, target)
        left, right = index - 1, index
        results = []
        for i in range(k):
            if self.is_left_closer(a, left, right, target):
                results.append(a[left])
                left -= 1
            else:
                results.append(a[right])
                right += 1
        return results

    def is_left_closer(self, a, left, right, target):
        if left < 0:
            return False
        if right == len(a):
            return True
        return target - a[left] <= a[right] - target

    def find_upper_closest(self, a, target):
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] >= target:
                end = mid
            else:
                start = mid
        if a[start] >= target:
            return start
        if a[end] >= target:
            return end
        return len(a)
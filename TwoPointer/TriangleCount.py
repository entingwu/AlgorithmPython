from typing import (List)

class TriangleCount:
    """
    @param s: A list of integers
    @return: An integer
    """

    def triangle_count(self, s: List[int]) -> int:
        s = sorted(s)
        count = 0
        for i in reversed(range(len(s))):
            left, right = 0, i - 1
            while left < right:
                if s[left] + s[right] > s[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count

    def triangle_count_1(self, s: List[int]) -> int:
        if not s:
            return 0
        s.sort()
        total = 0
        for i in range(2, len(s)):
            total += self.get_triangle_count(s, i)
        return total

    def get_triangle_count(self, s, index):
        count = 0
        target = s[index]
        left, right = 0, index - 1
        while left < right:
            if s[left] + s[right] > target:
                count += right - left  # right + other ptrs
                right -= 1
            else:
                left += 1
        return count
from typing import (
    List,
)

class FindPeakElement:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        if not a:
            return -1
        start, end = 0, len(a) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < a[mid - 1]:
                end = mid
            elif a[mid] < a[mid + 1]:
                start = mid
            else:
                end = mid
        return start if a[start] > a[end] else end


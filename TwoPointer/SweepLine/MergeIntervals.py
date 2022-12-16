from typing import (
    List,
)
from TwoPointer.SweepLine.Interval import Interval

class MergeIntervals:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        boundaries = []
        for interval in intervals:
            boundaries.append((interval.start, 1))
            boundaries.append((interval.end, -1))
        boundaries = sorted(boundaries, key=lambda x: x[0])

        result = []
        is_matched = 0
        for boundary in boundaries:
            if is_matched == 0:
                left = boundary[0]
            is_matched += boundary[1]
            if is_matched == 0:
                right = boundary[0]
                if len(result) > 0 and result[-1].end == left:
                    result[-1].end = max(result[-1].end, right)
                else:
                    result.append(Interval(left, right))
        return result

    def merge1(self, intervals: List[Interval]) -> List[Interval]:
        intervals = sorted(intervals, key=lambda x:x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or interval.start > result[-1].end:
                result.append(interval)
            else:
                result[-1].end = max(interval.end, result[-1].end)
        return result
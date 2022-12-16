from typing import (
    List,
)
from TwoPointer.SweepLine.Interval import Interval
import heapq

class MeetingRooms:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms1(self, intervals: List[Interval]) -> int:
        heap = []
        for interval in intervals:
            heapq.heappush(heap, (interval.start, 1))
            heapq.heappush(heap, (interval.end, -1))
        meetings, result = 0, 0
        while heap:
            meetings += heapq.heappop(heap)[1]
            result = max(meetings, result)
        return result

    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        boundaries = []
        for interval in intervals:
            boundaries.append((interval.start, 1))
            boundaries.append((interval.end, -1))
        boundaries.sort()
        is_matched = 0
        min_rooms = 0
        for boundary in boundaries:
            is_matched += boundary[1]
            min_rooms = max(abs(is_matched), min_rooms)
        return min_rooms
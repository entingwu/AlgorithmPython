from TwoPointer.SweepLine.Interval import Interval
from typing import List
import heapq

class EmployeeFreeTime:
    def employee_free_time(self, schedule: List[List[int]]) -> List[Interval]:
        heap = []
        for employee in schedule:
            for i in range(0, len(employee), 2):
                heapq.heappush(heap, (employee[i], -1))
                heapq.heappush(heap, (employee[i + 1], 1))
        count, n = 0, len(heap)
        result = []
        while n > 1:
            left = heapq.heappop(heap)
            right = heap[0] # top
            count += left[1]
            if left[1] == 1 and right[1] == -1 and count == 0:
                result.append(Interval(left[0], right[0]))
                print(left[0], right[0])
            n -= 1
        return result
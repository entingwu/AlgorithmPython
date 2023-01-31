from typing import List
class RemoveInterval:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        for interval in intervals:
            print(interval, toBeRemoved)
            if interval[1] > toBeRemoved[0] > interval[0]:
                result.append([interval[0], toBeRemoved[0]])
            if interval[0] < toBeRemoved[1] < interval[1]:
                result.append([toBeRemoved[1], interval[1]])
            if interval[1] < toBeRemoved[0] or interval[0] > toBeRemoved[1]:
                result.append(interval)
        return result


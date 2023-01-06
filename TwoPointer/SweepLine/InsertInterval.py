from typing import List
class InsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        boundaries = []
        for start, end in intervals:
            boundaries.append((start, 1))
            boundaries.append((end, -1))
        boundaries.append((newInterval[0], 1))
        boundaries.append((newInterval[1], -1))
        boundaries.sort()

        result = []
        is_matched = 0
        for boundary in boundaries:
            if is_matched == 0:
                left = boundary[0]
            is_matched += boundary[1]
            if is_matched == 0:
                right = boundary[0]
                if len(result) > 0 and left == result[-1][1]:
                    result[-1][1] = max(right, result[-1][1])
                else:
                    result.append([left, right])
        return result


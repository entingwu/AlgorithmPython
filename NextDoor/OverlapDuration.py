from typing import List
class OverlapDuration:
    # interval1 = [1, 6], interval2 = [5, 10]
    # duration = 6 - 5 = 1
    def find_overlap(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        intervals.sort()

        prev_end, overlaps = 0, 0
        for start, end in intervals:
            if start < prev_end:
                overlaps += abs(prev_end - start)
            prev_end = end
        return overlaps

    # Busy time window:
    #                 [10, 15]
    # [1,5], [8, 12], [10, 14]
    # (1,1), (5,-1), (8,1), (10,1), (12,-1), (14,-1)
    # (14-10)/(15-10) = 0.8
    def busy_time_window(self, customer_intervals, busy_interval) -> float:
        # merge intervals
        boundaries = []
        for start, end in customer_intervals:
            boundaries.append((start, 1))
            boundaries.append((end, -1))

        boundaries = sorted(boundaries, key=lambda x: x[0])

        is_matched, left = 0, 0
        intervals = []
        for boundary in boundaries:
            if is_matched == 0:
                left = boundary[0]
            is_matched += boundary[1]
            if is_matched == 0:
                right = boundary[0]
                if len(intervals) > 0 and intervals[-1][1] == left:
                    intervals[-1][1] = max(right, intervals[-1][1])
                else:
                    intervals.append([left, right])
        print(intervals)
        overlap = 0
        for interval in intervals:
            overlap += self.find_overlap([interval, busy_interval])
        print(overlap)
        return overlap / (busy_interval[1] - busy_interval[0])




from typing import (
    List,
)

"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class IntervalSum:
    """
    @param a: An integer list
    @param queries: An query list
    @return: The result list
    """
    def interval_sum(self, a: List[int], queries: List[Interval]) -> List[int]:
        presum = [0]
        for num in a:
            presum.append(presum[-1] + num)

        result = []
        for query in queries:
            i, j = query.start, query.end
            result.append(presum[j + 1] - presum[i])
        return result
from heapq import heappush, heappop
from typing import (
    List,
)

class Heap:
    def __init__(self):
        self.minheap = []
        self.deleted_set = set() # index

    def push(self, value, index):
        heappush(self.minheap, (value, index))

    def _lazy_deletion(self):
        while self.minheap and self.minheap[0][1] in self.deleted_set:
            index, prefix = heappop(self.minheap)
            self.deleted_set.remove(index)

    def top(self):
        self._lazy_deletion()
        return self.minheap[0]

    def pop(self):
        self._lazy_deletion()
        heappop(self.minheap)

    def delete(self, index):
        self.deleted_set.add(index)

    def is_empty(self):
        return len(self.minheap) > 0

class ShortestSubarrayWithSumAtLeastK:
    """
    @param a: the array
    @param k: sum
    @return: the length
    """
    def shortest_subarray(self, a: List[int], k: int) -> int:
        prefix_sum = self.get_prefix_sum(a)
        print(prefix_sum)
        start, end = 1, len(a)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.is_valid(prefix_sum, k, mid):
                end = mid
            else:
                start = mid
        if self.is_valid(prefix_sum, k, start):
            return start
        if self.is_valid(prefix_sum, k, end):
            return end

    def is_valid(self, prefix_sum, k, length):
        minheap = Heap()
        for end in range(len(prefix_sum)):
            index = end - length - 1
            minheap.delete(index)

            if not minheap.is_empty() and prefix_sum[end] - minheap.top()[0] >= k:
                return True
            minheap.push(end, prefix_sum[end])
        return False

    def get_prefix_sum(self, a):
        prefix_sum = [0]
        for i in range(len(a)):
            prefix_sum.append(prefix_sum[-1] + a[i])
        return prefix_sum

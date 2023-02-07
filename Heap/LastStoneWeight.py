import heapq
from typing import List
class LastStoneWeight:
    # Time: O(nlogn), create heap O(n)
    # Space: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1).
        for i in range(len(stones)):
            stones[i] *= -1
        # Heapify all the stones.
        heapq.heapify(stones)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            max1 = heapq.heappop(stones)
            max2 = heapq.heappop(stones)
            if max1 != max2:
                heapq.heappush(stones, max1 - max2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0

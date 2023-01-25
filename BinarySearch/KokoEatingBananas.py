from typing import List
import math
class Solution:
    #  0  1  2  3
    # [3, 6, 7, 11]
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        while start + 1 < end:
            mid = (start + end) // 2 # 6
            if self.canFinish(piles, mid, h):
                end = mid
            else:
                start = mid

        if self.canFinish(piles, start, h): # min value first
            return start
        return end

    # cannot finish means speed too small, so start = mid
    def canFinish(self, piles, speed, H):
        hours = 0
        for num in piles:
            hours += math.ceil(num / speed)
        return hours <= H
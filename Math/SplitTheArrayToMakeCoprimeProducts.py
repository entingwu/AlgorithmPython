import collections
import math
from typing import List

class SplitTheArrayToMakeCoprimeProducts:

    def findValidSplit(self, nums: List[int]) -> int:
        right = collections.defaultdict(int)
        left = collections.defaultdict(int)
        for num in nums:
            for factor in self.getFactors(num):
                right[factor] = right.get(factor, 0) + 1

        for i in range(len(nums) - 1):
            factors = self.getFactors(nums[i])
            for factor in factors:
                right[factor] = right.get(factor) - 1
                left[factor] = left.get(factor, 0) + 1
                if right.get(factor) <= 0:
                    left.pop(factor, None)
                if len(left) == 0:
                    return i
        return -1

    def getFactors(self, N):
        factors = []
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                factors.append(i)
                while N % i == 0:
                    N /= i
        if N > 1:
            factors.append(int(N))
        return factors


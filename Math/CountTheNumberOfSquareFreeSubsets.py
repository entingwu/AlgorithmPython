import collections
import math
from typing import List

class CountTheNumberOfSquareFreeSubsets:

    candidates = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
    MOD = 10 ** 9 + 7

    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(int)
        for num in nums:
            if num in self.candidates:
                cnt[num] += 1
        print(cnt)

        ones = nums.count(1)
        tmp = 1
        for _ in range(ones):
            tmp = tmp * 2
        return (self.count(sorted(cnt), cnt) * tmp - 1) % self.MOD

    def count(self, arr, cnt):
        if not arr:
            return 1
        if len(arr) == 1:
            return cnt[arr[0]] + 1

        remain = []
        for num in arr[1:]:
            if math.gcd(num, arr[0]) == 1:
                remain.append(num)
        return (self.count(arr[1:], cnt) + cnt[arr[0]] * self.count(remain, cnt)) % self.MOD

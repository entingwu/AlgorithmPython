from typing import List

class MinimumOperationsMakeAllArrayElementsEqualTo1:

    def minOperations(self, nums: List[int]) -> int:
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
        if ones > 0:
            return len(nums) - ones

        op = float('inf')
        for i in range(len(nums)):
            last = nums[i]
            for j in range(i + 1, len(nums)):
                last = self.gcd(last, nums[j])
                if last == 1:
                    op = min(op, j - i + len(nums) - 1)
                    break
        return op if op != float('inf') else -1

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)

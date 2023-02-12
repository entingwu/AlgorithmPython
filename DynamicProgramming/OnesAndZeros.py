import collections
from typing import List

class OnesAndZeros:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 剩余空间是m个0、n个1时，最多可以装多少用品
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        print(dp)
        for str in strs:
            # 对每一个物品的size进行统计，每个物品的空间为zero个0, one个1
            one, zero = 0, 0
            for ch in str:
                if ch == '1':
                    one += 1
                else:
                    zero += 1
            print(one, zero)

            # 只要比这个物品大的空间，都可以选择拿这个物品，牺牲空间得到count + 1
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j] = max(dp[i - zero][j - one] + 1, dp[i][j])
        print(dp)
        return dp[m][n]

    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concat = []
        while len(nums) > 1:
            first = nums[0]
            last = nums[-1]
            nums.pop(0)
            nums.pop(-1)

            n = last
            new_num = first
            while n != 0:
                new_num = new_num * 10
                n = n // 10
            new_num = new_num + last
            concat.append(new_num)
            print(nums, concat)

        if len(nums) == 1:
            concat.append(nums[0])
        return sum(concat)


    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        numToIndex = collections.defaultdict(list)
        for i, num in enumerate(nums):
            numToIndex[num].append(i)
        print(numToIndex)

        n = len(nums)
        nums.sort()
        result = set()
        for i in range(n):
            for j in range(i, n):
                sum = nums[i] + nums[j]
                if sum < lower or sum > upper:
                    continue
                if lower <= sum <= upper:
                    pair1 = numToIndex[nums[i]]
                    pair2 = numToIndex[nums[j]]
                    print(pair1, pair2)
                    for p1 in pair1:
                        for p2 in pair2:
                            result.add((p1, p2))
        print(result)
        return len(result)

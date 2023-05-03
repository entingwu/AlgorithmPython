import collections
from typing import List

class CountTheNumberOfBeautifulSubarrays:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        count = 0
        hmap = collections.defaultdict(int)
        hmap[0] = 1
        xor = [0]
        for num in nums:
            curr = xor[-1] ^ num
            xor.append(curr)
            if curr in hmap:
                count += hmap[curr]
                hmap[curr] += 1
            else:
                hmap[curr] = 1
        return count


    def beautifulSubarrays1(self, nums: List[int]) -> int:
        count = 0
        xor = [0]
        for num in nums:
            xor.append(xor[-1] ^ num)
        print(xor)

        for i in range(len(xor)):
            for j in range(i, len(xor) - 1):
                if xor[j+1] ^ xor[i] == 0:
                    count += 1
        return count

    # for i in range(len(nums)):
    #     result = nums[i]
    #     if nums[i] == 0:
    #         count += 1
    #     for j in range(i + 1, len(nums)):
    #         result ^= nums[j]
    #         if result == 0:
    #             count += 1
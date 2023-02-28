import collections
from typing import List
import math

class ThreeSumWithMultiplicity:
    MOD = 10 ** 9 + 7
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        result = 0
        count = collections.Counter(arr)
        keys = sorted(count)
        print(keys)
        for i, x in enumerate(keys):
            diff = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < diff:
                    j += 1
                elif y + z > diff:
                    k -= 1
                else:
                    if i < j < k:
                        result += count[x] + count[y] + count[z]
                    elif i == j < k:
                        result += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        result += count[x] * count[y] * (count[y] - 1) / 2
                    else:
                        result += count[x] * (count[x] - 1) * (count[x] - 2) / 6
                    j += 1
                    k -= 1
        return result % self.MOD

    def threeSumMulti1(self, arr: List[int], target: int) -> int:
        result = 0
        count = collections.Counter(arr)
        keys = sorted(count)
        print(keys)
        for i in keys:
            for j in keys:
                k = target - i - j
                if k in count:
                    cnt_i, cnt_j, cnt_k = count[i], count[j], count[k]
                    if i == j == k:
                        result += cnt_i * (cnt_i - 1) * (cnt_i - 2) / 6
                    elif i == j and j != k:
                        result += cnt_i * (cnt_j - 1) * cnt_k / 2
                    elif i < j < k:
                        result += cnt_i * cnt_j * cnt_k
                    result %= self.MOD
        return int(result)

    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            id1, val1 = nums1[i]
            id2, val2 = nums2[j]
            print(id1, val1, id2, val2)
            if id1 == id2:
                result.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < len(nums1):
            result.append(nums1[i])
            i += 1
        while j < len(nums2):
            result.append(nums2[j])
            j += 1
        return result
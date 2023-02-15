import collections
from typing import List

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
from typing import List

def distinctDifferenceArray(nums: List[int]) -> List[int]:
    suffix = []
    sufsum = set()
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            suffix.insert(0, 0)
        else:
            suffix.insert(0, len(sufsum))
        sufsum.add(nums[i])
    print(suffix)

    diffs = []
    prefix = []
    presum = set()
    for i in range(len(nums)):
        presum.add(nums[i])
        prefix.append(len(presum))
        diffs.append(len(presum) - suffix[i])
    print(prefix)
    return diffs

nums = [37, 37, 37, 37, 33]
nums = [1,2,3,4,5]
print(distinctDifferenceArray(nums))
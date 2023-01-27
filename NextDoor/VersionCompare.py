from typing import List
from functools import cmp_to_key

def compareVersion(version1: str, version2: str) -> int:
    nums1, nums2 = version1.split("."), version2.split(".")
    len1, len2 = len(nums1), len(nums2)

    #        i
    # [1, 0]
    # [1, 0, 0]
    for i in range(max(len1, len2)):
        num1 = int(nums1[i]) if i < len1 else 0
        num2 = int(nums2[i]) if i < len2 else 0
        if num1 < num2:
            return -1
        elif num1 > num2:
            return 1
    return 0

def compareVersionBranch(version1: str, version2: str) -> int:
    strs1 = version1.split("-")
    strs2 = version2.split("-")
    v1, v2 = strs1[0], strs2[0]
    br1 = strs1[1] if len(strs1) > 1 else ""
    br2 = strs2[1] if len(strs2) > 1 else ""

    version_compare = compareVersion(v1, v2)
    if version_compare != 0:
        return version_compare
    # == 0
    if br1 == br2:
        return 0
    return 1 if br1 > br2 else -1

versions = ["1.1", "1.2.2", "1.1.2", "1.2"]
stages = ["1.1-dev", "1.1-rc2", "1.1.2-rc1", "1.2.2", "1.2-dev", "1.2-prod"]

#print(compareVersionBranch("1.1.2-rc1", "1.1.2-rc2"))
#print(sorted(versions, key=cmp_to_key(compareVersion)))
print(sorted(stages, key=cmp_to_key(compareVersionBranch)))

nums = [1, 4, 2, 5]
print(list(map(str, nums)))


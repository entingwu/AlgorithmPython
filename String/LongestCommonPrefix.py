from typing import List
class LongestCommonPrefix:
    # 遍历字符串数组，每次用当前prefix和下一个字符串匹配以生成新的prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            curr = strs[i]
            while j < len(curr) and j < len(prefix):
                if curr[j] != prefix[j]:
                    break
                j += 1
            prefix = curr[:j]
        return prefix

from typing import List
import collections
class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs) == 0:
            return []
        patterns = collections.defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            patterns[key].append(word)
        result = list(patterns.values())
        return result
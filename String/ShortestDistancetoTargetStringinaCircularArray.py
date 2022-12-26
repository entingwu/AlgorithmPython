from typing import List
class ShortestDistancetoTargetStringinaCircularArray:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        n, min_steps = len(words), float('inf')
        for i in range(n):
            if words[i] == target:
                min_steps = min(abs(i - startIndex), n - abs(i - startIndex), min_steps)
        return min_steps if min_steps != float('inf') else -1
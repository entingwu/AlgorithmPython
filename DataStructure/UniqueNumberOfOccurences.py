from typing import List


class UniqueNumberOfOccurences:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        valueToTimes = {}
        occurSet = set()
        for num in arr:
            if num not in valueToTimes:
                valueToTimes[num] = 1
            valueToTimes[num] += 1
        for value, times in valueToTimes.items():
            occurSet.add(times)
        return len(valueToTimes) == len(occurSet)
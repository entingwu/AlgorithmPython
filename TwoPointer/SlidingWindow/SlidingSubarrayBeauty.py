from collections import deque
from sortedcontainers import SortedList
from typing import List

class SlidingSubarrayBeauty:

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        window = SortedList()
        result = []
        for i in range(k):
            window.add(nums[i])
        result.append(min(0, window[x - 1]))
        print(window)
        for i in range(k, len(nums)):
            window.discard(nums[i - k])
            window.add(nums[i])
            result.append(min(0, window[x - 1]))
        return result

    def getSubarrayBeauty1(self, nums: List[int], k: int, x: int) -> List[int]:
        window = SortedList()
        result = []
        for i in range(len(nums)):
            window.add(nums[i])
            if i - k >= 0:
                window.discard(nums[i - k])
            if i >= k - 1:
                result.append(min(window[x - 1], 0))
        return result

    def getSubarrayMax(self, nums: List[int], k: int, x: int) -> List[int]:
        window = deque()
        result = []
        for i in range(len(nums)):
            while window and window[0] <= i - k:
                window.popleft()

            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            print(window)
            if i >= k - 1:
                item = nums[window[0]]
                result.append(item)
        return result
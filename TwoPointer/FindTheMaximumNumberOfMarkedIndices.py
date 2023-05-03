from typing import List
class FindTheMaximumNumberOfMarkedIndices:

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        print(nums)
        marked = [0] * n
        count = 0
        result = []
        for j in range(n - 1, -1, -1):
            if marked[j] == 1:
                continue
            i = j // 2
            while i >= 0 and nums[i] * 2 > nums[j] or marked[i] == 1:
                i -= 1
            if nums[i] * 2 <= nums[j]:
                count += 2
                result.append((nums[i], nums[j]))
                marked[i] = 1
                marked[j] = 1
        print(result)
        return count


    def maxNumOfMarkedIndices1(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        print(nums)
        marked = [0] * n
        cnt = 0
        j = n - 1
        i = n // 2 - 1
        while i >= 0:
            if marked[i] == 1:
                i -= 1
            elif marked[j] == 1:
                j -= 1
            else:
                if nums[i] * 2 <= nums[j]:
                    print((nums[i], nums[j]))
                    cnt += 2
                    marked[i] = 1
                    marked[j] = 1
                    i -= 1
                    j -= 1
                else:
                    i -= 1
        print(cnt)
        return cnt
from typing import List

class Subsets:
    """
        @param nums: A set of numbers
        @return: A list of lists
                 we will sort your return value in output
                 [1,2]
        """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results

    def dfs(self, nums, index, subset, results):
        #results.append(subset)
        results.append(list(subset))

        for index in range(index, len(nums)):
            #newSet = subset[:]
            #newSet.append(nums[index])
            subset.append(nums[index])
            self.dfs(nums, index + 1, subset, results)
            subset.pop()

    def subsets_bfs(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        queue = [[]]
        for num in sorted(nums):
            for i in range(len(queue)):
                subset = list(queue[i])
                subset.append(num)
                queue.append(subset)
        return queue




    # def dfs(self, nums, index, subset, results):
    #     if index == len(nums):
    #         sorted(subset)
    #         results.append(subset[:])
    #         return
    #
    #     subset.append(nums[index]) # [1]
    #     self.dfs(nums, index + 1, subset, results)
    #
    #     subset.pop()
    #     self.dfs(nums, index + 1, subset, results)
from typing import List

class KSum:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """

    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        if not a:
            return []
        a.sort()
        results = []
        self.dfs(a, 0, k, target, [], results)
        return results

    def dfs(self, a, index, k, target, temp, results):
        if k == 0 and target == 0:
            results.append(temp[:])
            return
        if k == 0 or target <= 0:
            return

        for i in range(index, len(a), 1):
            temp.append(a[i])
            self.dfs(a, i + 1, k - 1, target - a[i], temp, results)
            temp.pop()

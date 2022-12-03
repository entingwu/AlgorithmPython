from typing import (
    List,
)

class StringPermutation:
    """
    @param str: A string
    @return: all permutations
             we will sort your return value in output
    """
    def string_permutation2(self, str: str) -> List[str]:
        if not str or len(str) == 0:
            return [""]
        chars = sorted(str)
        visited = [False for i in range(len(str))]
        results = []
        self.dfs(chars, visited, "", results)
        return results

    def dfs(self, chars, visited, permutation, results):
        if len(permutation) == len(chars):
            results.append(permutation)
            return

        for i in range(len(chars)):
            if visited[i]:
                continue
            if i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            self.dfs(chars, visited, permutation + chars[i], results)
            visited[i] = False
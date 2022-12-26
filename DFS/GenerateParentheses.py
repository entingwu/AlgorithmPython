from typing import (
    List,
)

class GenerateParentheses:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
             we will sort your return value in output
    """
    def generate_parenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        results = []
        self.dfs(n, "", 0, 0, results)
        return results

    def dfs(self, n, sequence, left_cnt, right_cnt, results):
        if 2 * n == len(sequence):
            results.append(sequence[:])
            return
        if right_cnt > left_cnt:
            return
        if left_cnt < n:
            self.dfs(n, sequence + "(", left_cnt + 1, right_cnt, results)

        if right_cnt < n:
            self.dfs(n, sequence + ")", left_cnt, right_cnt + 1, results)
from typing import (
    List,
)

class NQueens:
    """
    @param n: The number of queens
    @return: All distinct solutions
             we will sort your return value in output
    """
    def solve_n_queens(self, n: int) -> List[List[str]]:
        results = []
        self.search(n, [], results)
        return results

    def search(self, n, permutation, results):
        row = len(permutation)
        if row == n:
            results.append(self.print(permutation))
        for col in range(n):
            if self.is_valid(permutation, row, col):
                permutation.append(col)
                self.search(n, permutation, results)
                permutation.pop()

    def is_valid(self, permutation, row, col):
        for preRow, preCol in enumerate(permutation):
            if col == preCol:
                return False
            if (row - col == preRow - preCol) or (preRow + preCol == row + col):
                return False
        return True

    def print(self, permutation):
        n = len(permutation)
        board = []
        for col in permutation:
            row = ["Q" if j == col else "." for j in range(n)]
            rowStr = "". join(row)
            board.append(rowStr)
        return board



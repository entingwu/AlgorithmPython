from typing import List
class WhereWillTheBallFall:
    # Time: O(M*N), Space: O(M)
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        if n <= 1 or m <= 1:
            return [-1]

        result = [-1] * m
        for col in range(m):
            result[col] = self.findBallDropCol(0, col, grid)
        return result

    def findBallDropCol(self, row, col, grid):
        # ball reaches the last row
        if row == len(grid):
            return col

        next_col = col + grid[row][col]
        if next_col < 0 or next_col > len(grid[0]) - 1:
            return -1
        # g[r][c] == 1 or -1
        if grid[row][col] != grid[row][next_col]:
            return -1
        return self.findBallDropCol(row + 1, next_col, grid)


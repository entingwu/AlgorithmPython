from typing import (
    List,
)

class KnightShortestPath:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    DIRECTIONS = [(2,-1), (1,-2), (-1,-2), (-2, -1)]
    def shortest_path2(self, grid: List[List[bool]]) -> int:
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * 3 for _ in range(n)]
        dp[0][0] = 0

        for j in range(1, m):
            for i in range(n):
                dp[i][j % 3] = float('inf')
                if grid[i][j]:
                    continue
                for delta_x, delta_y in self.DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j % 3] = min(dp[i][j % 3], dp[x][y] + 1)
        print(dp)
        if dp[n - 1][(m - 1) % 3] == float('inf'):
            return -1
        return dp[n - 1][(m - 1) % 3]

    def shortest_path(self, grid: List[List[bool]]) -> int:
        if not grid or not grid[0]:
            return -1
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * m for _ in range(n)]
        dp[0][0] = 0

        for j in range(m):
            for i in range(n):
                if grid[i][j]:
                    continue
                for delta_x, delta_y in self.DIRECTIONS:
                    x, y = i + delta_x, j + delta_y
                    if 0 <= x < n and 0 <= y < m:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)
        print(dp)
        if dp[n-1][m-1] == float('inf'):
            return -1
        return dp[n-1][m-1]

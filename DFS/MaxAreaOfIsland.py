from typing import List
class MaxAreaOfIsland:
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        visited = set()
        max_area = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if (i, j) in visited:
                    continue
                if grid[i][j] == 1:
                    area = self.dfs(grid, i, j, n, m, visited)
                    max_area = max(area, max_area)
        return max_area

    def dfs(self, grid, x, y, n, m, visited):
        visited.add((x, y))
        area = 1
        for delta_x, delta_y in self.DIRECTIONS:
            new_x = x + delta_x
            new_y = y + delta_y
            if self.is_valid(grid, new_x, new_y, visited):
                area += self.dfs(grid, new_x, new_y, n, m, visited)
        return area

    def is_valid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == 1

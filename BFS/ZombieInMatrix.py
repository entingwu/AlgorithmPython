import collections
from typing import (
    List,
)

class ZombieInMatrix:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def zombie(self, grid: List[List[int]]) -> int:
        if not grid:
             return -1

        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        day = 0
        while queue:
            size = len(queue)
            day += 1
            for k in range(size):
                x, y = queue.popleft()
                for dx, dy in self.DIRECTIONS:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = 1
                        queue.append((new_x, new_y))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1
        return day - 1
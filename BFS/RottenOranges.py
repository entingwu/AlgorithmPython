from typing import List
import collections
class STATUS:
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

class RottenOranges:
    DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        queue = collections.deque([])
        visited = set([])
        fresh_cnt = 0
        # 1. initialize
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == STATUS.ROTTEN:
                    queue.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == STATUS.FRESH:
                    fresh_cnt += 1
        if fresh_cnt == 0:
            return 0
        # 2. BFS
        level = -1
        while queue:
            level += 1
            for i in range(len(queue)):
                x, y = queue.popleft()
                if grid[x][y] != STATUS.ROTTEN:
                    continue
                else:
                    fresh_cnt -= 1
                for delta_x, delta_y in self.DIRECTIONS:
                    new_x = x + delta_x
                    new_y = y + delta_y
                    if self.isFresh(new_x, new_y, grid, visited):
                        grid[new_x][new_y] = STATUS.ROTTEN
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == STATUS.FRESH:
                    return -1
        return level

    def isFresh(self, x, y, grid, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y] == STATUS.FRESH
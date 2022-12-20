import collections
from typing import (
    List,
)

class GridType:
    EMPTY = 0
    HOUSE = 1
    WALL = 2

class BuildPostOffice:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]
    def shortest_distance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if not grid or n == 0:
            return -1
        # 空地 => 到所有房子最短距离之和
        distance_sum = collections.defaultdict(int)
        # 空地 => 可以到达房子总是
        reachable_count = collections.defaultdict(int)
        houses = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.HOUSE:
                    self.bfs(grid, i, j, distance_sum, reachable_count)
                    houses += 1

        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                # 如果某个空地不能被所有房子到达，则不适合建邮局
                if (i, j) not in reachable_count or reachable_count[(i, j)] != houses:
                    continue
                min_dist = min(distance_sum[(i, j)], min_dist)
        return min_dist if min_dist != float('inf') else -1

    def bfs(self, grid, row, col, distance_sum, reachable_count):
        queue = collections.deque([(row, col)])
        distance = {(row, col): 0}
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in self.DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y
                if not self.is_valid(grid, new_x, new_y):
                    continue
                if (new_x, new_y) in distance:
                    continue
                # 如果空地还没被到达过，则入队
                queue.append((new_x, new_y))
                distance[(new_x, new_y)] = distance[(x, y)] + 1

                # add up into distance_sum & reachable_count
                distance_sum[(new_x, new_y)] += distance[(new_x, new_y)]
                reachable_count[(new_x, new_y)] += 1

    def is_valid(self, grid, row, col):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return False
        return grid[row][col] == GridType.EMPTY

    # TLE
    def shortest_distance1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if not grid or n == 0:
            return -1

        min_dist = float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == GridType.EMPTY:
                    distance = self.bfs1(grid, i, j)
                    dist_sum = self.get_distance_sum(grid, distance)
                    min_dist = min(dist_sum, min_dist)
        return min_dist if min_dist != float('inf') else -1

    def bfs1(self, grid, row, col):
        queue = collections.deque([(row, col)])
        distance = {(row, col): 0}
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in self.DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y
                if not self.is_valid1(grid, new_x, new_y) or (new_x, new_y) in distance:
                    continue
                distance[(new_x, new_y)] = distance[(x, y)] + 1
                if grid[new_x][new_y] == GridType.EMPTY:
                    queue.append((new_x, new_y))
        return distance

    def get_distance_sum(self, grid, distance):
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == GridType.HOUSE:
                    # can not access
                    if (i, j) not in distance:
                        return float('inf')
                    sum += distance[(i, j)]
        return sum

    def is_valid1(self, grid, row, col):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
            return False
        return grid[row][col] != GridType.WALL

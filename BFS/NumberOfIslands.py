import collections
from typing import List

class NumberOfIslands:
    DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def num_islands(self, grid: List[List[bool]]) -> int:
        if not grid or not grid[0]:
            return 0
        islands = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.dfs(grid, i, j, visited)
                    islands += 1
        return islands

    def dfs(self, grid, x, y, visited):
        if not self.is_valid(grid, x, y, visited):
            return

        visited.add((x, y))
        for dx, dy in self.DIRECTIONS:
            new_x = x + dx
            new_y = y + dy
            self.dfs(grid, new_x, new_y, visited)

    def bfs(self, grid, x, y, visited):
        queue = collections.deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in self.DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y
                if not self.is_valid(grid, new_x, new_y, visited):
                    continue
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))

    def is_valid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]

    # 305. Number of Islands II
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        is_lands = set()
        num_of_lands = []
        for position in positions:
            x, y = position[0], position[1]
            if (x, y) in is_lands:
                num_of_lands.append(uf.get_num_of_set())
                continue
            is_lands.add((x, y))
            uf.add((x, y))

            for delta_x, delta_y in self.DIRECTIONS:
                new_x = x + delta_x
                new_y = y + delta_y
                if self.is_valid2(m, n, new_x, new_y, is_lands):
                    uf.union((x, y), (new_x, new_y))
            num_of_lands.append(uf.get_num_of_set())
        return num_of_lands

    def is_valid2(self, m, n, x, y, is_lands):
        if not (0 <= x < m and 0 <= y < n):
            return False
        return (x, y) in is_lands
class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_set = 0
        self.size_of_set = {}

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.num_of_set += 1
        self.size_of_set[x] = 1

    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]

        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_set -= 1
            self.size_of_set[root_y] += self.size_of_set[root_x]

    def get_num_of_set(self):
        return self.num_of_set

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]


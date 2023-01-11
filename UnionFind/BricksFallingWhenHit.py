from typing import List
class BricksFallingWhenHit:
    WALL = (-1, -1)
    DIRECTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        dropped_bricks = [0] * len(hits)
        uf = UnionFind()
        self.initialization(uf, grid, hits)

        for i in range(len(hits)-1, -1, -1):
            x, y = hits[i]
            grid[x][y] += 1
            if grid[x][y] != 1:
                continue
            before = uf.get_size_of_set(self.WALL)

            uf.add((x, y))
            # 把填补的砖块与四面邻居合并
            self.union_neighbors(uf, grid, x, y)
            # 如果该点与墙相邻，与墙壁合并（unionNeighbors不会合并墙）
            if x == 0:
                uf.union((0, y), self.WALL)

            # 判断新加入的砖块是否和墙相连
            if uf.is_connected((x, y), self.WALL):
                # 填补后，与墙相连的砖块数量
                after = uf.get_size_of_set(self.WALL)
                dropped_bricks[i] = max(0, after - before - 1)
            else:
                dropped_bricks[i] = 0
        return dropped_bricks

    def initialization(self, uf, grid, hits):
        n, m = len(grid), len(grid[0])
        # 预先敲下所有目标砖块
        for x, y in hits:
            grid[x][y] -= 1
        print(grid)

        # 将存在的砖块和墙接入并查集
        uf.add(self.WALL)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    uf.add((i, j))

        # 将直接贴墙的砖合并到墙上
        for j in range(m):
            if grid[0][j] == 1:
                uf.union((0, j), self.WALL)

        # 将所有砖和他们的邻居合并
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.union_neighbors(uf, grid, i, j)

    # 将(x,y)的砖块和四周的砖块合并
    def union_neighbors(self, uf, grid, x, y):
        for delta_x, delta_y in self.DIRECTIONS:
            new_x = x + delta_x
            new_y = y + delta_y
            # 将(x,y)的砖块和出界的相邻砖块相连
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
                uf.union((x, y), (new_x, new_y))

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

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_num_of_set(self):
        return self.num_of_set

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]
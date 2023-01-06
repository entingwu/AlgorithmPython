from typing import List

class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_set = 0

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.num_of_set += 1

    def find(self, x):
        root = x
        while self.father[root] is not None:
            root = self.father[root]
        # path compression
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_set -= 1

    def get_num_of_set(self):
        return self.num_of_set

class NumberOfProvinces:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, m = len(isConnected), len(isConnected[0])
        uf = UnionFind()
        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1:
                    uf.add(i)
                    uf.add(j)
                    uf.merge(i, j)
        return uf.get_num_of_set()


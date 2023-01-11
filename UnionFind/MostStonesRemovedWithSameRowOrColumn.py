from typing import List
class MostStonesRemoveWithSameRowOrColumn:
    # Max stones can be removed = all - connected components
    def removeStones1(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [False] * n
        num_of_components = 0
        for i in range(n):
            if visited[i]:
                continue
            self.dfs(stones, visited, i)
            num_of_components += 1
        return n - num_of_components

    def dfs(self, stones, visited, index):
        visited[index] = True
        for i in range(len(stones)):
            if visited[i]:
                continue
            if stones[i][0] == stones[index][0] or stones[i][1] == stones[index][1]:
                self.dfs(stones, visited, i)

    # Max stones can be removed = all - connected components
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        if not stones or n <= 1:
            return 0
        uf = UnionFind()
        for i, stone1 in enumerate(stones):
            for j, stone2 in enumerate(stones[i+1:], start=i+1):
                uf.add(i)
                uf.add(j)
                if (stone1[0] == stone2[0]) or (stone1[1] == stone2[1]):
                    uf.merge(i, j)
        print(uf.num_of_set)
        return n - uf.get_num_of_set()

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


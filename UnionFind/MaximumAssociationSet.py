import collections
from typing import (
    List,
)

class MaximumAssociationSet:
    """
    @param list_a: The relation between ListB's books
    @param list_b: The relation between ListA's books
    @return: The answer
             we will sort your return value in output
    """
    def maximum_association_set(self, list_a: List[str], list_b: List[str]) -> List[str]:
        uf = UnionFind()
        max_size, root = 0, ""
        for i in range(len(list_a)):
            a, b = list_a[i], list_b[i]
            uf.add(a)
            uf.add(b)
            uf.union(a, b)
        # 找到最大的集合大小max_size和最大结合的根root
        for i in range(len(list_a)):
            a, b = list_a[i], list_b[i]
            if max_size < uf.get_size_of_set(a):
                root = a
                max_size = uf.get_size_of_set(a)
            if max_size < uf.get_size_of_set(b):
                root = b
                max_size = uf.get_size_of_set(b)

        # 遍历字符串，找到所有和root相连的字符串
        result = set()
        for i in range(len(list_a)):
            a, b = list_a[i], list_b[i]
            if uf.is_connected(a, root):
                result.add(a)
            if uf.is_connected(b, root):
                result.add(b)
        return list(result)


    def maximum_association_set1(self, list_a: List[str], list_b: List[str]) -> List[str]:
        graph = collections.defaultdict(set)
        for i in range(len(list_a)):
            u, v = list_a[i], list_b[i]
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        max_group = set()
        for a in list_a:
            if a in visited:
                continue
            group = self.bfs(a, graph, visited)
            if len(group) > len(max_group):
                max_group = group
        return list(max_group)

    def bfs(self, node, graph, visited):
        queue = collections.deque([node])
        visited.add(node)
        group = set()
        while queue:
            curr = queue.popleft()
            group.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return group

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
            origin_father = self.father[x]
            self.father[x] = root
            x = origin_father
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
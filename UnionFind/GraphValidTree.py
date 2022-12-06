import collections
from typing import (
    List,
)
from UnionFind.UnionFind import UnionFind

class GraphValidTree:

    def __init__(self):
        self.uf = UnionFind()
        self.num_of_edges = 0
        self.has_cycle = False

    def addEdge(self, x, y):
        self.uf.add(x)
        self.uf.add(y)
        self.num_of_edges += 1
        if self.uf.is_connected(x, y):
            self.has_cycle = True
        self.uf.merge(x, y)

    def isValidTree(self):
        if self.num_of_edges != len(self.uf.father) - 1:
            return False
        return not self.has_cycle

    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # Tree: n nodes and n-1 edges
        if len(edges) != n - 1:
            return False
        # build graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # source connects to all nodes
        visited = self.bfs(graph, edges[0][0])
        return len(visited) == n

    def bfs(self, graph, source):
        queue = collections.deque([source])
        visited = set([source])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return visited

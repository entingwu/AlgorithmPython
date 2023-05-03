import collections
from typing import List

# 1. Tree: no cycle, no island
class MinimizeTheTotalPriceOfTheTrips:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for from_edge, to_edge in edges:
            graph[from_edge].append(to_edge)
            graph[to_edge].append(from_edge)
        print(graph)

        count = [0] * len(graph)
        for trip in trips:
            self.dfs(graph, trip[0], trip[1], set(), count)
        print(count)

    def dfs(self, graph, curr, to, path, count):
        if curr in path:
            return
        if curr == to:
            path.add(curr)
            for node in path:
                count[node] += 1
            return
        for neighbor in graph[curr]:
            path.add(curr)
            self.dfs(graph, neighbor, to, path, count)
            path.remove(curr)


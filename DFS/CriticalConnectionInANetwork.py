import collections
import sys
from typing import List

class CriticalConnectionInANetwork:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # 1. build graph
        graph = self.get_graph(connections)
        print(graph)
        result = set(map(tuple, map(sorted, connections)))
        print(result)
        # for i in range(len(connections)):
        #     print(tuple(sorted(connections[i])))
        rank = [-sys.maxsize] * n
        self.dfs(0, 0, rank, graph, result, n)
        print(rank)
        return list(result)

    def dfs(self, node, depth, rank, graph, result, n):
        if rank[node] >= 0:
            return rank[node]

        rank[node] = depth
        min_dfs_depth = n
        for neighbor in graph[node]:
            if rank[neighbor] == depth - 1: # prev node
                continue
            dfs_depth = self.dfs(neighbor, depth + 1, rank, graph, result, n)
            if dfs_depth <= rank[node]:
                result.discard(tuple(sorted((node, neighbor))))
            min_dfs_depth = min(dfs_depth, min_dfs_depth)

        return min_dfs_depth


    def get_graph(self, connections):
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        return graph
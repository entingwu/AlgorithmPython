import collections
from typing import List
class MinimumHeightTrees:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. build graph
        graph = collections.defaultdict(list)
        for edge in edges:
            start, end = edge
            graph[start].append(end)
            graph[end].append(start)
        print(graph)
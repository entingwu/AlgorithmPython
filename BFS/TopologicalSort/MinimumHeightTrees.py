import collections
from typing import List
class MinimumHeightTrees:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. build graph
        graph = collections.defaultdict(list)
        in_degree = [0] * n
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            in_degree[start] += 1
            in_degree[end] += 1
        print(graph)
        print(in_degree)

        queue = collections.deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 1:
                queue.append(i)
        print(queue)
        level = []
        while queue:
            centroid = []
            for j in range(len(queue)):
                curr = queue.popleft()
                centroid.append(curr)
                level.append(curr)
                for neighbor in graph[curr]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        queue.append(neighbor)
        print(level)
        return centroid
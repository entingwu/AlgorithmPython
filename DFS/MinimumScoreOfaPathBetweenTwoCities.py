import collections
from typing import (
    List,
)

class MinimumScoreOfaPathBetweenTwoCities:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = self.construct_graph(roads, n)
        print(graph)
        # Run BFS to find minimum path and do not visit seen nodes
        visited = set([])
        path = []
        self.dfs(graph, visited, 1, path)
        # results = []
        # self.dfs(graph, visited, 1, path, results)
        # print(results)
        return min(path)

    def dfs(self, graph, visited, node, path):
        visited.add(node)
        for neighbor, weight in graph[node]:
            path.append(weight)
            if neighbor not in visited:
                self.dfs(graph, visited, neighbor, path)

    def construct_graph(self, roads, n):
        graph = {} # node: (neighbor, weight)
        for road in roads:
            node, neighbor, weight = road
            if node not in graph:
                graph[node] = []
            if neighbor not in graph:
                graph[neighbor] = []
            graph[node].append((neighbor, weight))
            graph[neighbor].append((node, weight))
        return graph

    def bfs(self, graph):
        queue = collections.deque([1])
        visited = set()
        min_path = []
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in graph[node]:
                min_path.append(weight)
                queue.append(neighbor)
        return min(min_path)

    # def dfs(self, graph, visited, node, path, results):
    #     if len(path) == len(graph):
    #         results.append(path[:])
    #         return
    #
    #     for neighbor, weight in graph[node]:
    #         if neighbor in visited:
    #             continue
    #
    #         visited.add(neighbor)
    #         path.append(weight)
    #         self.dfs(graph, visited, neighbor, path, results)
    #         path.pop()
    #         visited.pop()
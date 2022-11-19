from typing import (
    List,
)

class Result:
    def __init__(self):
        self.min_cost = float('inf')

class TravelingSalesmanProblem:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def min_cost(self, n: int, roads: List[List[int]]) -> int:
        graph = self.construct_graph(roads, n)
        print(graph)
        result = Result()
        self.dfs(1, n, set([1]), 0, graph, result)
        return result.min_cost

    def dfs(self, city, n, visited, cost, graph, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return

        for next_city in graph[city]: # 1, 2, 3
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_city, n, visited, cost + graph[city][next_city], graph, result)
            visited.remove(next_city)

    def construct_graph(self, roads, n):
        graph = { # dict {i, dict}
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }
        for a, b, cost in roads:
            graph[a][b] = min(graph[a][b], cost)
            graph[b][a] = min(graph[b][a], cost)
        return graph

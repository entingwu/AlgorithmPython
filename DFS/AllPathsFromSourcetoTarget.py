from typing import List

class AllPathsFromSourcetoTarget:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph or len(graph) == 0:
            return []
        results = []
        self.dfs(graph, 0, [0], results)
        return results

    def dfs(self, graph, node, path, results):
        if node == len(graph) - 1:
            results.append(list(path))
            return
        for neighbor in graph[node]:
            path.append(neighbor)
            self.dfs(graph, neighbor, path, results)
            path.pop()
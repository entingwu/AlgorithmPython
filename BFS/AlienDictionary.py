import collections
import heapq
from heapq import heapify
from typing import (
    List,
)

class AlienDictionary:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        graph = self.build_graph(words)
        print(graph)
        if not graph:
            return ""
        return self.topological_sort(graph)

    def topological_sort(self, graph):
        indegree = self.get_indegree(graph)
        print(indegree)
        queue = [node for node in indegree if indegree[node] == 0]
        heapq.heapify(queue)
        order = ""
        while queue:
            node = heapq.heappop(queue)
            order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(queue, neighbor)
        return order if len(order) == len(graph) else ""

    def get_indegree(self, graph):
        indegree = {node: 0 for node in graph}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                indegree[neighbor] += 1
        return indegree

    def build_graph(self, words):
        # 字母->右面的多个字母
        graph = {}
        # point
        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch] = set()
        # edge
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                ch1, ch2 = words[i][j], words[i + 1][j]
                if ch1 != ch2:
                    graph[ch1].add(ch2)
                    break
                # ["abc", "ab"]
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        return None
        return graph



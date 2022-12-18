import collections
from typing import (
    List,
)

class ModernLudo:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modern_ludo(self, length: int, connections: List[List[int]]) -> int:
        graph = self.build_graph(connections, length)
        print(graph)
        queue = collections.deque([1])
        distance = {1: 0}

        while queue:
            node = queue.popleft()
            # 找最短路径，联通块
            for neighbor in range(node + 1, min(node + 7, length + 1)):
                connected_nodes = self.get_unvisited_nodes(graph, neighbor, distance)
                for connected_node in connected_nodes:
                    queue.append(connected_node)
                    distance[connected_node] = distance[node] + 1
        print(distance)
        return distance[length]

    def get_unvisited_nodes(self, graph, start, distance):
        print(distance)
        queue = collections.deque([start])
        unvisited_nodes = set()
        while queue:
            node = queue.popleft()
            if node in distance:
                continue
            unvisited_nodes.add(node)
            for neighbor in graph[node]:
                if neighbor in distance:
                    continue
                queue.append(neighbor)
                unvisited_nodes.add(neighbor)
        return unvisited_nodes

    def build_graph(self, connections, length):
        graph = {
            i: set()
            for i in range(1, length + 1)
        }
        for start, end in connections:
            graph[start].add(end)
        return graph


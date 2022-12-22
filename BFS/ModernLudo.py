import collections
import heapq
from typing import (
    List,
)

class ModernLudo:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """

    def modern_ludo2(self, length: int, connections: List[List[int]]) -> int:
        graph = self.build_graph_dp(connections, length)
        # state, initialize
        dp = [float('inf')] * (length + 1) # 0~15, len=15
        dp[1] = 0
        # function
        for to_node in range(2, length + 1):
            # edge 1
            left_limit = max(to_node - 6, 1)
            for from_node in range(left_limit, to_node):
                dp[to_node] = min(dp[from_node] + 1, dp[to_node])
            # edge 0
            for from_node in graph[to_node]:
                dp[to_node] = min(dp[from_node], dp[to_node])
        return dp[length]

    def build_graph_dp(self, connections, length):
        graph = {i: set()
                 for i in range(1, length + 1)}
        for from_node, to_node in connections:
            graph[to_node].add(from_node)
        return graph
    def modern_ludo1(self, length: int, connections: List[List[int]]) -> int:
        graph = self.build_graph(connections, length)
        print(graph)
        # queue = collections.deque([1])
        queue = [(0, 1)] # (dist, node)
        distance = {i: float('inf') for i in range(1, length + 1)}
        distance[1] = 0
        while queue:
            dist, node = heapq.heappop(queue)
            # node = queue.popleft()
            # edge = 0
            for next_node in graph[node]:
                if dist < distance[next_node]:
                    distance[next_node] = dist
                    heapq.heappush(queue, (dist, next_node))
                    # queue.append(next_node)
            # edge = 1
            right_limit = min(node + 7, length + 1)
            for next_node in range(node + 1, right_limit):
                if dist + 1 < distance[next_node]:
                    distance[next_node] = dist + 1
                    heapq.heappush(queue, (dist + 1, next_node))
                    #queue.append(next_node)
        print(distance)
        return distance[length]



    def modern_ludo(self, length: int, connections: List[List[int]]) -> int:
        graph = self.build_graph(connections, length)
        queue = collections.deque([1])
        distance = {1: 0}

        while queue:
            node = queue.popleft()
            print(node)
            # 找最短路径，联通块
            for neighbor in range(node + 1, min(node + 7, length + 1)):
                connected_nodes = self.get_unvisited_nodes(graph, neighbor, distance)
                for connected_node in connected_nodes:
                    queue.append(connected_node)
                    distance[connected_node] = distance[node] + 1
        return distance[length]

    def get_unvisited_nodes(self, graph, start, distance):
        print(distance)
        queue = collections.deque([start])
        unvisited_nodes = set([])
        while queue:
            node = queue.popleft()
            # 基于初始的那个neighbor没有访问过的前提下做的
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


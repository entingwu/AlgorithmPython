import collections
from typing import (
    List,
)

class LongestPathOnTheTree:
    """
    @param n: The number of nodes
    @param starts: One point of the edge
    @param ends: Another point of the edge
    @param lens: The length of the edge
    @return: Return the length of longest path on the tree.
    """
    def longest_path(self, n: int, starts: List[int], ends: List[int], lens: List[int]) -> int:
        graph = {}
        for i in range(n - 1):
            start, end, dist = starts[i], ends[i], lens[i]
            if start not in graph:
                graph[start] = []
            if end not in graph:
                graph[end] = []
            graph[start].append((end, dist))
            graph[end].append((start, dist))
        print(graph)
        # longest_path, longest_chain = self.dfs(graph, starts[0], -1)
        # return: 离root最远的点，该点离root的距离
        start, _ = self.bfs(graph, starts[0])
        print(start)
        end, longest_path = self.bfs(graph, start)
        return longest_path

    def bfs(self, graph, root):
        queue = collections.deque([root])
        distance_to_root = {root: 0}
        max_distance, max_node = 0, -1
        while queue:
            curr = queue.popleft()
            if distance_to_root[curr] > max_distance:
                max_distance = distance_to_root[curr]
                max_node = curr

            for neighbor, dist in graph[curr]:
                if neighbor in distance_to_root:
                    continue
                queue.append(neighbor)
                distance_to_root[neighbor] = distance_to_root[curr] + dist
        return max_node, max_distance


    def dfs(self, graph, node, parent):
        longest_chain, longest_path = 0, 0 # current neighbor max
        child_longest_chain, child_second_longest_chain = 0, 0 # global among all children
        
        for neighbor, dist in graph[node]:
            if neighbor == parent:
                continue

            child_path, child_chain = self.dfs(graph, neighbor, node)
            # current
            child_chain += dist
            longest_path = max(child_path, longest_path)
            longest_chain = max(child_chain, longest_chain)
            # global chain
            _, child_second_longest_chain, child_longest_chain = \
                sorted([child_longest_chain, child_second_longest_chain, child_chain])
        # global path
        longest_path = max(child_longest_chain + child_second_longest_chain, longest_path)

        print(node, longest_chain, longest_path, child_second_longest_chain)
        return [longest_path, longest_chain]


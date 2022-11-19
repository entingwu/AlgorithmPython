import collections

class Node:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class TopologicalSort:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        node_to_indegree = self.get_indegree(graph)
        # {0:0, 1:1, 2:1, 3:2}
        order = []
        start_nodes = [n for n in graph if node_to_indegree[n] == 0]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node.label)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order

    def get_indegree(self, graph):
        node_to_indegree = {x:0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
        # for node, indegree in node_to_indegree.items():
        #     print(node.label, indegree)
        return node_to_indegree


import collections

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class CloneGraph:
    def clone_graph(self, node: UndirectedGraphNode) -> UndirectedGraphNode:
        if not node:
            return node

        nodes = self.find_nodes_by_bfs(node)
        mapping = self.copy_nodes(nodes)
        self.copy_edges(nodes, mapping)
        # for old, new in mapping.items():
        #     for neighbor in new.neighbors:
        #         print(new.label, ":", neighbor.label)
        return mapping[node]


    def find_nodes_by_bfs(self, node):
        queue = collections.deque([node])
        enqueued = set([node])
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor in enqueued:
                    continue
                queue.append(neighbor)
                enqueued.add(neighbor)
        return enqueued

    def copy_nodes(self, nodes):
        mapping = {} # {node, new_node}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping

    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            # new node to new neighbor
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)


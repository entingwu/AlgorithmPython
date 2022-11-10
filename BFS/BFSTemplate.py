import collections

class Node:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class BFSTemplate:
    def bfs(self, node):
        queue = collections.deque([node])
        distance = {node: 0}

        while queue:
            node = queue.popleft()
            print("%s" % node.label + " ")
            for neighbor in node.neighbors:
                if neighbor in distance: # key in dict
                    continue
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)


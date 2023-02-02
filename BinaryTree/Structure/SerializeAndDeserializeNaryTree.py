"""
# Definition for a Node.
"""
import collections

class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children


class SerializeAndDeserializeNaryTree:
    DELIMITER = " "
    # 1 3 3 2 5 0 6 0 2 0 4 0
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ""
        nodes = []
        self.dfs_serialize(root, nodes)
        return self.DELIMITER.join(nodes)

    def dfs_serialize(self, root, nodes):
        if not root:
            return
        nodes.append(str(root.val)) # value
        nodes.append(str(len(root.children))) # children count
        for child in root.children:
            self.dfs_serialize(child, nodes)

	# <node value, child size>
    # 1 3 3 2 5 0 6 0 2 0 4 0
    def deserialize(self, data: str) -> 'Node':
        nodes = data.split(self.DELIMITER)
        queue = collections.deque(nodes)
        root = self.dfs_deserialize(queue)
        return root

    def dfs_deserialize(self, queue):
        val = queue.popleft() # node_value
        root = Node(val, [])
        size = int(queue.popleft()) # child_size
        for i in range(size):
            root.children.append(self.dfs_deserialize(queue))
        return root
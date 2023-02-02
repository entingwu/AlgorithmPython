# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SerializeAndDeserializeBinaryTree:
    DELIMITER = " "
    """Encodes a tree to a single string. """
    def serialize(self, root):

        if not root:
            return "#"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return self.DELIMITER.join([str(root.val), left, right])


    def deserialize(self, data):
        """Decodes your encoded data to tree. """
        nodes = data.split(self.DELIMITER)
        queue = collections.deque(nodes)
        return self.dfs(queue)

    def dfs(self, queue):
        val = queue.popleft()
        if val == "#":
            return None
        root = TreeNode(val)
        root.left = self.dfs(queue)
        root.right = self.dfs(queue)
        return root
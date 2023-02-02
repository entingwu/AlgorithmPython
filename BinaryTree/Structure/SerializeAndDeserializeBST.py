# Definition for a binary tree node.
import collections
from typing import Optional
import sys

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SerializeAndDeserializeBST:
    #           3
    #        1     6
    #      0     4   7
    # [3, 1, 6, 0, null, 4, 7]
    #  3, 1, 0, 6, 4, 7
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        data = str(root.val)
        if root.left:
            data += "," + self.serialize(root.left)
        if root.right:
            data += "," + self.serialize(root.right)
        return data

    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if data == "":
            return None
        nodes = data.split(",")
        queue = collections.deque(nodes)
        return self.dfs(queue, float('-inf'), float('inf'))

    def dfs(self, queue, lower, upper):
        if len(queue) == 0:
            return None

        val = int(queue[0])
        if val < lower or val > upper:
            return None

        val = int(queue.popleft())
        root = TreeNode(val)
        root.left = self.dfs(queue, lower, val)
        root.right = self.dfs(queue, val, upper)
        return root
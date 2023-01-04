import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeRightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == size - 1:
                    result.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return result

    def rightSideView1(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        self.dfs(root, result, 0)
        return result

    def dfs(self, root, result, level):
        if level == len(result):
            result.append(root.val)
        if root.right:
            self.dfs(root.right, result, level + 1)
        if root.left:
            self.dfs(root.left, result, level + 1)


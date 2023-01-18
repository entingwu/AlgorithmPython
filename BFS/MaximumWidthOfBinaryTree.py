# Definition for a binary tree node.
import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaximumWidthOfBinaryTree:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 0)])
        max_width = 0
        while queue:
            _, level_head_idx = queue[0]
            for i in range(len(queue)):
                curr, col_idx = queue.popleft()
                if curr.left:
                    queue.append((curr.left, col_idx * 2))
                if curr.right:
                    queue.append((curr.right, col_idx * 2 + 1))
            max_width = max(col_idx - level_head_idx + 1, max_width)
        return max_width



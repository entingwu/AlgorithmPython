# Definition for a binary tree node.
import collections
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PrintBinaryTree:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        depth = self.get_depth(root)
        m = depth # col
        n = 2 ** depth - 1 # row
        output = [[""] * n for _ in range(m)]
        self.insert_node(root, 0, 0, n, output)
        return output

    def insert_node(self, root, depth, left, right, output):
        if not root:
            return
        mid = (left + right) // 2
        output[depth][mid] = str(root.val)
        self.insert_node(root.left, depth + 1, left, mid, output)
        self.insert_node(root.right, depth + 1, mid, right, output)


    def printTree1(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.get_depth(root) - 1
        m = height + 1
        n = 2 ** (height + 1) - 1
        output = [[""] * n for _ in range(m)]
        self.bfs(root, n, height, output)
        return output

    def bfs(self, root, col_len, height, output):
        queue = collections.deque([(root, col_len // 2)])
        r = 0
        while queue:
            for i in range(len(queue)):
                node, c = queue.popleft()
                output[r][c] = str(node.val)
                if node.left:
                    queue.append((node.left, c - 2 ** (height-r-1)))
                if node.right:
                    queue.append((node.right, c + 2 ** (height-r-1)))
            r += 1

    def get_depth(self, root) -> int:
        if not root:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1


from typing import (
    List,
)

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class MaxTree:
    """
    @param a: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    # 1. Monotone Stack
    def max_tree(self, a: List[int]) -> TreeNode:
        n = len(a)
        stack = [0] * n
        nodes = []
        for i in range(0, n):
            node = TreeNode(a[i])
            nodes.append(node)

            while stack and a[stack[-1]] < a[i]:
                left_idx = stack.pop()
                node.left = nodes[left_idx]

            if stack and a[stack[-1]] > a[i]:
                parent = nodes[stack[-1]]
                parent.right = node

            stack.append(i)
        return nodes[stack[0]]

    # 2. Divide Conquer
    def max_tree1(self, a: List[int]) -> TreeNode:
        return self.dfs(a, 0, len(a) - 1)

    def dfs(self, a, left, right):
        if left > right:
            return None
        max_value, max_idx = self.get_max_position(a, left, right)
        print(max_value, max_idx)
        root = TreeNode(max_value)
        left_tree = self.dfs(a, left, max_idx - 1)
        right_tree = self.dfs(a, max_idx + 1, right)
        root.left = left_tree
        root.right = right_tree
        return root


    def get_max_position(self, a, left, right):
        max_value, max_idx = float('-inf'), float('-inf')
        for i in range(left, right + 1):
            if a[i] > max_value:
                max_value = a[i]
                max_idx = i
        return max_value, max_idx



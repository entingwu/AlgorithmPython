from typing import (
    List,
)
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class NaryTreePreorderTraversal:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            output.append(node.val)
            stack.extend(node.children[::-1])

        return output


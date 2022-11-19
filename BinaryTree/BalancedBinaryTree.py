"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BalancedBinaryTree:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def is_balanced(self, root: TreeNode) -> bool:
        is_balanced, height = self.binary_tree_height(root)
        return is_balanced

    def binary_tree_height(self, root):
        if not root:
            return True, 0
        if root.left is None and root.right is None:
            return True, 1

        is_left_balanced, left_height = self.binary_tree_height(root.left)
        is_right_balanced, right_height = self.binary_tree_height(root.right)
        root_height = max(left_height, right_height) + 1

        if not is_left_balanced or not is_right_balanced:
            return False, root_height
        if abs(left_height - right_height) > 1:
            return False, root_height

        return True, root_height

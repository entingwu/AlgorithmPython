"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BinaryTreeLongestConsecutiveSequence:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longest_consecutive2(self, root: TreeNode) -> int:
        if not root:
            return 0
        root_max_len, root_max_desc, root_max_incr = self.get_max_length(root)
        return root_max_len

    def get_max_length(self, root):
        if not root:
            return 0, 0, 0
        left_max_len, left_max_desc, left_max_incr = self.get_max_length(root.left)
        right_max_len, right_max_desc, right_max_incr = self.get_max_length(root.right)

        root_max_desc, root_max_incr = 0, 0
        if root.left is not None and root.left.val - 1 == root.val:
            root_max_incr = max(root_max_incr, left_max_incr + 1)
        if root.left is not None and root.left.val + 1 == root.val:
            root_max_desc = max(root_max_desc, left_max_desc + 1)
        if root.right is not None and root.right.val - 1 == root.val:
            root_max_incr = max(root_max_incr, right_max_incr + 1)
        if root.right is not None and root.right.val + 1 == root.val:
            root_max_desc = max(root_max_desc, right_max_desc + 1)

        root_max_len = max(root_max_incr + 1 + root_max_desc, left_max_len, right_max_len)
        return root_max_len, root_max_desc, root_max_incr

    """
        @param root: the root of binary tree
        @return: the length of the longest consecutive sequence path
        """

    def longest_consecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.get_max_len(root)[0]

    def get_max_len(self, root):
        if not root:
            return 0, 0
        left_max_len, left_max_incr = self.get_max_len(root.left)
        right_max_len, right_max_incr = self.get_max_len(root.right)

        root_max_incr = 0
        if root.left is not None and root.left.val - 1 == root.val:
            root_max_incr = max(root_max_incr, left_max_incr + 1)
        if root.right is not None and root.right.val - 1 == root.val:
            root_max_incr = max(root_max_incr, right_max_incr + 1)

        root_max_len = max(root_max_incr + 1, left_max_len, right_max_len)
        return root_max_len, root_max_incr

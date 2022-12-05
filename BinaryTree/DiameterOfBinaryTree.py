"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class DiameterOfBinaryTree:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_ld, max_lc = self.dfs(root)
        return max_ld

    def dfs(self, root):
        if not root:
            return [0, 0]
        ld, lc = self.dfs(root.left)
        rd, rc = self.dfs(root.right)
        return [max(ld, rd, lc + rc), max(lc, rc) + 1]

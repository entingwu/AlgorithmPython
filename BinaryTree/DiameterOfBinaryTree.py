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
        max_diameter, max_chain = self.dfs(root)
        return max_diameter

    def dfs(self, root):
        if not root:
            return [0, 0]
        left_max_diameter, left_max_chain = self.dfs(root.left)
        right_max_diameter, right_max_chain = self.dfs(root.right)

        max_diameter = max(left_max_diameter, right_max_diameter, left_max_chain + right_max_chain)
        max_chain = max(left_max_chain, right_max_chain) + 1
        return [max_diameter, max_chain]

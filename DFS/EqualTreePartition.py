import collections
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class EqualTreeParition:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def check_equal_tree(self, root: TreeNode) -> bool:
        #subtree_sum = collections.defaultdict(int)
        subtree_sum = set()
        root_sum = root.val + self.dfs(root.left, subtree_sum) + self.dfs(root.right, subtree_sum)
        return root_sum % 2 == 0 and (root_sum // 2) in subtree_sum

    def dfs(self, root, subtree_sum):
        if not root:
            return 0
        left = self.dfs(root.left, subtree_sum)
        right = self.dfs(root.right, subtree_sum)
        sum = left + root.val + right
        subtree_sum.add(sum)
        return sum

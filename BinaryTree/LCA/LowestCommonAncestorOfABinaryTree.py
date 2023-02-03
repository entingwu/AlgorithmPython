# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LowestCommonAncestorOfABinaryTree:

    # If either node p or q does not exist in the tree, return null.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not self.canFind(root, p) or not self.canFind(root, q):
            return None
        return self.lca(root, p, q)

    def canFind(self, root, node):
        if not root:
            return False
        return root == node or self.canFind(root.left, node) or self.canFind(root.right, node)

    def lca(self, root, p, q):
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)

        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        return None

    # Version 1
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
from DivideConquer import ParentTreeNode
from DivideConquer import TreeNode

class LowestCommonAncestor:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        if not root:
            return None
        if root == A or root == B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None

    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        if not root:
            return None
        parent_set = set()
        curr = A
        while curr:
            parent_set.add(curr)
            curr = curr.parent

        curr = B
        while curr:
            if curr in parent_set:
                return curr
            curr = curr.parent

        return None
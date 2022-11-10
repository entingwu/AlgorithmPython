from BinaryTree import TreeNode

class InvertBinaryTree:

    def invert_binary_tree(self, root: TreeNode):
        if not root:
            return None
        left_tree = self.invert_binary_tree(root.left)
        right_tree = self.invert_binary_tree(root.right)
        root.left = right_tree
        root.right = left_tree
        return root
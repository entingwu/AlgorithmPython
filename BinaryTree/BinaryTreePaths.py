from typing import (List)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BinaryTreePaths:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
             we will sort your return value in output
    """

    def binary_tree_paths2(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        paths = []
        self.find_paths2(root, [root], paths)
        return paths

    def find_paths2(self, root, path, paths):
        if not root:
            return
        if root.left is None and root.right is None:
            paths.append("->".join([str(node.val) for node in path]))
            return

        if root.left:
            path.append(root.left)
            self.find_paths2(root.left, path, paths)
            path.pop()

        if root.right:
            path.append(root.right)
            self.find_paths2(root.right, path, paths)
            path.pop()

    def find_paths1(self, root, path, paths):
        if not root:
            return
        if root.left is None and root.right is None:
            paths.append(path)
            return

        if root.left:
            self.find_paths1(root.left, path + "->" + str(root.left.val), paths)

        if root.right:
            self.find_paths1(root.right, path + "->" + str(root.right.val), paths)


    def binary_tree_paths1(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]

        paths = []
        left_paths = self.binary_tree_paths1(root.left)
        for path in left_paths:
            paths.append(str(root.val) + "->" + path)

        right_paths = self.binary_tree_paths1(root.right)
        for path in right_paths:
            paths.append(str(root.val) + "->" + path)
        return paths


    # def binary_tree_paths(self, root: TreeNode) -> List[str]:
    #     if not root:
    #         return []
    #
    #     paths = []
    #     self.find_paths(root, [root], paths)
    #     return paths
    #
    #
    # def find_paths(self, node, path, paths):
    #     if not node:
    #         return
    #
    #     if not node.left and not node.right:
    #         paths.append('->'.join([str(n.val) for n in path]))
    #         return
    #
    #     path.append(node.left)
    #     self.find_paths(node.left, path, paths)
    #     path.pop()
    #
    #     path.append(node.right)
    #     self.find_paths(node.right, path, paths)
    #     path.pop()
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def __init__(self):
        self.map = {} # value, index
        self.pre_index = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        for i in range(n):
            self.map[inorder[i]] = i
        return self.helper(preorder, inorder, 0, n - 1)

    def helper(self, preorder, inorder, startIn, endIn):
        if startIn > endIn:
            return None
        # 1. root
        val = preorder[self.pre_index]
        self.pre_index += 1
        root = TreeNode(val)

        # 2. spilt inorder[]
        split = self.map[val]

        # 3. dfs
        root.left = self.helper(preorder, inorder, startIn, split - 1)
        root.right = self.helper(preorder, inorder, split + 1, endIn)
        return root

    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder, 0, 0, len(inorder) - 1)

    def dfs(self, preorder, inorder, prePos, startIn, endIn):
        if startIn > endIn:
            return None
        root_val = preorder[prePos]
        root = TreeNode(root_val)

        split = 0
        for i in range(startIn, endIn + 1):
            if inorder[i] == root_val:
                split = i
                break

        left_tree_size = split - startIn
        root.left = self.dfs(preorder, inorder, prePos + 1, startIn, split - 1)
        root.right = self.dfs(preorder, inorder, prePos + left_tree_size + 1, split + 1, endIn)
        return root
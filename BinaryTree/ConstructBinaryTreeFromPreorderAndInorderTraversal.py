from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructBinaryTreeFromPreorderAndInorderTraversal:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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

        root.left = self.dfs(preorder, inorder, prePos + 1, startIn, split - 1)
        root.right = self.dfs(preorder, inorder, prePos + (split - startIn) + 1, split + 1, endIn)
        return root
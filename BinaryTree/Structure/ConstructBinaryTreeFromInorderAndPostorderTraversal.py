from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructBinaryTreeFromInorderAndPostorderTraversal:

    def __init__(self):
        self.map = {} # inorder value to index

    # postorder [[9], 15, 7, [20], [3]]
    # inorder   [9,   3,  15, 20,   7]
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        for i in range(n):
            self.map[inorder[i]] = i
        postPos = n - 1 # curr root in postorder
        return self.dfs(inorder, postorder, postPos, 0, n - 1)

    def dfs(self, inorder, postorder, postPos, startIn, endIn):
        if startIn > endIn:
            return None

        # 1. root
        val = postorder[postPos]
        root = TreeNode(val)

        # 2. spilt inorder[]
        split = self.map[val]
        right_tree_size = endIn - split

        # 3. dfs
        root.left = self.dfs(inorder, postorder, postPos - right_tree_size - 1, startIn, split - 1) # post left tree root: postPos
        root.right = self.dfs(inorder, postorder, postPos - 1, split + 1, endIn)  # post right tree root: postPos
        return root

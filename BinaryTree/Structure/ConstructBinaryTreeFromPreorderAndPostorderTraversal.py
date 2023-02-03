from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructBinaryTreeFromPreorderAndPostorderTraversal:

    def __init__(self):
        self.map = {}
        self.startPre = 0
        self.len = 0

    # preorder  [1, [2], 4, 3, 7]
    # postorder [4, [2], 7, 3, 1]
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        for i in range(n):
            self.map[postorder[i]] = i
        self.len = n
        return self.helper(preorder, postorder, 0, n - 1)
        #return self.dfs(preorder, postorder, 0, n - 1, 0, n - 1)

    def helper(self, preorder, postorder, startPost, endPost):
        if startPost > endPost or self.startPre >= self.len:
            return None

        # 1. root
        val = preorder[self.startPre]
        root = TreeNode(val)
        self.startPre += 1

        if startPost == endPost or self.startPre == self.len: # 结束左子树，不然分界不合理
            return root

        # 2. split postorder
        # 找到分割点，pre左子树的第一个孩子，即pre第二个，post左子树最后一个。post左子树结束分割点
        split = self.map[preorder[self.startPre]]

        # 3. dfs
        root.left = self.helper(preorder, postorder, startPost, split)
        root.right = self.helper(preorder, postorder, split + 1, endPost - 1)
        return root


    def dfs(self, preorder, postorder, startPre, endPre, startPost, endPost):
        if startPost > endPost or startPre > endPre:
            return None
        if startPre == endPre:
            return TreeNode(preorder[startPre])

        # 1. root
        val = preorder[startPre]
        root = TreeNode(val)

        # 2. spilt postorder
        # 找到分割点，pre左子树的第一个孩子，即pre第二个，post左子树最后一个。post左子树结束分割点
        split = self.map[preorder[startPre + 1]] # post_idx
        left_tree_size = split - startPost

        # 3. dfs
        left_pre_end = startPre + 1 + left_tree_size
        root.left = self.dfs(preorder, postorder, startPre + 1, left_pre_end, startPost, split)

        right_pre_start = startPre + left_tree_size + 2
        root.right = self.dfs(preorder, postorder, right_pre_start, endPre, split + 1, endPost - 1)
        return root


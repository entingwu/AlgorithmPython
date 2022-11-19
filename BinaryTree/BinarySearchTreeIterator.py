"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    stack = []
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        return len(self.stack) > 0

    """
    @return: return next node
     下一个点=右子树最小点 or 路径中最近一个通过左子树包含当前点的点
    """
    def _next(self):
        node = self.stack[-1]
        if node.right is not None:
            # 加入右子树左边最小点
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
        else:
            # 右子树关系则弹出
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()

        return node

    def next(self):
        node = self.stack.pop()
        if node.right:
            curr = node.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return node
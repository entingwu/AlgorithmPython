class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class KthSmallestElementInaBST:

    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return stack[-1].val

    def kth_smallest2(self, root: TreeNode, k: int) -> int:
        stack = []
        results = []
        curr = root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            results.append(curr.val)
            curr = curr.right

        return results[k - 1] if results else 0

    order = 0
    result = 0
    def kth_smallest1(self, root: TreeNode, k: int) -> int:
        self.dfs(root, k)
        return self.result

    def dfs(self, root, k):
        if not root:
            return

        self.dfs(root.left, k)

        self.order += 1
        if self.order == k:
            self.result = root.val

        self.dfs(root.right, k)
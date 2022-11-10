import collections
from typing import List
from BinaryTree.TreeNode import TreeNode

class BinaryTreeVerticalOrderTraversal:
    """
        @param root: the root of tree
        @return: the vertical order traversal
        """

    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # [(0, [])] default items are empty list objects
        column_table = collections.defaultdict(list) # 0->[x,x,x]
        queue = collections.deque([(root, 0)])
        min_col, max_col = 0, 0

        while queue:
            node, column = queue.popleft()
            min_col = min(min_col, column)
            max_col = max(max_col, column)
            column_table[column].append(node.val)
            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))

        return [column_table[i] for i in range(min_col, max_col + 1)]


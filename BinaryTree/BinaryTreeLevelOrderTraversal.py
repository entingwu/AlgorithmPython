import collections
from typing import List
from BinaryTree.TreeNode import TreeNode

class BinaryTreeLevelOrderTraversal:
    """
        @param root: A Tree
        @return: Level order a list of lists of integer
        """

    def level_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        results = []

        while queue:
            # results.append([node.val for node in queue]) # [1]
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level[:])

        return results
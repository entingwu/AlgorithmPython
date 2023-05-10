import collections
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class MakeCostsOfPathsEqualInBinaryTree:
    increment = 0
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.dfs(n, cost, 1)
        return self.increment

    def dfs(self, n, cost, i) -> int:
        if i > n:
            return 0
        left_cost = self.dfs(n, cost, 2 * i)
        right_cost = self.dfs(n, cost, 2 * i + 1)
        self.increment += abs(left_cost - right_cost)
        return max(left_cost, right_cost) + cost[i - 1]


    def minIncrements1(self, n: int, cost: List[int]) -> int:
        nodes = []
        for i in range(n):
            nodes.append(i)

        root = TreeNode(nodes.pop(0))
        queue = collections.deque([root])
        count = 0
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                curr_cost = cost[node.val]
                level.append(curr_cost)
                if len(nodes) > 0:
                    node.left = TreeNode(nodes.pop(0))
                    queue.append(node.left)
                if len(nodes) > 0:
                    node.right = TreeNode(nodes.pop(0))
                    queue.append(node.right)
            max_val = max(level)
            for num in level:
                count += abs(max_val - num)
        return count

if __name__ == '__main__':
    p = MakeCostsOfPathsEqualInBinaryTree()
    n = 7
    cost = [1,5,2,2,3,3,1]
    print(p.minIncrements(n, cost))
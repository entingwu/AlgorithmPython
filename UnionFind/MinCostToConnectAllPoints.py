from typing import List

class MinCostToConnectAllPoints:
    # points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        all_edges = []

        # Storing all edges of our complete graph
        for curr_node in range(n):
            for next_node in range(curr_node + 1, n):
                #print(points[curr_node], points[next_node])
                weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                all_edges.append((weight, curr_node, next_node))

        # Sorting all edges in increasing order
        all_edges.sort()
        print(all_edges)

        uf = UnionFind()
        mst = []
        mst_cost = 0
        edges = 0
        for weight, node1, node2 in all_edges:
            print(weight, node1, node2)
            uf.add(node1)
            uf.add(node2)
            if not uf.is_connected(node1, node2):
                uf.union(node1, node2)
                mst.append([node1, node2])
                mst_cost += weight
                edges += 1
                if edges == n - 1:
                    break
        print(mst)
        return mst_cost



class UnionFind:
    def __init__(self):
        self.father = {}
        self.nums_of_set = 0

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.nums_of_set += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        root = x
        while self.father[root] != None:
            root = self.father[root]

        while x != root:
            origin_father = self.father[x]
            self.father[x] = root
            x = origin_father
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.nums_of_set -= 1

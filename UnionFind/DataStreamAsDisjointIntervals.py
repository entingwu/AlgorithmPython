from typing import List
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class SummaryRanges:

    def __init__(self):
        self.uf = UnionFind()

    def addNum(self, value: int) -> None:
        self.uf.add(value)
        if value - 1 in self.uf.father:
            self.uf.union(value - 1, value)
        if value + 1 in self.uf.father:
            self.uf.union(value + 1, value)

    def getIntervals(self) -> List[List[int]]:
        result = []
        for root in self.uf.father.keys():
            if self.uf.father[root] is None:
                interval = self.uf.intervals[root]
                result.append(interval)
        return result

class UnionFind:
    def __init__(self):
        self.father = {}
        self.intervals = {}

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.intervals[x] = [x, x]

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
        if root_x is not root_y:
            self.father[root_x] = root_y
            start = min(self.intervals[root_x][0], self.intervals[root_y][0])
            end = max(self.intervals[root_x][1], self.intervals[root_y][1])
            self.intervals[root_y] = [start, end]
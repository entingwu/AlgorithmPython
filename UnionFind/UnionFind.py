class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}
        self.num_of_set = 0

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.num_of_set += 1
        self.size_of_set[x] = 1

    def find(self, x):
        # 1. Find root for x
        root = x
        while self.father[root] != None:
            root = self.father[root]

        # 2. Compression
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

        self.size_of_set[root_y] += self.size_of_set[root_x]
        self.num_of_set -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_num_of_set(self):
        return self.num_of_set

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]



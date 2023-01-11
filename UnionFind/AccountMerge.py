import collections
from typing import List
class AccountMerge:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts or len(accounts) == 0:
            return []
        uf = UnionFind()
        emailToIndex = {}
        # Create unions between indexes
        for i, emails in enumerate(accounts):
            uf.add(i)
            for email in emails[1:]:
                # common email in different account indexes that can be merged
                if email in emailToIndex:
                    uf.union(i, emailToIndex[email])
                emailToIndex[email] = i

        # Append emails to correct index
        indexToEmails = collections.defaultdict(list)
        for email, index in emailToIndex.items():
            father = uf.find(index)
            indexToEmails[father].append(email)

        result = []
        for index, emails in indexToEmails.items():
            temp = [accounts[index][0]] + sorted(emails)
            result.append(temp)
        return result

class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_set = 0
        self.size_of_set = {}

    def add(self, x):
        if x in self.father:
            return
        self.father[x] = None
        self.num_of_set += 1
        self.size_of_set[x] = 1

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
            self.num_of_set -= 1
            self.size_of_set[root_y] += self.size_of_set[root_x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_num_of_set(self):
        return self.num_of_set

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]

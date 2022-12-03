import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.valueToIndex = {}
    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.valueToIndex:
            return False
        self.nums.append(val)
        self.valueToIndex[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.valueToIndex:
            return False
        index = self.valueToIndex[val]
        last = self.nums[-1]
        # move the last element to index
        self.nums[index] = last
        self.valueToIndex[last] = index

        # remove last element
        del self.valueToIndex[val]
        self.nums.pop()
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]


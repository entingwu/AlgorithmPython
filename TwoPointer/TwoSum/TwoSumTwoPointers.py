class TwoSumTwoPointers:
    def __init__(self):
        self.list = []

    """
    @Add the number to an internal data structure
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        self.list.append(number)
        index = len(self.list) - 1
        while index > 0 and (self.list[index - 1] > self.list[index]):
            self.list[index - 1], self.list[index] = self.list[index], self.list[index - 1]
            index -= 1

    """
    @Find if there exists any pair of numbers which sum is equal to the value
    @param value: An integer
    @return: true if can be found or false, (2,1) 4-2=2
    """

    def find(self, value):
        left, right = 0, len(self.list) - 1
        while left < right:
            two_sum = self.list[left] + self.list[right]
            if two_sum < value:
                left += 1
            elif two_sum > value:
                right -= 1
            else:
                return True
        return False

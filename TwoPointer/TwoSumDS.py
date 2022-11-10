class TwoSum:

    def __init__(self):
        self.count = {}

    """
    @Add the number to an internal data structure
    @param number: An integer
    @return: nothing
    """

    def add(self, number):
        #self.count[number] = self.count.get(number, 0) + 1
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    """
    @Find if there exists any pair of numbers which sum is equal to the value
    @param value: An integer
    @return: true if can be found or false, (2,1) 4-2=2
    """

    def find(self, value):
        for number in self.count:
            num2 = value - number
            if (num2 in self.count) and \
                    (self.count[number] > 1 or num2 != number):
                return True
        return False

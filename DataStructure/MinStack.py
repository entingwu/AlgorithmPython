class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        self.stack.append(number)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)
        # if self.min_stack and number > self.min_stack[-1]:
        #     self.min_stack.append(self.min_stack[-1])
        # else:
        #     self.min_stack.append(number)

    """
    @return: An integer
    """

    def pop(self):
        number = self.stack.pop()
        if self.min_stack[-1] == number:
            self.min_stack.pop()
        return number
        # self.min_stack.pop()
        # return self.stack.pop()

    """
    @return: An integer
    """

    def min(self):
        return self.min_stack[-1]
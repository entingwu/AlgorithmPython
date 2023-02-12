class BasicCalculator:
    i = 0
    # +, -, *, (, ) /
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        num = 0
        while self.i < len(s):
            ch = s[self.i]
            self.i += 1
            if ch.isdigit():
                num = num * 10 + int(ch)
            # run into recursion
            if ch == '(':
                num = self.calculate(s)

            if self.i >= len(s) or ch in ['+', '-', '*', '/', ')']:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:  # '/'
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:  # 14-3/2,
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = ch  # current operator
                num = 0  # clear
            # out of recursion
            if ch == ')': break
        return sum(stack)

    # +, -, *, /
    def calculate1(self, s: str) -> int:
        stack = []
        sign = "+"
        num = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if i == len(s) - 1 or ch in ['+', '-', '*', '/']:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else: # '/'
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0: # 14-3/2,
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                sign = ch  # current operator
                num = 0  # clear
        return sum(stack)


    # only +, -
    def calculate0(self, s: str) -> int:
        stack = []
        sign = "+"
        num = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if i == len(s) - 1 or ch in ['+', '-']:
                if sign == '+':
                    stack.append(num)
                else: # -
                    stack.append(-num)
                sign = ch # current operator
                num = 0 # clear
        return sum(stack)
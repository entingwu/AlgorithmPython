class BasicCalculatorII:

    def calculate1(self, s: str) -> int:
        if not s:
            return 0
        num, stack, sign = 0, [], "+"
        for i, ch in enumerate(s):
            print(i, ch)
            if ch.isdigit():
                num = num * 10 + int(ch)
                print(num)
            if (not ch.isdigit() and not ch.isspace()) or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp // num + 1)
                    else:
                        stack.append(tmp // num)
                num = 0
                sign = ch
        return sum(stack)

    def get_expression(self, s):
        expression = []
        val = None
        for char in s:
            if char == ' ':
                continue
            if char in ['+', '-', '*', '/', '(', ')']:
                if val is not None:
                    expression.append(str(val))
                expression.append(char)
                val = None
            else:
                if val is None:
                    val = 0
                val = val * 10 + ord(char) - ord('0')
        if val is not None:
            expression.append(str(val))
        return expression


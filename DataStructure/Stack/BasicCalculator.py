class BasicCalculator:
    def calculate(self, s: str) -> int:
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


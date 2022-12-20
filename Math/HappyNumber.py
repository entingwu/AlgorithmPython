class HappyNumber:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            sum = self.get_next(n)
            n = sum
        return n == 1

    def get_next(self, num):
        total_sum = 0
        while num > 0:
            # (n // 10, n % 10)
            n, digit = divmod(num, 10)
            total_sum += digit ** 2 # pow(digit, 2)
            num = n
        return total_sum

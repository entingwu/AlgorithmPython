import math
class SmallestValueAfterReplacingWithSumOfPrimeFactors:
    def smallestValue(self, n: int) -> int:
        while True:
            next = self.findNext(n)
            if next == n:
                break
            n = next
        return n

    def findNext(self, n):
        sum = 0
        pre = n
        # findNext(5) pre=5//5=1 sum=5
        for i in range(2, n + 1):
            while pre % i == 0:
                sum += i
                pre = pre // i
        return sum


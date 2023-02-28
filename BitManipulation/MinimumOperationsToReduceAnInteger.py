class MinimumOperationsToReduceAnInteger:
    # n = 39
    # 100111 -> 101000 -> 100000 -> 0
    # n = 54
    # 110110 +10-> 111000 +1000-> 1000000 -> 0
    def minOperations(self, n: int) -> int:
        binStr = bin(n)[2:]
        print(binStr)
        ones = 0
        ops = 0
        for i in range(32):
            bit = n & (1 << i)
            if bit != 0: # 1
                ones += 1
            else:
                # 110110 +10-> 111000, i=3
                # 111000 +1000-> 1000000, i=6
                if ones > 1:
                    ops += 1
                    ones = 1
                elif ones == 1: # 1000000 -> 0
                    ops += 1
                    ones = 0
        if ones == 1:
            ops += 1
        elif ones > 1:
            ops += 2
        return ops


    def minOperations1(self, n: int) -> int:
        binStr = "{0:b}".format(int(n)) # bin(n)[2:]
        strs = binStr.split("0")
        count = 0
        for i, ch in enumerate(strs):
            if len(ch) != 0:
                if ch == "1":
                    count += 1
                else:
                    if i == 0 or (i >= 1 and strs[i - 1] == ''):
                        count += 2
                    else:
                        if i >= 1 and strs[i - 1] == '1':
                            count += 2
                        else:
                            count += 1
        return count
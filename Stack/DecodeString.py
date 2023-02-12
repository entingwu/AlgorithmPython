class DecodeString:
    # Time O(maxK * n), Space: O(m + n)
    # 3[a2[c]]
    # 2[c] => cc => acc => accaccacc
    def decodeString(self, s: str) -> str:
        counter = []
        strStack = []
        res = ""
        i = 0
        while i < len(s):
            if s[i] >= "0" and s[i] <="9":
                num = 0
                while s[i] >= "0" and s[i] <="9":
                    num = int(s[i]) + num * 10
                    i += 1
                counter.append(num)
            elif s[i] == "[":
                strStack.append(res) # prev
                res = "" # str for []
                i += 1
            elif s[i] == "]":
                prev = strStack.pop()
                num = counter.pop()
                for _ in range(num):
                    prev += res  # res = "c", prev = ""
                res = prev
                i += 1
            else: # char
                res += s[i]
                i += 1
        return res

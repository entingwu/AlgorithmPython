import collections


class MinimumWindowSubstring:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def min_window(self, source: str, target: str) -> str:
        len_s, len_t = len(source), len(target)
        if len_s == 0 or len_t == 0:
            return ""
        counter_t = collections.defaultdict(int)
        for ch in target:
            counter_t[ch] += 1

        left, count = 0, 0
        min_start, min_len = 0, float('inf')
        for i in range(len_s):
            curr = source[i]
            if curr in counter_t:
                if counter_t[curr] > 0:
                    count += 1 # valid count
                counter_t[curr] -= 1
            while count == len_t:
                if i - left + 1 < min_len:
                    min_len = i - left + 1
                    min_start = left
                l_ch = source[left]
                if l_ch in counter_t:
                    counter_t[l_ch] += 1 # to be filled
                    if counter_t[l_ch] > 0: # 2B, -1 no need to substract
                        count -= 1 # have found
                left += 1

        if min_len == float('inf'):
            return ""
        return source[min_start: min_start + min_len]


    def min_window2(self, source: str, target: str) -> str:
        len_s, len_t = len(source), len(target)
        if len_s == 0 or len_t == 0:
            return ""
        counter_s = collections.defaultdict(int)
        counter_t = collections.defaultdict(int)
        for char in target:
            counter_t[char] = counter_t.get(char, 0) + 1

        j = 0
        # 匹配上的字符数量
        matched_chars = 0
        start, substr_len = 0, float('inf')

        for i in range(len_s):
            # j指针前移条件：j < n 且匹配数量不足
            while j < len_s and matched_chars < len(counter_t):
                char = source[j]
                counter_s[char] = counter_s.get(char, 0) + 1
                # 加1后恰好相等，匹配数量加1
                if counter_s[char] == counter_t.get(char, 0):
                    matched_chars += 1
                j += 1

            # 达到目标匹配数量，更新最短子串
            if matched_chars == len(counter_t):
                curr_len = j - i
                if substr_len > curr_len:
                    substr_len = curr_len
                    start = i

            # 减一后更新匹配数量
            old_char = source[i]
            if counter_s[old_char] == counter_t.get(old_char, 0):
                matched_chars -= 1
            counter_s[old_char] -= 1

        if substr_len == float('inf'):
            return ""
        return source[start: start + substr_len]

    # RIGHT
    def min_window1(self, source: str, target: str) -> str:
        len_s, len_t = len(source), len(target)
        counter_s = collections.defaultdict(int)
        counter_t = collections.defaultdict(int)
        for char in target:
            counter_t[char] = counter_t.get(char, 0) + 1
        print(counter_t)

        min_str = ""
        j = 0
        for i in range(len_s):
            while j < len_s and not self.isSubStr(counter_s, counter_t):
                char = source[j]
                counter_s[char] += 1
                j += 1

            if self.isSubStr(counter_s, counter_t):
                curr_len = j - i
                if curr_len <= len(min_str) or min_str == "":
                    min_str = source[i: j]

            old_char = source[i]
            counter_s[old_char] -= 1
            if counter_s[old_char] < 1:
                del counter_s[old_char]

        return min_str


    def isSubStr(self, counter_s, counter_t):
        if len(counter_t) > len(counter_s):
            return False
        keys_s, keys_t = set(counter_s.keys()), set(counter_t.keys())
        if not keys_t.issubset(keys_s):
            return False
        for key, count in counter_s.items():
            if key in counter_t and count < counter_t[key]:
                return False
        return True



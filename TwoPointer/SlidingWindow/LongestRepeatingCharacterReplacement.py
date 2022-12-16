import collections


class LongestRepeatingCharacterReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = collections.defaultdict(int)
        # maxFreq 以打擂台的方式记录出现最多的字符数量
        max_freq, max_len = 0, 0
        j = 0
        for i in range(len(s)):
            # 当j作为下标合法 且最少需要被替换的字母数目<=k
            while j < len(s) and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                max_freq = max(counter[s[j]], max_freq)
                j += 1
            # 如果替换 除出现次数最多的字母之外的其他字母 的数目>k,
            # 说明有一个不能换，答案与j-i-1进行比较；
            # 否则说明直到字符串末尾替换数目都<=k，可以全部换掉
            # 答案与子串长度j-i进行比较
            if j - i - max_freq > k:
                max_len = max(j - i - 1, max_len)
            else:
                max_len = max(j - i, max_len)

            # 起点后移一位，当前起点位置的字母个数-1
            counter[s[i]] -= 1
        return max_len

    def characterReplacement1(self, s: str, k: int) -> int:
        letters = set(s)
        n = len(s)
        max_len = 0
        for letter in letters:
            start, count = 0, 0
            for end in range(n):
                if s[end] == letter:
                    count += 1
                while start < n and not self.is_window_valid(start, end, count, k):
                    if s[start] == letter:
                        count -= 1
                    start += 1

                max_len = max(end + 1 - start, max_len)
        return max_len

    def is_window_valid(self, start, end, count, k):
        return end + 1 - start - count <= k

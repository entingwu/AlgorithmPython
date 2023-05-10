from typing import List

class WordBreak:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # state
        dp = [False] * (n + 1)
        # initiate
        dp[0] = True
        max_len = 0
        for word in wordDict:
            max_len = max(len(word), max_len)

        # function
        for i in range(1, n + 1):
            dp[i] = False
            # 枚举最后一个单词长度
            for last_word_len in range(1, max_len + 1):
                if i - last_word_len < 0:
                    break
                word = s[i-last_word_len: i]
                # f[j]为true，且最后单词在词典中 == > f[i] true
                if word in wordDict and dp[i - last_word_len]:
                    dp[i] = True
                    break # 找到后进行下一f[i]
        # answer
        return dp[n]


    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        if not s or len(s) == 0:
            return False
        max_len = 0
        for word in wordDict:
            max_len = max(len(word), max_len)
        return self.dfs(s, wordDict, [], 0, max_len)

    def dfs(self, s, wordDict, temp, i, max_len):
        if i == len(s):
            return True

        for word_len in range(max_len + 1):
            word = s[i:i+word_len]
            if word in wordDict:
                temp.append(word)
                if self.dfs(s, wordDict, temp, i + word_len, max_len):
                    return True
                temp.pop()
            elif word_len == max_len:
                return False



p = WordBreak()
s = "leetcode"
wordDict = ["leet", "code"]
print(p.wordBreak(s, wordDict))
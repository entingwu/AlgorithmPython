from typing import (
    Set, List
)

class WordBreak:
    """
    @param s: A string
    @param word_dict: A set of words.
    @return: All possible sentences.
             we will sort your return value in output
    """
    def word_break(self, s: str, word_dict: Set[str]) -> List[str]:
        if len(s) == 0:
            return True
        max_len = self.get_max_len(word_dict)
        results = []
        self.dfs(s, 0, max_len, word_dict, {}, [], results)
        return results

    def dfs(self, s, idx, max_len, word_dict, memo, path, results):
        if idx == len(s):
            results.append(" ".join(path[:]))
            return
        if not self.is_possible(s, idx, max_len, word_dict, memo):
            return

        for end in range(idx + 1, len(s) + 1):
            if end - idx > max_len:
                break
            word = s[idx:end]
            if word not in word_dict:
                continue
            path.append(word)
            self.dfs(s, end, max_len, word_dict, memo, path, results)
            path.pop()


    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break1(self, s: str, word_set: Set[str]) -> bool:
        if len(s) == 0:
            return True
        max_len = self.get_max_len(word_set)
        return self.is_possible(s, 0, max_len, word_set, {})

    # 判断s[start_index: ] 可以由dict中的单词组成
    def is_possible(self, s, idx, max_len, dict, memo):
        if idx in memo:
            return memo[idx]
        if idx == len(s):
            return True

        for end in range(idx + 1, len(s) + 1):
            if end - idx > max_len:
                break
            word = s[idx: end]
            if word not in dict:
                continue
            if self.is_possible(s, end, max_len, dict, memo):
                return True
        memo[idx] = False
        return memo[idx]

    def get_max_len(self, dict):
        max_len = -1
        for word in dict:
            max_len = max(max_len, len(word))
        return max_len
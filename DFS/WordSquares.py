import collections
from typing import (
    List,
)

class WordSquares:
    """
    @param words: a set of words without duplicates
    @return: all word squares
             we will sort your return value in output
    """
    def word_squares(self, words: List[str]) -> List[List[str]]:
        prefix_to_words = self.get_prefix_to_words(words)
        print(prefix_to_words)
        results = []
        for word in words:
            self.search(prefix_to_words, [word], results)
        return results

    def search(self, prefix_to_words, temp, results):
        print(temp)
        n = len(temp[0])
        curr_index = len(temp)
        if curr_index == n:
            results.append(temp[:])
            return

        # pruning
        word_set, prefix = [], ""
        for row_index in range(curr_index, n):
            prefix = "".join(temp[i][row_index] for i in range(curr_index))
            print("#" + prefix)
            if prefix not in prefix_to_words:
                return


        word_set = []
        for i in range(curr_index):
            word_set.append(temp[i][curr_index])
            prefix = "".join(word_set)
        print("@", prefix)

        for next in prefix_to_words[prefix]:
            temp.append(next)
            self.search(prefix_to_words, temp, results)
            temp.pop()


    def get_prefix_to_words(self, words):
        prefix_to_words = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                prefix = word[:i+1]
                prefix_to_words[prefix].add(word)
        return prefix_to_words

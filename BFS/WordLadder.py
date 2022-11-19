import collections
from typing import (
    Set,
)

class WordLadder:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer O(50*N^2)
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        dict.add(end)
        queue = collections.deque([start])
        distance = {start: 1}

        while queue:
            curr = queue.popleft()
            if curr == end:
                return distance[curr]
            for next in self.get_next_words(curr, dict):
                if next in distance:
                    continue
                queue.append(next)
                distance[next] = distance[curr] + 1
        return 0

    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == word[i]:
                    continue
                next_word = left + ch + right
                if next_word in dict:
                    words.append(next_word)
        return words

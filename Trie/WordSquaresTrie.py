import collections
from typing import List
class WordSquaresTrie:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        result = []
        for word in words:
            self.dfs(trie, len(word), [word], result)
        return result

    def dfs(self, trie, n, temp, result):
        curr_index = len(temp)
        if curr_index == n:
            result.append(temp[:])
            return

        word_set, prefix = [], ""
        for row in temp:
            word_set.append(row[curr_index]) # a, le, lad
            prefix = "".join(word_set)

        for next in trie.get_word_set(prefix):
            temp.append(next)
            self.dfs(trie, n, temp, result)
            temp.pop(-1)

    # def get_prefix_to_words(self, words):
    #     prefix_to_words = collections.defaultdict(set)
    #     for word in words:
    #         for i in range(len(word)):
    #             prefix = word[:i+1]
    #             prefix_to_words[prefix].add(word)
    #     return prefix_to_words

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.word_set.add(word)
        node.is_word = True
        node.word = word

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def get_word_set(self, prefix):
        node = self.search(prefix)
        return [] if node is None else node.word_set

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.word_set = set()
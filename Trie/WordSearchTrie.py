from typing import (
    List,
)

class WordSearchTrie:
    DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    MAX_LEN = 0
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i_i(self, board: List[List[str]], words: List[str]) -> int:
        n, m = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        result, word_count = [0], 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if self.is_valid(board, i, j, visited):
                    self.dfs(board, words, trie, trie.root, i, j, word_count, visited, board[i][j], result, i, j)
        return result[0]

    def dfs(self, board, words, trie, node, x, y, word_count, visited, prefix, result, start_x, start_y):
        n, m = len(board), len(board[0])
        char = board[x][y]
        if char not in node.children:
            return

        visited.add((x, y))
        child = node.children[char]
        # prev is word, find next word
        if child.is_word:
            word_count += 1
            child.is_word = False
            result[0] = max(word_count, result[0])
            for i in range(start_x, n):
                new_start_y = 0
                if i == start_x:
                    new_start_y = y
                for j in range(new_start_y, m):
                    if self.is_valid(board, i, j, visited):
                        self.dfs(board, words, trie, trie.root, i, j, word_count, visited, board[i][j], result, i, j)
            word_count -= 1
            child.is_word = True

        for delta_x, delta_y in self.DIRECTION:
            new_x = x + delta_x
            new_y = y + delta_y
            if self.is_valid(board, new_x, new_y, visited):
                self.dfs(board, words, trie, child, new_x, new_y, word_count, visited, prefix + board[new_x][new_y], result, start_x, start_y)

        visited.remove((x, y))


    def is_valid(self, board, x, y, visited):
        if not (0 <= x < len(board) and 0 <= y < len(board[0])):
            return False
        return (x, y) not in visited

    def get_prefix_set(self, words):
        prefixes = set()
        max_len = 0
        for word in words:
            for i in range(len(word)):
                prefixes.add(word[:i+1])
                max_len = max(max_len, len(word[:i+1]))
        return prefixes, max_len

    # def dfs(self, board, words, trie, node, x, y, visited, prefix, result):
    #     char = board[x][y]
    #     if char not in node.children:
    #         return
    #     child = node.children[char]
    #
    #     if prefix in words:
    #         result.add(prefix)
    #
    #     visited.add((x, y))
    #
    #     for delta_x, delta_y in self.DIRECTION:
    #         new_x = x + delta_x
    #         new_y = y + delta_y
    #         if self.is_valid(board, new_x, new_y, visited):
    #             self.dfs(board, words, trie, child, new_x, new_y, visited, prefix + board[new_x][new_y], result)
    #
    #     visited.remove((x, y))

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True
        node.word = word

    def search(self, word):
        return self.helper(self.root, word, 0)

    def helper(self, node, word, index):
        if index == len(word):
            return node.is_word

        ch = word[index]
        if ch not in node.children:
            return False
        return self.helper(node.children[ch], word, index + 1)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


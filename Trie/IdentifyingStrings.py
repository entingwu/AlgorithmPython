from typing import (
    List,
)

class TrieNode:
    def __init__(self):
        self.children = {} # char=>TrieNode
        self.is_word = False
        self.prefix_cnt = 0

class IdentifyingStrings:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_cnt += 1
        node.is_word = True

    def search(self, root, word, index, prefixs):
        if index == len(word):
            prefixs.append(word)
            return True
        if root.prefix_cnt == 1:
            prefixs.append(word[:index])
            return True

        letter = word[index]
        if letter in root.children:
            return self.search(root.children[letter], word, index + 1, prefixs)
        return False

    def get_unique_prefix(self, root, word):
        node = root
        for i in range(len(word)):
            letter = word[i]
            if node.prefix_cnt == 1:
                return word[:i]
            node = node.children[letter]
        return word

    """
    @param string_array: a string array
    @return: return every strings'short peifix
    """
    def short_perfix(self, string_array: List[str]) -> List[str]:
        for word in string_array:
            self.insert(word)
        prefixs = []
        for word in string_array:
            prefixs.append(self.get_unique_prefix(self.root, word))
            #self.search(self.root, word, 0, prefixs)
        print(prefixs)
        return list(prefixs)



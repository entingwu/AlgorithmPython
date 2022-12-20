class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.max_len = 0

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        self.max_len = max(len(word), self.max_len)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        if len(word) > self.max_len:
            return False
        return self.dfs(self.root, word, 0)

    def dfs(self, root, word, index):
        if index == len(word):
            return root.is_word

        char = word[index]
        if word[index] == ".":
            for child in root.children:
                if self.dfs(root.children[child], word, index + 1):
                    return True
            return False
        if char in root.children:
            return self.dfs(root.children[char], word, index + 1)
        return False

class WordDictionary1:
    def __init__(self):
        self.trie = Trie1()

    def addWord(self, word):
        node = self.trie.get_root()
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                node.children[char] = TrieNode1()
            node = node.children[char]
        node.is_word = True
        node.word = word

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        return self.dfs(self.trie.get_root(), word, 0)

    def dfs(self, root, word, index):
        if index == len(word):
            return root.is_word

        char = word[index]
        if word[index] == ".":
            for child in root.children:
                if self.dfs(root.children[child], word, index + 1):
                    return True
            return False
        if char in root.children:
            return self.dfs(root.children[char], word, index + 1)
        return False


class Trie1:
    def __init__(self):
        self.root = TrieNode1()

    def get_root(self):
        return self.root


class TrieNode1:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None




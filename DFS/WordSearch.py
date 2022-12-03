from typing import (
    List,
)

class WordSearch:
    DIRECTION = {(1, 0), (0, 1), (-1, 0), (0, -1)}
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or len(board) == 0:
            return []
        if not board[0] or len(board[0]) == 0:
            return []

        prefix_set = {}
        for word in words:
            for i in range(len(word)):
                prefix_set[word[:i+1]] = False
            prefix_set[word] = True

        results = set()
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited.add((i, j))
                self.dfs(board, i, j, board[i][j], prefix_set, visited, results)
                visited.remove((i, j))
        return results

    def dfs(self, board, x, y, word, prefix_set, visited, results):
        print(word)
        if word not in prefix_set:
            return
        if prefix_set[word]:
            results.add(word[:])

        for delta_x, delta_y in self.DIRECTION:
            new_x, new_y = x + delta_x, y + delta_y
            if not self.inside(board, new_x, new_y):
                continue
            if (new_x, new_y) in visited:
                continue
            visited.add((new_x, new_y))
            self.dfs(board, new_x, new_y, word + board[new_x][new_y], prefix_set, visited, results)
            visited.remove((new_x, new_y))

    def inside(self, board, i, j):
        return 0 <= i < len(board) and 0 <= j < len(board[0])

from typing import List
class SudokuSolver:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)

    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    for num in range(1, 10):
                        if self.isValid(board, i, j, str(num)):
                            board[i][j] = str(num)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def isValid(self, board, i, j, num):
        # check same column
        for row in range(9):
            if board[row][j] == num:
                return False
        # check same row
        for col in range(9):
            if board[i][col] == num:
                return False
        # check 3 * 3 block
        for row in range((i // 3) * 3, (i // 3) * 3 + 3):
            for col in range((j // 3) * 3, (j // 3) * 3 + 3):
                if board[row][col] == num:
                    return False
        return True


from typing import List

class FindWinnerOnTicTacToeGame:

    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        grid = [[0] * n for _ in range(n)]

        def checkRow(row, playid):
            for j in range(n):
                if grid[row][j] != playid:
                    return False
            return True

        def checkCol(col, playid):
            for i in range(n):
                if grid[i][col] != playid:
                    return False
            return True

        def checkDiagonal(playid):
            for i in range(n):
                if grid[i][i] != playid:
                    return False
            return True

        def checkAntiDiagonal(playid):
            for i in range(n):
                if grid[i][n - 1 - i] != playid:
                    return False
            return True

        playid = 1
        for i, move in enumerate(moves):
            row, col = move
            grid[row][col] = playid

            if checkRow(row, playid) or checkCol(col, playid):
                return 'A' if playid == 1 else 'B'
            if (row == col and checkDiagonal(playid)) or (row + col == n - 1 and checkAntiDiagonal(playid)):
                return 'A' if playid == 1 else 'B'

            playid *= -1

        return "Draw" if len(moves) == n * n else "Pending"

import collections
from typing import List

class FirstCompletelyPaintedRowOrColumn:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        map = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                map[mat[i][j]] = [i, j]

        rows, cols = [0] * m, [0] * n
        for i, num in enumerate(arr):
            row, col = map[num]
            mat[row][col] = 0
            rows[row] += 1
            cols[col] += 1
            if rows[row] == n or cols[col] == m:
                return i
        return -1

def check(mat, row, col, m, n):
    is_row, is_col = True, True
    for j in range(n):
        if mat[row][j] != 0:
            is_row = False
            break
    if is_row:
        return True

    for i in range(m):
        if mat[i][col] != 0:
            is_col = False
            break
    return is_col


arr = [1,3,4,2]
mat = [[1,4],[2,3]]
# arr = [2,8,7,4,1,3,5,6,9]
# mat = [[3,2,5],[1,4,6],[8,7,9]]
arr = [1,4,5,2,6,3]
mat = [[4,3,5],[1,2,6]]
#print(firstCompleteIndex(arr, mat))
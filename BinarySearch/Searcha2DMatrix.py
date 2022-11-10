from typing import (
    List,
)

class Searcha2DMatrix:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row_index = self.find_row_index(matrix, target)
        if row_index == -1:
            return False
        return self.find_target_in_row(matrix[row_index], target)

    def find_target_in_row(self, row, target):
        start, end = 0, len(row) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                start = mid
            else:
                end = mid
        return row[start] == target or row[end] == target


    def find_row_index(self, matrix, target):
        row_cnt = len(matrix)
        col_cnt = len(matrix[0])
        start, end = 0, row_cnt - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][0] == target:
                return mid
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[start][0] <= target <= matrix[start][col_cnt - 1]:
            return start
        if matrix[end][0] <= target <= matrix[end][col_cnt - 1]:
            return end
        return -1

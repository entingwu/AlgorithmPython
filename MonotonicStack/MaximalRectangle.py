from typing import (
    List,
)

class MaximalRectangle:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximal_rectangle(self, matrix: List[List[bool]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        max_area = 0
        heights = [0] * m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
            curr_area = self.largest_rectangle_area(heights)
            max_area = max(curr_area, max_area)
        return max_area

    def largest_rectangle_area(self, heights):
        if not heights:
            return 0
        stack = []
        n, max_area = len(heights), 0
        for right in range(n + 1):
            right_height = -1 if right == n else heights[right]
            while stack and heights[stack[-1]] >= right_height:
                curr_height = heights[stack.pop()] if stack else -1
                left = stack[-1] if stack else -1
                width = right - left - 1
                max_area = max(curr_height * width, max_area)
            stack.append(right)
        return max_area


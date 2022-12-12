from typing import (
    List,
)

class LargestRectangleInHistogram:
    """
    @param heights: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largest_rectangle_area(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        max_area, n = 0, len(heights)
        for i in range(0, n + 1):
            # 设置特殊数据heights[n] = -1
            value = -1 if i == n else heights[i]
            while stack and heights[stack[-1]] >= value:
                top = stack.pop(-1)
                # 找左端点时栈空，设置特殊数据heights[-1] = -1
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(width * heights[top], max_area)
            stack.append(i)
        return max_area

    def largest_rectangle_area1(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area = 0
        for start in range(len(heights)):
            for end in range(start, len(heights)):
                height = float('inf')
                for i in range(start, end + 1):
                    height = min(heights[i], height)
                max_area = max((end - start + 1) * height, max_area)
        return max_area


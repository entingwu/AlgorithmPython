from typing import List
class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water_area = 0
        for i in range(n):
            water_area += min(right_max[i], left_max[i]) - height[i]
        return water_area

    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        water_area = 0
        for i in range(1, n):
            right_max = height[i]
            for j in range(i + 1, n):
                right_max = max(height[j], right_max)
            left_max = height[i]
            for j in range(i):
                left_max = max(height[j], left_max)
            water_area += min(right_max, left_max) - height[i]
        return water_area
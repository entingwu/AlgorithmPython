from typing import List

class FloodFill:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr, sc, set(), image[sr][sc], color)
        return image

    def dfs(self, image, x, y, visited, old_color, new_color):
        image[x][y] = new_color
        visited.add((x, y))
        for delta_x, delta_y in self.DIRECTIONS:
            new_x = x + delta_x
            new_y = y + delta_y
            if not (0 <= new_x < len(image) and 0 <= new_y < len(image[0])):
                continue
            if image[new_x][new_y] == old_color and (new_x, new_y) not in visited:
                self.dfs(image, new_x, new_y, visited, old_color, new_color)


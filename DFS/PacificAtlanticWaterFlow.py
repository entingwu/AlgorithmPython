from typing import List
class PacificAtlanticWaterFlow:
    DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(heights), len(heights[0])
        if not m or not n:
            return result

        p_visited = set()
        a_visited = set()
        for i in range(m):
            # p_visited[i][0] = True
            self.dfs(i, 0, heights, p_visited)
            # a_visited[i][n-1] = True
            self.dfs(i, n - 1, heights, a_visited)

        for j in range(n):
            # p_visited[0][j] = True
            self.dfs(0, j, heights, p_visited)
            # a_visited[m-1][j] = True
            self.dfs(m - 1, j, heights, a_visited)

        return list(a_visited & p_visited)

    def dfs(self, x, y, heights, visited):
        visited.add((x, y))
        for delta_x, delta_y in self.DIRECTIONS:
            new_x = x + delta_x
            new_y = y + delta_y
            if not self.isValid(new_x, new_y, x, y, heights, visited):
                continue
            self.dfs(new_x, new_y, heights, visited)

    def isValid(self, new_x, new_y, x, y, heights, visited):
        if not (0 <= new_x < len(heights) and 0 <= new_y < len(heights[0])):
            return False
        if (new_x, new_y) in visited:
            return False
        return heights[new_x][new_y] >= heights[x][y] # 往更高的内陆递归
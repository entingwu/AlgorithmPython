import collections
from typing import List

class WallsAndGates:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def walls_and_gates(self, rooms: List[List[int]]):
        if not rooms and not rooms[0]:
            return []

        ROOM, GATE = (1 << 31) - 1, 0
        row_cnt, col_cnt = len(rooms), len(rooms[0])
        queue = collections.deque()
        for row in range(row_cnt):
            for col in range(col_cnt):
                if rooms[row][col] == GATE:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for row_delta, col_delta in self.DIRECTIONS:
                curr_row = row + row_delta
                curr_col = col + col_delta
                if 0 <= curr_row < row_cnt and 0 <= curr_col < col_cnt and rooms[curr_row][curr_col] == ROOM:
                    # if rooms[row][col] + 1 < rooms[curr_row][curr_col]:
                    rooms[curr_row][curr_col] = rooms[row][col] + 1
                    queue.append((curr_row, curr_col))

        return rooms
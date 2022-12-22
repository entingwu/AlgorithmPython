import collections
from typing import (
    List,
)

class GridType:
    EMPTY = 0
    WALL = 1

class TheMaze:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """
    DIRECTIONS_HASH = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}
    def find_shortest_way(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        n, m = len(maze), len(maze[0])
        if not maze or n == 0 or m == 0:
            return "impossible"

        hole = (hole[0], hole[1])
        queue = collections.deque([(ball[0], ball[1])])
        distance = {(ball[0], ball[1]): (0, '')}
        while queue:
            x, y = queue.popleft()
            dist, path = distance[(x, y)]

            for direction in self.DIRECTIONS_HASH:
                new_x, new_y = self.kill_ball(x, y, direction, maze, hole)
                new_dist = dist + abs(new_x - x) + abs(new_y - y)
                new_path = path + direction
                # 如果distance中的next更小，则无需入队
                if (new_x, new_y) in distance and distance[(new_x, new_y)] <= (new_dist, new_path):
                    continue
                queue.append((new_x, new_y))
                distance[(new_x, new_y)] = (new_dist, new_path)

        if hole in distance:
            return distance[hole][1]
        return 'impossible'


    def kill_ball(self, x, y, direction, maze, hole):
        dx, dy = self.DIRECTIONS_HASH[direction]
        while (x, y) != hole and not self.is_wall(x, y, maze):
            x += dx
            y += dy
        if (x, y) == hole:
            return x, y
        # wall
        return x - dx, y - dy

    def is_wall(self, x, y, maze):
        if not (0 <= x < len(maze) and 0 <= y < len(maze[0])):
            return True # wall
        return maze[x][y] == GridType.WALL



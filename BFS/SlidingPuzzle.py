import collections
from typing import (
    List,
)

class SlidingPuzzle:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    def min_move_step(self, init_state: List[List[int]], final_state: List[List[int]]) -> int:
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)
        forward_queue = collections.deque([source])
        forward_set = set([source])

        backward_queue = collections.deque([target])
        backward_set = set([target])

        steps = 0
        while forward_queue and backward_queue:
            steps += 1
            if self.extend_queue(forward_queue, forward_set, backward_set):
                return steps

            steps += 1
            if self.extend_queue(backward_queue, forward_set, backward_set):
                return steps
        return -1

    def extend_queue(self, queue, source_set, target_set):
        # 遍历当前层
        for i in range(len(queue)):
            curr = queue.popleft()
            for next in self.get_next(curr):
                if next in source_set:
                    continue
                if next in target_set:
                    return True
                queue.append(next)
                source_set.add(next)
        return False

    def min_move_step1(self, init_state: List[List[int]], final_state: List[List[int]]) -> int:
        source = self.matrix_to_string(init_state)
        target = self.matrix_to_string(final_state)
        queue = collections.deque([source])
        distance = {source: 0}
        while queue:
            curr = queue.popleft()
            if curr == target:
                return distance[curr]

            for next in self.get_next(curr):
                if next in distance:
                    continue
                queue.append(next)
                distance[next] = distance[curr] + 1
        return -1

    def matrix_to_string(self, state):
        str_list = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                str_list.append(str(state[i][j]))
        return "".join(str_list)

    def get_next(self, state):
        states = []
        zero_index = state.find("0")
        x, y = zero_index // 3, zero_index % 3

        for delta_x, delta_y in self.DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            if 0 <= x_ < 3 and 0 <= y_ < 3:
                next_state = list(state)
                next_state[x * 3 + y] = next_state[x_ * 3 + y_]
                next_state[x_ * 3 + y_] = "0"
                states.append("".join(next_state))
        return states


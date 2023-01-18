import collections
from typing import (
    List,
)

class CourseSchedule:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegree = self.get_indegree(num_courses, prerequisites)
        start_nodes = [i for i in range(num_courses) if indegree[i] == 0]
        num_taken = 0
        queue = collections.deque(start_nodes)
        while queue:
            curr = queue.popleft()
            num_taken += 1
            for next in graph[curr]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    queue.append(next)
        return num_taken == num_courses

    def get_indegree(self, num_courses, prerequisites):
        graph = [[] for i in range(num_courses)]
        indegree = [0] * num_courses
        for condition in prerequisites:
            start, end = condition[1], condition[0]
            graph[start].append(end)
            indegree[end] += 1
        return graph, indegree


    def can_finish1(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        node_to_indegree = self.get_indegree1(num_courses, prerequisites)
        start_nodes = [n for n in node_to_indegree if node_to_indegree[n] == 0]
        num_taken = 0
        order = []
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            num_taken += 1
            order.append(node)
            for condition in prerequisites:
                start, end = condition[1], condition[0]
                if start == node:
                    node_to_indegree[end] -= 1
                    if node_to_indegree[end] == 0:
                        queue.append(end)
        print(order)
        return num_taken == num_courses

    def get_indegree1(self, num_courses, prerequisites):
        node_to_indegree = {i: 0 for i in range(num_courses)}
        for condition in prerequisites:
            start, end = condition[1], condition[0]
            node_to_indegree[end] += 1
        return node_to_indegree


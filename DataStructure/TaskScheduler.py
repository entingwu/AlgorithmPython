import heapq
from typing import List
import collections
class TaskScheduler:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
        frequencies.sort()
        print(frequencies)

        max_cnt = frequencies.pop()
        idle_time = (max_cnt - 1) * n
        print(idle_time)

        while frequencies and idle_time > 0:
            cnt = frequencies.pop()
            idle_time -= min(max_cnt - 1, cnt)
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)

    # Wrong
    def leastInterval1(self, tasks: List[str], n: int) -> int:
        taskToCnt = collections.defaultdict(int)
        for task in tasks:
            taskToCnt[task] += 1
        heap = []
        for task, cnt in taskToCnt.items():
            heapq.heappush(heap, (cnt, task))

        max_cnt, max_task = heapq.heappop(heap)
        idle_time = (max_cnt - 1) * n
        print(idle_time)

        while len(heap) > 0 and idle_time > 0:
            cnt, task = heapq.heappop(heap)
            idle_time -= min(max_cnt - 1, cnt)
            print(task, cnt, idle_time)
        idle_time = max(0, idle_time)
        return idle_time + len(tasks)
import collections
import heapq
from typing import List

class MinimumCostOfaPathWithSpecialRoads:

    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        map = collections.defaultdict(list)
        #map[tuple(target)].append((0, 0, 0))
        for x1, y1, x2, y2, cost in specialRoads:
            map[x1, y1].append([x2, y2, cost])

        dist = collections.defaultdict(lambda: float('inf'))
        dist[tuple(start)] = 0
        minHeap = [(0, *start)] # unpack start => [(0, 1, 1)]

        while minHeap:
            d1, x1, y1 = heapq.heappop(minHeap) # (0, 1, 1)
            if [x1, y1] == target:
                return d1

            for x2, y2, cost in map[x1, y1]:
                new_d = d1 + cost
                # (3, 3, 3), # (5, 4, 5)
                if new_d < dist[x2, y2]:
                    dist[x2, y2] = new_d
                    heapq.heappush(minHeap, (new_d, x2, y2))

            for x2, y2 in map:
                new_d = d1 + abs(x2 - x1) + abs(y2 - y1)
                # (1, 1, 2), (5, 3, 4), # (4, 3, 4)
                if new_d < dist[x2, y2]:
                    dist[x2, y2] = new_d
                    heapq.heappush(minHeap, (new_d, x2, y2))

            new_d = d1 + abs(target[0] - x1) + abs(target[1] - y1)
            heapq.heappush(minHeap, (new_d, target[0], target[1]))

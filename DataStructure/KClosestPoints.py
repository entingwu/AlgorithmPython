from typing import (
    List,
)
import heapq

"""
Definition for a point:
"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class KClosestPoints:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(heap, (dist, point.x, point.y))

        results = []
        i = 0
        while len(heap) > 0 and i < k:
            dist, x, y = heapq.heappop(heap)
            results.append(Point(x, y))
            i += 1
        return results

    def get_distance(self, pa, pb):
        return (pa.x - pb.x) ** 2 + (pa.y - pb.y) ** 2

import heapq


class UglyNumber:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nth_ugly_number(self, n: int) -> int:
        heap = [1]
        visited = set([1])

        val = None
        for i in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                num = val * factor
                if num not in visited:
                    visited.add(num)
                    heapq.heappush(heap, num)
        return val
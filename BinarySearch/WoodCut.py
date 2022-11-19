from typing import List

class WoodCut:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def wood_cut(self, l: List[int], k: int) -> int:
        if not l:
            return 0
        start, end = 1, min(max(l), sum(l) // k)
        if end < 1:
            return 0
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_count(l, mid) >= k:
                start = mid
            else:
                end = mid
        return end if self.get_count(l, end) >= k else start
        # if self.get_count(l, end) >= k:
        #     return end
        # return start

    def get_count(self, l, len):
        return sum(item // len for item in l)
        # sum = 0
        # for item in l:
        #     sum += item // len
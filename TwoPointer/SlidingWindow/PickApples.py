from typing import (
    List,
)

class PickApples:
    """
    @param a: a list of integer
    @param k: a integer
    @param l: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def pick_apples(self, a: List[int], k: int, l: int) -> int:
        max_apples, n = float("-inf"), len(a)
        for i in range(n):
            left_max_l = self.find_max(a, 0, i, k)
            right_max_k = self.find_max(a, i, n, l)

            left_max_k = self.find_max(a, 0, i, l)
            right_max_l = self.find_max(a, i, n, k)

            if left_max_l != -1 and right_max_k != -1:
                max_apples = max(left_max_l + right_max_k, max_apples)

            if left_max_k != -1 and right_max_l != -1:
                max_apples = max(left_max_k + right_max_l, max_apples)

        return max_apples if max_apples != float("-inf") else -1

    def find_max(self, a, start, end, len):
        if len > end - start:
            return -1
        left, right = start, start + len
        sum_window = sum(a[i] for i in range(left, right))
        max_sum = sum_window

        while right < end:
            sum_window += a[right]
            sum_window -= a[left]
            max_sum = max(sum_window, max_sum)
            left += 1
            right += 1
        return max_sum

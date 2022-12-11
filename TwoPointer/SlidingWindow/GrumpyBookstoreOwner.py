from typing import (
    List,
)

class GrumpyBookstoreOwner:
    """
    @param customers: the number of customers
    @param grumpy: the owner's temper every day
    @param x: X days
    @return: calc the max satisfied customers
    """
    def max_satisfied(self, customers: List[int], grumpy: List[int], x: int) -> int:
        n, sum_window = len(customers), 0
        for i in range(n):
            if i < x:
                sum_window += customers[i]
            else:
                sum_window += (1 - grumpy[i]) * customers[i]

        result = sum_window
        left, right = 0, x # right是窗口外右端
        while right < n:
            # 出去的是坏脾气
            if grumpy[left] == 1:
                sum_window -= customers[left]
            # 加入的是坏脾气
            if grumpy[right] == 1:
                sum_window += customers[right]
            result = max(sum_window, result)
            left += 1
            right += 1
        return result
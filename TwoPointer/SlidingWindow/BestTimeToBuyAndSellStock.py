from typing import (
    List,
)

class BestTimeToBuyAndSellStock:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def max_profit(self, prices: List[int]) -> int:
        max_profit, n = 0, len(prices)
        for i in range(n):
            left_cost = self.get_cost(prices, 0, i)
            right_cost = self.get_cost(prices, i, n)
            max_profit = max(left_cost + right_cost, max_profit)
        return max_profit

    def get_cost(self, prices, start, end):
        min_price, max_profit = float('inf'), 0
        for i in range(start, end):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)
        return max_profit

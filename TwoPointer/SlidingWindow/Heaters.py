from typing import (
    List,
)

class Heaters:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def find_radius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n, m = len(houses), len(heaters)
        i, j = 0, 0
        heater_radius = 0
        while i < n and j < m:
            now_radius = abs(heaters[j] - houses[i])
            next_radius = float('inf')
            if j < m - 1:
                next_radius = abs(heaters[j + 1] - houses[i])
            if now_radius < next_radius:
                heater_radius = max(now_radius, heater_radius)
                i += 1
            else:
                j += 1
        return heater_radius


    def find_radius1(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heat_radius = 0
        for house in houses:
            radius = self.get_minimum_radius(house, heaters)
            heat_radius = max(radius, heat_radius)
        return heat_radius

    def get_minimum_radius(self, house, heaters):
        left, right = 0, len(heaters) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if heaters[mid] <= house:
                left = mid
            else:
                right = mid

        left_distance = abs(heaters[left] - house)
        right_distance = abs(heaters[right] - house)
        return min(left_distance, right_distance)
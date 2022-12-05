from typing import (
    List,
)

class DividePlayersIntoTeamsOfEqualSkill:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) % 2 != 0:
            return -1
        if len(skill) <= 2:
            return skill[0] * skill[1]
        target = sum(skill) * 2 // len(skill)
        if sum(skill) * 2 % len(skill) != 0:
            return -1

        numToCount = {}
        total = 0
        for i in range(len(skill)):
            num = target - skill[i] # prev
            if num in numToCount:
                numToCount[num] -= 1
                if numToCount[num] == 0:
                    del numToCount[num]
                total += num * skill[i]
            else:
                numToCount[skill[i]] = numToCount.get(skill[i], 0) + 1 # current
        print(numToCount, total)
        for num, count in numToCount.items():
            if count != 0:
                return -1
        return total
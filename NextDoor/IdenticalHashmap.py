from typing import Iterable


class IdenticalHashmap:
    # p100_1.are_identical({'k': {'nk': 1}}, {'k': {'nk': 2}})
    def are_identical(self, map1, map2):
        if type(map1) != dict and type(map2) != dict:
            return map1 == map2
        elif type(map1) != dict or type(map2) != dict:
            return False

        keys1, keys2 = map1.keys(), map2.keys()
        if set(keys1) != set(keys2):
            print(keys1, keys2)
            return False
        for key in keys1:
            if not self.are_identical(map1[key], map2[key]):
                print(map1[key], map2[key])
                return False
        return True
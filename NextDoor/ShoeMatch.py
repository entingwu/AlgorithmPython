import collections
from typing import List
class Shoe:
    def __init__(self, style = None, pos = 0):
        self.style = style
        self.pos = pos

def find_shoe(shoes: List[Shoe])-> List[List[Shoe]]:
    map = {}
    for i in range(len(shoes)):
        shoe = shoes[i]
        style, pos = shoe.style, shoe.pos
        if style not in map:
            map[style] = {}
        if pos not in map[style]:
            map[style][pos] = []
        map[style][pos].append(i)

    results = []
    for style, shoe_map in map.items():
        if len(shoe_map.keys()) != 2:
            continue

        left_shoes = shoe_map[0]
        right_shoes = shoe_map[1]
        for left in left_shoes:
            for right in right_shoes:
                results.append([left, right])

    print("#", map)
    return results

shoes = [Shoe("A", 0), Shoe("B", 1), Shoe("A", 1), Shoe("B", 0), Shoe("B", 1), Shoe("C", 0)]
style_shoes = find_shoe(shoes)
print(style_shoes)

# def print_shoe(style_shoes):
#     for shoes in style_shoes:
#         for shoe in shoes:
#             print(shoe.style, shoe.pos)
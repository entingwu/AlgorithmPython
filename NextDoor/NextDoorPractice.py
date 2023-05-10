import collections
import re
from typing import List

class Comment:
    def __init__(self, id=None, parent_id=None):
        self.id = id
        self.parent_id = parent_id

class CommentNode:
    def __init__(self, id=None, children=None):
        self.id = id
        self.children = children


class NextDoorPractice:

    def flat_to_tree1(self, comments: List[Comment]) -> List[CommentNode]:
        id_to_nodes = {}
        roots = []
        for comment in comments:
            id, parent_id = comment.id, comment.parent_id
            if id not in id_to_nodes:
                node = CommentNode(id, [])
                id_to_nodes[id] = node
            else:
                node = id_to_nodes[id]

            if parent_id is not None:
                if parent_id not in id_to_nodes:
                    parent_node = CommentNode(parent_id, [])
                    id_to_nodes[parent_id] = parent_node
                else:
                    parent_node = id_to_nodes[parent_id]
            else:
                roots.append(node)
                continue

            parent_node.children.append(node)
        print(roots)
        return roots


def print_tree(comment_nodes: List[CommentNode]):
    if comment_nodes is None:
        print("#")
        return
    for node in comment_nodes:
        print(node.id)
        print_tree(node.children)

def flat_to_tree(comments: List[Comment]) -> List[CommentNode]:
    graph = collections.defaultdict(set)
    for comment in comments:
        id, parent_id = comment.id, comment.parent_id
        if parent_id:
            graph[parent_id].add(id)
    print(graph)
    result = []
    for comment in comments:
        if comment.parent_id is None:
            parent = dfs(graph, comment.id)
            result.append(parent)
    return result

def dfs(graph, id):
    if id not in graph: # leaf
        return CommentNode(id)
    children = set()
    for neighbor in graph[id]:
        node = dfs(graph, neighbor)
        children.add(node)
    return CommentNode(id, children)

comments = [Comment(1, None), Comment(2, 1), Comment(3, 1), Comment(3, 1), Comment(4, None), Comment(5, 4), Comment(6, 5)]
comment_nodes = flat_to_tree(comments)
print_tree(comment_nodes)

# Overlap Duration
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def find_overlap(intervals: List[Interval]) -> int:
    if not intervals or len(intervals) == 0:
        return -1
    intervals.sort(key=lambda x: (x.start, x.end))

    prev_end, overlaps = 0, 0
    for interval in intervals:
        start, end = interval.start, interval.end
        if start < prev_end:
            overlaps += abs(prev_end - start)
        prev_end = end
    return overlaps

interval1 = Interval(1, 6)
interval2 = Interval(5, 10)
#print(find_overlap([interval1, interval2]))

# buy time window interval
# [10, 15]
# [1, 5], [8, 12], [10, 14]
def find_busy_time_window(intervals: List[Interval], busy_interval: Interval) -> float:
    if not intervals or len(intervals) == 0:
        return 0

    boundaries = []
    for interval in intervals:
        boundaries.append((interval.start, -1))
        boundaries.append((interval.end, 1))
    boundaries.sort()

    is_matched, left = 0, 0
    result = []
    for boundary in boundaries:
        if is_matched == 0:
            left = boundary[0]
        is_matched += boundary[1]
        if is_matched == 0:
            right = boundary[0]
            if len(result) > 0 and result[-1].end == left:
                result[-1].end = right
            else:
                result.append(Interval(left, right))

    overlaps = 0
    for interval in result:
        overlap = find_overlap([interval, busy_interval])
        overlaps += overlap
    return overlaps / (busy_interval.end - busy_interval.start)

customer_intervals = [Interval(1, 5), Interval(8, 12), Interval(10, 14)]
#print(find_busy_time_window(customer_intervals, Interval(10, 15)))

# LRU cache
# data structure supports append, pop => linkedlist
# find prev of the node
class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

# Least Recently Use
# 1. search key: to check whether Node is already in the doubly linked list: HashMap O(1)
# 2. In: delete the Node and add it to the tail (recently): LinkedList O(1)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # 1. get函数是通过输入key来获得value，如果成功获得后，这对(key, value)升至缓存器中最常用的位置（顶部），如果key不存在，则返回-1。
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        node.next.prev = node.prev
        node.prev.next = node.next
        self.move_to_tail(node)
        return node.value

    # 2. set函数是插入一对新的(key, value)，如果原缓存器中有该key，则需要先删除掉原有的，将新的插入到缓存器的顶部。如果不存在，则直接插入到顶部。
    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.map[key] = value
            return

        if len(self.map) == self.capacity:
            node = self.head.next
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.map[node.key]

        curr = Node(key, value)
        self.map[key] = curr
        self.move_to_tail(curr)

    def move_to_tail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail

# Identical Hashmap
def is_identical(map1: dict, map2: dict) -> bool:
    if type(map1) != dict and type(map2) != dict:
        return map1 == map2
    elif type(map1) != dict or type(map2) != dict:
        return False

    keys1, keys2 = map1.keys(), map2.keys()

    if set(keys1) != set(keys2):
        print(keys1, keys2)
        return False

    for key in keys1:
        if not is_identical(map1[key], map2[key]):
            print(map1[key], map2[key])
            return False
    return True

# print(is_identical({'k': 1}, {'k': 1}))
# print(is_identical({'k': {'nk': None}}, {'k': {'nk': 1}}))
# print(is_identical({'k': 1}, {'k': 1, 'k2': 2}))
# print(is_identical({'k': {'nk': 1}, 'k2': 2}, {'k': {'nk': 1}}))

# Convert JSON

camel_pat = re.compile(r'([A-Z])')
snake_pat = re.compile(r'_([a-z])')

def camel_to_snake(s):
    return camel_pat.sub(lambda x: '_' + x.group(1).lower(), s)

#pattern.sub(repl_pat, input_str)
def snake_to_camel(s):
    return snake_pat.sub(lambda x: x.group(1).upper(), s)

# print(snake_to_camel("abc_xy"))
# print(camel_to_snake("abcXy"))

def convert_array_snake_to_camel(s:list) -> list:
    newArray = []
    for item in s:
        new_item = item
        if isinstance(item, dict):
            new_item = convert_snake_to_camel(item)
        elif isinstance(item, list):
            new_item = convert_array_snake_to_camel(item)
        newArray.append(new_item)
    return newArray

def convert_snake_to_camel(s:dict) -> dict:
    output = {}
    for key in s:
        new_key = snake_to_camel(key)
        new_value = s[key]
        if isinstance(s[key], dict):
            new_value = convert_snake_to_camel(s[key])
        elif isinstance(s[key], list):
            new_value = convert_array_snake_to_camel(s[key])
        output[new_key] = new_value
    return output

msg = {
    "validation_errors": [
       {
           "first_name": "christy",
           "description_msg": "required",
       },
       {
           "last_name": "wu",
           "description_msg": "required",
       },
    ],
    "request_id": "1234",
}
# print(convert_snake_to_camel(msg))

# list/array, dictionary/object, int
def recurse(nested_dict, obj, sep, parent_key=""):
    if isinstance(nested_dict, list):
        for i in range(len(nested_dict)):
            new_key = parent_key + sep + str(i) if parent_key else str(i)
            recurse(nested_dict[i], obj, sep, new_key)

    elif isinstance(nested_dict, dict):
        for key, value in nested_dict.items():
            new_key = parent_key + sep + key if parent_key else key
            recurse(value, obj, sep, new_key)
    else:
        obj[parent_key] = nested_dict
def flattenDict(nested_dict, sep="_"):
    obj = collections.OrderedDict()
    recurse(nested_dict, obj, sep)
    return obj

#print(flattenDict(msg))

# FlatternNestedListIterator
def parseNestedList(nested_list, result) -> List[int]:
    if type(nested_list) == int:
        return result.append(nested_list)
    for item in nested_list:
        parseNestedList(item, result)

nested_list = [[1,1],2]
result = []
parseNestedList(nested_list, result)
# print(result)

# ShoeMatch
class Shoe:
    def __init__(self, style, pos):
        self.style = style
        self.pos = pos

def find_shoe(shoes: List[Shoe]) -> List[List[Shoe]]:
    map = {}
    for i, shoe in enumerate(shoes):
        style, pos = shoe.style, shoe.pos
        if style not in map:
            map[style] = {}
        if pos not in map[style]:
            map[style][pos] = []
        map[style][pos].append(i)
    print(map)

    pairs = []
    for style, shoe_map in map.items():
        if len(map[style]) != 2:
            continue

        left_shoes = shoe_map[0]
        right_shoes = shoe_map[1]

        for left in left_shoes:
            for right in right_shoes:
                pairs.append([left, right])
    return pairs

shoes = [Shoe("A", 0), Shoe("B", 1), Shoe("A", 1), Shoe("B", 0), Shoe("B", 1), Shoe("C", 0)]
# style_shoes = find_shoe(shoes)
# print(style_shoes)

# Range Split
# [1,2,0,4,6,7,0,9,0] -> [[1,2], [4,6,7], [9]]
def split_range(nums: List[int]) -> List[List[int]]:
    result = []
    temp = []
    for i, num in enumerate(nums):
        if num != 0:
            temp.append(num)
        if num == 0 or i == len(nums) - 1:
            result.append(temp[:])
            temp = []
    return result

nums = [1, 0 ,1]
# print(split_range(nums))

# Follow up: given an array of integers, and an index k, return the Range contains kth indexed number. If kth number if 0, return None
#  0 1 2 3 4 5 6 7 8
# [1,2,0,4,6,7,0,9,0] => [[1,2], [4,6,7], [9]]
# index 7 -> [9]
# index 1 -> [1,2]
# index 4 -> [4,7]

def find_range(nums: List[int], k: int) -> List[int]:
    ranges = split_range(nums)
    start, end = 0, len(ranges) - 1
    while start + 1 < end:
        mid = start + (end - start) // 2
        if ranges[mid][0] <= nums[k] <= ranges[mid][-1]:
            return ranges[mid]
        elif nums[k] < ranges[mid][0]:
            end = mid
        else:
            start = mid

    if ranges[start][0] <= nums[k] <= ranges[start][-1]:
        return ranges[start]
    if ranges[end][0] <= nums[k] <= ranges[end][-1]:
        return ranges[end]
    return None

def split_index_to_range(nums: List[int]) -> dict[int, List[int]]:
    if not nums or len(nums) == 0:
        return {}
    range_map = collections.defaultdict(list)
    for i, num in enumerate(nums):
        if num != 0:
            range_map[i] = find_range(nums, i)
    return range_map

nums = [1,2,0,4,6,7,0,9,0]
print(find_range(nums, 1))
print(split_index_to_range(nums))
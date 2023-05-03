import collections
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


    def flat_to_tree(self, comments: List[Comment]) -> List[CommentNode]:
        graph = collections.defaultdict(set)
        id_to_comment = {}
        for comment in comments:
            id, parent_id = comment.id, comment.parent_id
            if parent_id is not None:
                graph[parent_id].add(id)
                id_to_comment[id] = comment

        results = []
        for comment in comments:
            if comment.parent_id is None: # root
                root = self.dfs(graph, comment, id_to_comment)
                results.append(root)
        return results

    # Return the CommentNode which id is node.id, children is List[CommentNode]
    def dfs(self, graph, node, id_to_comment):
        if node.id not in graph:
            return CommentNode(node.id)

        children = []
        for neighbor_id in graph[node.id]:
            neighbor = id_to_comment[neighbor_id]
            child = self.dfs(graph, neighbor, id_to_comment)
            children.append(child)
        return CommentNode(node.id, children)

    def print_tree(self, comment_nodes: List[CommentNode]):
        if comment_nodes is None:
            print("#")
            return
        for node in comment_nodes:
            print(node.id)
            self.print_tree(node.children)

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
print(find_overlap([interval1, interval2]))

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
    print(boundaries)

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
print(find_busy_time_window(customer_intervals, Interval(10, 15)))

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


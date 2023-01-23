class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.map:
            return -1
        curr = self.map.get(key)
        curr.next.prev = curr.prev
        curr.prev.next = curr.next

        self.move_to_tail(curr)
        return curr.value

    def put(self, key, value):
        if self.get(key) != -1:
            self.map.get(key).value = value

        if len(self.map) == self.capacity:
            node = self.head.next
            node.next.prev = node.prev
            node.prev.next = node.next
            del self.map[node.key]

        curr = Node(key, value)
        self.map[key] = curr
        self.move_to_tail(curr)

    def move_to_tail(self, node):
        node.prev = self.tail.prev
        self.tail.prev = node
        node.prev.next = node
        node.next = self.tail
